#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from flaskr.db import get_db,get_engine
from flaskr.auth import login_required
import pandas as pd

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    db = get_db()
    posts = db.execute(
        "select p.id, p.title, p.body, p.created, p.author_id, u.username"
        "  from post p join user u on p.author_id = u.id"
        " order by p.created desc"
    ).fetchall()
    # sql = """
    # select p.id, p.title, p.body, p.created, p.author_id, u.username
    #   from post p join user u on p.author_id = u.id
    #  order by p.created desc
    # """
    # posts = pd.read_sql(sql=sql,con=get_engine()).to_dict("records")
    # print(posts)
    return render_template("blog/index.html", posts=posts)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "insert into post (title, body ,author_id)"
                "values (:title, :body, :author_id)",
                {"title": title, "body": body, "author_id": g.user["id"]}
            )
            db.commit()
            return redirect(url_for("blog.index"))
    return render_template("blog/create.html")


def get_post(id, check_author=True):
    post = get_db().execute(
        "select p.id, title, body, created, author_id, username"
        "  from post p join user u on p.author_id = u.id"
        " where p.id = :id",
        {"id": id}
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "update post set title = :title, body = :body"
                " where id = :id",
                {"title": title, "body": body, "id": id}
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute("delete from post where id = :id", {"id": id})
    db.commit()
    return redirect(url_for('blog.index'))
