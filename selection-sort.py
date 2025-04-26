class Solution: 
    def selectionSort(self, arr):
        #code here
        def swap(o, p):
            arr[o] , arr[p] = arr[p] , arr[o]
        for i in range (len(arr)):
            current_minimum = i
            for j in range (i+1, len(arr)):
                if arr[j] < arr[current_minimum]:
                    current_minimum = j
            swap(i,current_minimum)
        return arr
#https://www.geeksforgeeks.org/problems/selection-sort/1
