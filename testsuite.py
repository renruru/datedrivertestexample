import unittest
from alltestcases.test_login import UserActionTest


def suit():
    login = unittest.TestLoader().loadTestsFromTestCase(UserActionTest)
    
    # suite = unittest.TestSuite()
    # suite.addTest(UserActionTest('test_login'))
    # suite.addTest(UserActionTest('test_register'))
    # return suite
    return unittest.TestSuite([login])

if __name__ == '__main__': 
    runner = unittest.TextTestRunner()
    runner.run(suit())