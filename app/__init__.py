#!/usr/bin/env python
# coding=utf-8

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from app.routes import api_route
from app.common.logger import get_logger

db = SQLAlchemy()
logger = get_logger(__name__)


def create_app(config_name=None):
    # instance_relative_config 使用instance实例文件夹
    app = Flask(__name__, instance_relative_config=True)

    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

    if config_name:
        app.config.from_object(config[config_name])
    else:
        app.config.from_object(config["default"])

    app.config.from_pyfile('settings.py')

    # config[config_name].init_app(app)
    db.init_app(app)

    # 注册蓝图
    from app.views import index
    from app.views import download
    from app.views import analysis
    from app.views import sample

    app.register_blueprint(index.index, url_prefix="/")
    app.register_blueprint(analysis.analysis, url_prefix="/analysis")
    app.register_blueprint(download.download, url_prefix="/download")
    app.register_blueprint(sample.sample, url_prefix="/sample")

    # app.add_url_rule("/", endpoint="index")
    # 注册api路由
    logger.info("add api")
    api_route(app)
    logger.info("add api done")

    @app.before_request
    def before_request():
        logger.info("before request do something...")

    @app.after_request
    def after_request(response):
        """参数和返回值必须有"""
        logger.info("after request do something...")
        return response

    # @app.teardown_request
    # def teardown_request():
    #     print("teardown")

    # @app.errorhandler(404)
    # def page_not_found(e):
    #     print(e)
    #     return render_template("404.html")

    logger.debug(app.config["APP_NAME"])
    logger.debug(app.config["SECRET_KEY"])
    app.logger.info("testing logging")

    # 修改jinja模版语言的分隔符，避免和vue的冲突
    app.jinja_env.variable_start_string = "[["
    app.jinja_env.variable_end_string = "]]"

    return app
