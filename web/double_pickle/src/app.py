import base64
import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return "有两个路由，长度都是4。"

@app.route('/calc', methods=['GET'])
def getFlag():
    payload = request.args.get("payload")
    pickle.loads(base64.b64decode(payload).replace(b'os', b'').replace(b'reduce', b'').replace(b'system', b'').replace(b'env', b'').replace(b'flag', b''))    #反序列化，字符替换,过滤。
    return "祝你成功~"

@app.route('/hint', methods=['GET'])
def hint():
    return "我写过滤防止骇客的时候感觉很困，不过没事，我过滤了很多，骇客们肯定打不进来。给你们看看我的杰作："+"\n"+"pickle.loads(base64.b64decode(payload).replace(b'os', b'').replace(b'reduce', b'').replace(b'system', b'').replace(b'env', b'').replace(b'flag', b''))"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
