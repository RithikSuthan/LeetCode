class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        target=sum(skill)//(len(skill)//2)
        # print(target)
        skill.sort()
        l=len(skill)//2
        i=0
        j=len(skill)-1
        chem=0
        while(i<=l and j>=l):
            # print(skill[i]," ",skill[j])
            if (skill[i] + skill[j])==target:
                chem+=skill[i] * skill[j]
            else:
                return -1
            i+=1
            j-=1
        return chem