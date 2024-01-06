import flask,requests,json,bcrypt, psycopg2, uuid
from configparser import ConfigParser

app = flask.Flask(__name__)
app.secret_key = uuid.uuid4().hex
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial'

key = bcrypt.kdf(
     password=b'password',
     salt=b'salt',
     desired_key_bytes=32,
     rounds=100)



@app.route("/")
def home_view():
    return flask.render_template("index.html")

@app.route("/reg")
def car_view():
    return flask.render_template("reg.html")



@app.route("/newreg", methods = ["POST"])
def cat_view():
    if flask.request.method == "POST":
        
        uname = flask.request.form["email"]
        pw1 = flask.request.form["password1"]
        pw2 = flask.request.form["password2"]
        if pw1 == pw2:
            hashed = bcrypt.hashpw(pw1.encode("utf-8"),  bcrypt.gensalt())
            url = "postgresql://mathobotix.irvine.lab:VBQRvxA2dP9i@ep-shrill-hill-95052366.us-west-2.aws.neon.tech/neondb?sslmode=require"
            con = psycopg2.connect(url)
            cur = con.cursor()
            cur.execute("SELECT * FROM people WHERE id = %s", (uname,))
            results = cur.fetchall()
            print(results)
            if len(results) > 0:
                con.close()
                return "User taken"


            cur.execute("INSERT INTO people(id, pass) VALUES(%s, %s)", (uname, hashed.decode("utf-8")))
            con.commit()
            con.close()
        else:
            return "Password does not match"
        print(uname)
        return {"status":200}

@app.route("/login", methods = ["POST"])
def dog_view():
    if flask.request.method == "POST":
        uname = flask.request.form["email"]
        pw = flask.request.form["pw"]
        url = "postgresql://mathobotix.irvine.lab:VBQRvxA2dP9i@ep-shrill-hill-95052366.us-west-2.aws.neon.tech/neondb?sslmode=require"
        con = psycopg2.connect(url)
        cur = con.cursor()
        cur.execute("SELECT * FROM people WHERE id = %s", (uname,))
        results = cur.fetchall()
        if len(results) > 0:
            results = results[0]
            if bcrypt.checkpw(pw.encode("utf-8"), results[1].encode("utf-8")):
                flask.session["uname"] = uname
                return flask.redirect("/dashboard")
            else:
                return "Passwords not match"
        else:
            return "No users found"
        
@app.route("/logout")
def tiger_view():
    flask.session.clear()
    return flask.redirect(flask.url_for("home_view"))
@app.route("/dashboard")
def squirrel_view():
    if(flask.session.get("uname")!= None):
        url = "postgresql://mathobotix.irvine.lab:VBQRvxA2dP9i@ep-shrill-hill-95052366.us-west-2.aws.neon.tech/neondb?sslmode=require"
        con = psycopg2.connect(url)
        cur = con.cursor()
        cur.execute("SELECT * FROM people WHERE id = %s", (flask.session["uname"],))
        results = cur.fetchall()
        if len(results) > 0:
            results = results[0]
        weatherinfo = weather(results[3])    
        if weatherinfo == None:
            weatherinfo = [0,0,0,0,0]
        con.close()
        return flask.render_template("user dashboard.html", uname = flask.session["uname"], phonenum = results[2], city = results[3], weather = weatherinfo)
    else:
        return flask.redirect(flask.url_for("home_view"))
@app.route("/updateinfo", methods = ["POST"])
def tree_view():
    if flask.request.method == "POST":
        phonenum = flask.request.form["pn"]
        city = flask.request.form["city"]
        url = "postgresql://mathobotix.irvine.lab:VBQRvxA2dP9i@ep-shrill-hill-95052366.us-west-2.aws.neon.tech/neondb?sslmode=require"
        con = psycopg2.connect(url)
        cur = con.cursor()
        cur.execute("UPDATE people SET phonenumber = %s, city = %s WHERE id = %s", (phonenum, city, flask.session["uname"]))
        con.commit()
        con.close()
        return flask.redirect(flask.url_for("squirrel_view"))
    
def weather(city):
    
      
    result = requests.get(url.format(city,api_key))
    if result:
        json = result.json()
        city = json['name']
        wind = json['wind']['speed']
        humidity = json['main']['humidity']
        min = json['main']['temp_min']
        max = json['main']['temp_max']
        country = json['sys']
        temp_farenheit = json['main']['temp']
        weather1 = json['weather'][0]['main']
        final = [city, country, round(temp_farenheit, 0), wind, humidity, min, max, weather1]
        return final
    else:
        return None