class Palindrome:
  @staticmethod
  def is_palindrome(word):
    i = len(word) - 1
    for c in word:
        if c.lower() != word[i].lower():
            return False
        i -= 1
    return True
word = input()
print(Palindrome.is_palindrome(word))