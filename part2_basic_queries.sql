SELECT * FROM Sales;

SELECT Product, SUM(Price * Quantity) AS TotalRevenue
FROM Sales
GROUP BY Product;

SELECT Product, Price
FROM Sales
ORDER BY Price DESC
LIMIT 1;

SELECT * FROM Sales
WHERE OrderDate = '2024-01-30';
