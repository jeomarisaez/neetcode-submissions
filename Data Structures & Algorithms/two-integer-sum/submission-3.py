class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in dictionary:
                return [dictionary[dif], i]
            dictionary[nums[i]] = i
