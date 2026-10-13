class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        for i in operations:
            if i == 'D':
                lst.append(int(lst[-1])*2)
            elif i == 'C':
                lst.pop()
            elif i == '+':
                lst.append(int(lst[-1]) + int(lst[-2]))
            else:
                lst.append(int(i))
        return sum(lst)