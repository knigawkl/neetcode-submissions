class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Each subset is created by making a decision for each input element."""
        res = []  # global list of subsets
        subset = []  # state of the current partial solution

        def visit(i):
            if i == len(nums):
                res.append(subset[:])
                return
            # choice 1: pick nums[i]
            subset.append(nums[i])
            visit(i + 1)
            subset.pop()  # undo choice 1
            # choice 2: skip s[i]
            visit(i + 1)
        
        visit(0)
        return res
