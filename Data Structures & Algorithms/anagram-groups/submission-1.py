from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        return_list = []
        for strr in strs:
            key = tuple(sorted(Counter(strr).items()))
            if key in dictt:
                dictt[key].append(strr)
            else:
                dictt[key] = [strr]
        for key, value in dictt.items():
            return_list.append(value)
        return return_list


            