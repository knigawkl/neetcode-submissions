import math
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        missing = defaultdict(int)
        for c in t:
            missing[c] += 1
        distinct_missing = len(missing)
        cur_min = math.inf
        result = ''
        while True:
            must_grow = distinct_missing > 0
            if must_grow:
                if r == len(s):
                    break
                if s[r] in missing:
                    missing[s[r]] -= 1
                    if missing[s[r]] == 0:
                        distinct_missing -= 1
                r += 1
            else:
                if r - l < cur_min:
                    cur_min = r - l
                    result = s[l:r]
                # cur_min = min(cur_min, r - l)
                if s[l] in missing:
                    missing[s[l]] += 1
                    if missing[s[l]] == 1:
                        distinct_missing += 1
                l += 1
        return result
        # return cur_min if cur_min != math.inf else -1
        
