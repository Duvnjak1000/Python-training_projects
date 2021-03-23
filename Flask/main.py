from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, SmartNinja!"


if __name__ == '__main__':
    app.run()

#Click on the http://127.0.0.1:5000/ link and your first web app will open in the Terminal.