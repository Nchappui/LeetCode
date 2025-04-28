from typing import List


class Solution:
    ##GOOD IDEA BUT CANNOT WORK LIKE THAT
    def findSubstring3(self, s: str, words: List[str]) -> List[int]:
        if not s : return []
        currentWordToAdd = ""
        currentWordToRemove = ""
        currentSubstring = ""
        start = end = 0
        ans = []

        canBeAddedWords = words.copy()
        def canBeAdded(curr):
            if curr in canBeAddedWords:
                canBeAddedWords.remove(curr)
                return True
            else:
                return False
            
        def isItLegit(curr, start, end, currSub, canBeAddedWords):
            while curr!=0:
                for elem in words:
                    if elem[0:len(curr)] == curr:
                        return curr, start, currSub, canBeAddedWords
                curr = curr[1::]
                start = end + 1
                currSub= ""
                canBeAddedWords = words.copy()
            return curr, start, currSub, canBeAddedWords

        while end < len(s):
            while currentWordToAdd not in words:
                currentWordToAdd += s[end]
                currentWordToAdd, start, currentSubstring, canBeAddedWords = isItLegit(currentWordToAdd, start, end, currentSubstring, canBeAddedWords)        
                end+=1
                if end == len(s):
                    if ((canBeAdded(currentWordToAdd) and len(currentSubstring+currentWordToAdd) == len("".join(words)))):
                        ans.append(start)
                    elif (currentWordToAdd == currentSubstring[:len(currentWordToAdd):] and len(currentSubstring) == len("".join(words))):
                        ans.append(start+len(currentWordToAdd))
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

                if len(currentSubstring) == len("".join(words)):
                    ans.append(start)
                        

        return ans
    

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s : return []
        start, end = 0, len(''.join(words))
        ans = []
        notValid = set()
        valid = set()
        wordLength = len(words[0])

        def isItLegit(start, end, s, words):
            if s[start:end] in valid: return True
            if s[start:end] in notValid: return False
            canBeAddedWords = words.copy()
            i = 0
            while i < len("".join(words)):
                currWord = s[i + start : i + wordLength + start]
                if currWord in canBeAddedWords:
                    canBeAddedWords.remove(currWord)
                i += wordLength
            if canBeAddedWords==[]:
                valid.add(s[start:end])
                return True
            else:
                notValid.add(s[start:end])
                return False

        while end < len(s):
            if isItLegit(start, end, s, words):
                ans.append(start)
            end+=1
            start+=1
        
        if isItLegit(start, end, s, words):
            ans.append(start)

        return ans
    
    def findSubstring4(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # all string words the same length
        ret = []
        n = len(s)
        k = len(words)
        m = len(words[0])
        p = m * k # total len of words
        initWindow = []
        notValid = set()
        valid = set()

        if n < p:
            # dont have enough words
            return []
            
        def validSubtring(substring):
            tempWords = words[:]
            i = 0
            while i < p:
                currWord = substring[i: i + m]
                if currWord in tempWords:
                    tempWords.remove(currWord)
                i += m
            
            return tempWords == []

        for i in range(p):
            letter = s[i]
            initWindow.append(letter)

        if validSubtring("".join(initWindow)):
            ret.append(0)

        i = p
        
        while i < n:
            letter = s[i]
            initWindow.pop(0)
            initWindow.append(letter)
            tempString = "".join(initWindow)
            # use caching here so no need to travsert again
            if tempString not in notValid:
                if tempString in valid or validSubtring(tempString):
                    ret.append(i - p + 1)
                    valid.add(tempString)
                else:
                    notValid.add(tempString)

            i += 1
        
        return ret

##[0, 9]
print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))   

##[]
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))

##[6, 9, 12]
print(Solution().findSubstring("barfoofoobarthefoobarman", ["foo","bar", "the"]))    

##[8]
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))    

##[13]
print(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))

##[0, 3, 6]
print(Solution().findSubstring("foobarfoobar", ["foo","bar"]))

##[[0,1,2,3,4,5,6,7,8,9,10]]
print(Solution().findSubstring("aaaaaaaaaaaaaa", ["aa","aa"]))