
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cables", strict_slashes=False)
def cables():
    return render_template("cables.html")


if __name__ == "__main__":
    app.run(debug=True)
