from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lettersDict = {
            '2' : ["a","b","c"],
            '3' : ["d","e","f"],
            '4' : ["g","h","i"],
            '5' : ["j","k","l"],
            '6' : ["m","n","o"],
            '7' : ["p","q","r","s"],
            '8' : ["t","u","v"],
            '9' : ["w","x","y","z"]
        }

        letters = []
        for digit in digits:
            letters.append(lettersDict[digit])
        result = []
        def recFunc(index, curr):
            if(index==len(letters)):
                result.append(curr)
            else:
                for letter in letters[index]:
                    recFunc(index+1, curr + letter)
        
        recFunc(0, "")
        return result if digits else []
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    digits = "23"
    print(solution.letterCombinations(digits))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

