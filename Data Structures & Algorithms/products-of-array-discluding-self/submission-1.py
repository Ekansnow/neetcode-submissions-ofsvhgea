import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        prod = 1
        numsy = []
        if nums.count(0) == 1:
            loc = nums.index(0)
            numsy[:] = nums
            numsy.pop(loc)
            prod = math.prod(numsy)
            for i in range(len(nums)):
                if i != loc:
                    nums[i] = 0
                else:
                    nums[i] = prod
            return nums

        for i in range(len(nums)):
            prod *= nums[i]

        for i in range(len(nums)):
            prodx = prod//(nums[i] if nums[i] != 0 else 1)
            a.append(prodx)
        return a