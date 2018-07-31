from flask import Flask

print('running flask_app')

app = Flask(__name__)
@app.route('/')
def hello_world():
  return "hello world!"

