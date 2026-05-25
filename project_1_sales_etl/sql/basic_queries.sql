INSERT INTO orders (order_id, customer_id, order_date, amount)
VALUES
    (1, 101, '2024-01-01', 120.00),
    (2, 102, '2024-01-02', 250.00),
    (3, 101, '2024-01-04', 300.00),
    (4, 103, '2024-01-05', 90.00),
    (5, 102, '2024-01-07', 400.00);

SELECT
    customer_id,
    COUNT(order_id) AS order_count,
    SUM(amount) AS total_spending,
    AVG(amount) AS avg_order_value
FROM orders
GROUP BY customer_id
ORDER BY total_spending DESC;