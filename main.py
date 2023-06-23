
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/cables", strict_slashes=False)
def cables():
    return render_template("cables.html")


@app.get("/contact", strict_slashes=False)
def contact():
    return render_template("contact.html")


@app.post("/forms/contact", strict_slashes=False)
def formsContact():
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
