import pytest
import os

if __name__ == '__main__':
    print('m' * 50)
    pytest.main(['--alluredir', './report/xml', 'test002.py'])
    # split = 'allure' + 'generate' + '/Users/lijianpei/code/jenkins_test/testDemo/report/result' + '-o' + '/Users/lijianpei/code/jenkins_test/testDemo/report/html' + '--clean'
    print('-9-' * 50)
    split = 'allure generate ./report/xml -o ./report/html --clean'
    print('-0-' * 50)
    os.system(split)
