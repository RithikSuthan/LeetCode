-- select distinct sales.product_id ,product.product_name from sales 
-- inner join product on 
-- sales.product_id=product.product_id
--  where sales.product_id not in
-- (
-- select distinct product_id from sales where 
--  sale_date between '2019-04-01' and '2019-12-31'
-- );

SELECT DISTINCT sales.product_id, product.product_name 
FROM sales
right JOIN product ON sales.product_id = product.product_id
group by sales.product_id 
having min(sales.sale_date)>='2019-01-01' and
max(sales.sale_date)<='2019-03-31';
