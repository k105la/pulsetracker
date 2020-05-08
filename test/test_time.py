import heartrate as h
import time
import unittest

class TimeTest(unittest.TestCase):
    # Test the speed of the heartrate algorithm 
    def testOne(self):
        heart = h.HeartRate()
        heart.bpm()

if __name__ == '__main__':
    time_test = unittest.TestLoader().loadTestsFromTestCase(TimeTest)
    unittest.TextTestRunner(verbosity=0).run(time_test)
