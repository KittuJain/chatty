import logging

from core.glados import Glados
from flask_restful import Resource, reqparse
from utils.file import File
from utils.path import *
from utils.utils import *


def get_awayday_details(emp_id):
  away_day_info = {
    'name': 'Amar',
    'date': '30th October 2016',
    'room_mates': 'Akbar and Anthony',
    'venue': 'Khandala',
    'track': '1',
    'flight_time': '09:30',
    'speaker': 'Mogembo'
  }
  return away_day_info

data_filename = "data.txt"
help_agent = Glados(data_filename)


class HelpApi(Resource):
  def __init__(self):
    self.parser = reqparse.RequestParser()
    self.parser.add_argument('text', required=False, type=str)
    self.parser.add_argument('ID', required=False, type=int)
    logging.basicConfig(level=logging.INFO)
    self.logger = logging.getLogger("Help")
    self.file = File()

  def post(self):
    global help_agent, data_filename
    args = self.parser.parse_args()
    question = args['text']
    emp_id = args['ID']
    default_response = "I'm afraid, I don't understand. I'm sorry"

    awayday_info = get_awayday_details(emp_id)
    if is_empty(question):
      return {"reply": "You said nothing!! What's up? Are you okay?"}

    ans = help_agent.get_help(question)
    answer = ans['answer']

    if is_empty(answer):
      return default_response
    ans['answer'] = format_answer(ans['answer'], awayday_info)
    ans['timestamp'] = get_timestamp()

    if ans['probability'] < 0.1:
      ans['answer'] = default_response
    return {"reply": ans['answer']}
