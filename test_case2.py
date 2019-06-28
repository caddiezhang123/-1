#!coding:utf-8
# from base.get_data import GetData
# from base.requests_method import RequestsMethod
# import pytest
# from base.get_conf import *
# from util.compare import *
# from util.operater_xlsx import OperaterXlsx
import requests


def add(url,data):
    result = requests.post(url=url,data=data)
    return result.json()

url = 'https://m.imooc.com/passport/user/login'
data = {'username': '18513199586', 'password': '111111', 'verify': '', 'referer': 'http://m.imooc.com'}
    # pytest.main('-s,test_case2.py')

    # url = 'https://m.imooc.com/passport/user/login'
    # data = {'username': '18513199586', 'password': '111111', 'verify': '', 'referer': 'http://m.imooc.com'}
    # result = requests.post(url=url, data=data)
    # print(result.json())