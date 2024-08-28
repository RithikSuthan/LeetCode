select p.firstName,p.lastName,c.city,c.state from person p left join
 address c on p.personid=c.personid; 