import os

CURR_PATH = os.path.dirname(__file__)
module_path = os.path.abspath(os.path.join(CURR_PATH, '../..'))
resource_path = os.path.abspath(os.path.join(CURR_PATH, '../resources'))

def get_resource(file_name):
  return os.path.abspath(os.path.join(resource_path, file_name))

def get_module_path(file_name):
  return os.path.abspath(os.path.join(module_path, file_name))