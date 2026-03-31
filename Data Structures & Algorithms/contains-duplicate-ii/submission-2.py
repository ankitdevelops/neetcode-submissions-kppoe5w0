class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and abs(i -j) <= k:
        #             return True
        # return False
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp and abs(i - mp[nums[i]]) <= k:
                return True
            mp[nums[i]] = i
        return False