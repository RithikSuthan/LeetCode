-- delete from person where id in (
--     select x.id from person x,person y where 
--     x.id>y.id and
--     x.email=y.email);
-- this will not be supported by mysql  because both query na d subquery uses same 
-- id it raises an error so use join

delete person from person join (select x.id from person x,person y where 
    x.id>y.id and
    x.email=y.email) as subquery on subquery.id=person.id;




