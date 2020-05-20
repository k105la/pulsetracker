import time
import unittest
import pulse as p


class TimeTest(unittest.TestCase):
    """This Class tests the whole systems time speed.""" 
    def setUp(self):
        """Setup function"""
        self.startTime = time.time()

    def tearDown(self):
        """This function gets called after setUp() succeeds."""
        t = time.time() - self.startTime
        print('{}: {}'.format(self.id(), t))

    def testSysetemSpeed(self):
        """This function runs the entire heart rate system."""
        pulse = p.Pulse()
        pulse.video_to_frames('./data/hr_test.mp4')
        pulse.bpm()


unittest.main()
