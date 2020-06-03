import unittest
import pulse as p


class TestPeaks(unittest.TestCase):
    """Class for testing get_peaks()"""

    def test_get_peaks(self):
        """
        This function assures that get_peaks()
        returns a one dimentional matrix.
        """
        testing_uid = "1kzd0DmeunLGEeB0nWLFFaIfuFZn"
        pulse = p.Pulse()
        pulse.pulsebox_to_frames(testing_uid)
        peaks = pulse.get_peaks()
        peaks_dim = peaks.reshape(-1, 1).shape[1]
        self.assertEqual(peaks_dim, 1)


unittest.main()
