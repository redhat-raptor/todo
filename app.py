from chalice import Chalice

app = Chalice(app_name='todo')


@app.route('/todo')
def index():
    return {'hello': 'world'}


@app.route('/todo', methods=['POST'])
def create_user():
    user_as_json = app.current_request.json_body
    return {'user': user_as_json}

