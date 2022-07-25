class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = dict()
        j = 0
        for i in range(len(key)):
            if key[i].isalnum() and key[i] not in alphabet:
                alp = chr(97 + j)
                alphabet[key[i]] = alp
                j += 1

        res = [' ']*len(message)
        for i in range(len(message)):
            if message[i].isalnum():
                res[i] = alphabet[message[i]]

        return res

s = Solution()
s.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv")
s.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
