import unittest 
import pulse as p 

class TestPeaks(unittest.TestCase):
    """Class for testing get_peaks()"""
    def test_get_peaks(self):
        """
        This function assures that get_peaks()
        returns a one dimentional matrix.
        """
        pulse = p.Pulse()
        pulse.video_to_frames('./data/hr_test.mp4')
        peaks = pulse.get_peaks()
        peaks_dim = peaks.reshape(-1, 1).shape[1]
        self.assertEqual(peaks_dim, 1)


unittest.main()
