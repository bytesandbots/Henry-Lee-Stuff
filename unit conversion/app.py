import flask
import conversion
app = flask.Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def conversion():
    if flask.request.method == "POST":
        unit1 = flask.request.form.get('unitOne')
        unit2 = flask.request.form.get('unitTwo')
        value = flask.request.form.get('firstValue')
        result = conversion.convert(unit1, unit2, value)
        return "{} is equal to {} {} {}".format(unit1, value, result, value)
    return flask.render_template("index.html")
    