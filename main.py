from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Hello, World!')
    return 'Hello, World!'

@app.route('/hello')
def hello():
    print('Hello, World!')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=5684, debug=True)