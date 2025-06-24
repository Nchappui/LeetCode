class Solution:
   
    ## RECURSION SOLUTION
    """
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.tribonacci(n-1)+ self.tribonacci(n-2) + self.tribonacci(n-3)
    """
    ## DP SOLUTION
    def tribonacci(self, n: int) -> int:
        arr = [0,1,1]
        while len(arr)<n+1:
            arr.append(arr[-1] + arr[-2] + arr[-3])
        return arr[n]
    
Solution().tribonacci(5)