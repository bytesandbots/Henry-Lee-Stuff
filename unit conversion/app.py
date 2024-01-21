import flask
import conversion
import requests
app = flask.Flask(__name__)
BASE_URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_wjkuyywumTDkUReNACdX5hWJTFfjaZSoQxEAM16E&currencies={}&base_currency={}"

def convert(value:float, target:str, base : str):
        r = requests.get(BASE_URL.format(target, base))
        rate = r.json()['data'][target]
        result = value*rate
        return "{} {} is equal to {} {}".format(value, base, result, target)

@app.route("/", methods = ['GET','POST'])
def home():
    if flask.request.method == 'GET':
        return flask.render_template("index.html")
    elif flask.request.method == 'POST':
        value = float(flask.request.form.get('value'))
        base = str(flask.request.form.get('base'))
        target = str(flask.request.form.get('target'))
        return convert(value, base, target)
        

    
        
    #     value = float(flask.request.form.get('value'))
    #     base = str(flask.request.form.get('base'))
    #     target = str(flask.request.form.get('target'))
    #     r = requests.get(BASE_URL.format(target, base))
    #     rate = r.json()['data'][target]
    #     result = value*rate
    #     return "{} {} is equal to {} {}".format(value, base, result, target)


# @app.route("/")
# def home():
#     return flask.render_template("index.html")
# @app.route("/convertUnits", methods = ['POST'])
# def twist():
#     if flask.request.method == "POST":
#         value = float(flask.request.form.get('firstValue'))
#         unit1 = flask.request.form.get('initialUnit')
#         unit2 = flask.request.form.get('secondaryUnit')
#         print(value,unit1,unit2)
#         result = conversion.Conversion().convert(unit1, unit2, value)
#         return "{} {} is equal to {} {} ".format(value, unit1, result, unit2)
    
    
    