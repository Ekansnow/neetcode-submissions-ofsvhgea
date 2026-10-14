class Solution:
    def validPalindrome(self, s: str) -> bool:
        flag = False
        flag = flag or (True if list(s) == list(s)[::-1] else False)

        for i in range(len(s)):
            lsts = list(s)
            lsts.pop(i)
            s_up = "".join(lsts)
            flag = flag or (True if list(s_up) == list(s_up)[::-1] else False)

        return flag