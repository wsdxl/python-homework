import unittest

class MyTest1(unittest.TestCase):
    def test_up(self):
        self.assertEqual('foo'.upper(),'FOO')
    def test_isUp(self):
        self.assertTrue('FOO'.isupper())  
        self.assertFalse('foo'.isupper())  
    
    def test_split(self):
        s='hello world'
        self.assertEqual(s.split(),['hello','world'])

if __name__=='__main__':
    unittest.main(verbosity=2)
    