USE `seschool_06`;

CREATE TABLE Customers (
   id INT PRIMARY KEY,
   name VARCHAR(255),
   gender VARCHAR(10),
   age INT
);


CREATE TABLE Orders (
   id INT PRIMARY KEY,
   customer_id INT,
   order_date DATE,
   FOREIGN KEY (customer_id) REFERENCES Customers(id)
);


CREATE TABLE Dishes (
   id INT PRIMARY KEY,
   name VARCHAR(255),
   price DECIMAL(5,2),
   category VARCHAR(255)
);


CREATE TABLE Order_Dishes (
   order_id INT,
   dish_id INT,
   quantity INT,
   FOREIGN KEY (order_id) REFERENCES Orders(id),
   FOREIGN KEY (dish_id) REFERENCES Dishes(id)
);


SELECT c.name, o.order_date FROM Customers c
	JOIN Orders o ON c.id = o.customer_id
	ORDER BY c.name, o.order_date;

SELECT c.name, d.name AS dish_name FROM Customers c
	JOIN Orders o ON c.id = o.customer_id
	JOIN Order_Dishes od ON o.id = od.order_id
	JOIN Dishes d ON od.dish_id = d.id
	ORDER BY c.name, d.name;

SELECT c.name, SUM(d.price * od.quantity) AS total_amount FROM Customers c
	JOIN Orders o ON c.id = o.customer_id
	JOIN Order_Dishes od ON o.id = od.order_id
	JOIN Dishes d ON od.dish_id = d.id
	GROUP BY c.name
	ORDER BY total_amount DESC;

SELECT c.name, SUM(od.quantity) AS total_dishes FROM Customers c
	JOIN Orders o ON c.id = o.customer_id
	JOIN Order_Dishes od ON o.id = od.order_id
	GROUP BY c.name
	ORDER BY total_dishes DESC;

SELECT d.name, SUM(od.quantity) AS total_orders FROM Dishes d
	JOIN Order_Dishes od ON d.id = od.dish_id
	GROUP BY d.name
	ORDER BY total_orders DESC;

SELECT DISTINCT c.name FROM Customers c
	JOIN Orders o ON c.id = o.customer_id
	JOIN Order_Dishes od ON o.id = od.order_id
	JOIN Dishes d ON od.dish_id = d.id
	WHERE d.price > 50;

SELECT c.name, o.order_date, SUM(od.quantity) AS total_dishes FROM Customers c
	JOIN Orders o ON c.id = o.customer_id
	JOIN Order_Dishes od ON o.id = od.order_id
	GROUP BY c.name, o.order_date
	ORDER BY c.name, o.order_date;

SELECT d.category, SUM(od.quantity) AS total_orders FROM Dishes d
	JOIN Order_Dishes od ON d.id = od.dish_id
	GROUP BY d.category
	ORDER BY total_orders DESC;