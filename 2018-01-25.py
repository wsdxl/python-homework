import unittest
import HTMLReport

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
    def test_03topic(self):
        print('test_03topic')
    def tearDown(self):
        print('tearDown')
    
    @classmethod
    def tearDownClass(self):
        print('tearDownClass')

def suite():
    suite=unittest.TestSuite()
    suite.addTest(MyTest('test_01register'))
    suite.addTest(MyTest('test_02login'))
    suite.addTest(MyTest('test_03topic'))
    return suite
if __name__=='__main__':
    suite()
    runner=HTMLReport.TestRunner(
        report_file_name='test',  # 报告文件名，默认“test”
        output_path='report',  # 保存文件夹名，默认“report”
        verbosity=2,  # 控制台输出详细程度，默认 2
        title='测试报告',  # 报告标题，默认“测试报告”
        description='无测试描述',  # 报告描述，默认“无测试描述”
        thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
        sequential_execution=True  # 是否按照套件添加(addTests)顺序执行，
                               # 会等待一个addTests执行完成，再执行下一个，默认 False                   
    )
    runner.run(suite())

