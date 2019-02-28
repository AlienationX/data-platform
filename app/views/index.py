#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template, request, session, redirect, url_for

index = Blueprint("index", __name__)


@index.route("/")
def home():
    return render_template("index.html")


@index.route("/login", methods=["GET", "POST"])
def login():
    context = {}
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        message = "所有字段都必须填写"
        if username and password:
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            # print(username, password)

            # user = models.User.objects.get(name=username)
            # if user.password == password:
            if username == "admin" and password == "admin":
                session["is_login"] = True
                session["user_id"] = -99
                session["user_name"] = username
                return redirect(url_for("index.home"))
            else:
                message = "Invalid username/password"

        context["message"] = message
        context["input_username"] = username
        context["input_password"] = password
    # else:
    #     session.flush()
    #     # if request.session.get("is_login", None):
    #     return render_template("index.html")
    return render_template("login.html", context=context)

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))
