from flask import Flask

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def index():
    return '<h1>Hello World, how are you!</h1>'

@app.route('/test')
def test():
    return 'This is a test'