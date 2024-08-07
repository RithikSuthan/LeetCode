class Solution:
    import re
    def numberToWords(self, num: int) -> str:
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        def helper(temp):
            val=""
            if temp<20:
                val=less_than_20[temp]
            elif temp<100:
                val=tens[temp//10]+" "+less_than_20[temp%10]
            else:
                val=helper(temp//100)+" Hundred " +helper(temp%100)
            return val 
                
        if num==0:
            return "Zero"
        result=[]
        for i in range(len(thousands)):
            if num%1000!=0:
                result.append(helper(num%1000)+" "+thousands[i]) 
            num=num//1000
        result=result[::-1]
        for i in range(0,len(result)):
            result[i]=re.sub('\s+',' ',result[i])
        for i in range(len(result)):
            while (result[i] and result[i][-1]==" "):
                result[i]=result[i][0:len(result[i])-1]
        print(result)
        result=" ".join(result)
        return result


