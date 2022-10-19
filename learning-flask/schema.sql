
DROP TABLE IF EXISTS orderDetails;

CREATE TABLE orderDetails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    customer_name TEXT NOT NULL,
    sales_channel TEXT NOT NULL,
    destination TEXT NOT NULL,
    items INTEGER,
    item_status TEXT NOT NULL
);