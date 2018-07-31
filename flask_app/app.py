from flask import Flask

print('running flask_app')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
@app.route('/')
def hello_world():
  return "hello world! python3"


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
