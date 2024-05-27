from flask import Flask
from flask import request
from urllib.parse import parse_qs
import json
from db import get_data

app = Flask(__name__)


# 路由
@app.route("/hello")
def hell0_world():
    get_data()
    return "hello world"


# <>里面是变量
@app.route("/hey/<username>")
def hey_jiujiu(username):
    return "hey %s" % username


# <>里面是变量,number 前面指定类型
@app.route("/my/<int:number>", methods=["GET"])
def hey_number(number):
    return "my %s" % (number + number)


@app.route("/test/my/first", methods=["POST"])
def first_post():
    data = request.get_json()
    print(data)
    get_name = data.get("name")
    print(get_name)

    return "yes"


# app.run()
# 放到服务器上，需要用这个代码


app.run(host="0.0.0.0", port=5000)
