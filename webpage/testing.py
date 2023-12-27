import psycopg2
url = "postgresql://mathobotix.irvine.lab:VBQRvxA2dP9i@ep-shrill-hill-95052366.us-west-2.aws.neon.tech/neondb?sslmode=require"
con = psycopg2.connect(url)
cur = con.cursor()
uname = "sadiasjdi"
pw = "sojsdg"

cur.execute("INSERT INTO people(id, pass) VALUES(%s, %s)", (uname, pw))
con.commit()
con.close()
