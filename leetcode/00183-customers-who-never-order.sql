SELECT name AS Customers
FROM Customers a
LEFT JOIN Orders b
ON a.id = b.customerId
WHERE b.id IS NULL
