select d.name as Department,e1.name as Employee
,e1.salary from employee e1
inner join department as d on e1.departmentid=d.id
where e1.salary=(
    select max(e2.salary) from employee e2 where
    e2.departmentid=e1.departmentid
)
;

