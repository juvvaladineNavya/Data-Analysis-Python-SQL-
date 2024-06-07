SELECT * FROM pythonsqlproject.df_orders;

describe df_orders;

-- find top 10 highest reveue generating products 

SELECT product_id , round(sum(sale_price),2) as sales from df_orders
group by product_id  order by sales desc limit 10;

-- find top 5 highest selling products in each region
with cte1 AS 
(select product_id, region, round(sum(sale_price),2) as sales
from df_orders
group by product_id, region
order by region, sales desc) 

select * from (select * , row_number() over(partition by region order by sales desc) as rownumber
from cte1 ) as subquery where rownumber <=5;

-- find month over month growth comparison for 2022 and 2023 sales eg : jan 2022 vs jan 2023
 with cte as (
 select year(order_date) as order_year, month(order_date) as order_month, round(sum(sale_price),2) as sales
 from df_orders
 group by year(order_date), month(order_date)
 -- order by year(order_date), month(order_date)
 )
 select order_month,
 sum(case when order_year = 2022 then sales else 0 end) AS '2022',
  sum(case when order_year = 2023 then sales else 0 end) AS '2023'
  from cte
  group by order_month
  order by order_month;
 
 -- for each category which month had highest sales 
 with cte as(
 select DATE_FORMAT(order_date, '%Y-%m') as order_year_month, category, round(sum(sale_price),2) as sales
 from df_orders
 group by category, order_year_month
 order by sales desc)
 
 select * from (select *, row_number() over(partition by category order by sales desc) as rownumber from cte) subquery
 where rownumber = 1;
 
 -- --which sub category had highest growth by profit in 2023 compare to 2022
 with cte  as(
select year(order_date) as order_year, sub_category, round(sum(sale_price),2) as sales
from df_orders
group by sub_category, order_year
order by sub_category, sales ),
cte2 as (
select sub_category,
sum(case when order_year =  2022 then sales else 0 end ) as sale_2022,
sum(case when order_year =  2023 then sales else 0 end ) as sale_2023
from cte 
group by sub_category )

select *, round((sale_2023-sale_2022)/(sale_2022)*100,2)as change_per
from cte2
order by change_per desc
limit 1;




