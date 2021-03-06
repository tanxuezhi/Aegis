import unittest
from water_manage.reservoir import Reservoir
import numpy as np
#TODO - fix reservoir tests!


class TestReservoir(unittest.TestCase):
    def setUp(self):
        """Set up a new object to be tested"""
        self.r1 = Reservoir()
        self.r1.water_level = 9.9
        self.r1.spillway_crest = 10.9

    def tearDown(self):
        """Destroy the object after running tests"""
        del self.r1
        
    def testVolumeEqualQuantity(self):
        self.assertEqual(self.r1.volume, self.r1.quantity)

    def testReducedOutflow(self):
        self.r1.inflow = 10
        for i in range(10):
            self.r1.update()
            
        self.assertAlmostEqual(self.r1.volume, 273.25, 2)

    def testChangeCapacityOverflow(self):
        """Test that volume == capacity when updated capacity is
                changed to be less than the current volume
        """
        updated_capacity = 25.0
        self.r1.capacity = updated_capacity
        self.assertEqual(self.r1.capacity, updated_capacity)
    
    def testExcessInflowOverflow(self):
        """Test that volume == capacity after update when:
                - inflow + outflow + initial volume > capacity
        """
        self.r1.capacity = 25.0
        self.r1.requests[0].amount = np.random.random() + 2.0
        self.r1.update()
        self.r1.inflow = 5.0 + np.random.random()
        self.r1.update()
        self.assertEqual(self.r1.volume, self.r1.capacity)
        
    def testLevelOutput(self):
        """Test that correct water level is reported."""
        water_level_expected = 9.9
        self.assertEqual(water_level_expected, self.r1.water_level)
        
    def testUpdateLevel(self):
        """Test that correct volume is reported after updating level."""
        new_water_level = 3.4
        self.r1.water_level = new_water_level
        volume_expected = 59.5
        self.assertAlmostEqual(volume_expected, self.r1.volume, 2)

    def testAreaOutput(self):
        """Test that correct pool area is reported."""
        self.r1.water_level = 12.52
        self.assertAlmostEqual(self.r1.area, 38.276, 2)

    def testEvaporation(self):
        """Check the evaporation outflow rate."""
        evap_rate = 0.0155      # m/day
        expected_volume = 172.71   # m3
        self.r1.evaporation = evap_rate
        self.r1.update()
        self.assertAlmostEqual(self.r1.volume, expected_volume, 2)