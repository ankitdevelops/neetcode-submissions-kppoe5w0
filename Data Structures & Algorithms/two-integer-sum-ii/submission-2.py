class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     left = i + 1
        #     right = len(numbers) - 1
        #     required_no = target - numbers[i]
        #     while left <= right:
        #         mid = left + (right - left)//2
        #         if numbers[mid] == required_no:
        #             return [i + 1,mid + 1]
        #         elif numbers[mid] < required_no:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        # return []

        left = 0
        right = len(numbers) - 1
        
        while left <= right:
            current_sum = numbers[left] + numbers[right]
            if current_sum < target:
                left += 1
            if current_sum > target:
                right -= 1
            else:
                return [left + 1,right + 1]
        return []