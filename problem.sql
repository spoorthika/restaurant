create database restaurant;
use restaurant;
CREATE TABLE orders_history (
    order_date DATE,
    order_id INT,
    item_id INT,
    size VARCHAR(20),
    price FLOAT,
    qty INT,
    status VARCHAR(20),
    total FLOAT
);
select * from orders_history;
CREATE TABLE payments (
    payment_date DATE,
    payment_id INT,
    order_id INT,
    amount_due FLOAT,
    tips FLOAT,
    discount FLOAT,
    total_paid FLOAT,
    payment_type VARCHAR(20),
    payment_status VARCHAR(20)
);

CREATE TABLE categories (
    cat_id INT PRIMARY KEY,
    category_name VARCHAR(50),
    menu_id INT,
    FOREIGN KEY (menu_id) REFERENCES menus(menu_id)
);

CREATE TABLE menu (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(50),
    cat_id INT,
    menu_id INT,
    size VARCHAR(50),
    price VARCHAR(50),
    FOREIGN KEY (cat_id) REFERENCES categories(cat_id),
    FOREIGN KEY (menu_id) REFERENCES menus(menu_id)
);
INSERT INTO menus (menu_id, menu_name) VALUES
(1, 'Food'),
(2, 'Drinks');

INSERT INTO categories (cat_id, category_name, menu_id) VALUES
(1, 'Starters', 1),
(2, 'Soft Drinks', 2),
(3, 'Mains', 1),
(4, 'Desserts', 2),
(5, 'Hot Drinks', 2);

INSERT INTO menu (item_id, item_name, cat_id, menu_id, size, price) VALUES
(1, 'Item1', 1, 1, 'Small, Large', '1.50, 2.50'),
(2, 'Item2', 1, 1, '', '3'),
(3, 'Item3', 2, 2, '', '2.5'),
(4, 'Item4', 2, 2, '', '1.5'),
(5, 'Item5', 2, 1, '', '1'),
(6, 'Item6', 3, 1, 'Small, Large', '2.50, 3.6'),
(7, 'Item7', 3, 1, '', '2.5'),
(8, 'Item8', 4, 2, 'Small, Large', '3.75, 6.5'),
(9, 'Item9', 4, 2, '', '1.5'),
(10, 'Item10', 5, 2, '', '2');


CREATE USER IF NOT exists 'root'@'localhost' IDENTIFIED BY 'root123';
FLUSH PRIVILEGES;
