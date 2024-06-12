from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, Flask is running"


@app.route("/home")
def hello():
    return "from home"


@app.route("/greet/<name>")  # url processor or dynamic urls
def greet(name):
    return f"Hello {name}"


@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


@app.route("/handle_url_parameter")
def handle():
    if "greetings" in request.args.keys() and "name" in request.args.keys():
        greetings = request.args["greetings"]
        name = request.args["name"]
        return f"{greetings}, {name}"
    else:
        return "Something is missing"


if __name__ == "__main__":
    app.run(debug=True)
