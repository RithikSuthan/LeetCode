select s.user_id,
coalesce(
 round( ( sum(case when c.action='confirmed' then 1 else 0 end )/count(c.user_id)) ,2)
    ,0) as confirmation_rate   


from signups s left join confirmations c 
on s.user_id=c.user_id 
group by s.user_id
;
-- where c.action='confirmed' or c.user_id is nul
-- round( (count(c.action)/count(c.user_id)) ,2)