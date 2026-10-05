class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return_list = []
        for i in range(n):
            product = 1
            for j in range(n):
                if j == i:
                    continue
                product *= nums[j]
            return_list.append(product)
        return return_list