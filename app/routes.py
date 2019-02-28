#!/usr/bin/env python
# coding=utf-8

from flask_restful import Api
from flask import make_response, jsonify
from app.common.logger import get_logger
from app.common.status_code import StatusCode
import os

logger = get_logger(__name__)


def api_route(app):
    apis_folder = "api_resource"
    apis_path = os.path.join(os.path.dirname(__file__), apis_folder)
    app_names = [x for x in os.listdir(apis_path) if os.path.isdir(os.path.join(apis_path, x)) and x != "__pycache__"]

    logger.info("app_names" + str(app_names))

    api = Api(app)
    api.representations['application/json'] = output_json

    for app_name in app_names:
        # import_string = "from app.%s import %s as apis" % (apis_folder, app_name)
        # print(import_string)
        # exec(import_string)
        # apis_path = os.path.dirname(__file__)
        packages = [x for x in os.listdir(os.path.join(apis_path, app_name)) if os.path.isdir(os.path.join(apis_path, app_name, x)) and x != "__pycache__"]

        for package in packages:
            package_path = os.path.join(apis_path, app_name, package)
            if not os.path.isdir(package_path):
                continue
            files = os.listdir(package_path)
            for file in files:
                file_name = file[:-3]
                file_type = file[-3:]
                if file_name == "__init__" or file_type != ".py":
                    continue
                else:
                    resource = file_name

                model_str = "{}.{}.{}.{}.{}".format("app", apis_folder, app_name, package, resource)
                print("model_str", model_str)
                # model_name = __import__(model_str, globals(), locals(), "Api")
                model_name = __import__(model_str, fromlist=[resource])
                url_name = "/api/{app_name}/{package}/{resource}".format(app_name=app_name, package=package, resource=resource)
                class_name = resource.capitalize()
                print(model_name, url_name, class_name)
                api.add_resource(model_name.Api, url_name, endpoint=class_name)


def output_json(data, code, headers=None):
    res = {
        "status_code": code,
        "message": StatusCode().http_code[code],
        "result": data
    }
    resp = make_response(jsonify(res), code)
    resp.headers.extend(headers or {})
    return resp
