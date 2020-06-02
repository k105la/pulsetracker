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
        pulse.pulsebox_to_frames('FX4lQF6rwoc805hDjWBK9cECuro2')
        red = pulse.signal_diff()
        self.assertEqual(len(red), 200)


unittest.main()
