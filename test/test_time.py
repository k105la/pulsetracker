import heartrate as h
import time
import unittest

class TimeTest(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print(f'{self.id()}: {t}')

    # Test the speed of the heartrate algorithm 
    def testBPM(self):
        heart = h.HeartRate()
        heart.bpm() 

    # Test the time it takes to get frames from an input video
    def testVideoProcessing(self):
        heart = h.HeartRate()
        heart.video_to_frames()

if __name__ == '__main__':
    time_test = unittest.TestLoader().loadTestsFromTestCase(TimeTest)
    unittest.TextTestRunner(verbosity=0).run(time_test)
