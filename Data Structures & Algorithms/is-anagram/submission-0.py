class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
            
            
""" 
Notes:
Anagram solution is based of hash taples (key, value) pairs.
We iterated over the first string and kept track of the number of instances of each letter
We then iterated over the second string and kept track of the number of instances of each letter
Finally we compared both strings' hashtables
If they don't share the same length of characters then there's no way they can be anagrams.

"""