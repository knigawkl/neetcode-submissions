class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we want to find the transition point
        # for instance in [3,4,5,6,1,2], 6->1
        # before region is where values >= nums[0]
        def is_before(i):
            return nums[i] >= nums[0]

        l, r = 0, len(nums) - 1
        if is_before(r):
            return nums[l]
        while r - l > 1:
            mid = (l + r) // 2
            if is_before(mid):
                l = mid
            else:
                r = mid
        return nums[r]
