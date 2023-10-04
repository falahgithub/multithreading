from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
import threading, time

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def home():
    return render_template("index.html")



@socketio.on("connect")
def connect():
    print("I am connect function of main.py")

@socketio.on("message")
def data(n):

    # Generator
    def countdown(n):
        while n > 0:
            n += 1
            yield n

    counter = countdown(n)
    while True:
        value = next(counter)
        print(value)
        time.sleep(1)
        socketio.emit("message", value)


@socketio.on("inputtext")
def text(input):
    emit("inputtext", input)

thread1 = threading.Thread(target=data)
thread2 = threading.Thread(target=text)

thread1.start()
thread2.start()






if __name__=='__main__':
    app.run(debug=True)