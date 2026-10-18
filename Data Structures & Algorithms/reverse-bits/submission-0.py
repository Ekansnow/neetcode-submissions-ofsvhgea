class Solution:
    def reverseBits(self, n: int) -> int:
        # m = list(n)
        return (int("".join(list(bin(n)[2:])[::-1])+"0"*(32-len(bin(n)[2:])),2))