"""
    Base terminal command manager.

    Define terminal commands here to run actions
"""
from flask.ext.script import Manager, Server
from flask.ext.sqlalchemy import SQLAlchemy
# from flask_socketio import SocketIO
# from flask.ext.migrate import Migrate, MigrateCommand
from system.init import app
from system import socketio
# from system.init.database import create_database
import subprocess
import os

from system.init.configuration import initialize_config
from system.init.database import initialize_db
from system.init.routes import initialize_routes



initialize_config(app)
initialize_db(app)
initialize_routes(app)


if __name__ == '__main__':
    socketio.run(app)
