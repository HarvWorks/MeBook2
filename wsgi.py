from system.init import app
from system import socketio
import subprocess

from system.init.configuration import initialize_config
from system.init.database import initialize_db
from system.init.routes import initialize_routes



initialize_config(app)
initialize_db(app)
initialize_routes(app)

if __name__ == "__main__":
	socketio.run(app)
