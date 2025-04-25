from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)

        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range (1,n):
            if height[i]>leftMax[i-1]:
                leftMax[i] = height[i]
            else:
                leftMax[i] = leftMax[i-1]

        rightMax = [0] * n
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])


        for i in range(n):
            res += min(leftMax[i],rightMax[i]) - height[i]

        return(res)


print(Solution().trap([4,2,0,3,2,5]))
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))