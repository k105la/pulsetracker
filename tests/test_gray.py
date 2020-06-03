import unittest
import pulse as p


class GrayTest(unittest.TestCase):
    """This test Class is variances()"""

    def testFramesToGray(self):
        """
        This function assures that variances()
        returns a one dimensional matrix.
        """
        testing_uid = "1kzd0DmeunLGEeB0nWLFFaIfuFZn"
        pulse = p.Pulse()
        pulse.pulsebox_to_frames(testing_uid)
        gray = pulse.frames_to_gray()
        self.assertEqual(len(gray), 300)


unittest.main()
