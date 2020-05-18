import time
import unittest
import pulse as p


class TimeTest(unittest.TestCase):    
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('{}: {}'.format(self.id(), t))

    def testVideoProcessing(self):
        pulse = p.Pulse()
        pulse.bpm()

if __name__ == '__main__':
    time_test = unittest.TestLoader().loadTestsFromTestCase(TimeTest)
    unittest.TextTestRunner(verbosity=0).run(time_test)
