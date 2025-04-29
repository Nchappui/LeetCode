from typing import List


class Solution:
    ## WORKING BUT SCALES POORLY
    def longestConsecutiveScalingPoorly(self, nums: List[int]) -> int:
        sequence = {}
        if nums == [] : return 0
        def updateSequence(num, val):
            if num - 1 in sequence and sequence[num - 1] != val : 
                sequence[num - 1] = val
                updateSequence(num-1, val)
            if num + 1 in sequence and sequence[num +1] != val: 
                sequence[num + 1] = val
                updateSequence(num+1, val)

        for i in range(len(nums)):
            if nums[i] in sequence:
                continue
            elif (nums[i]-1 in sequence or nums[i]+1 in sequence):
                sequence[nums[i]] = sequence.get(nums[i]-1,0) + sequence.get(nums[i]+1,0) + 1
                updateSequence(nums[i], sequence[nums[i]])
            else:
                sequence[nums[i]] = 1
        return max(sequence.values())
    

    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = {}
        if nums == [] : return 0
        res = 0

        for i in range(len(nums)):
            if nums[i] in sequence:
                continue
            elif (nums[i]-1 in sequence or nums[i]+1 in sequence):
                newRes = sequence.get((nums[i]-1),[0,0,0])[0] + sequence.get((nums[i]+1),[0,0,0])[0] + 1
                minChain = min(sequence.get(nums[i]-1,[float('inf'),float('inf'),float('inf')])[1], sequence.get(nums[i]+1,[float('inf'),float('inf'),float('inf')])[1], nums[i])
                maxChain = max(sequence.get(nums[i]-1,[float('-inf'),float('-inf'),float('-inf')])[2],sequence.get(nums[i]+1,[float('-inf'),float('-inf'),float('-inf')])[2], nums[i])
                sequence[nums[i]] = [newRes,minChain,maxChain]
                sequence[minChain] = [newRes,minChain,maxChain]
                sequence[maxChain] = [newRes,minChain,maxChain]
                if newRes > res : res = newRes
            else:
                sequence[nums[i]] = [1, nums[i], nums[i]]
                if 1 > res : res = 1
        return res
    
print(Solution().longestConsecutive([-3,2,8,5,1,7,-8,2,-8,-4,-1,6,-6,9,6,0,-7,4,5,-4,8,2,0,-2,-6,9,-4,-1]))
Solution().longestConsecutive([100,4,200,1,3,2])