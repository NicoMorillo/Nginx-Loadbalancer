from flask import Flask
import socket


app = Flask(__name__)

@app.route('/')
def home():
    return f'Welcome to web from port and container {socket.gethostname()}'

if __name__=='__main__':
    app.run(host='0.0.0.0')