import unittest
from clock import Clock
from wgen import Wgen
import numpy as np

class TestWGEN(unittest.TestCase):
    def setUp(self):
        """Set up a new object to be tested"""
        self.rain_obs = [1.41, 1.68, 2.51, 3.63, 4.45, 4.15, 3.95,
                         2.84, 4.00, 3.12, 1.58, 1.66]
        self.min_temp_obs = [19.73, 24.25, 31.42, 44.59, 54.4, 63.32,
                         67.51, 65.65, 57.49, 46.77, 34.2, 24.88]
        self.max_temp_obs = [28.99, 33.75, 41.5, 55.37, 65.06, 73.66,
                             78.14, 76.57, 68.98, 58.03, 44.17, 33.45]
        self.avg_temp_obs = [38.24, 43.24, 51.57, 66.15, 75.71, 83.99,
                             88.77, 87.48, 80.46, 69.28, 54.13, 42.02]
        self.c = Clock()
        self.w = Wgen()
        self.precision = 1
    
    def tearDown(self):
        """Destroy the object after running tests"""
        del self.w
    
    def testDetermRain(self):
        """Check rain total using known chance of rain"""
        self.w.markov_deterministic = True
        realizations = 100
        rain_total = 0.0
        for r in range(0, realizations):
            self.w.update()
            rain_total += self.w.rain
        rain = rain_total / realizations
        self.assertAlmostEqual(rain, 0.15, self.precision)
    
    def testMonthlyRain(self):
        """Check cumulative rain avg"""
        rain_array = [0.0] * 12
        realizations = 5000
        self.w.min_rain = 0.0
        for r in range(1, realizations):
            self.c.reset()
            while self.c.running:
                month = self.c.current_date.month - 1
                self.w.update(self.c.current_date)
                rain_array[month] += self.w.rain
                self.c.advance()
        
        for i in range(0, 12):
            rain_array[i] /= realizations

        np.testing.assert_almost_equal(self.rain_obs, rain_array, decimal=1, err_msg='test', verbose=True)
        
        #for i in range(0, 12):
        #    self.assertAlmostEqual(rain_array[i], self.rain_obs[i], precision, "Month: " + str(i+1))

    def testAvgTemp(self):
        """Test max calc_temperature for 1 day"""
        
        # Below are daily average temps from deterministic GoldSim model
        # Each value taken from the 1st day of each month starting with Jan
        goldsim_tavg = [37.43, 19.04, 23.47, 33.7, 47.97, 63.43,
                        73.54, 74.41, 65.17, 50.55, 35.4, 24.74]
        self.w.temp_determ = True
        self.w.rain_deterministic = True
        self.w.markov_deterministic = True
        monthly_temps = []
        while self.c.running:
            self.w.update(self.c.current_date)
            if self.c.current_date.day == 1 and self.c.current_date.year == 2019:
                monthly_temps.append(self.w.tavg)
            self.c.advance()
        
        #self.assertSequenceEqual(monthly_temps, goldsim_tavg)
        np.testing.assert_almost_equal(goldsim_tavg, monthly_temps, decimal=1, err_msg='test', verbose=True)

if __name__ == '__main__':
    unittest.main()