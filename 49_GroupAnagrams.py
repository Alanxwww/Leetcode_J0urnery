# from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}  # Use a regular dictionary instead of defaultdict

        for s in strs:
            count = [0] * 26  # Initialize character count array            
            for c in s:
                count[ord(c) - ord('a')] += 1  # Convert character to index and update count
            
            key = tuple(count)  # Convert count list to a tuple (hashable)
            
            if key not in res:  # Check if key exists
                res[key] = []  # Initialize empty list if key is not present
            
            res[key].append(s)  # Append string to the correct group
        
        return list(res.values())  # Return the grouped anagrams