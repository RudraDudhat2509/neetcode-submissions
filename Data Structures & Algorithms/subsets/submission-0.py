class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, curr):
            if i == len(nums):
                result.append(curr[:])
                return

            # Don't take nums[i]
            backtrack(i + 1, curr)

            # Take nums[i]
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

        backtrack(0, [])
        return result