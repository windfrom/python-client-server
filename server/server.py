from flask import Flask, request

app = Flask(__name__)

@app.route ('/hello', methods =['GET'])
def index():
    error = None 
    return 'Hello, World!'
        
@app.route ('/hello', methods =['POST'])
def user(name):
    name = input()
    print('Hello, %s !') % name
if __name__ == '__main__':
    app.run()