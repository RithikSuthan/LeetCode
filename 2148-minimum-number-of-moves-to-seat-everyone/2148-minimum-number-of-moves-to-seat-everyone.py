class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort(key=lambda x:x)
        students.sort(key=lambda x:x)
        soln=0
        for i in range(len(seats)):
            soln=soln+abs(seats[i]-students[i])
        return soln