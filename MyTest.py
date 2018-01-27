'''
unittest
'''
import unittest
print(__name__)
class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('setUPClass')
    def setUp(self):
        print('setUP')
    def test_01register(self):
        print('test_01register')  
    def test_02login(self):
        print('test_02login')
    def tearDown(self):
        print('tearDown')
    
    @classmethod
    def tearDownClass(self):
        print('tearDownClass')

if __name__=='__main__':
    unittest.main(verbosity=2)
    
