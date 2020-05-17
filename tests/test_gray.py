import unittest
import pulse as p

class GrayTest(unittest.TestCase):
    def testFramesToGray(self):
        pulse = p.Pulse()
        pulse.video_to_frames('./data/hr_test.mp4')
        gray = pulse.frames_to_gray()
        self.assertEqual(len(gray), 300)


if __name__ == '__main__':
    frame_count_test = unittest.TestLoader().loadTestsFromTestCase(GrayTest)
    unittest.TextTestRunner(verbosity=0).run(frame_count_test)
