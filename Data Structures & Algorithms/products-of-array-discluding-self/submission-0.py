class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_list = []
        for i in nums:
            product = 1
            for j in nums:
                if i == j:
                    continue
                else:
                    product *= j
            res_list.append(product)
        return res_list