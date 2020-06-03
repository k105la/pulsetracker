import unittest
import pulse as p


class TestVariances(unittest.TestCase):
    """This test Class is variances()"""

    def test_variances(self):
        """
        This function assures that variances()
        returns a one dimensional matrix.
        """
        testing_uid = "1kzd0DmeunLGEeB0nWLFFaIfuFZn"
        pulse = p.Pulse()
        pulse.pulsebox_to_frames(testing_uid)
        v = pulse.variances()
        v_dim = v.reshape(-1, 1).shape[1]
        self.assertEqual(v_dim, 1)


unittest.main()
