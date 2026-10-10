class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num = []
        cnt = 0
        for i in nums:
            if i != val:
                num.insert(0,i)
                cnt += 1
            else:
                num.append(val)
        nums[:] = num
        return cnt