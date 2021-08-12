from chalice import Chalice
from os import environ as env
import redis

redis_client = redis.Redis(host=env.get('REDIS_HOST'), port=env.get('REDIS_PORT'), password=env.get('REDIS_PASSWORD'))
redis_client.set('todo', '{"foo": "bar"}')

app = Chalice(app_name='todo')


@app.route('/todo')
def index():
    todo = redis_client.get('todo')
    return todo


@app.route('/todo', methods=['POST'])
def create_user():
    user_as_json = app.current_request.json_body
    return {'user': user_as_json}

