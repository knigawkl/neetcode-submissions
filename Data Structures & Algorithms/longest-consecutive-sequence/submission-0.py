class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        result = 0

        for num in unique:
            if (num - 1) not in unique:
                current = 1
                while (num + current) in unique:
                    current += 1
                result = max(result, current)
        return result