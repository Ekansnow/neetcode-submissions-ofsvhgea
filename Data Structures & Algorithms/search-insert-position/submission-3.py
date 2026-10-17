class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] < target:
                    return i+1
            else:
                return 0