``` Valid Palindrome ```

<img width="597" alt="Screenshot 2023-11-18 at 11 36 54 AM" src="https://github.com/efloresz/FloresLeetcodeGuide/assets/110843762/7581f257-a41d-44b7-a1cb-85f99350df85">

```python
pseudo code # approach 1 not efficient 
# remove all non-alphanumeric chars
# convert string to lowercase
# get the length -> reverse the string
# check if string is the same reversed

Solution #1 -- uses built in functions and extra memory 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""

        for char in s:
            if char.isalnum():
                newString += char.lower()
        # string reversal
        return newString == newString[::-1]

psuedo code # approach 2 more efficient using two pointers
# left and right pointer -> check if chars are ==
# Eg. A_man : Panama
#     ^            ^  valid -> shift pointers
# continue incrementing left and decementing right until middle
# use ascii to determine if char is alphanumeric (while loop)

Solution #2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            while right > left and not self.isAlphanumeric(s[right]):
                right -= 1    
                
            if s[left].lower() != s[right].lower():
                return False   
            left, right = left + 1, right - 1      
        return True

    def isAlphanumeric(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

    
```

```python
# Difficulty: Easy

# Data Structures Used: Two Pointers

# Time Complexity: O(n) 

# Space Complexity: O(1)

```
