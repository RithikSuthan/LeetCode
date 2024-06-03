class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            print("same")
            return 0
        prev=0
        i=0
        while(i<len(t)):
            index_in_substring = s[prev:].find(t[i])
            if index_in_substring != -1:
                prev = prev + index_in_substring + 1
            else:
                break
            i=i+1
        print(i," t len ",len(t))
        return len(t)-i