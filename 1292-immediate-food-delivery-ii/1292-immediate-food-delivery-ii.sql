# Write your MySQL query statement below
with first_order as(
    select customer_id,min(order_date) as col2,min(customer_pref_delivery_date) as col1 
    from delivery group by customer_id
)

select round(sum(datediff(col1,col2)=0)*100
/count(customer_id),2) as immediate_percentage from first_order;