# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/27 23:23
# 文件名：api.py
# 开发工具：PyCharm
import requests


class BaseApi(object):
    url = ""
    method = "GET"
    headers = {}
    params = {}
    data = {}
    json = {}

    def validate(self, key, expected_value):
        value = self.response
        for _key in key.split("."):
            print("value---------------", _key,value)
            if isinstance(value, requests.Response):
                value = getattr(value, _key)
            elif isinstance(value, requests.structures.CaseInsensitiveDict):
                value = value[_key]
        assert value == expected_value
        return self

    def set_data(self, data):
        self.data = data
        return self

    def set_json(self, json_data):
        self.json = json_data
        return self

    def set_params(self, **params):
        self.params = params
        return self

    def run(self):
        self.response = requests.request(
            self.method,
            self.url,
            params=self.params,
            headers=self.headers,
            data=self.data,
            json=self.json
        )
        return self