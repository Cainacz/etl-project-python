SELECT
    customer_type,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY customer_type;