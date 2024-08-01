-- select person_name from employee where person_id=
-- (select person_id from emplo)


with temp as(
select person_name,turn,(select sum(weight)
from queue where turn<=q1.turn
) as total_weight from queue q1
order by turn
)

select person_name from temp where total_weight <=1000 order by total_weight
desc limit 1
;
