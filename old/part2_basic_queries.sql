SELECT * FROM Sales;

SELECT Product, (Price * Quantity) AS TotalRevenue FROM Sales;

SELECT Product, Price
FROM Sales
WHERE Price = (SELECT MAX(Price) FROM Sales);

SELECT * FROM Sales WHERE OrderDate = '2024-01-01';
