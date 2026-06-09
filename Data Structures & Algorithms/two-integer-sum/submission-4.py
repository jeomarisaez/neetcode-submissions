class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_Dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in my_Dict:
                return [my_Dict[difference], i]
            else:
                my_Dict[nums[i]] = i