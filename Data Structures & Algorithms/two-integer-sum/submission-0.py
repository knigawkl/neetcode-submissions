class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_pos = dict()
        for pos, num in enumerate(nums):
            diff = target - num
            if diff in val_to_pos:
                return [val_to_pos[diff], pos]
            val_to_pos[num] = pos
