SELECT
    strftime('%H', sale_time) AS hour,
    COUNT(*) AS transactions,
    ROUND(SUM(total), 2) AS total_revenue
FROM sales
GROUP BY hour
ORDER BY hour;