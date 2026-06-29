-- Dropping the tables if it already exists
DROP TABLE IF EXISTS orders;

DROP TABLE IF EXISTS users;

-- Table creation with schema

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users (user_id) ON DELETE CASCADE,
    product_name VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL
);

-- Data insertion into the tables

INSERT INTO
    users (name, email)
VALUES ('Alice', 'alice@gmail.com'),
    ('Bob', 'bob@gmail.com'),
    (
        'Charlie',
        'charlie@gmail.com'
    ),
    ('David', 'david@gmail.com');

INSERT INTO
    orders (user_id, product_name, amount)
VALUES (1, 'Laptop', 1200.00),
    (1, 'Mouse', 25.00),
    (2, 'Keyboard', 75.00),
    (NULL, 'Guest book', 15.00);

-- INNER JOIN

SELECT users.name, orders.product_name, orders.amount
FROM users
    INNER JOIN orders ON users.user_id = orders.user_id;

-- LEFT JOIN

SELECT users.name, users.email, orders.product_name
FROM users
    left JOIN orders on users.user_id = orders.user_id;

-- RIGHT JOIN

SELECT users.name, orders.product_name, orders.amount
FROM users
    RIGHT JOIN orders ON users.user_id = orders.user_id;

-- OUTER JOIN

SELECT users.name, users.email, orders.product_name, orders.amount
FROM users FULL OUTER
    JOIN orders on users.user_id = orders.user_id;