SELECT * FROM dim_customer
LIMIT 10;

SELECT
SUM(revenue) AS total_revenue
FROM fact_orders;

SELECT
COUNT(DISTINCT order_id)
FROM fact_orders;

SELECT
COUNT(DISTINCT customer_id)
FROM dim_customer;

SELECT
c.state,
SUM(f.revenue)
FROM fact_orders f
JOIN dim_customer c
ON f.customer_id = c.customer_id
GROUP BY c.state
ORDER BY 2 DESC;

SELECT
p.category,
SUM(f.revenue)
FROM fact_orders f
JOIN dim_product p
ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY 2 DESC;

SELECT
seller_id,
SUM(revenue)
FROM fact_orders
GROUP BY seller_id
ORDER BY 2 DESC;

SELECT
AVG(revenue)
FROM fact_orders;

SELECT
d.year,
d.month,
SUM(f.revenue)
FROM fact_orders f
JOIN dim_date d
ON f.order_date = d.date
GROUP BY
d.year,
d.month
ORDER BY
d.year,
d.month;

SELECT
p.category,
SUM(f.revenue)
FROM fact_orders f
JOIN dim_product p
ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY 2 DESC;

SELECT
c.city,
SUM(f.revenue)
FROM fact_orders f
JOIN dim_customer c
ON f.customer_id = c.customer_id
GROUP BY c.city
ORDER BY 2 DESC;

SELECT *
FROM fact_orders
LIMIT 5;

SELECT *
FROM fact_orders
LIMIT 5;