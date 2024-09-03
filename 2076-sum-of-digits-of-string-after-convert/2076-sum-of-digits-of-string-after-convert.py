class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dict1={
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
        'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
        'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
        'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
        }
        temp=""
        for ele in s:
            temp+=str(dict1[ele])
        #print(temp)
        for i in range(0,k):
            temp1=[]
            for ele in temp:
                temp1.append(int(ele))
            temp1=sum(temp1)
            temp=str(temp1)
            #print(temp1)
        print("Ans ",temp)
        return int(temp)