import pytest
from funcDemo.Calc import Calc
import allure
import os
import subprocess


class TestClass():
    def setup(self):
        print('setup-----start')  # 一条用例输出一次

    def setup_class(self):
        print('setup_class-----start')  # 一条用例输出一次

    @allure.feature('allure测试')
    @allure.story('test001')
    def test001(self):
        c = Calc()
        a = c.add(2, 3)
        assert a == 5

    @allure.feature('allure测试')
    @allure.story('test002')
    def test002(self):
        c = Calc()
        a = c.jian(2, 3)
        assert a == 5

    @allure.feature('allure测试')
    @allure.story('test003')
    def test003(self):
        c = Calc()
        a = c.jian(2, 6)
        assert a == 5

    def teardown(self):
        print('teardown------end')  # 只运行类结束


# pytest.main(['test002.py'])
# path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
# print(path,'123456')



