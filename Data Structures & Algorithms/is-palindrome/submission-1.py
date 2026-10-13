class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_up = ""
        for i in s:
            if (i <= 'Z' and i >= 'A') or (i <= 'z' and i >= 'a') or (i <= '9' and i >= '0'):
                s_up += i.lower()

        return True if list(s_up) == list(s_up)[::-1] else False