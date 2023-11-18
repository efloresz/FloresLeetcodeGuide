```Valid Anagram ```

<img width="680" alt="Screenshot 2023-11-17 at 10 28 29 PM" src="https://github.com/efloresz/FloresLeetcodeGuide/assets/110843762/b42bf4b5-6179-4f46-a8b1-9f7789d128cb">

```python
Solution:
# same total and quantity of chars
# count occurances of each char in both strings
# array or HashMap for each string (more efficient)
# input: s = "anagram", t = "nagaram"
# Eg. key : value -> s = {a, 3}, {n, 1} & t = {a, 3}, {n, 1}
# check length & iterate through keys in 1 string and compare to 2nd map

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCount, tCount = {}, {}

        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        for char in sCount:
            if sCount[char] != tCount.get(char, 0):
                return False
        return True

```

```python
# Difficulty: Easy

# Data Structures Used: Arrays & Hashing

# Time Complexity: O(n)

# Space Complexity: O(n)

```
