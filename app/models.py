#!/usr/bin/env python
# coding=utf-8

from app import db


class RequestLog(db.Model):
    __tablename__ = "request_log"

    id = db.Column(db.Integer, db.Sequence('field_id'), primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    position = db.Column(db.Integer)
    f_type = db.Column(db.FieldType)  # The error is happening here.
    table_info = db.Column(db.Integer, db.ForeignKey('table_info.id'))
