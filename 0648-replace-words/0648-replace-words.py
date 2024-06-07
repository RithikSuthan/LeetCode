class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict1={}
        for i in dictionary:
            dict1[i]=i
        
        # print(dict1)
        ls=sentence.split(" ")
        # print(ls)
        for i in range(len(ls)):
            for ele in dict1:
                if ele == ls[i][0:len(ele)]: 
                    ls[i]=dict1[ele]
        # print(ls)
        result=" ".join(ls)
        # print(result)
        return result