class Solution:
    from itertools import product
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        temp=[]
        if len(digits)==0:
            return ""
        if len(digits)==1 and digits in  dict1:
            return dict1[digits]
        elif len(digits)==2:
            temp=product( dict1[digits[0]],dict1[digits[1]])
        elif len(digits)==3:
            temp=product(dict1[digits[0]],dict1[digits[1]],dict1[digits[2]])
        elif len(digits)==4:
            temp=product(dict1[digits[0]],dict1[digits[1]],dict1[digits[2]],dict1[digits[3]])
        print(temp)
        result=[]
        for i in temp:
            result.append("".join(i))
        print(result)
        return result


