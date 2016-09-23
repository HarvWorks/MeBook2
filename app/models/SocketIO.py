from flask_socketio import SocketIO, join_room, leave_room
if __name__ == '__main__':
    socketio.run(app)
class SocketIO(Model):
    def __init__(self):
        super(SocketIO, self).__init__()
        self.load_model('MyFace')
