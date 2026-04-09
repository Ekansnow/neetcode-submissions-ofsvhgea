class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in str(bin(n)):
            if i == "1":
                cnt += 1
        return cnt
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            lst.append(self.hammingWeight(i))
        return lst