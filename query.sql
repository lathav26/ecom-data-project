SELECT 
    c.name AS customer_name,
    p.name AS product_name,
    o.order_date,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total_amount
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
JOIN 
    order_items oi ON o.order_id = oi.order_id
JOIN 
    products p ON oi.product_id = p.product_id
ORDER BY 
    c.name, o.order_date;
