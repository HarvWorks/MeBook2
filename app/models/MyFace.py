import re
from system.core.model import Model
from system.core.controller import *
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
lowercase = re.compile("[a-z]+")
uppercase = re.compile("[A-Z]+")
number = re.compile('[0-9]+')
class MyFace(Model):
    def __init__(self):
        super(MyFace, self).__init__()

    def selectUsers(self):
        query = "SELECT * FROM users ORDER BY users.first_name DESC"
        return self.db.query_db(query)

    def selectFriends(self, id):
        query = "SELECT L1.friend_id, DATE_FORMAT(L1.created_at,'%b %d %Y') as friend_created_at, users.id, users.first_name, users.last_name, users.email, users.num_friends, users.level, DATE_FORMAT(users.created_at,'%b %d %Y') as users_created_at FROM   friends L1 left join users ON users.id = L1.friend_id  WHERE user_id = :id AND EXISTS(SELECT * FROM   friends L2 WHERE  L1.user_id = L2.friend_id AND L1.friend_id = L2.user_id) ORDER BY L1.created_at ASC"
        data = { 'id': id }
        return self.db.query_db(query, data)

    def selectFriendsId(self, id):
        query = "SELECT users.id, users.level FROM   friends L1 left join users ON users.id = L1.friend_id  WHERE user_id = :id AND EXISTS(SELECT * FROM   friends L2 WHERE  L1.user_id = L2.friend_id AND L1.friend_id = L2.user_id) ORDER BY L1.created_at ASC"
        data = { 'id': id }
        return self.db.query_db(query, data)

    def selectNotFriends(self):
        query = "SELECT users.id, users.email, users.first_name, users.last_name, users.num_friends, DATE_FORMAT(users.created_at,'%b %d %Y') as created_at FROM users WHERE users.id NOT IN (SELECT friends.friend_id FROM friends WHERE friends.friend_id = :id or friends.user_id = :id) and users.id NOT IN (SELECT friends.user_id FROM friends WHERE friends.friend_id = :id or friends.user_id = :id) and not users.id = :id ORDER BY last_name ASC"
        data = {'id': session['user']}
        return self.db.query_db(query, data)

    def selectPendingFriends(self, id):
        query = "SELECT L1.friend_id, DATE_FORMAT(L1.created_at,'%b %d %Y') as friend_created_at, users.id, users.first_name, users.last_name, users.email, users.num_friends, users.level, DATE_FORMAT(users.created_at,'%b %d %Y') as user_created_at FROM   friends L1 left join users ON users.id = L1.friend_id  WHERE user_id = :id AND not EXISTS(SELECT * FROM friends L2 WHERE  L1.user_id = L2.friend_id AND L1.friend_id = L2.user_id) ORDER BY L1.created_at ASC"
        data = { 'id': id }
        return self.db.query_db(query, data)

    def selectRequestingFriends(self, id):
        query = "SELECT L1.friend_id, DATE_FORMAT(L1.created_at,'%b %d %Y') as friend_created_at, users.id, users.first_name, users.last_name, users.email, users.num_friends, users.level, DATE_FORMAT(users.created_at,'%b %d %Y') as user_created_at FROM   friends L1 left join users ON users.id = L1.user_id  WHERE friend_id = :id AND not EXISTS(SELECT * FROM friends L2 WHERE L1.user_id = L2.friend_id AND L1.friend_id = L2.user_id) ORDER BY L1.created_at ASC"
        data = {'id': id}
        return self.db.query_db(query, data)

    def addFriend(self, id):
        query = "INSERT INTO friends ( user_id, friend_id, created_at, updated_at ) VALUES( :user_id, :friend_id, NOW(), NOW() )"
        data = {'user_id': session['user'], 'friend_id': id}
        return self.db.query_db(query, data)

    def unFriend(self, user_id):
        query = "DELETE FROM friends WHERE  user_id = :user_id and friend_id = :friend_id or user_id = :friend_id and friend_id = :user_id"
        data = {'user_id': user_id, 'friend_id': session['user']}
        return self.db.query_db(query, data)

    def ignore(self, user_id):
        query = "DELETE FROM friends WHERE  user_id = :user_id and friend_id = :friend_id"
        data = {'user_id': user_id, 'friend_id': session['user']}
        user = self.findUser(user_id)
        flash(user[0]['first_name'] + " " + user[0]['last_name'] + " has been ignored!", "ignored")
        return self.db.query_db(query, data)

    def cancelRequest(self, user_id):
        query = "DELETE FROM friends WHERE  user_id = :user_id and friend_id = :friend_id"
        data = {'user_id': session['user'], 'friend_id': user_id}
        user = self.findUser(user_id)
        flash("The friend request to " + user[0]['first_name'] + " " + user[0]['last_name'] + " has been canceled!", "ignored")
        return self.db.query_db(query, data)

    def usersOfMessage(self, user_id):
        query = "SELECT user_id FROM private_messages WHERE friend_id = :id UNION SELECT friend_id FROM private_messages WHERE user_id = :id"
        data = {"id": user_id}
        users = self.db.query_db(query, data)
        usersMessage = []
        for user in reversed(users):
            query = "SELECT id, first_name as friend_first_name, last_name as friend_last_name FROM users WHERE id = :id"
            data = { 'id': user['user_id'] }
            usersMessage.append(self.db.query_db(query, data)[0])
            query = "SELECT private_messages.message, private_messages.user_id, private_messages.created_at, users.first_name, users.last_name FROM private_messages LEFT JOIN users ON users.id = private_messages.user_id WHERE user_id = :id and friend_id = :friend_id OR user_id = :friend_id and friend_id = :id ORDER BY created_at DESC LIMIT 1"
            data = { 'id': user_id, 'friend_id': user['user_id'] }
            usersMessage[len(usersMessage)-1].update(self.db.query_db(query, data)[0])
        return usersMessage

    def privateMessages(self, user_id, friend_id):
        query = "SELECT private_messages.message, private_messages.created_at, users.id, users.first_name, users.last_name FROM private_messages left join users on users.id = user_id where user_id = :user_id and friend_id = :friend_id or user_id = :friend_id and friend_id = :user_id ORDER BY created_at ASC LIMIT 50"
        data = {"user_id": user_id, "friend_id": friend_id}
        return self.db.query_db(query, data)

    def privateMessagesUpdate(self, user_id, friend_id):
        query = "SELECT private_messages.message, private_messages.created_at, users.id, users.first_name, users.last_name FROM private_messages left join users on users.id = user_id where user_id = :user_id and friend_id = :friend_id or user_id = :friend_id and friend_id = :user_id ORDER BY created_at ASC LIMIT 50"
        data = {"user_id": user_id, "friend_id": friend_id}
        return self.db.query_db(query, data)

    def postPrivateMessages(self, message, user_id, friend_id):
        query = "INSERT INTO private_messages (message, user_id, friend_id, created_at, updated_at) VALUES (:message, :user_id, :friend_id, NOW(), NOW())"
        data = {'message': message, 'user_id': user_id, 'friend_id': friend_id}
        return self.db.query_db(query, data)

    def postToWall(self, message):
        query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :id)"
        data = {'message': message, 'id': session['user']}
        return self.db.query_db(query, data)

    def initFetchWall(self):
        query = "SELECT users.id, messages.id as message_id, messages.message, messages.user_id, messages.updated_at, messages.created_at, users.first_name, users.last_name FROM messages LEFT JOIN users ON users.id = messages.user_id WHERE users.id IN ( SELECT users.id FROM friends L1 left join users ON users.id = L1.friend_id WHERE user_id = :id AND EXISTS ( SELECT * FROM friends L2 WHERE  L1.user_id = L2.friend_id AND L1.friend_id = L2.user_id ) ) or users.id in ( :id ) ORDER BY created_at DESC"
        data = { 'id': session['user'] }
        return self.db.query_db(query, data)

    def commentToWall(comment, message_id):
        query = "INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) VALUES (:comment, NOW(), NOW(), :user_id, :message_id)"
        data = {'comment': comment, 'user_id': session['id'], 'message_id': message_id}
        return self.db.query_db(query, data)

    def registration(self, registration):
        query = "INSERT INTO users (first_name, last_name, email, password, num_friends, level, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, 0, :level, NOW(), NOW())"
        data = {'first_name': registration['first_name'], 'last_name': registration['last_name'], 'email': registration['email'], 'password': registration['pw_hash'], 'level': registration['level']}
        flash(registration['first_name'] + " " + registration['last_name'] + " has been registered!","sucess")
        return self.db.query_db(query, data)

    def numFriends(self, num_friends, id = session['user']):
        query = "UPDATE users SET num_friends = :num_friends WHERE id = :id"
        data = {'num_friends': num_friends, 'id': id}
        return self.db.query_db(query, data)

    def processInfo(self, info, id):
        sucess = 0
        if len(info['email']) < 1:
            flash("Email cannot be blank!","email_err")
        elif not EMAIL_REGEX.match(info['email']):
            flash("Invalid Email Address!","email_err")
        else:
            sucess += 1
        if len(info['first_name']) < 1:
            flash("Please enter a first name.","first_name_err")
        elif  len(info['first_name']) < 3 or number.search(info['first_name']):
            flash("Please enter a valid first name.","first_name_err")
        else:
            sucess += 1

        if len(info['last_name']) < 1:
            flash("Please enter a last name.","last_name_err")
        elif len(info['first_name']) < 3 or number.search(info['last_name']):
            flash("Please enter a valid last name.","last_name_err")
        else:
            sucess += 1

        if sucess >= 3:
            self.editInfo(info,id)
            return
        return

    def editInfo(self, info, id):
        query = "UPDATE users SET email = :email, first_name = :first_name, last_name = :last_name WHERE id = :id"
        data = {'email': info['email'], 'first_name': info['first_name'], 'last_name': info['last_name'], 'id': id}
        return self.db.query_db(query, data)

    def processPass(self, password, id):
        if len(password['password']) < 1:
            flash("Please enter a password.","password_err")
        elif len(password['password']) < 8 or not lowercase.search(password['password']) or not uppercase.search(password['password']) or not number.search(password['password']):
            flash("Please enter a password at least 8 characters long, containing a lowercase, an uppercase, and a number.","password_err")
        elif len(password['confirm']) < 1:
            flash("Please enter a password confirmation.","confirm_err")
        elif not password['password'] == password['confirm']:
            flash("Passwords do not match.","confirm_err")
        else:
            pw_hash = self.bcrypt.generate_password_hash(registration['password'])
            self.editPass(pw_hash, id)
            return
        return

    def editPass(self, password, id):
        query = "UPDATE users SET password = :password WHERE id = :id"
        data = {'password': password, 'id': id}
        return self.db.query_db(query, data)

    def editDesc(self, description, id):
        query = "UPDATE users SET description = :description WHERE id = :id"
        data = {'description': description, 'id': id}
        return self.db.query_db(query, data)

    def login(self, login):
        query = "SELECT COUNT(*) as count FROM users "
        temp = self.db.query_db(query)
        if not temp[0]['count'] == 0:
            query = "SELECT * FROM users WHERE email = :email"
            data = {'email': login}
            return self.db.query_db(query, data)
        else:
            return False

    def findUser(self, login):
        query = "SELECT * FROM users WHERE id = :id"
        data = {'id': login}
        return self.db.query_db(query, data)

    def regCheck(self, registration):
        pw_hash = ''
        flash(registration['email'],'email')
        flash(registration['first_name'],"first_name")
        flash(registration['last_name'],'last_name')
        sucess = 0

        if len(registration['email']) < 1:
            flash("Email cannot be blank!","email_err")
        elif not EMAIL_REGEX.match(registration['email']):
            flash("Invalid Email Address!","email_err")
        else:
            sucess += 1
        if len(registration['first_name']) < 1:
            flash("Please enter a first name.","first_name_err")
        elif  len(registration['first_name']) < 3 or number.search(registration['first_name']):
            flash("Please enter a valid first name.","first_name_err")
        else:
            sucess += 1

        if len(registration['last_name']) < 1:
            flash("Please enter a last name.","last_name_err")
        elif len(registration['first_name']) < 3 or number.search(registration['last_name']):
            flash("Please enter a valid last name.","last_name_err")
        else:
            sucess += 1

        if len(registration['password']) < 1:
            flash("Please enter a password.","password_err")
        elif len(registration['password']) < 8 or not lowercase.search(registration['password']) or not uppercase.search(registration['password']) or not number.search(registration['password']):
            flash("Please enter a password at least 8 characters long, containing a lowercase, an uppercase, and a number.","password_err")
        elif len(registration['confirm']) < 1:
            flash("Please enter a password confirmation.","confirm_err")
        elif not registration['password'] == registration['confirm']:
            flash("Passwords do not match.","confirm_err")
        else:
            sucess += 1
            pw_hash = self.bcrypt.generate_password_hash(registration['password'])

        query = "SELECT COUNT(*) as count FROM users "
        temp = self.db.query_db(query)

        if sucess >= 4:
            level = 1
            query = "SELECT COUNT(*) as count FROM users "
            temp = self.db.query_db(query)
            if temp[0]['count'] == 0:
                level = 9;
            # if registration['remember'] == 'yes':
            data = {'first_name': registration['first_name'], 'last_name': registration['last_name'], 'email': registration['email'], 'pw_hash':pw_hash, 'level':level}
            self.registration(data)
            temp = self.login(registration['email'])
            session['user'] = temp[0]['id']
            return
        return False

    def password(self, pw_hash, password):
        if self.bcrypt.check_password_hash(pw_hash, password):
            return True
        else:
            return False
