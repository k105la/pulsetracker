import unittest
import pulse as p

class SignalTest(unittest.TestCase):
	""" This test Class is for signal_diff()""" 
	def test_signal(self):
		""" 
		This function test to assure that signal_diff()
		returns a size of 200.
		"""
		pulse = p.Pulse()
		pulse.video_to_frames('./data/hr_test.mp4')
		red = pulse.signal_diff()
		self.assertEqual(len(red), 200)


if __name__ == '__main__':
	DIFF_TEST = unittest.TestLoader().loadTestsFromTestCase(SignalTest)
	unittest.TextTestRunner(verbosity=0).run(DIFF_TEST)
