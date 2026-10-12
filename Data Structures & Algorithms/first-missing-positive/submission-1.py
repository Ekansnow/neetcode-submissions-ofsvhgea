class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        miny = 1
        while True:
            if miny <= 0:
                miny += 1
            else:
                if miny in nums:
                    miny += 1
                else:
                    return miny