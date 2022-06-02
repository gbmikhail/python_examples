import unittest


def mul(a: int, b: int) -> int:
    return a * b


class MulTest(unittest.TestCase):
    def test_mul(self):
        a = mul(5, 4)
        self.assertEqual(a, 20)
