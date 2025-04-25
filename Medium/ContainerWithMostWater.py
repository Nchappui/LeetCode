from typing import List


class Solution(object):
    def maxArea(self, height):
        start, end, max_area = 0,0,0
        for x in height:
            start += 1
            end = start
            for y in height[start::]:
                end += 1
                area = min(x, y) * (end - start)
                if area > max_area:
                    max_area = area
        return max_area
    
    def maxArea2(self, height):
        start, end, max_area = 0,len(height) - 1,0
        while start < end:
            max_area = max(max_area, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1 
            else:
                end -= 1
        return max_area
                
                
height = [6,2,2,6,2,2,2,14,8]
solution = Solution()
print(solution.maxArea2(height))