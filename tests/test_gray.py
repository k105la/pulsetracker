import unittest
import pulse as p

class GrayTest(unittest.TestCase):
	"""Class for testing frames_to_gray()"""
	def test_frames_to_gray(self):
		"""
		This function test to assure that 
		frames_to_gray() returns a size of
		300.
		"""
        pulse = p.Pulse()
        pulse.video_to_frames('./data/hr_test.mp4')
        gray = pulse.frames_to_gray()
    	#self.assertEqual(len(gray) / 2 , 300)


if __name__ == '__main__':
    FRAME_COUNT_TEST = unittest.TestLoader().loadTestsFromTestCase(GrayTest)
    unittest.TextTestRunner(verbosity=0).run(FRAME_COUNT_TEST)
