import unittest
from palindrome import Palindrome

class PalindromeTest(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_fun_returns_8(self):
      self.assertEqual(palindrome.fun(8), 8)

    def test_is_palindrome(self):
      pal = Palindrome()
      self.assertTrue(pal.is_palindrome("mom"))
      self.assertTrue(pal.is_palindrome("Mom"))
      self.assertFalse(pal.is_palindrome("Fred"))
      self.assertFalse(pal.is_palindrome(""))
      self.assertFalse(pal.is_palindrome(33))
      self.assertFalse(pal.is_palindrome('z'))

if __name__ == '__main__':
    unittest.main()
