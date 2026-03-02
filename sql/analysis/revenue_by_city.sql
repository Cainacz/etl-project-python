SELECT
    c.city AS city,
    ROUND(SUM(s.total), 2)  AS total_revenue,
    ROUND(SUM(s.profit), 2) AS total_profit
FROM sales s
JOIN branch b
    ON s.branch_id = b.branch_id
JOIN city c
    ON b.city_id = c.city_id
GROUP BY c.city
ORDER BY total_revenue DESC;