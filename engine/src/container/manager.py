# Set the path
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from api import app, properties

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("run", Server(
    use_debugger=properties.get_boolean("server.debugger"),
    use_reloader=properties.get_boolean("server.reloader"),
    host=properties.get_string("server.host"),
    port=properties.get_int("server.port"))
)

if __name__ == "__main__":
    manager.run()