```python
import json
from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

projectChat = {}

@app.route('/initialize_chat', methods=['POST'])
def initialize_chat():
    project_id = request.json['project_id']
    projectChat[project_id] = []
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@socketio.on('message')
def handle_message(data):
    project_id = data['project_id']
    message = data['message']
    projectChat[project_id].append(message)
    emit('message', {'project_id': project_id, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
```