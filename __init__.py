from flask import Flask
from flask import request
from parse_command import parse_command
import searcher

app = Flask(__name__)

confirm = {'type': 'confirmation', 'group_id':164038901}

@app.route('/', methods=['GET'])
def index():
    return '<h1>Hello World</h1>'

@app.route('/', methods=['POST'])
def get_post():
    r = request.get_json()
    if r['type'] == 'message_new':
        parse_command(r['object'])
    elif r['type'] == 'send_digest':
        searcher.search()
    return 'ok'


if __name__ == '__main__':
    app.run()