with first_table as
(
select product_id,min(year) as first_year1 from sales group by
product_id
)

select s.product_id,s.year as first_year,quantity,price from sales s inner join
first_table f on s.product_id=f.product_id and s.year=f.first_year1;
