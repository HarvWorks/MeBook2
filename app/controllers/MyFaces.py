from system.core.controller import *
import datetime
from flask_socketio import SocketIO, join_room, leave_room, emit, send
from system import socketio
import time
from werkzeug.datastructures import ImmutableMultiDict

#
# import sys
# sys.path.insert(0, '/UserDashboard')
# from manage import socketio


class MyFaces(Controller):
    def __init__(self, action):
        super(MyFaces, self).__init__(action)
        self.load_model('MyFace')

    def index(self):
        if "user" in session:
            return redirect('/wall')
        return self.load_view('index.html')

    def register(self):
        if "user" in session:
            return redirect('/wall')
        return self.load_view("register.html")

    def login(self):
        if "user" in session:
            return redirect('/wall')
        return self.load_view("login.html")

    def process(self):
        if request.form["type"] == "register":
            temp = 'yes'
            if len(request.form.getlist('remember')) == 0:
                temp = 'no'
            data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email'], 'password': request.form['password'], 'confirm': request.form['confirm'], 'remember': temp}
            sucess = self.models['MyFace'].regCheck(data)
            if not sucess == False:
                flash("User registered!","sucess")
                session['first_name'] = request.form['first_name']
                session['last_name'] = request.form['last_name']
                flash(request.form['first_name'] + " " + request.form['last_name'] + " has been registered!","sucess")
                flash('','email')
                flash('',"first_name")
                flash('','last_name')
                return redirect('/wall')
            return redirect('/register')

        elif request.form['type'] == "login":
            session['first_name'] = ''
            session['last_name'] = ''
            session['password'] = ''
            success = 0
            user = self.models['MyFace'].login(request.form['email'])
            pw_hash = ''
            if not user:
                flash("There is no such email.","email_login_err")
            else:
                pw_hash  = user[0]['password']
                success += 1

                if not self.models['MyFace'].password(pw_hash, request.form['password']) :
                    flash("Password does not match.","password_login_err")
                else:
                    success += 1

            if success >= 2:
                session['first_name'] = user[0]['first_name']
                session['last_name'] = user[0]['last_name']
                session['user'] = user[0]['id']
                flash( session['first_name'] + " " + session['last_name'] + " has logged in!","success")
                return redirect('/wall')
            return redirect('/login')

        return redirect('/')

    def wall(self):
        if not "user" in session:
            return redirect('/login')
        return self.load_view('dashboard.html')

    def postWall(self):
        if not "user" in session:
            return redirect('/login')
        if request.form['message']:
            self.models['MyFace'].postToWall(request.form['message'])
        return redirect('/')

    def newWall_json(self):
        if not "user" in session:
            return redirect('/login')
        messages = self.models['MyFace'].initFetchWall()
        return jsonify( messages = messages )

    def logout(self):
        session.clear()
        return redirect('/')

    def dashboard(self):
        if not "user" in session:
            return redirect('/login')
        friends = self.models['MyFace'].selectFriends(session['user'])
        self.models['MyFace'].numFriends(len(friends), session['user'])
        not_friends = self.models['MyFace'].selectNotFriends(session['user'])
        pending_friends = self.models['MyFace'].selectPendingFriends(session['user'])
        requesting_friends = self.models['MyFace'].selectRequestingFriends(session['user'])
        return self.load_view('user_table.html', not_friends = not_friends, friends = friends, pending_friends = pending_friends, requesting_friends = requesting_friends)

    def edit(self):
        if not "user" in session:
            return redirect('/login')
        user = self.models['MyFace'].findUser(session['user'])
        flash(user[0]['email'], "email")
        flash(user[0]['first_name'], "first_name")
        flash(user[0]['last_name'], "last_name")
        flash(user[0]['description'], "description")
        return self.load_view('edit_user.html')

    def profile(self, user_id):
        if not "user" in session:
            return redirect('/login')
        user = self.models['MyFace'].findUser(user_id)
        return self.load_view('profile.html', user = user)

    def message(self):
        if not "user" in session:
            return redirect('/login')
        users = self.models['MyFace'].usersOfMessage(session['user'])
        if not users:
            return self.load_view('message.html')
        return redirect('/message/' + str(users[0]['id']))

    def userMessage(self, user_id):
        if not "user" in session:
            return redirect('/login')
        users = self.models['MyFace'].usersOfMessage(session['user'])
        user = self.models['MyFace'].findUser(user_id)
        return self.load_view('message.html', users = users, user_id = user_id, user = user)

    def grabMessages(self, user_id):
        if not "user" in session:
            return redirect('/login')
        messages = self.models['MyFace'].privateMessages(session['user'], user_id)
        session['currentTimeStamp'] = messages[-1]
        return jsonify(messages = messages)

    @socketio.on('chat_message', namespace = '/chat')
    def chat_message_send(message):
        if not message['message'] == "":
            message['created_at'] = int(time.time())
            emit('chat_message', message, broadcast=True)

    @socketio.on('set_location', namespace = '/map')
    def chat_message_send(location):
        print "sdfdsafjdskfjsdjkfjdsfdhsfkjdjskfjdsjklafhsdajfhadsl"
        print location
        emit('set_location', location, broadcast=True, namespace = '/map')

    def userMessageSend(self, user_id):
        if not "user" in session:
            return redirect('/login')
        if request.form['message']:
            session['currentTimeStamp'] = datetime.datetime.now()
            self.models['MyFace'].postPrivateMessages(request.form['message'], session['user'], user_id)
        return redirect('/message/' + user_id)

    def updateMessages(self, user_id):
        if not "user" in session:
            return redirect('/login')
        messages = self.models['MyFace'].privateMessagesUpdate(session['user'], user_id)
        session['currentTimeStamp'] = datetime.datetime.now()
        return jsonify(messages = messages)

    def requestFriend(self, user_id):
        if not "user" in session:
            return redirect('/login')
        user = self.models['MyFace'].findUser(user_id)
        self.models['MyFace'].addFriend(user_id)
        flash( "A friend request has been sent to " + user[0]['first_name'] + " " + user[0]['last_name'] + "!", "success")
        return redirect('/dashboard')

    def processUser(self, user_id):
        user = self.models['MyFace'].findUser(session['user'])
        if int(user_id) == session['user'] or user[0]['level'] == 9:
            if request.form['type'] == 'edit_info':
                info = {'email': request.form['email'],'first_name': request.form['first_name'],'last_name': request.form['last_name']}
                self.models['MyFace'].processInfo(info, user_id)
            if request.form['type'] == 'edit_pass':
                info = { 'password': request.form['password'], 'confirm': request.form['confirm'] }
                self.models['MyFace'].processPass(info, user_id)
            if request.form['type'] == 'edit_desc':
                info = request.form['description']
                self.models['MyFace'].editDesc(info, user_id)
            flash("MOOOO!!!")
        return redirect('/profile')

    def ignore(self, user_id):
        if not "user" in session:
            return redirect('/login')
        self.models['MyFace'].ignore(user_id)
        return redirect('/dashboard')

    def cancelRequest(self, user_id):
        if not "user" in session:
            return redirect('/login')
        self.models['MyFace'].cancelRequest(user_id)
        return redirect('/dashboard')

    def acceptFriend(self, user_id):
        if not "user" in session:
            return redirect('/login')
        user = self.models['MyFace'].findUser(user_id)
        self.models['MyFace'].addFriend(user_id)
        friends = self.models['MyFace'].selectFriends(user_id)
        self.models['MyFace'].numFriends(len(friends), user_id)
        flash( user[0]['first_name'] + " " + user[0]['last_name'] + " has been friended!", "success")
        return redirect('/dashboard')

    def unfriend(self, user_id):
        if not "user" in session:
            return redirect('/login')
        user = self.models['MyFace'].findUser(user_id)
        self.models['MyFace'].unFriend(user_id)
        friends = self.models['MyFace'].selectFriends(user_id)
        self.models['MyFace'].numFriends(len(friends), user_id)
        flash( user[0]['first_name'] + " " + user[0]['last_name'] + " has been unfriended!!!", "success")
        return redirect('/dashboard')

    def search(self):
        if not "user" in session:
            return redirect('/login')
        print "XxXxsjsdfndsfadsflkjdsfjhdshfdshkjfdshfjkdsjkafhdshfjdsa %s" %(request.form['id'])
        return redirect('/message/'+request.form['id'])

    def grabFriends(self):
        if not "user" in session:
            return redirect('/login')
        friends = self.models['MyFace'].selectFriends(session['user'])
        if len(friends) < 50:
            friends += self.models['MyFace'].selectRequestingFriends(session['user'])
        if len(friends) < 50:
            friends += self.models['MyFace'].selectPendingFriends(session['user'])
        if len(friends) < 50:
            friends += self.models['MyFace'].selectNotFriends(session['user'])
        return jsonify(friends = friends)
