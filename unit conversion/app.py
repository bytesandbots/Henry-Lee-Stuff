import flask
import conversion
app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")
@app.route("/convertUnits", methods = ['POST'])
def twist():
    if flask.request.method == "POST":
        value = float(flask.request.form.get('firstValue'))
        unit1 = flask.request.form.get('initialUnit')
        unit2 = flask.request.form.get('secondaryUnit')
        result = conversion.Conversion().convert(unit1, unit2, value)
        return "{} {} is equal to {} {} ".format(value, unit1, result, unit2)
    
    
    