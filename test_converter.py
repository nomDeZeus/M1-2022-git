from unittest import TestCase

from converter import bin_to_dec, dec_to_bin


class Test(TestCase):
    def test_bin_to_dec_odd(self):
        bits = [0, 1, 1, 0, 1, 0, 1]  # 53
        expected = 53
        self.assertEqual(expected, bin_to_dec(bits))

    def test_bin_to_dec_even(self):
        bits = [1, 1, 0, 0, 0, 0]  # 48
        expected = 48
        self.assertEqual(expected, bin_to_dec(bits))

    def test_dec_to_bin_odd(self):
        n = 37
        expected = [1, 0, 0, 1, 0, 1]
        self.assertListEqual(expected, dec_to_bin(n))

    def test_dec_to_bin_eveb(self):
        n = 38
        expected = [1, 0, 0, 1, 1, 0]
        self.assertListEqual(expected, dec_to_bin(n))

    def test_dec_to_dec(self):
        n = 155
        self.assertEqual(n, bin_to_dec(dec_to_bin(n)))

    def test_bin_to_bin(self):
        bits = [1, 0, 0, 1, 1, 1, 1, 0]
        self.assertListEqual(bits, dec_to_bin(bin_to_dec(bits)))
