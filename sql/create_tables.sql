CREATE TABLE IF NOT EXISTS city (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS branch (
    branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES city(city_id),
    UNIQUE (branch_name, city_id)
);

CREATE TABLE IF NOT EXISTS product_line (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_category TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id TEXT NOT NULL UNIQUE,

    sale_date DATE NOT NULL,
    sale_time TIME NOT NULL,

    product_id INTEGER NOT NULL,
    branch_id INTEGER NOT NULL,

    customer_type TEXT NOT NULL,
    gender TEXT NOT NULL,
    payment_method TEXT NOT NULL,

    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL CHECK (unit_price >= 0),
    cogs REAL NOT NULL,

    tax_5_percent REAL NOT NULL,
    total REAL NOT NULL CHECK (total >= 0),

    profit REAL NOT NULL,
    profit_margin REAL NOT NULL CHECK (profit_margin BETWEEN -1 AND 1),
    customer_rating REAL CHECK (customer_rating BETWEEN 0 AND 10),


    FOREIGN KEY (product_id) REFERENCES product_line(product_id),
    FOREIGN KEY (branch_id) REFERENCES branch(branch_id)
);

CREATE INDEX IF NOT EXISTS idx_sales_date
ON sales(sale_date);

CREATE INDEX IF NOT EXISTS idx_sales_branch
ON sales(branch_id);

CREATE INDEX IF NOT EXISTS idx_sales_product
ON sales(product_id);

CREATE INDEX IF NOT EXISTS idx_sales_product_date
ON sales(product_id, sale_date);
