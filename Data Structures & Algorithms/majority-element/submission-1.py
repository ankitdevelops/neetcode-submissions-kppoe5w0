class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     for num in nums:
    #         count = sum(1 for i in nums if i == num)
    #         if count > n // 2:
    #             return num
        
        count = defaultdict(int)
        res = max_count = 0

        for num in nums:
            count[num] += 1
            if max_count < count[num]:
                res = num
                max_count = count[num]
        return res