USE amazon;

-- Ques 1: Write a query to create a procedure that selects all products and call the procedure.
-- Create procedure to select all products
DELIMITER //
CREATE PROCEDURE select_all_products()
BEGIN
    SELECT * FROM products;
END //
DELIMITER ;

CALL select_all_products();

-- Ques 2: Write a query to create a function that calculates the total revenue from the 'orders' and 'payment' tables for completed orders, and call the function to get the total revenue.
-- Create function to get total revenue
DELIMITER $$
CREATE FUNCTION get_total_revenue()
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE total_revenue DECIMAL(10,2);
    SELECT SUM(p.amount) INTO total_revenue
    FROM payment p
    INNER JOIN orders o ON p.oid = o.oid
    WHERE p.status = 'completed';
    RETURN total_revenue;
END$$
DELIMITER ;

SELECT get_total_revenue();

-- Ques 3: Write a query to create a procedure with an IN parameter to retrieve details of a specific product based on the product ID passed as a parameter. Call the procedure for product ID 5.
-- Create procedure with IN parameter to get product details
DELIMITER $$
CREATE PROCEDURE get_product_details(IN product_id INT)
BEGIN
    SELECT * FROM products WHERE pid = product_id;
END$$
DELIMITER ;

CALL get_product_details(5);

-- Ques 4: Write a query to create a procedure with an OUT parameter to get the count of products in the 'products' table, store it in a variable, and select the variable to display the count.
-- Create procedure with OUT parameter to get product count
DELIMITER $$
CREATE PROCEDURE get_product_count(OUT product_count INT)
BEGIN
    SELECT COUNT(*) INTO product_count FROM products;
END$$
DELIMITER ;

CALL get_product_count(@product_count);
SELECT @product_count AS product_count;

-- Ques 5: Write a query to use the predefined SUM() cursor to calculate the total price of all products in the 'products' table where the product category is 'Electronics'.
-- Create procedure to calculate total price of electronics
DELIMITER $$
CREATE PROCEDURE calc_total_electronics_price(OUT total_price DECIMAL(10,2))
BEGIN
    SELECT SUM(price) INTO total_price
    FROM products
    WHERE category = 'Electronics';
END$$
DELIMITER ;

CALL calc_total_electronics_price(@total);
SELECT @total AS total_electronics_price;

-- Ques 6: Write a query to declare and use a cursor to iterate through the 'products' table and print the product name for each product.
-- Create procedure to print product names using cursor
DELIMITER //
CREATE PROCEDURE print_product_names()
BEGIN
    DECLARE product_name VARCHAR(100);
    DECLARE done INT DEFAULT FALSE;
    DECLARE product_cursor CURSOR FOR SELECT pname FROM products;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN product_cursor;

    get_names: LOOP
        FETCH product_cursor INTO product_name;
        IF done THEN
            LEAVE get_names;
        END IF;
        SELECT product_name;
    END LOOP get_names;

    CLOSE product_cursor;
END //
DELIMITER ;
