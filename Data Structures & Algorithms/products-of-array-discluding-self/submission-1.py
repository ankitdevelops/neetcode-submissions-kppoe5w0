class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_list = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            res_list.append(product)
        return res_list