class Solution:
    def isValid(self, s: str) -> bool:
        lst = ['0']
        for i in s:
            if i == "]" and lst[-1] == "[":
                lst = lst[:-1]
            elif i == ")" and lst[-1] == "(":
                lst = lst[:-1]
            elif i == "}" and lst[-1] == "{":
                lst = lst[:-1]
            else:
                lst.append(i)
        return True if len(lst) == 1 else False