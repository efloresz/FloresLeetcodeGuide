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
Eg: input nums = [2, 4, 6, 7, 5], target = 8
    output: [1, 4]
Explaination: The elements in index 1 = '4' and 4 = '5' add up to the target. 

Potential approache #1: pointers 
[2, 4, 6, 7, 5]
^            ^  -> [2, 5] = 7 (X)

[2, 4, 6, 7, 5]
    ^     ^  -> [4, 7] = 11 (X)
Limitations: 
# odd num array: what number would 6 be compared to? (can not use element twice)

Potential approach #2: Hash map ? Hash table ? 
TODO: explain logic and approach 

'''
