1.
SELECT LastName, FirstName, Title
FROM employees;

2.
SELECT *
FROM employees
WHERE City = "Seattle";

3.
SELECT *
FROM employees
WHERE City = "London";

4.
SELECT *
FROM employees
WHERE Title LIKE "%Sales%";

5.
SELECT *
FROM employees
WHERE Title LIKE "%Sales%" AND TitleOfCourtesy IN ( "Ms.", "Mrs.");

6.
SELECT *
FROM employees
ORDER BY BirthDate
LIMIT 5;

7.
SELECT *
FROM employees
ORDER BY HireDate
LIMIT 5;

8.
SELECT *
FROM employees
WHERE ReportsTo IS NULL;

9.
SELECT employees.FirstName, employees.LastName, bosses.FirstName, bosses.LastName
FROM employees JOIN employees AS bosses
ON employees.ReportsTo = bosses.EmployeeID;

10.
SELECT COUNT(TitleOfCourtesy)
FROM employees
WHERE TitleOfCourtesy = "Ms." OR TitleOfCourtesy = "Mrs.";

11.
SELECT COUNT(TitleOfCourtesy)
FROM employees
WHERE TitleOfCourtesy = "Mr.";

12.
SELECT City, COUNT(City)
FROM employees
GROUP BY City;

13.
SELECT orders.OrderID, employees.FirstName, employees.LastName
FROM orders JOIN employees
ON orders.EmployeeID = employees.EmployeeID;

14.
SELECT orders.OrderID, shippers.CompanyName
FROM orders JOIN shippers
ON orders.ShipVia = shippers.ShipperID;

15.
SELECT ShipCountry, COUNT(ShipCountry)
FROM orders
GROUP BY ShipCountry;

16.
SELECT COUNT(orders.OrderID), employees.FirstName, employees.LastName
FROM orders JOIN employees
ON orders.EmployeeID = employees.EmployeeID
GROUP BY orders.EmployeeID
ORDER BY COUNT(orders.OrderID) DESC
LIMIT 1;

17.
SELECT COUNT(orders.CustomerID),  customers.CompanyName
FROM orders JOIN customers
ON orders.CustomerID = customers.CustomerID
GROUP BY orders.CustomerID
ORDER BY COUNT(orders.CustomerID) DESC
LIMIT 1;

18.
SELECT orders.OrderID, employees.FirstName, employees.LastName, customers.CompanyName
FROM orders
JOIN employees ON orders.EmployeeID = employees.EmployeeID
JOIN customers ON orders.CustomerID = customers.CustomerID

19.
SELECT customers.CompanyName, shippers.CompanyName
FROM customers
JOIN  shippers ON customers.CustomerID IN (
    SELECT orders.CustomerID
    FROM orders
    WHERE orders.ShipVia = shippers.ShipperID);
