import unittest
from test_demoa import TestDemoAdd

# 生成一个套件对象
#suite = unittest.TestLoader().discover(start_dir='.',pattern='test*.py')

suite = unittest.TestSuite()
suite.addTest(TestDemoAdd('test_add01'))
suite.addTest(TestDemoAdd('test_add02'))
suite.addTest(TestDemoAdd('test_add03'))

runner = unittest.TextTestRunner()
runner.run(suite)

