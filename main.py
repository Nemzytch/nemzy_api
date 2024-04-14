from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Hello, World!')
    return 'Hello, World!!!'

@app.route('/hello')
def hello():
    print('Hello, World!')
    return 'Hello, World!!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3241, debug=True)


# https://apipreprod.cuik.io/
# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=9463, debug=True)
    
# nemzy.cuik.io   
# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=5684, debug=True)