import unittest
from cnodeClub import CnodeJS
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
class CnodeTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('setUPClass...')

    def setUp(self):
        print('setUP...')

    def test_a_login(self):
        assertuserName = CnodeJS().login(driver, 'doudou','12341234')
        self.assertEqual('doudou',assertuserName)

    def test_b_login(self):
        assertuserName = CnodeJS().login(driver,'helloworld','123456')
        self.assertEqual(loginUserName,assertuserName)
    # 发布帖子
    def test_c_postAtopic(self):
        nodejs = CnodeJS()
        nodejs.login(driver, "helloworld", '123456')
        assertTitle = nodejs.createATopic(driver, '今天是周五啦', '周末要开始啦，好开心啊！！')
        self.assertEqual(title1,assertTitle)
    # 删除帖子
    def test_deleteTopic(self):
        pass

    def tearDown(self):
        driver.save_screenshot('xxx.png')
        driver.delete_all_cookies()


    @classmethod
    def tearDownClass(self):
        # driver.quit()

    


def main():
    unittest.main()

if __name__ == '__main__':
    main()
