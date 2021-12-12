import pytest
import allure
import requests
import json


@allure.feature('test测试')
@allure.story('a测试')
def test_ihome_login():
    url = 'http://127.0.0.1:7890/api/v1.0/sessions'
    body = {
        "mobile": "13620228033",
        "password": "123456"
    }
    header = {
        'Content-Type': 'application/json'
    }
    ret = requests.post(url=url, data=json.dumps(body), headers=header).json()
    assert ret.get('errmsg') == '登录成功'


if __name__ == '__main__':
    pytest.main(['--alluredir', 'report/result', 'test001.py'])
