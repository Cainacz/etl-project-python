SELECT
    pl.product_category AS product,
    ROUND(SUM(s.total), 2)  AS total_revenue,
    ROUND(SUM(s.profit), 2) AS total_profit,
    ROUND(
        SUM(s.profit) / NULLIF(SUM(s.total), 0),
        2
    ) AS profit_margin
FROM sales s
JOIN product_line pl
    ON s.product_id = pl.product_id
GROUP BY pl.product_category
ORDER BY total_revenue DESC;