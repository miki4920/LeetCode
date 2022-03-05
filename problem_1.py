from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_dictionary = {}
        for i in nums:
            if i not in value_dictionary:
                value_dictionary[target - i] = i
            else:
                return [i, value_dictionary[i]]
