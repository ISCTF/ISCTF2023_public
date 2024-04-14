from flask import Flask
from flask import request
from flask import config
from flask import session
from flask import make_response
from flask import render_template,render_template_string
from waf import waf
import base64
import pickle

app = Flask(__name__)

@app.route("/")
def Hello():
	html = '''<html>
	<head>
	<title>Welcome ISCTF</title>
	</head>
	<body>
	<h1>Hello CTFer,Welcome to ISCTF 排位赛联盟</h1>
	<br>
	<h2>了解你的撼胃者</h2>
	<img src={{url_for("static",filename="/img/1.jpg")}}>
	<h3>你知道我什么成分，来找我吧</h3>
	<br>
	<a href="/zhuwangxiagu"> 前往猪王峡谷</a>
	</body>
	</html>'''
	return render_template_string(html)

@app.route("/zhuwangxiagu",methods=["GET","POST"])
def pig():
	html = '''
	<html>
	<head>
	<title>猪王峡谷 排位赛联盟</title>
	</head>
	<body>
	<form action="/game" method="post" enctype="multipart/form-data">
		<p>选择你的角色</p>
		<input type="text" name="char" required>
		<input type="submit" value = "林肯死大头！">
	</form>
	</body>
	</html>
	'''
	return html

@app.route("/game",methods=["GET","POST"])
def game():
	name = request.form.get('char')
	# print(request.form)
	if name is None:
		name = "undefined"

	user = base64.b64encode(pickle.dumps({"name":name,"is_champion":0}))
	resp = make_response(render_template("game.html",name=name))
	resp.set_cookie('userInfo', user)
	return resp

@app.route("/champion")
def getflag():
	userInfoCookies = request.cookies.get('userInfo')
	if userInfoCookies is None:
		return "<h1>Bad Request</h1>",400
	user = base64.b64decode(userInfoCookies)
	if not waf(user):
		return "<h1>403 Forbidden a</h1>",403
	user = pickle.loads(user)
	if (champion := user.get("is_champion") is None) or (username := user.get("name") is None):
		return "<h1>You are Not TruE champion</h1>",401
	if champion != 1:
		return "<h1>You are Not TruE champion</h1>",401
	else:
		return f"<h1>Welcome champion: {name},But flag in f1__A_g.txt, Get it!</h1>"

app.run(host="0.0.0.0")