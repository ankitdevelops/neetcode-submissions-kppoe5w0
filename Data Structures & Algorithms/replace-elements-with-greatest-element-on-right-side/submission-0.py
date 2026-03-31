class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n  = len(arr)
        # for i in range(n):
        #     right_max = -1
        #     for j in range(i +1, n):
        #         if arr[j] > right_max:
        #             right_max = arr[j]
        #     arr[i] = right_max
        # return arr


        ans = [0] * n
        right_max = -1
        for i in range(n -1,-1,-1):
            ans[i] = right_max
            if arr[i] > right_max:
                right_max = arr[i]
        return ans
