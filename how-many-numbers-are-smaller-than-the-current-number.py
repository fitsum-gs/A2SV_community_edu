class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = sorted(nums)
        ans = []
        for num in nums:
            ans.append(new.index(num))
        return ans
#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
