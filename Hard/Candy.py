from typing import List


class Solution:
    def candy2(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n==1: return 1

        candies = [1] * n
        satisfiedNum=0

        def isSatisfied(index1, index2):
            if ratings[index1]<=ratings[index2]:
                return True
            else:
                return candies[index1]>candies[index2]
            
        while(True):
            for i in range (n):
                if i == 0:
                    if(isSatisfied(i,i+1)):
                        satisfiedNum += 1
                    else:
                        candies[i]=candies[i+1]+1
                elif i == n-1:
                    if(isSatisfied(i,i-1)):
                        satisfiedNum += 1
                    else:
                        candies[i]=candies[i-1]+1
                else:
                    if(isSatisfied(i,i+1) and isSatisfied(i,i-1)):
                        satisfiedNum +=1
                    else:
                        
                        if isSatisfied(i,i+1):
                            candies[i]=candies[i-1]+1
                        else:
                            candies[i]=candies[i+1]+1
            if (satisfiedNum != n) : 
                satisfiedNum = 0
                continue
            else:
                break

        print(candies)
        return sum(candies)
    
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n==1: return 1

        candies = [1] * n

        def isSatisfied(index1, index2):
            if ratings[index1]<=ratings[index2]:
                return True
            else:
                return candies[index1]>candies[index2]
            
        for i in range (1, n):
            if not isSatisfied(i,i-1):
                candies[i] = candies[i-1] +1

        for i in range (n-2, -1, -1):
            if not isSatisfied(i,i+1):
                candies[i] = candies[i+1] +1

        
        print(candies)
        return sum(candies)
    
print(Solution().candy2([1,2,87,87,87,2,1]))