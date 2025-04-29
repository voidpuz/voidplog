from unittest import TestCase

def func():
    return "Hello"


class MytestCase(TestCase):
    def test_func(self):
        self.assertEqual(func(), "Hello")
        self.assertNotEqual(func(), "Hello")