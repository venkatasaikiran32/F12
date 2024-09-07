from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('update_data')
def handle_update_data(data):
    # Here you can process the data and broadcast it
    emit('update_response', {'data': data}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
