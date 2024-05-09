import copy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = ''.join(sorted(s1))
        
        i = 0
        j = len(s1) - 1
        while j < len(s2):
            s2_substring = s2[i:j+1]
            s2_sorted = ''.join(sorted(s2_substring))
            if s2_sorted == s1_sorted:
                return True
            i += 1
            j += 1
        return False
