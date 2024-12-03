class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str=[]
        last_index=0
        for i in spaces:
            new_str.append(s[last_index:i])
            new_str.append(" ")
            last_index=i
        new_str.append(s[last_index:])
        return "".join(new_str)
