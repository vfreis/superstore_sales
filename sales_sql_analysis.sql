use banco_estudos

select 
    top 2 * 
from 
    superstore_sales


--- sales from south
select 
    *
from 
    superstore_sales
WHERE
    region = 'South'

-- compute total sales
SELECT 
    sum(sales) as total_sales
from 
    superstore_sales

-- total sales by region
SELECT 
    region
    ,sum(sales) as total_sales
FROM
    superstore_sales
group BY
    region

-- customer by segment
SELECT
    segment
    ,count(distinct customer_id) as customer_count
FROM
    banco_estudos.dbo.superstore_sales
group by
    segment

-- joins e subquerys

create table customer_segments(
    customer_id varchar(50),
    segment varchar(50)
)

insert into customer_segments (customer_id, segment)
select distinct customer_id, segment from superstore_sales

--- validating inserted data
SELECT
    s.customer_name
    ,s.segment
    ,c.segment as verified_segment
FROM
    superstore_sales s
inner JOIN
    customer_segments c on s.customer_id = c.customer_id

-- find products above avarage
SELECT
    product_name
    ,sales
from
    superstore_sales
where 
    sales > (select avg(sales) from superstore_sales)
order BY
    sales asc



select 
    avg(sales)
FROM
    superstore_sales

--- total sales by category above $ 5,000
SELECT
    category
    ,sum(sales) as total_sales
from
    superstore_sales
group BY
    category
HAVING
    sum(sales) > 5000
order BY
    sum(sales) desc

-- top 5 cities with most sale value
SELECT
    top 5
    city
    ,sum(sales) as total_sales
FROM
    superstore_sales
group BY
    city
order BY
    sum(sales)  desc   

-- sales by category and subcategory
SELECT
    category
    ,sub_category
    ,sum(sales) as total_sales
FROM
    superstore_sales
group BY
    category
    ,sub_category
order BY
    sum(sales) desc

-- advanced querys

with regional_sales as (
    SELECT
        region
        ,sum(sales) as total_sales
    FROM
        superstore_sales
    group BY
        Region
)

select * from regional_sales order by total_sales desc



select
    *
into
    #_temp_sales
FROM
    superstore_sales

select * from #_temp_sales


-- part 2

--- 3 most profitable states by segment
with statesales as (
    SELECT
        state
        ,segment
        ,sum(sales) total_sales
        ,rank() over (partition by segment order by sum(sales) desc) as rank
    FROM
        superstore_sales
    group BY
        state
        ,segment
)
SELECT
    state
    ,segment
    ,total_sales
FROM
    statesales
where 
    rank <= 3
order BY
    segment
    ,total_sales desc

-- analyze monthly sales

with monthlysales as (
    SELECT
        year(order_date) year
        ,month(order_date) month
        ,sum(sales) as total_sales
    FROM
        superstore_sales
    group BY
        year(order_date)
        ,month(order_date)
)

select
    year
    ,month
    ,total_sales
    ,rank() over (partition by year order by total_sales desc) as rank
into
    #_temp_monthlysales
FROM
    monthlysales
order BY
    year

SELECT
    *
FROM
    #_temp_monthlysales
WHERE
    rank = 1

--- shipping efficiency
SELECT
    region
    ,avg(DATEDIFF(day, order_date, ship_date)) avgshippingtime
FROM
    superstore_sales
group BY
    region
order BY
    avg(DATEDIFF(day, order_date, ship_date))

--- identify buying patters
SELECT  
    product_name
    ,count(*) purchase_count
FROM
    superstore_sales
WHERE
    segment = 'Corporate'
group BY
    product_name
order BY
    count(*) desc

---- sales percentage by category
SELECT
    category
    ,sum(sales) category_sales
    ,ROUND(sum(sales) * 100 / sum(sum(sales)) over (), 2) as percentage_sales
from
    superstore_sales
group by
    category
order BY
    percentage_sales desc

---- recurring purchase by customer
select
    customer_id
    ,customer_name
    ,count(order_id) total_orders
    ,sum(sales) total_sales
FROM
    superstore_sales
group BY
    customer_id
    ,customer_name
HAVING
    count(order_id) > 5
order BY
    total_orders desc

select 
    sobjects.name
FROM
    sysobjects sobjects
WHERE
    sobjects.xtype = 'U'

select * from INFORMATION_SCHEMA.tables

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'superstore_sales'