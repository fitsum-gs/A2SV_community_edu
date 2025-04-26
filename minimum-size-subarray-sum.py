class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = total = 0
        ans = float("inf")
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                ans = min(ans , right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if ans == float("inf") else ans
#https://leetcode.com/problems/minimum-size-subarray-sum/
