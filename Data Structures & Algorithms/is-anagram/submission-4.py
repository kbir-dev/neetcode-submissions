class Solution:
    def frequencyCounter(self, string):
        freqCounter = {}
        for char in string:
            if char not in freqCounter:
                freqCounter[char] = 1
            else:
                freqCounter[char] += 1
        return freqCounter

    def isAnagram(self, s: str, t: str) -> bool:
        s = self.frequencyCounter(s)
        t = self.frequencyCounter(t)
        if s == t:
            return True
        else:
            return False