'''
Name: Emily Flores
Purpose: Two Sum Problem
Date Started: 10-11-23
Date Modified: 10-11-23
'''

'''
NOTES: 
int nums[]
int target 
return indicies -> two nums a + b = target 
(X): can not use same element twice 
Eg: input nums = [2, 3, 6, 7, 5], target = 8
    output: [1, 4]
Explaination: The elements in index 1 = '3' and 4 = '5' add up to the target. 

Potential approache #1: pointers 
[2, 3, 6, 7, 5]
^            ^  -> [2, 5] = 7 (X)

[2, 3, 6, 7, 5]
    ^     ^  -> [3, 7] = 10 (X)
[2, 3, 6, 7, 5]
 ^  ^        -> [2, 3] = 5 (X)
 
[2, 3, 6, 7, 5]
    ^  ^     -> [3, 6] = 9 (X)

[2, 3, 6, 7, 5]
       ^  ^  -> [6, 7] = 13 (X)
[2, 3, 6, 7, 5]
          ^  ^  -> [7, 5] = 12 (X)
Limitations: 
# odd num array: what number would 6 be compared to? (can not use element twice)
# no two elements add to the target num 

Potential approach #2: Hash map ? Hash table ? 
TODO: explain logic and approach 

'''
