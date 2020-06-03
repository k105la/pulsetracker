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
        testing_uid = '1kzd0DmeunLGEeB0nWLFFaIfuFZn'
        pulse = p.Pulse()
        pulse.pulsebox_to_frames(testing_uid)
        pulse.bpm()

unittest.main()
