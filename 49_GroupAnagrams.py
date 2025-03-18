# from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}                # key:[26*0] -> [str]

        for s in strs:
            l = [0] * 26
            for c in s:         # loop char
                l[ord(c) - ord("a")] += 1
            
            key = tuple(l)      # convert character to idx(0-25)
            if key not in res:
                res[key] = [s]
            else:
                res[key].append(s)
            
        return list(res.values())