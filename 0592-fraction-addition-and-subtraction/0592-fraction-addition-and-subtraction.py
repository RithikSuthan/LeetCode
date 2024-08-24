class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a,b):
            if a==0:
                return b
            return gcd(b%a,a)

        def lcm(a,b):
            return (a//gcd(a,b))*b
        
        if expression=="":
            return ""
        ls=[]
        queue=[]
        start=0
        if expression[0]!="-":
            queue.append("+")
        elif expression[0]=="-":
            queue.append("-")
            start=1
        # print("Beginning : ",queue,start)
        for i in range(start,len(expression)):
            if (expression[i] =="+" or expression[i]=="-") and len(queue)>1:
                # print("New line "," ls ",ls,queue)
                ls.append("".join(queue))
                queue=[]
                queue.append(expression[i])
                continue
            queue.append(expression[i])
            # print(queue)
        ls.append("".join(queue))
        # print(ls)

        # lcm=0
        temp=[]
        for i in range(len(ls)):
            if ls[i][-2]=="/":
                temp.append(int(ls[i][-1]))
            else:
                temp.append(int(ls[i][-2]+ls[i][-1]))

        # print(temp)

        while(len(temp)>1):
            a=temp.pop(0)
            b=temp.pop(0)
            lcm_res=lcm(a,b)
            temp.insert(0,lcm_res)

        print("After finding lcm ",temp)
        for i in range(len(ls)):
            if ls[i][-2]=="/":
                val=temp[0]//int(ls[i][-1])
            else:
                val=temp[0]//int(ls[i][-2]+ls[i][-1])
            # print("val ",val)
            # ls[i]=int(ls[i][0]+str(val))
            if ls[i][2]=="/":
                ls[i]=int(ls[i][0]+str(  int(ls[i][1])*val  ))
            else:
                ls[i]=int(ls[i][0]+str(  int(ls[i][1]+ls[i][2])*val  ))
        # print(ls)
        result=sum(ls)
        # print("result ",result)
        if result==0:
            return "0/1"
        temp1=gcd(abs(result),abs(temp[0]))
        num=result//temp1
        denom=temp[0]//temp1
        return str(num)+"/"+str(denom)