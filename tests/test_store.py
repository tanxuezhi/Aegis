import unittest
from store import Store

class TestOutflowsCase(unittest.TestCase):
    def setUp(self):
        """Set up a new object to be tested"""
        self.store_name = "Reservoir01"
        init_quantity = 10.0
        self.capacity = 15.0
        self.s1 = Store(init_quantity, self.capacity)
        self.s1.name = self.store_name

        #print("Test: " + str(self.s1.getInstanceCount()))

    def tearDown(self):
        """Destroy the object after running tests"""
        #print("Tear down " + type(self.s1).__name__)
        del self.s1

    def testReducedOutflow(self):
        """Outflow < request when _quantity reaches lower bound"""
        inflow = 0.43
        request = 15.0
        self.s1.update(inflow, request)
        self.assertTrue(self, self.s1.outflow < request)

class TestStoreBoundsCase(unittest.TestCase):
    def setUp(self):
        """Set up a new object to be tested"""
        self.store_name = "Reservoir01"
        init_quantity = 10.0
        self.capacity = 15.0
        self.s1 = Store(init_quantity, self.capacity)
        self.s1.name = self.store_name

        #print("Test: " + str(self.s1.getInstanceCount()))

    def tearDown(self):
        """Destroy the object after running tests"""
        #print("Tear down " + type(self.s1).__name__)
        del self.s1

    def testName(self):
        """Check to make sure the name is correct"""
        self.assertEqual(self.s1.name, self.store_name)

    def testUpper(self):
        """Store _quantity == capacity when inflow causes overflow"""
        inflow = 7.43
        outflow = 0.03
        self.s1.update(inflow, outflow)
        self.assertEqual(self.s1._quantity, self.capacity)

    def testLower(self):
        """Store _quantity == 0.0 when outflow causes empty"""
        inflow = 0.43
        outflow = 10.438
        self.s1.update(inflow, outflow)
        self.assertEqual(self.s1._quantity, 0.0)

    def testSettingQuantity(self):
        """Make sure a new _quantity is limited to the store's bounds"""
        test_amount1 = self.s1.set_quantity(999.99)
        test_amount2 = self.s1.set_quantity(-100.0)
        test_amount3 = self.s1.set_quantity(13.8685)

        self.assertEqual(test_amount1, self.s1.capacity)
        self.assertEqual(test_amount2, 0.0)
        self.assertEqual(test_amount3, 13.8685)


if __name__ == '__main__':
    unittest.main()