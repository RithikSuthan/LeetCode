class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        start=0
        cyclic_mapping = {
            'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g',
            'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm',
            'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's',
            's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y',
            'y': 'z', 'z': 'a'
        }
        for i in range(0,len(str1)):
            if start==len(str2):
                return True
            if str1[i]==str2[start] or cyclic_mapping[str1[i]]==str2[start]:
                start+=1
            if start==len(str2):
                return True
        return False