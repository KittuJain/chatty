import time
from datetime import datetime

def is_empty(text):
  return text is None or len(text) == 0

def is_not_empty(text):
  return not is_empty(text)

def get_timestamp():
  d = datetime.now()
  return time.mktime(d.timetuple())

def format_answer(text, leave_info):
  return text % leave_info
