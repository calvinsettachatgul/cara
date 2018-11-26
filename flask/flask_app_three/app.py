from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def connection():
    # print(request.url)
    # print(request.path)
    print_path_if_index(request)
    helper_method()
    return 'connection executed'
    
@app.route('/about')
def view_about():
    print_path_if_index(request)
    return 'we are on the about page'
    
def helper_method():
    print("we fired helper method")
    
def print_path_if_index(request):
    path_of_request = request.path
    if(path_of_request == '/'):
        print('we went to the index route')
    else:
        print('not at index')
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)