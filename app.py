from chalice import Chalice
from os import environ as env
from dotenv import load_dotenv
from os.path import join, dirname
import redis

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
redis_client = None

app = Chalice(app_name='todo')


@app.route('/todo')
def index():
    redis_connect()
    redis_client.set('todo', '{"foo": "bar"}')
    todo = redis_client.get('todo')
    return todo


@app.route('/todo', methods=['POST'])
def create_user():
    user_as_json = app.current_request.json_body
    return {'user': user_as_json}

def redis_connect():
    redis_client = redis.Redis(host=env.get('REDIS_HOST'), port=env.get('REDIS_PORT'), password=env.get('REDIS_PASSWORD'))


redis_connect()