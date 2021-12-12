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


if __name__ == '__main__':
    print('m' * 50)
    pytest.main(['--alluredir', './report/xml', 'test002.py'])
    # split = 'allure' + 'generate' + '/Users/lijianpei/code/jenkins_test/testDemo/report/result' + '-o' + '/Users/lijianpei/code/jenkins_test/testDemo/report/html' + '--clean'
    print('-9-' * 50)
    split = 'allure generate ./report/xml -o ./report/html --clean'
    print('-0-' * 50)
    os.system(split)


