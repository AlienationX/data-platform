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
                "dims": [
                    {
                        "table": "dim_date",
                        "table_desc": "日期",
                        "columns": [
                            {"date": "日"},
                            {"weeknum17": "周(1~7)"},
                            {"weeknum54": "周(5~4)"},
                            {"zyear_month": "月"},
                            {"quarter": "季"},
                            {"zyear": "年"},
                        ]
                    },
                    {
                        "table": "dim_clinic",
                        "table_desc": "医院",
                        "columns": [
                            {"brand": "品牌"},
                            {"region": "大区"},
                            {"area": "区域"},
                            {"province": "省份"},
                            {"city": "城市"},
                            {"system": "系统"},
                            {"clinic_name": "医院名称"},
                        ]
                    },
                    {
                        "table": "dim_cus",
                        "table_desc": "客户维度",
                        "columns": [
                            {"cus_gender": "性别"},
                            {"cus_age_group": "年龄段"},
                            {"cus_province": "省份"},
                            {"cus_city": "城市"},
                            {"cus_source": "客户来源"},
                            {"cus_anonymous": "客户类型"},
                            {"cus_status": "是否启用"},
                        ]
                    }
                ],
                "facts": [
                    {
                        "table": "fact_pay",
                        "table_desc": "金额事实表",
                        "columns": [
                            {"accrual_basis": "全责发生制"},
                            {"payed_by_caishe": "现金"},
                            {"payed_by_card": "POS"},
                            {"payed_by_group": "团购"},
                            {"keep_account": "记账"},
                            {"cus_anonymous": "会员卡充值"},
                            {"cus_status": "会员卡消费"},
                            {"cus_anonymous": "押金充值"},
                            {"cus_status": "押金消费"},
                            {"cus_anonymous": "账户充值"},
                            {"cus_status": "账户消费"},
                        ]
                    }
                ]
            }
            return data
        except Exception as e:
            err_msg = traceback.format_exc()
            self.logger.error(err_msg)
            return {"err_msg": err_msg}, 400
