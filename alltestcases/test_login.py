import unittest
from selenium import webdriver

class UserActionTest(unittest.TestCase):
    
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get('http://118.31.19.120:3000/signin')
        driver.find_element_by_id('name').send_keys('testuser5')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_id('pass').submit()
        okurl = driver.current_url
        self.assertEqual(okurl,"http://118.31.19.120:3000/")


    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()