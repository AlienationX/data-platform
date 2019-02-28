#!/usr/bin/env python
# coding=utf-8


class StatusCode(object):
    # class_name = "StatusCode"  # 类属性
    http_code = {}  # http code
    api_code = {}  # api code

    def __init__(self):
        # Informational 1xx
        self.http_code[100] = "Continue"
        self.http_code[101] = "Switching Protocols"
        self.http_code[102] = "Processing"

        # Successful 2xx
        self.http_code[200] = "OK"
        self.http_code[201] = "Created"
        self.http_code[202] = "Accepted"
        self.http_code[203] = "Non-Authoritative Information"
        self.http_code[204] = "No Content"
        self.http_code[205] = "Reset Content"
        self.http_code[206] = "Partial Content"
        self.http_code[226] = "IM Used"

        # Redirection 3xx
        self.http_code[300] = "Multiple Choices"
        self.http_code[301] = "Moved Permanently"
        self.http_code[302] = "Found"
        self.http_code[303] = "See Other"
        self.http_code[304] = "Not Modified"
        self.http_code[305] = "Use Proxy"
        self.http_code[307] = "Temporary Redirect"
        self.http_code[308] = "Permanent Redirect"

        # Client Error 4xx
        self.http_code[400] = "Bad Request"
        self.http_code[401] = "Unauthorized"
        self.http_code[402] = "Payment Required"
        self.http_code[403] = "Forbidden"
        self.http_code[404] = "Not Found"
        self.http_code[405] = "Method Not Allowed"
        self.http_code[406] = "Not Acceptable"
        self.http_code[407] = "Proxy Authentication Required"
        self.http_code[408] = "Request Time-out"
        self.http_code[409] = "Conflict"
        self.http_code[410] = "Gone"
        self.http_code[411] = "Length Required"
        self.http_code[412] = "Precondition Failed"
        self.http_code[413] = "Request Entity Too Large"
        self.http_code[414] = "Request-URI Too Large"
        self.http_code[415] = "Unsupported Media Type"
        self.http_code[416] = "Requested range not satisfiable"
        self.http_code[417] = "Expectation Failed"
        self.http_code[418] = "I\"m a teapot"
        self.http_code[422] = "Unprocessable Entity"
        self.http_code[423] = "Locked"
        self.http_code[424] = "Failed Dependency"
        self.http_code[426] = "Upgrade Required"
        self.http_code[428] = "Precondition Required"
        self.http_code[429] = "Too Many Requests"
        self.http_code[431] = "Request Header Fields Too Large"
        self.http_code[444] = "Connection Closed Without Response"
        self.http_code[451] = "Unavailable For Legal Reasons"
        self.http_code[499] = "Client Closed Request"

        # Server Error 5x
        self.http_code[500] = "Internal Server Error"
        self.http_code[501] = "Not Implemented"
        self.http_code[502] = "Bad Gateway"
        self.http_code[503] = "Service Unavailable"
        self.http_code[504] = "Gateway Time-out"
        self.http_code[505] = "HTTP Version Not Supported"
        self.http_code[506] = "Variant Also Negotiates"
        self.http_code[507] = "Insufficient Storage"
        self.http_code[509] = "Bandwidth Limit Exceeded"
        self.http_code[510] = "Not Extended"
        self.http_code[511] = "Network Authentication Required"
        self.http_code[599] = "Network Connect Timeout Error"

        # Server Error 6xx
        self.http_code[600] = "Unparseable Response Headers"

        # 正常
        self.api_code[0] = "成功"

        # 参数型错误
        self.api_code[1000] = "未知错误"
        self.api_code[1001] = "参数不能为空"
        self.api_code[1002] = "非法参数"
        self.api_code[1003] = "参数类型错误"
        self.api_code[1004] = "参数格式错误"
        self.api_code[1005] = "参数必须为整数"
        self.api_code[1006] = "参数值超出范围"
        self.api_code[1007] = "参数长度超出限制"

        # 身份验证相关
        self.api_code[2001] = "缺少参数"
        self.api_code[2002] = "Token错误"
        self.api_code[2003] = "签名值错误"
        self.api_code[2004] = "请求时间戳过期"
        self.api_code[2005] = "非法请求"
        self.api_code[2006] = "身份验证失败"
        self.api_code[2100] = "已经登录"
        self.api_code[2101] = "该用户不存在"
        self.api_code[2102] = "非登录状态"
        self.api_code[2103] = "该用户已存在"
        self.api_code[2104] = "用户信息需要完善"
        self.api_code[2105] = "用户名或密码错误"
        self.api_code[2106] = "没有权限"

        # 路由相关
        self.api_code[3001] = "指定模块不存在"
        self.api_code[3002] = "请求方法不存在"

        # 内容相关
        self.api_code[4001] = "没有数据"

        # 数据库相关
        self.api_code[5001] = "数据库连接错误"
        self.api_code[5101] = "没有数据库表格式定义"
        self.api_code[5102] = "数据库表格式定义错误"
        self.api_code[5103] = "数据项不符合数据库表字段类型"
        self.api_code[5104] = "数据库表非空字段没有传值"
        self.api_code[5105] = "数据项值不是可用的枚举值"
        self.api_code[5106] = "数据项值小于允许的最小值"
        self.api_code[5107] = "数据项值大于允许的最大值"
        self.api_code[5201] = "没有获取到数据"
        self.api_code[5203] = "数据库插入失败"
        self.api_code[5204] = "数据库更新失败"
        self.api_code[5205] = "数据库删除失败"
        self.api_code[5206] = "数据库查询失败"
        self.api_code[5207] = "数据读取发生异常"
        self.api_code[5208] = "数据写入发生异常"
        self.api_code[5209] = "数据更新发生异常"
        self.api_code[5210] = "数据删除发生异常"
        self.api_code[5211] = "数据没有更新"
        self.api_code[5212] = "重复操作"

        # 自动接口错误
        self.api_code[6001] = "中间层查询失败"
        self.api_code[6002] = "RPC框架返回有误"
        self.api_code[6003] = "数据源类型不一致"
        self.api_code[6004] = "中间件层请求已超时"

        # 队列缓存相关
        self.api_code[7001] = "进入队列失败"
        self.api_code[7001] = "缓存失败"

        # 其它
        self.api_code[8000] = "发送验证码失败"
        self.api_code[8100] = "找不到上传文件"
        self.api_code[8101] = "文件大小超出限制"
        self.api_code[8102] = "文件上传不完整"
        self.api_code[8103] = "找不到上传文件"
        self.api_code[8104] = "临时文件夹错误"
        self.api_code[8105] = "保存失败"
        self.api_code[8106] = "文件上传中止"
