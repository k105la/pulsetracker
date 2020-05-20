import unittest
import pulse as p

class GrayTest(unittest.TestCase):
    """This test Class is variances()"""
    def testFramesToGray(self):
        """
        This function assures that variances()
        returns a one dimensional matrix.
        """
        pulse = p.Pulse()
        pulse.video_to_frames('./data/hr_test.mp4')
        gray = pulse.frames_to_gray()
        self.assertEqual(len(gray), 300)


unittest.main()
