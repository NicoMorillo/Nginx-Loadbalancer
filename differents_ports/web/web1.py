from flask import Flask
import os


app = Flask(__name__)

port_s = os.environ['PORT']
port_s = int(port_s)
@app.route('/')
def home():
    return '<h1>Welcome to web 1 in {} </h1>'.format(port_s)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=port_s)