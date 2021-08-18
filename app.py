from chalice import Chalice
from os import environ as env
from dotenv import load_dotenv
from os.path import join, dirname
import redis
import json

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
redis_client = None

app = Chalice(app_name='todo')


@app.route('/todo')
def index():
    redis_connect()
    todo = redis_client.get('todo')
    return todo


@app.route('/todo', methods=['POST'])
def create_user():
    redis_connect()
    todo_payload = app.current_request.json_body
    redis_client.set('todo', json.dumps(todo_payload))
    return todo_payload


def redis_connect():
    redis_client = redis.Redis(host=env.get('REDIS_HOST'), port=env.get('REDIS_PORT'), password=env.get('REDIS_PASSWORD'))
