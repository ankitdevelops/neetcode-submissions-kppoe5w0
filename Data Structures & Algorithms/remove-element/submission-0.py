class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp_list = []
        for i in nums:
            if i == val:
                continue
            else:
                temp_list.append(i)
        for i in range(len(temp_list)):
            nums[i] = temp_list[i]
        return len(temp_list)