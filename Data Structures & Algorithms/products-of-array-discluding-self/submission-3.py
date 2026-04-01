class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res_list = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             product *= nums[j]
        #     res_list.append(product)
        # return res_list

        prod = 1
        zero_count = 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zero_count:
                if c:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod//c
        return res