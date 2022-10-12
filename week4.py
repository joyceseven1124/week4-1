# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:05:49 2022

@author: 劉佳怡
"""

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session


app = Flask(__name__,static_folder="static" ,static_url_path = "/static")
app.secret_key = "no"

@app.route("/")
def form():
    state = "未登入"
    session["state"] = state
    return render_template("首頁.html")

   
@app.route("/signin",methods=["POST"])
def signin():
    input_account = request.form["account"]
    input_password = request.form["password"]
    if input_account == 'test' and input_password == 'test':
        state = "已登入"
        session["state"] = state
        return redirect("/member")
    elif input_account == '' or input_password == '':
        state = "未登入"
        session["state"] = state
        return redirect("/error?message=empty")
    else:
        state = "未登入"
        session["state"] = state
        return redirect("/error")


@app.route("/square/<number>")
def square(number):
    total = int(number)*int(number)
    return render_template("計算.html", result = total )
    
@app.route("/member")
def success():
    if session["state"] == "已登入":
        return render_template("成功.html")
    else:
        return redirect("/")
    
@app.route("/error")
def fail():
    message = request.args.get("message",None)
    if message == "empty":  
        return render_template("失敗.html",message="請輸入帳號、密碼")
    else:
        return render_template("失敗.html",message="帳號、或密碼輸入錯誤")
    
@app.route("/signout")
def signout():
    state = session["state"]
    state.replace("已登入","未登入")
    session["state"] = state
    return redirect("/")

app.run(port=3000)