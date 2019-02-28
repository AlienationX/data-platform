#!/usr/bin/env python
# coding=utf-8


from flask import Blueprint, render_template

sample = Blueprint("sample", __name__)


@sample.route("/todos")
def todos():
    return render_template("sample/todos.html")


@sample.route("singleselection")
def single_selection():
    return render_template("sample/singleselection.html")


@sample.route("demo")
def demo():
    return render_template("sample/demo.html")


@sample.route("test")
def test():
    return render_template("sample/test.html")
