# Write your MySQL query statement below
select e.employee_id,e.name,count(e.employee_id) as reports_count,
round(avg(m.age)) as average_age from employees e
 left join employees m on e.employee_id=m.reports_to where 
 m.reports_to is not null group by e.employee_id,e.name order by e.employee_id;