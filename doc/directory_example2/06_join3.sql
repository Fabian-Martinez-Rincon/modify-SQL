/* Join data from the Order table and Customer to the OrderDetail table */

SELECT 
	c.CompanyName              AS Customer, 
	c.Country                  AS Country, 
	c.City                     AS City,
	COUNT(DISTINCT od.OrderId) AS Orders,
	COUNT(od.Id)               AS OrderLines
FROM OrderDetail     AS od
INNER JOIN [Order]    AS o ON o.Id = od.orderid
INNER JOIN [Customer] AS c ON o.customerid = c.Id
WHERE c.Country = 'Nombre del país'
GROUP BY c.CompanyName, c.Country, c.City
ORDER BY c.CompanyName