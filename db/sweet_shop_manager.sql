DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    deactivated BOOLEAN
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity INT,
    buying_cost FLOAT,
    selling_price FLOAT,
    category VARCHAR(255),
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE
);