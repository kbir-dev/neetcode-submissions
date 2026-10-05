class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0
        for i in range(len(heights)-1):
            w = 1
            j = i + 1
            while j < len(heights):
                h = min(heights[i],heights[j])
                if h * w > maxx:
                    maxx = h * w
                j+=1
                w+=1
        return maxx