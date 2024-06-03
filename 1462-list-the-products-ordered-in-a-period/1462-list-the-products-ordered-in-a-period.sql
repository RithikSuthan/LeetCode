# Write your MySQL query statement below
select distinct p.product_name,sum(o.unit) as unit
from products p inner join orders o
on p.product_id=o.product_id and month(o.order_date)=2 and 
year(o.order_date)=2020
group by o.product_id
having sum(o.unit)>=100
;