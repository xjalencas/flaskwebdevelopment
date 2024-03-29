from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/user/<int:id>')
def userid(id):
    return '<h1>Hello again, id:{}!</h1>'.format(id)

