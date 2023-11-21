``` Binary Search ```

<img width="622" alt="Screenshot 2023-11-21 at 4 07 07 PM" src="https://github.com/efloresz/FloresLeetcodeGuide/assets/110843762/df24072d-2414-4be4-b676-9ef4e1ad504f">

```python
Solution:
# sorted input array: [ -1, 0, 3, 5, 9, 12]
#                               ^ ^
# target = 9; middle pointers by dividing L & R pointers by 2
# since it's sorted, all values to the left are smaller than target
# vise versa to the right are the values greater than target
# elimate left values  [ -1, 0, 3, 5, 9, 12]
#                        X   X  X  L  M  R      
# return index of M = 4

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else: 
                return middle    
        return -1
        
# fix overflow: take distance between pointers
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + ((right - 1 // 2)) # fixes overflow
            #middle = (left + left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else: 
                return middle    
        return -1
        
```

```python
# Difficulty: Easy

# Data Structures Used: Binary Search

# Time Complexity: O(log n)

# Space Complexity: O(n)

```
