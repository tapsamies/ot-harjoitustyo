import unittest
from index import main


class TestMain(unittest.TestCase):
    def test_peli_palauttaa_false(self):
        peli = main()
        self.assertEqual(peli, False)
