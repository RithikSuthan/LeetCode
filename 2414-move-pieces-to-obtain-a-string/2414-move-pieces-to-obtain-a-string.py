class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if( (start.count("L")!=target.count("L")) or (start.count("R")!=target.count("R")) ):
            return False
        
        n=len(start)
        start_ind,target_ind=0,0
        while(start_ind<n and target_ind<n):
            while(start_ind<n and start[start_ind]=="_"):
                start_ind+=1
            while(target_ind<n and target[target_ind]=="_"):
                target_ind+=1

            if(start_ind==n and target_ind==n):
                return True

            if(start_ind==n and target_ind!=n or start_ind!=n and target_ind==n):
                return False
            
            if(start[start_ind]!=target[target_ind]):
                return False

            if(start[start_ind]=='L' and start_ind<target_ind):
                return False

            if(start[start_ind]=='R' and start_ind>target_ind):
                return False
            start_ind+=1
            target_ind+=1
        # print(start_ind," ",target_ind)
        return True
        
