#!/usr/bin/env python
# coding=utf-8

# from flaskr import create_app
from app import create_app
import os
from config import config

app = create_app(config_name="development")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
