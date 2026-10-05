class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt = {}
        for x in nums:
            if x in dictt:
                return True
            else:
                dictt[x] = 1
        return False