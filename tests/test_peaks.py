import unittest
import numpy as np
import pulse as p

class PeaksTest(unittest.TestCase):
	"""Class for testing get_peaks()"""
	def test_get_peaks(self):
		"""
		This function assures that get_peaks() 
		returns a one dimensional matrix.	
		"""
		pulse = p.Pulse()
		pulse.video_to_frames('./data/hr_test.mp4')
		peaks = pulse.get_peaks()
		peaks_dim = peaks.reshape(-1, 1).shape[1]
		self.assertEqual(peaks_dim, 1)


if __name__ == '__main__':
	PEAKS_TEST = unittest.TestLoader().loadTestsFromTestCase(PeaksTest)
	unittest.TextTestRunner(verbosity=0).run(PEAKS_TEST)
