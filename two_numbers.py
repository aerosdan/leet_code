from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            temp_list = nums.copy()
            temp_list.remove(num)
            for num_i in temp_list:
                sum_result = num + num_i
                if sum_result == target:
                    return [nums.index(num), temp_list.index(num_i)+1]
        return "oooohhh no"


print(Solution().twoSum([2,7,11,15], 9))