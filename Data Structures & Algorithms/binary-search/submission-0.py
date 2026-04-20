class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        l, r = 0, n - 1
        if nums[l] >= target or nums[r] < target:
            if nums[l] == target:
                return 0
            return -1
        while r - l > 1:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        if nums[r] == target:
            return r
        return -1
