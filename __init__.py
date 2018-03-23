from flask import Flask
from flask import request
import vk_module

app = Flask(__name__)

confirm = {'type': 'confirmation', 'group_id':164038901}

@app.route('/', methods=['GET'])
def index():
    return '<h1>Hello World</h1>'

@app.route('/', methods=['POST'])
def get_post():
    r = dict(request.get_json())
    if r == confirm:
        return 'b5ad317f'
    elif r['type'] == 'message_new':
        vk_module.send_message(178261174, 'got the message : {}'.format(r['object']['body']))
        return 'ok'

if __name__ == '__main__':
    app.run()