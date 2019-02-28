#!/usr/bin/env python
# coding=utf-8


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        # DB_CONF={
        #     "host": "127.0.0.1",
        #     "port": 3306,
        #     "user": "root",
        #     "password": "root123",
        #     "database": "flaskr"
        # }
        # ENGINE_STR = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8".format(**DB_CONF)
    )

    # if test_config is None:
    #     app.config.from_pyfile("config")
    # else:
    #     app.config.from_mapping(test_config)
    db.init_app(app)

    @app.route("/hello")
    def hello():
        return "Hello World"

    # 注册蓝图
    from . import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")

    return app

# @before_app_request
# def print_time():
#     pass
#
# @alter_app_request
# def print_time():
#     pass
