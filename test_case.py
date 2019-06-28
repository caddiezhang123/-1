#!coding:utf-8
from base.get_data import GetData
from base.requests_method import RequestsMethod
import pytest
from base.get_conf import *
from util.compare import *
from util.operater_xlsx import OperaterXlsx

class Test_requests:

    data = tuple(conf_case1())

    @pytest.mark.parametrize("row,url,method,data,expect",data)
    def test_case1(self,row,url,method,data,expect):
        result = str(RequestsMethod(url,method,data).run_main())
        if expect in result:
            OperaterXlsx().write_res(row,"pass")
        else:
            OperaterXlsx().write_res(row, "fail")

if __name__=="__main__":
    pytest.main(["-s","test_case.py"])







