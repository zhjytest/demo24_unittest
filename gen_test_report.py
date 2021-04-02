import unittest
# 2. 导入HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner

# 3. 定义一个测试报告的文件
report_file = "test_report.html"

# 4.创建套件
suite = unittest.TestLoader().discover('.',pattern='test*.py')


# 5. 生成一个runner
with open(report_file,'wb') as f:
    runner = HTMLTestRunner(f,title='测试报告',description='v1.2版本的测试报告')
    runner.run(suite)
