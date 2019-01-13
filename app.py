from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Method use: %s' % request.method


@app.route('/cfn', methods=['GET', 'POST'])
def cfn():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are probabling using GET'

if __name__ == '__main__':
       app.run()
