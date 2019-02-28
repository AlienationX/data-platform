#!/usr/bin/env python
# coding=utf-8

from flask import current_app, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    db_conf = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "root",
        "database": "flaskr"
    }
    engine_str = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8".format(**db_conf)
    engine = create_engine(engine_str)
    return engine


def get_db():
    # 选择使用session
    if "db" not in g:
        DB_Session = sessionmaker(bind=get_engine())
        g.db = DB_Session()

    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
