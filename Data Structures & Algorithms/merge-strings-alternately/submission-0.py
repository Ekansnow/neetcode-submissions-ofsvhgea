class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        miny = min(len(word1),len(word2))
        for i in range(miny):
            lst.append(word1[i])
            lst.append(word2[i])
        return "".join(lst) + word1[miny:] + word2[miny:]
