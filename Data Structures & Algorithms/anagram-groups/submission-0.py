from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            chars = [0] * 26
            for char in string:
                chars[ord(char) - ord('a')] += 1
        
            groups[tuple(chars)].append(string)

        return list(groups.values())
