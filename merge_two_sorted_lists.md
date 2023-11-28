``` Merge Two Sorted Lists ```

<img width="492" alt="Screenshot 2023-11-27 at 9 47 18 PM" src="https://github.com/efloresz/FloresLeetcodeGuide/assets/110843762/44655bba-600a-4f91-9d06-68345afbc48c">

```python
# L1:  1  ->  2  ->  4
# L2: 1  ->   3  ->  4
# Since lists are already sorted, start at the beginning
# output is initially empty = edge case; create dummy node
# output ->  dummy_node  ->  1  ->  1  ->  2 ->  3  -> 4  -> 4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        tail = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next  
            tail = tail.next    
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2              
        return dummy_node.next    
        
```

```python
# Difficulty: Easy

# Data Structures Used: Linked List

# Time Complexity: O(n + m) -> lengths of the two input lists

# Space Complexity: O(1)

```
