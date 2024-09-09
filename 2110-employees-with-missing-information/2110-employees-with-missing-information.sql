select employee_id from
(
    select e.employee_id from employees e left join salaries s on
e.employee_id =s.employee_id where s.employee_id is null
union
select s.employee_id from employees e right join salaries s on
e.employee_id =s.employee_id where e.employee_id is null
) as temp order by employee_id
;  
