from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '<h1>Hello World</h1>'

@app.route('/test', methods=['POST'])
def test_post():
    result = request.get_json()
    req = ''
    for k,v in result:
        req += 'key : {} | value : {}'.format(k, v)
    return req

if __name__ == '__main__':
    app.run()