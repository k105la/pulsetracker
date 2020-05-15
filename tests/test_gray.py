import unittest
import heartrate as h

class GrayTest(unittest.TestCase):
    def testFramesToGray(self):
        heart = h.HeartRate()
        heart.video_to_frames('./data/hr_test.mp4')
        gray = heart.frames_to_gray()
        self.assertEqual(len(gray), 300)


if __name__ == '__main__':
    frame_count_test = unittest.TestLoader().loadTestsFromTestCase(GrayTest)
    unittest.TextTestRunner(verbosity=0).run(frame_count_test)
