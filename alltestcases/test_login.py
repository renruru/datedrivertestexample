import unittest
from common.creat_driver import getdriver
import time
from common.manger_dir import getPngFileName
from ddt import ddt,data,unpack,file_data
import csv

def get_data_csv(filename):
    users = []
    with open(filename,'r',encoding = 'utf-8') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            users.append(row)
    return users

@ddt
class UserActionTest(unittest.TestCase):
    driver = getdriver()

    def setUp(self):
        self.driver.maximize_window()
        self.driver.get('http://118.31.19.120:3000/')

    @data(*get_data_csv('./testdates/userlogin.csv'))
    def test_login(self,username,password,excpetStatus,checkpoint):
        self.driver.find_element_by_partial_link_text('登录').click()
        self.driver.find_element_by_id('name').send_keys(username)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_id('pass').submit()
        okurl = self.driver.current_url
        self.assertEqual(okurl,"http://118.31.19.120:3000/")


        self.driver.find_element_by_partial_link_text('注册').click()
        self.driver.find_element_by_id('loginname').send_keys('testuser3')
        self.driver.find_element_by_id('pass').send_keys('123456')
        self.driver.find_element_by_id('re_pass').send_keys('123456')
        self.driver.find_element_by_id('email').send_keys('123456@123.com')
        self.driver.find_element_by_id('email').submit()


    def tearDown(self):
        current_time = time.time()
        self.driver.save_screenshot(getPngFileName)
        self.driver.delete_all_cookies()

    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    


if __name__ == '__main__':
    unittest.main()