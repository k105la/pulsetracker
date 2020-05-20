import unittest
import pulse as p 

class SignalTest(unittest.TestCase):
    """This test Class is for signal_diff()"""
    def test_signal_diff(self):
        """
        This function test to assure that
        signal_diff() returns a size of 200.
        """
        pulse = p.Pulse()
        pulse.video_to_frames('./data/hr_test.mp4')
        red = pulse.signal_diff()
        self.assertEqual(len(red), 200)


unittest.main()
