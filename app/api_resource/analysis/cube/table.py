#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource
from flask_restful import reqparse
from app import db
from app.common.logger import get_logger
import pandas as pd
import numpy as np
import traceback
import time


class Api(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("col", help="column name")
        self.args = self.parser.parse_args()

        self.logger = get_logger(__name__)

    def get(self):
        try:
            df = pd.read_sql(sql="select * from information_schema.tables;", con=db.engine)
            # columns = df.columns.values.tolist()
            # df = df.replace({np.nan: None}).to_dict("record")
            #
            # data = {
            #     "columns": columns,
            #     "table": df
            # }

            data = df.replace({np.nan: None}).to_dict("split")
            data["jsgrid_data"] = df.replace({np.nan: None}).to_dict("record")
            data["jsgrid_fields"] = [{"name": x, "width": "200px"} for x in data["columns"]]
            # data["countTotal"] = max(data.index)
            time.sleep(1)
            return data
        except Exception as e:
            err_msg = traceback.format_exc()
            self.logger.error(err_msg)
            return {"err_msg": err_msg}, 400
