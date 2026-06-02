class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_sequence  = 0
        for i in nums:
            if (i - 1) not in num_set:
                length = 0
                while i + length in num_set:
                    length += 1
                longest_sequence = max(length,longest_sequence)
        return longest_sequence
