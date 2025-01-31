SELECT SUM(Price * Quantity) AS TotalRevenue FROM Sales;

SELECT Product, SUM(Quantity) AS TotalQuantity
FROM Sales
GROUP BY Product
ORDER BY TotalQuantity DESC
LIMIT 1;

SELECT SUM(Price * Quantity) / COUNT(DISTINCT OrderID) AS AverageOrderValue
FROM Sales;

SELECT COUNT(DISTINCT Product) AS UniqueProducts FROM Sales;

SELECT Product, SUM(Price * Quantity) AS TotalRevenue
FROM Sales
GROUP BY Product
ORDER BY TotalRevenue DESC
LIMIT 1;
