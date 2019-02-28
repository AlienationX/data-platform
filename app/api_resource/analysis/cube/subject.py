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
        self.parser.add_argument("subject", required=True, help="must be input subject")
        self.args = self.parser.parse_args()

        self.logger = get_logger(__name__)

    def get(self):
        try:
            data_mart = {
                "fact_pay": "金额主题",
                "fact_sale": "销售主题",
                "fact_case": "病例主题",
                "fact_cus": "客户主题",
                "fact_pet": "宠物主题",
            }
            sql = """select '{}' as table_name,'{}' as subject""".format(self.args.subject, data_mart[self.args["subject"]])
            self.logger.debug(sql)
            rows = db.engine.execute(sql)
            for row in rows:
                self.logger.info(row)

            df = pd.read_sql(sql, db.engine)
            self.logger.info(df)

            df_rows = pd.read_sql(sql="select * from information_schema.tables;", con=db.engine)
            df_rows = df_rows.replace({np.nan: None}).to_dict("record")

            data = {
                "subjects": ["金额主题", "销售主题", "宠物主题", "客户主题", "病例主题"],
                "subject": "销售主题",
                "table_name": "fact_sale",
                "dim": {"宠物": ["种类", "品种"], "客户": ["年龄段", "省份", "城市"], "产品": ["一级目录"], "日期": ["年", "季", "月", "日"]},
                "fact": ["实付金额", "病例量", "消费新客", "消费老客"],
            }
            return data
        except Exception as e:
            err_msg = traceback.format_exc()
            self.logger.error(err_msg)
            return {"err_msg": err_msg}, 400
