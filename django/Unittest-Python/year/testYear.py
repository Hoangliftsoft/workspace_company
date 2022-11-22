import unittest
import year

class TestYear(unittest.TestCase):
    def test_year_true(self):
        self.assertEqual(year.isLeafYear(2000),True)
        self.assertEqual(year.isLeafYear(2004),True)
        self.assertEqual(year.isLeafYear(1960),True)
        self.assertEqual(year.isLeafYear(1920),True)
        

    def test_year_false(self):
        self.assertEqual(year.isLeafYear(1900),False)
        self.assertEqual(year.isLeafYear(2003),False)
        self.assertEqual(year.isLeafYear(1962),False)
        self.assertEqual(year.isLeafYear(1922),False)
        
if __name__ == '__main__':
    unittest.main(verbosity=1)
    