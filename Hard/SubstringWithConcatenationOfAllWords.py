from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s : return []
        currentWordToAdd = ""
        currentWordToRemove = ""
        currentSubstring = ""
        start = end = toSkip = 0
        ans = []

        canBeAddedWords = words.copy()
        def canBeAdded(curr):
            if curr in canBeAddedWords:
                canBeAddedWords.remove(curr)
                return True
            else:
                return False      

        while end < len(s):
            while currentWordToAdd not in words:
                currentWordToAdd += s[end]
                if currentWordToAdd not in "".join(words):
                    currentWordToAdd = ""
                    toSkip+=1
                end+=1
                if end == len(s):
                    return ans
            if(canBeAdded(currentWordToAdd)):
                currentSubstring+=currentWordToAdd
                currentWordToAdd=""
                if len(currentSubstring) == len("".join(words)):
                    ans.append(start)
            else:
                while currentWordToRemove != currentWordToAdd:
                    currentWordToRemove +=s[start]
                    start+=1
                    if currentWordToRemove in words and currentWordToRemove!=currentWordToAdd:
                        currentSubstring=currentSubstring[len(currentWordToRemove):]
                        canBeAddedWords.append(currentWordToRemove)
                        currentWordToRemove=""
                currentSubstring=currentSubstring[len(currentWordToRemove):]
                #canBeAddedWords.append(currentWordToRemove)
                currentWordToRemove=""
                currentSubstring+=currentWordToAdd
                currentWordToAdd=""
                start+=toSkip
                toSkip=0
                        

        return ans

print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))    

print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))