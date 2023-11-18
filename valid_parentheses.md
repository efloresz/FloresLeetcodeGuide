``` Valid Parentheses ```

<img width="625" alt="Screenshot 2023-11-18 at 5 34 29 PM" src="https://github.com/efloresz/FloresLeetcodeGuide/assets/110843762/19e9b5d6-4213-4cc1-88fc-4dc3e8117a9e">


```python
Solution:
# must start with opening parenthesis ( , [ , {
# once parenthesis is closed remove from list
# close ending parenthesis -> pop opening from top of stack
# check HashMap for matching parenthesis
# if list is empty -> return true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False    
            else:
                stack.append(char)

        return True if not stack else False

```

```python
# Difficulty: Easy

# Data Structures Used: Stack

# Time Complexity: O(n)

# Space Complexity: O(n)

```
