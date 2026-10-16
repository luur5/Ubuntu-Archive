from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/stories")
def stories():
    return render_template("stories.html")


@app.route("/stories/lion")
def lion():
    return render_template("lion.html")


@app.route("/stories/rainqueen")
def rainqueen():
    return render_template("rainqueen.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)