class Solution:
    import copy
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        temp=copy.deepcopy(students)
        prev=[]
        while(True):
            if len(students)==0 and len(sandwiches)==0:
                return 0
            if prev==students:
                break
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                i=i+1
                prev=copy.deepcopy(students)
                students.append(students.pop(0))
            print(students," ",sandwiches)
        return len(students)