-- SELECT name Customers
-- FROM Customers c
-- WHERE c.id NOT IN (
--     SELECT o.customerId
--     FROM Orders o
-- )

SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
);