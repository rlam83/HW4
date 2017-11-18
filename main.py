from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Homepage!'


@app.route('/hello')
def hello():
    name = request.args.get('name')
    try:
        age = int(request.args.get('age'))
    except TypeError:
        age = 0
    age_msg = None

    if age < 30:
        age_msg = "You're quite young!"
    else:
        age_msg = "You're getting old!"

    return 'Hello {name}! {age_str}'.format(name=name, age_str=age_msg)


if __name__ == "__main__":
    app.run()