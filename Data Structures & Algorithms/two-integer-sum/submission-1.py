class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        location = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in location:
                return [location[complement] , i]
            else:
                location[nums[i]] = i
