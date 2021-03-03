from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
<<<<<<< HEAD
    return '<h1>Hello, Jhonathan!</h1>'
=======
    return '<h1>Hello, Class!</h1>'
>>>>>>> 9ee460c24db1e1a9422c00e9ff060ea080e4e59f


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
