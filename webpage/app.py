import flask,requests,json,bcrypt, psycopg2

app = flask.Flask(__name__)

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
            hashed = bcrypt.hashpw(pw1, bcrypt.gensalt())
            url = "postgresql://mathobotix.irvine.lab:VBQRvxA2dP9i@ep-shrill-hill-95052366.us-west-2.aws.neon.tech/neondb?sslmode=require"
            con = psycopg2.connect(url)
            cur = con.cursor()
            cur.execute("INSERT INTO people(id, pass) VALUES(%s, %s)", (uname, pw1))
            con.commit()
            con.close()
        else:
            return "Password does not match"
        print(uname)
        return {"status":200}
