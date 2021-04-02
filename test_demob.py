import unittest

# 加法操作
def mul(x,y):
    z = x * y
    return z


# 最原始的测试方式
"""
print(add(3,4) == 7)
print(add(3,4) == None)
print(add(1.2,4.5) == 5.7)
"""
"""
# 断言 ： 两个值进行比较，
测试断言: 预期结果和实际结果进行比较 
"""


class TestDemoAdd1(unittest.TestCase):


    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("===============执行setUpClass方法===========")
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("===============执行tearDownClass方法===========")

    # def setUp(self) -> None:
    #     print("===============执行setUp方法===========")
    #
    # def tearDown(self) -> None:
    #     print("===========执行tearDown方法============")

    def test_add01(self):
        print("====执行test_add01======")
        self.assertEqual(12,mul(3,4))

    def test_add02(self):
        print("====执行test_add02======")
        self.assertEqual(4.7,mul(1.2,4))

    # def test_add03(self):
    #     print("====执行test_add03======")
    #     self.assertEqual(5.7,add(1.2,4.5))
    #     #self.assertIsNone()


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(TestDemoAdd1('test_add01'))

    runner = unittest.TextTestRunner()
    runner.run(suite)