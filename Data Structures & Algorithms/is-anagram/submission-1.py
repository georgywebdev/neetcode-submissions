class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        

        for i in range(len(s)):
            # print("countS", countS)
            # print("s[i]", s[i])
            # print("s", s)
            # print("i", i)
            # countS {'r': 1, 'a': 1, 'c': 2, 'e': 1}
            # s[i] a
            # s racecar
            # i 5
            if s[i] in countS:
                countS[s[i]] += 1
            else:
                countS[s[i]] = 1

            if t[i] in countT:
                countT[t[i]] += 1
            else:
                countT[t[i]] = 1
        return countS == countT