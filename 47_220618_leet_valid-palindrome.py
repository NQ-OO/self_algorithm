import re

  
def isPalindrome(s: str) -> bool:
    new_str = s.lower()
    new_str = re.sub('[^a-z0-9]', '', new_str)
    reversed_new_str = new_str[::-1]
    print(reversed_new_str)
    if new_str == reversed_new_str : 
      return True
    else : 
      return False


input = "A man, a plan, a canal: Panama"
print(isPalindrome(input))