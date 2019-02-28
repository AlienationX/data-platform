#!/usr/bin/env python
# coding=utf-8

import logging.config


def get_logger(name=None):
    if "admin" in name:
        file_name = "admin"
    elif "analysis" in name:
        file_name = "analysis"
    elif "download" in name:
        file_name = "download"
    else:
        file_name = "app"

    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        # 日志格式
        "formatters": {
            "simple": {
                "format": "%(asctime)s %(levelname)s : %(message)s"
            },
            "standard": {
                "format": "%(asctime)s %(levelname)s %(name)s[line:%(lineno)d]: %(message)s"
            },
        },
        "handlers": {
            # 定义控制台日志的级别和样式
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "stream": "ext://sys.stdout"
            },
            # 定义INFO（以上)级别的日志处理器
            "info_file_handler_date": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "level": "INFO",
                "formatter": "standard",
                "filename": "app/log/{}_info.log".format(file_name),
                "when": "midnight",
                "interval": 1,
                "backupCount": 0,
                "encoding": "utf8"
            },
            # 定义ERROR（以上）级别的日志处理器
            "error_file_handler_size": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "standard",
                "filename": "app/log/{}_error.log".format(file_name),
                "maxBytes": 1024 * 1024 * 10,
                "backupCount": 20,
                "encoding": "utf8"
            }
        },
        # 定义不同name的logger的日志配置
        "loggers": {
            "admin": {
                "level": "DEBUG",
                "handlers": [
                    "info_file_handler_date",
                    "error_file_handler_size"
                ],
                "propagate": "no"
            },
            "analysis": {
                "level": "DEBUG",
                "handlers": [
                    "info_file_handler_date",
                    "error_file_handler_size"
                ],
                "propagate": "no"
            },
            "download": {
                "level": "DEBUG",
                "handlers": [
                    "info_file_handler_date",
                    "error_file_handler_size"
                ],
                "propagate": "no"
            },
        },
        #     定义全局日志配置
        "root": {
            "level": "DEBUG",
            "handlers": [
                "console",
                "info_file_handler_date",
                "error_file_handler_size"
            ]
        }
    }

    logging.config.dictConfig(log_config)
    return logging.getLogger(name)


logger = get_logger


# def create_logger(name=None):
#     """Get the ``'flask.app'`` logger and configure it if needed.
#
#     When :attr:`~flask.Flask.debug` is enabled, set the logger level to
#     :data:`logging.DEBUG` if it is not set.
#
#     If there is no handler for the logger's effective level, add a
#     :class:`~logging.StreamHandler` for
#     :func:`~flask.logging.wsgi_errors_stream` with a basic format.
#     """
#     logger = logging.getLogger(name)
#
#     if app.debug and logger.level == logging.NOTSET:
#         logger.setLevel(logging.DEBUG)
#
#     if not has_level_handler(logger):
#         logger.addHandler(default_handler)
#
#     return logger
#
# logger = create_logger