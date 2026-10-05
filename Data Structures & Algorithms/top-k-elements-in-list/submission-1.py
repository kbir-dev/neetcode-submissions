from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       dictt = Counter(nums)
       listt = []
       for i in range(k):
        max_valued_key = max(dictt, key=dictt.get)
        listt.append(max_valued_key)
        del dictt[max_valued_key]
       return listt