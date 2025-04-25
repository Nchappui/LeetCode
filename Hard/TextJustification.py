import math
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len("".join(words))
        currentRow = []

        currentChars = 0
        currentSpaces = 0
        for i in range (len(words)):
            if currentChars + len(words[i]) + currentSpaces + 1 > maxWidth and i!=0:
                ## BUILD LINE WITH MANY WORDS
                if currentSpaces>0:
                    spacesBetweenWords = math.floor((maxWidth - currentChars)/currentSpaces)
                    remainingSpaces = maxWidth - (spacesBetweenWords * currentSpaces + currentChars)
                    #print(currentSpaces, spacesBetweenWords, remainingSpaces)
                    for j in range(len(currentRow)):
                        if remainingSpaces>0:
                            currentRow[j]+=" "
                            remainingSpaces-=1
                    res.append((" "*spacesBetweenWords).join(currentRow))
                ## BUILD LINE WITH ONE WORD
                else:
                    res.append(currentRow[0] + " "*(maxWidth-len(currentRow[0])))

                #print(currentRow)
                #print(res)
                currentRow=[]
                currentChars = 0
                currentSpaces = 0

            if currentRow != []:
                currentSpaces +=1
            currentRow.append(words[i])
            currentChars+=len(words[i])

        ##BUILD LAST LINE
        res.append(" ".join(currentRow) + " "* (maxWidth -len(" ".join(currentRow))))
        #print(currentRow)
        #print(n)
        return res


print(Solution().fullJustify(["Listen","to","many,","speak","to","a","few."],6))
print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"],16))
print(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20))