# from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}                # key:[26*0] -> [str]

        for s in strs:          # loop strings
            l = [0] * 26
            for c in s:         # loop character
                l[ord(c) - ord("a")] += 1
            
            key = tuple(l)      # A list cannot be a dictionary key
            if key not in res:
                res[key] = [s]
            else:
                res[key].append(s)
            
        return list(res.values())