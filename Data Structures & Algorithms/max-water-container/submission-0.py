class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #left, right = 0, len(heights)
        max_area = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                curr_area = min(heights[i], heights[j])*abs(i - j)
                if curr_area > max_area:
                    max_area = curr_area
        return max_area
        