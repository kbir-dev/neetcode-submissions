class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        def Counter(strr):
            new_dictt = {}
            for char in strr:
                if char in new_dictt:
                    new_dictt[char] += 1
                else:
                    new_dictt[char] = 1
            return new_dictt
        for i in range(len(strs)):
            key = tuple(sorted(Counter(strs[i]).items()))
            if key in dictt:
                dictt[key].append(strs[i])
            else:
                dictt[key] = [strs[i]]
        listt = []
        for value in dictt.values():
            listt.append(value)
        return listt
        
        


