class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = set(nums)
        # nums = sorted(list(nums))
        # return len(nums)\\
        
        i = 1
        while i != len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                i-=1
            
            i+=1
        
        return len(nums)