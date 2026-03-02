SELECT
    payment_method,
    COUNT(*) AS transactions,
    ROUND(SUM(total), 2) AS total_revenue
FROM sales
GROUP BY payment_method
ORDER BY total_revenue DESC;