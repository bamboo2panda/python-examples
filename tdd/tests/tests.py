import unittest
import sys, os

sys.path.append(os.getcwd() + '/tdd')
from main import *


class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_mass(self):
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1590), 15)
        self.assertEqual(nitro_salt(800), 8)
    
    def test_nitro_salt_returns_integer(self):
        self.assertIsInstance(nitro_salt(1000), int)

    def test_nitro_salt_is_string_returns_integer(self):
        self.assertEqual(nitro_salt('1000'), 10)

    def test_nitro_salt_receives_alptha_string_returns_zero(self):
        self.assertEqual(nitro_salt('asdokahd'), 0)

if __name__ == '__main__':
    unittest.main()