from chalice import Chalice, Response
from os import environ as env
import redis
import json

app = Chalice(app_name='todo')

@app.route('/todo')
def index():
    try:
        redis_client = redis_connect()
    except Exception as e:
        return Response(body='Error connecting backend!',
                    headers={'Content-Type': 'text/plain'},
                    status_code=500)
    
    try:
        todo_content = redis_client.get('todo')
    except Exception as e:
        return Response(body='Error getting data from backend!',
                    headers={'Content-Type': 'text/plain'},
                    status_code=500)
    
    return json.loads(todo_content)

@app.route('/todo', methods=['POST'])
def create_user():
    redis_client = redis_connect()
    todo_payload = app.current_request.json_body
    redis_client.set('todo', json.dumps(todo_payload))
    return todo_payload


def redis_connect():
    return redis.Redis(host=env.get('REDIS_HOST'), port=env.get('REDIS_PORT'), password=env.get('REDIS_PASSWORD'))
