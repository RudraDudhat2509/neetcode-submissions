class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        cur = 0

        for x in nums:
            cur = max(x, cur + x)
            best = max(best, cur)

        return best