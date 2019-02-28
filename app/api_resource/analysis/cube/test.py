#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource
from flask_restful import reqparse
from app import db
from app.common.logger import get_logger
import pandas as pd
import numpy as np
import traceback


class Api(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("subject", help="testing")
        self.args = self.parser.parse_args()

        self.logger = get_logger(__name__)

    def get(self):
        df1 = pd.read_sql("select * from ttt", db.engine)
        # df1["registerdate"] = df1["registerdate"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S") if x is not pd.NaT else None)

        df1 = df1.replace({np.nan: None})
        for dtype in df1.dtypes:
            print(dtype)
        df1["birthday"] = df1["birthday"].apply(lambda x: x.strftime("%Y-%m-%d") if x is not None else None)
        df1["registerdate"] = df1["registerdate"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S") if x is not None else None)

        df2 = pd.read_sql("select * from clinic_accrual_reg_rate limit 12", db.get_engine(bind="xiaonuan")).replace({np.nan: None})

        # df3 = pd.read_sql("select brand,brand_code,clinic_name from data_xiaonuan_final.hospital_base_information", db.get_engine(bind="impala"))
        # print(df3)

        df4 = pd.read_sql("select part_dt, sum(price) as total_selled, count(distinct seller_id) as sellers from kylin_sales group by part_dt order by part_dt", db.get_engine(bind="kylin"))
        # print(df4)

        # data = {
        #     "local": df1.to_json(orient="records"),
        #     "xiaonuan": df2.to_json(orient="records"),
        #     "impala": df3.to_json(orient="records"),
        #     "kylin": df4.to_json(orient="records"),
        #     "testing": "I'm 中文测试"
        # }
        data = {
            "local": df1.to_dict("records"),
            "xiaonuan": df2.to_dict("records"),
            # "impala": df3[:12].to_dict("records"),
            "kylin": df4[:4].to_dict("records"),
            "testing": "I'm 中文测试"
        }

        return data
