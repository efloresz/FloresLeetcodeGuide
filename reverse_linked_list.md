``` Reverse Linked List ```

<img width="449" alt="Screenshot 2023-11-25 at 5 47 39 PM" src="https://github.com/efloresz/FloresLeetcodeGuide/assets/110843762/f2e5f0a0-4f41-41cc-a486-d3c9c767e1f8">

```python
Solution:
# iterative approach (more efficent) T O(n), S O(1): 
# The middle stays the same, inital head is new tail
# iteratively -> two pointers
# null previous pointer and current pointer to head of list
# null   ->  0   ->  1   ->   2   ->   3   ->   4   ->   5  
# ^prev      ^ cur
# shift pointers until previous pointer is in initial list tail
# null   <-  0   <-  1   <-   2   <-   3   <-   4   <-   5  <-    null
#                                                        ^prev    ^ cur

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
```

```python
# Difficulty: Easy

# Data Structures Used: Linked List

# Time Complexity: O(n)

# Space Complexity: O(1)

```
