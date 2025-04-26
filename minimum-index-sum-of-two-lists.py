class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minimum = float("inf")
        ans = []
        for word in list1:
            summ = 0 #sum of the indices
            if word in list2:
                summ = list1.index(word) + list2.index(word)
                if summ < minimum:
                    ans.clear()
                    ans.append(word)
                    minimum = summ
                elif summ == minimum:
                    ans.append(word)
        return ans
#https://leetcode.com/problems/minimum-index-sum-of-two-lists/
