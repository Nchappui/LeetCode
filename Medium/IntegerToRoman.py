class Solution(object):
    def intToRoman(self, num):
        romanDict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        currentindex = 1
        romanSoluce = ''
        while num >0:
            currentNumber = num % 10
            if currentNumber != 0:
                if currentNumber == 4:
                    romanSoluce = romanDict[currentindex] + romanDict[currentindex * 5] + romanSoluce
                elif currentNumber == 9:
                    romanSoluce = romanDict[currentindex] + romanDict[currentindex * 10] + romanSoluce
                else:
                    if currentNumber >= 5:
                        romanSoluce = romanDict[currentindex * 5] + romanDict[currentindex] * (currentNumber - 5) + romanSoluce
                    else:
                        romanSoluce = romanDict[currentindex] * currentNumber + romanSoluce
            num = num // 10
            currentindex *= 10

        return romanSoluce
    

print(Solution().intToRoman(1994))  # Output: "MCMXCIV"