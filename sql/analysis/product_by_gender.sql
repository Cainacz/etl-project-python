SELECT
    p.product_category,
    s.gender,
    SUM(s.quantity) AS total_quantity
FROM sales s
JOIN product_line p
    ON s.product_id = p.product_id
GROUP BY p.product_category, s.gender
ORDER BY p.product_category, total_quantity DESC;