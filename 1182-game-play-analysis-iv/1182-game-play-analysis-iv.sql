# Write your MySQL query statement below
with first_table as
(
    select player_id,min(event_date) as first_time from activity 
    group by player_id
)

select round(sum( datediff(a.event_date,t.first_time)=1)/count(distinct 
a.player_id
),2) 
as fraction from activity a inner join first_table t on
a.player_id=t.player_id;