import unittest
from hydrology.catchment import Catchment


class TestCatchment(unittest.TestCase):
    def setUp(self):
        """Set up a new object to be tested
            
            Compare results to Catchment Verification.gsm
        """
        self.area = 12600000.0
        self.c1 = Catchment(self.area, runoff_method='AWBM')
        self.precision = 1

    def tearDown(self):
        """Destroy the object after running tests"""
        del self.c1

    def testOutflow(self):
        """Outflow == defined value"""
        precip = 0.00654
        et = 0.00025
        q = 0

        for i in range(0, 11):
            q = self.c1.outflow(precip, et)

        self.assertAlmostEqual(q, 8321.71, self.precision)


if __name__ == '__main__':
    unittest.main()