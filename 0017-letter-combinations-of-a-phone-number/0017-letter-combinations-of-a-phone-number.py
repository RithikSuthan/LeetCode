class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1={
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }
        curr=[]
        result=[]
        if digits=="":
            return []
        def backtrack(i):
            if i==len(digits):
                result.append("".join(curr))
                return
            for j in dict1[digits[i]]:
                print(j,end="")
                curr.append(j)
                backtrack(i+1)
                curr.pop()
        backtrack(0)
        # print(result)
        return result