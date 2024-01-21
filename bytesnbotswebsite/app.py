from flask import render_template, url_for, redirect, Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def subPage(name):
    return render_template("url_for(f""{name}.html)")



if __name__ == "__main__":
    app.run(debug=True)