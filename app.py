from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, Flask is running"


if __name__ == "__main__":
    app.run(debug=True)
