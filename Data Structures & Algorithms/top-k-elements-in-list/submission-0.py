class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = {}
        listt = []
        for num in nums:
            if num in dictt:
                dictt[num] += 1
            else:
                dictt[num] = 1
        while k > 0:
            max_value = max(dictt.values())
            max_key = max(dictt, key=dictt.get)
            listt.append(max_key)
            dictt.pop(max_key)
            k -= 1
        return listt