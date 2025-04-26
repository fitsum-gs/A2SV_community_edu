class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        answer = []
        x = num//3
        if (x-1)+(x)+(x+1) == num:
            answer = [x-1, x, x+1]
        return answer
#https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
