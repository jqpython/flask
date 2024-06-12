from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    mylist = [13, 12, 43, 55, 98, 75, 33, 239, 21]
    return render_template("index.html", mylist=mylist)


if __name__ == "__main__":
    app.run(debug=True)
