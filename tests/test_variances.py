import unittest
import pulse as p

class VarianceTest(unittest.TestCase):
	""" This test Class is for variances()"""
	def test_variances(self):
		""" 
		This function assures that variances()
		returns a one dimensional matrix.
		"""
		pulse = p.Pulse()
		pulse.video_to_frames('./data/hr_test.mp4')
		v = pulse.variances()
		v_dim = v.reshape(-1, 1).shape[1]
		self.assertEqual(v_dim, 1)


if __name__ == '__main__':
	VARI_TEST = unittest.TestLoader().loadTestsFromTestCase(VarianceTest)
	unittest.TextTestRunner(verbosity=0).run(VARI_TEST)
