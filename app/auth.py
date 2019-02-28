#!/usr/bin/env python
# coding=utf-8

from flask import session, redirect


def login_required(func):
    def inner(*args, **kwargs):
        if not session.get("user_name"):
            return redirect("/login")
        return func(*args, **kwargs)

    return inner
