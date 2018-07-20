def fun(num):
  return num

class Palindrome():
  def is_palindrome(self, source_string):
    # Need more code to handle all the tests we threw at it. Try your hand at making them pass!

    reverse_string = source_string[::-1]
    # print(reverse_string)
    return source_string == reverse_string
