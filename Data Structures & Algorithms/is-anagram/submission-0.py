class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt = {}
        dictt2 = {}
        for x in s:
            if x in dictt:
                dictt[x] += 1
            else:
                dictt[x] = 1

        for x in t:
            if x in dictt2:
                dictt2[x] += 1
            else:
                dictt2[x] = 1

        if(dictt == dictt2):
            return True
        else:
            return False 