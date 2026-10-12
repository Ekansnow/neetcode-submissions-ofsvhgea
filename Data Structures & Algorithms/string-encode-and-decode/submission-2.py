class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            separator = s.find("#", i)
            length = int(s[i:separator])

            start = separator + 1
            end = start + length
            words.append(s[start:end])
            i = end

        return words