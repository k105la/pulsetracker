import unittest
import pulse as p

class TestBPM(unittest.TestCase):
    """This test Class is for variances()"""
    def test_range_of_bpm(self):
        """
        This function assures that variances()
        returns a one dimensional matrix.
		"""
        testing_uid = '1kzd0DmeunLGEeB0nWLFFaIfuFZn'
        pulse = p.Pulse()
        pulse.pulsebox_to_frames(testing_uid)
        hr = pulse.bpm()
        self.assertTrue(int(hr) > 0 and int(hr) <= 220)


unittest.main()
