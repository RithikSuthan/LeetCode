import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    ls=logs.values.tolist()
    result=[]
    count=0
    ls=sorted(ls,key=lambda x:x[0])
    print(ls)
    for i in range(len(ls)-1):
        if ls[i][1]==ls[i+1][1] and ls[i][0]+1==ls[i+1][0]:
            count=count+1
            if ls[i][1] not in result and count>=2:
                result.append(ls[i][1])
        else:
            count=0
    print(count)
    # if count==2 and len(ls)>2 and ls[-1][1]==ls[-2][1] and ls[-2][1]==ls[-3][1] and ls[-3][1]==ls[-1][1]:
    #     result.append(ls[-1][1])
    result1=pd.DataFrame({"ConsecutiveNums":result})
    return result1