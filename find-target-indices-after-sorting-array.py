class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans=[]
        if target in nums:
            indice = nums.index(target)
            while indice < len(nums) and nums[indice] == target:
                ans.append(indice)
                indice += 1
        return sorted(ans)
#https://leetcode.com/problems/find-target-indices-after-sorting-array/
