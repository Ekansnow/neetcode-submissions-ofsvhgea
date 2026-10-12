class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        miny = 1
        while True:
                if miny in nums:
                    miny += 1
                else:
                    return miny