class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtracking
        res = []
        current = []

        def visit(i, current_sum):
            if current_sum == target:
                res.append(current[:]) # shallow copy
                return
            if current_sum > target or i == len(nums):
                return

            # reuse current number
            current.append(nums[i])
            visit(i, current_sum + nums[i])
            current.pop()

            # exclude current number
            visit(i + 1, current_sum)

        visit(0, 0)
        return res
