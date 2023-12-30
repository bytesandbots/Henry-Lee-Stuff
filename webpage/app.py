import flask,requests,json,bcrypt, psycopg2

app = flask.Flask(__name__)
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
                return "Password match"
            else:
                return "Passwords not match"
        else:
            return "No users found"
        