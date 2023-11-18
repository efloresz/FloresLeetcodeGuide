```Contains Duplicates ```

<img width="543" alt="Screenshot 2023-11-17 at 8 23 36 PM" src="https://github.com/efloresz/FloresLeetcodeGuide/assets/110843762/2a58d772-9e56-4513-b66e-8fdaffdfa51b">

```python
Solution:
# 1st approach: (Brute force) pick val and compare to rest of array
# ^ time: O(n^2) & space: O(1)
# 2nd approach: (Sorting) vals will be adjacent shift pointers iterate array once
# ^ time: O(nlogn) & space: O(1)
# 3rd approach most efficent: (HashSet) insert elements into set & check if val exists in map
# ^ time: O(n) & space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

```

```python
# Difficulty: Easy

# Data Structures Used: Arrays & Hashing

# Time Complexity: O(n)

# Space Complexity: O(n)

```
