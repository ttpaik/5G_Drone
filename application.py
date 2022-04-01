from flask import Flask, render_template
import sys
application = Flask(__name__)


@application.route("/")
def hello():
    return render_template("hello.html")

@application.route("/visualization")
def visualization():
    return render_template("visualization.html")

@application.route("/prediction")
def prediction():
    return render_template("prediction.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0')
