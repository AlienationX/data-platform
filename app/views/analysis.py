#!/usr/bin/env python
# coding=utf-8


from flask import Blueprint, render_template

analysis = Blueprint("analysis", __name__)


@analysis.route("/")
def index():
    return render_template("analysis.html")
