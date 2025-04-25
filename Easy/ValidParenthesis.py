class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for elem in s:
            if elem == '(' or elem == '[' or elem == '{':
                queue.append(elem)
            else:
                if queue==[]: return False
                lastElem = queue.pop(len(queue)-1) 
                if lastElem == '(' and elem != ')' or lastElem == '[' and elem != ']' or lastElem == '{' and elem != '}' :
                    return False
                
        return True if queue == [] else False     
print(Solution().isValid("(())"))