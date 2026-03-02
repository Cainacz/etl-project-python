SELECT
    strftime('%Y-%m', sale_date) AS month,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY month
ORDER BY month;