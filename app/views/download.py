#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template

download = Blueprint("download", __name__)


@download.route("/")
def index():
    # return "This is download page!"
    return render_template("download.html")
