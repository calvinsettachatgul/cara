from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
@app.route('/')
def hello_world():
  return "hello world!"
  
@app.route('/index')
def index():
  return render_template('index.html', data={'key1': 'value1'})
  
@app.route('/indextwo')
def indextwo():
  return render_template('indextwo.html', data={'key1': 'value1'})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)