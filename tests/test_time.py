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
        print("{}: {}".format(self.id(), t))

    def testSystemSpeed(self):
        """This function runs the entire heart rate system."""
        testing_video = "https://firebasestorage.googleapis.com/v0/b/pulse-box.appspot.com/o/data%2F1kzd0DmeunLGEeB0nWLFFaIfuFZn%2Fhr_test.MOV?alt=media&token=221ee115-5fb1-4c38-8264-5b1f8a859fda"
        pulse = p.Pulse()
        pulse.video_to_frames(testing_video)
        pulse.bpm()


unittest.main()
