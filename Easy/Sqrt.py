class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start <= end:
            middle = (start + end) // 2
            if middle * middle > x:
                end = middle - 1
            else:
                start = middle + 1
            
        return start -1


print(Solution().mySqrt(10))
print(Solution().mySqrt(1))
print(Solution().mySqrt(9))
print(Solution().mySqrt(100))