/* Join data from the Category table to the Product table */

SELECT  
	Product.Id, 
	Product.ProductName, 
	Product.Price,
	Category.CategoryName, 
	Category.Description as [CategoryDescription]
FROM [Product]
INNER JOIN [Category] on Product.CategoryId = Category.id
WHERE Category.CategoryName = 'Nombre de la categoría'
ORDER BY Product.ProductName