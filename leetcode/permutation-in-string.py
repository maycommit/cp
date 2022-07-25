class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d = dict()
        for i in range(len(s1)):
            if i not in d:
                d[i] = 0
            else:
                d[i] += 1

        tmp = {}
        i = 0
        for j in range(len(s2)):
            if s2[j] in d:
                i = j + 1
                continue

            if s2[j] not in tmp:
                count = 0
            else:
                count = tmp[s2[j]]

            if count == 0 or count < s2.get(0):
                tmp[s2[j]] = count + 1

                if j - i + 1 == len(s1):
                    return True

            else:

                while i < j:
                    if s2[i] == s2[j]:
                        i += 1
                        break

                    tmp[s2[j]] = tmp[s2[i]] - 1
                    i += 1

        return False


s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))
print(s.checkInclusion("ab", "eidboaoo"))
print(s.checkInclusion("dinitrophenylhydrazine", "acetylphenylhydrazine"))
print(s.checkInclusion("prosperity", "properties"))
print(s.checkInclusion("abc", "bbbca"))
