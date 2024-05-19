select r.contest_id,
round(count(r.user_id)/(select count(user_id) from users)*100,2) as percentage 
from register r group by contest_id order by percentage desc,contest_id;