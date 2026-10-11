class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        val = strs[0]

        for i in range(len(val),-1,-1):
            cnt = 0
            for j in strs:
                if j.startswith(val[:i]):
                    cnt += 1
            if cnt == len(strs):
                return val[:i]