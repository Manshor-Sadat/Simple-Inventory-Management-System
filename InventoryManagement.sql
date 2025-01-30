CREATE DATABASE InventoryManagement;
USE InventoryManagement;

CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(50) NOT NULL
);

CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierName VARCHAR(100) NOT NULL,
    ContactInfo VARCHAR(255)
);

CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    CategoryID INT,
    SupplierID INT,
    StockLevel INT DEFAULT 0,
    Price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT,
    Quantity INT NOT NULL,
    TransactionDate DATE NOT NULL,
    TransactionType ENUM('IN', 'OUT') NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Categories (CategoryName) VALUES ('Electronics'), ('Furniture'), ('Stationery');

INSERT INTO Suppliers (SupplierName, ContactInfo) 
VALUES ('Supplier A', 'contact@supplierA.com'), ('Supplier B', 'contact@supplierB.com');

INSERT INTO Products (ProductName, CategoryID, SupplierID, StockLevel, Price)
VALUES ('Laptop', 1, 1, 50, 1000.00), 
       ('Chair', 2, 2, 150, 75.00);

INSERT INTO Transactions (ProductID, Quantity, TransactionDate, TransactionType)
VALUES (1, 10, '2024-11-25', 'OUT'), 
       (2, 5, '2024-11-25', 'IN');


-- Add more categories
INSERT INTO Categories (CategoryName) 
VALUES 
    ('Computers'), 
    ('Appliances'), 
    ('Books'), 
    ('Toys'), 
    ('Groceries'), 
    ('Clothing'), 
    ('Sports'), 
    ('Health & Beauty');

-- Add more suppliers
INSERT INTO Suppliers (SupplierName, ContactInfo) 
VALUES 
    ('Supplier C', 'contact@supplierC.com'), 
    ('Supplier D', 'contact@supplierD.com'), 
    ('Supplier E', 'contact@supplierE.com'), 
    ('Supplier F', 'contact@supplierF.com'), 
    ('Supplier G', 'contact@supplierG.com');

-- Add more products
INSERT INTO Products (ProductName, CategoryID, SupplierID, StockLevel, Price) 
VALUES 
    ('Smartphone', 1, 1, 120, 500.00), 
    ('Desk', 2, 2, 80, 150.00), 
    ('Notebook', 3, 3, 500, 5.00), 
    ('Refrigerator', 4, 4, 20, 800.00), 
    ('Basketball', 7, 5, 100, 30.00), 
    ('Treadmill', 7, 1, 15, 1200.00), 
    ('Shampoo', 8, 3, 200, 10.00), 
    ('Blender', 4, 2, 50, 45.00), 
    ('Novel', 3, 5, 300, 15.00), 
    ('T-Shirt', 6, 4, 400, 20.00);

-- Add more transactions
INSERT INTO Transactions (ProductID, Quantity, TransactionDate, TransactionType) 
VALUES 
    (1, 5, '2024-11-20', 'OUT'), 
    (1, 20, '2024-11-18', 'IN'), 
    (2, 10, '2024-11-17', 'OUT'), 
    (3, 100, '2024-11-16', 'IN'), 
    (4, 2, '2024-11-15', 'OUT'), 
    (5, 15, '2024-11-14', 'IN'), 
    (6, 3, '2024-11-13', 'OUT'), 
    (7, 25, '2024-11-12', 'IN'), 
    (8, 7, '2024-11-11', 'OUT'), 
    (9, 30, '2024-11-10', 'IN'), 
    (10, 50, '2024-11-09', 'OUT'), 
    (5, 5, '2024-11-08', 'IN'), 
    (3, 20, '2024-11-07', 'OUT'), 
    (2, 15, '2024-11-06', 'IN'), 
    (4, 4, '2024-11-05', 'OUT'), 
    (6, 8, '2024-11-04', 'IN'), 
    (8, 2, '2024-11-03', 'OUT'), 
    (9, 12, '2024-11-02', 'IN'), 
    (10, 10, '2024-11-01', 'OUT'), 
    (7, 40, '2024-10-31', 'IN'), 
    (3, 200, '2024-10-30', 'OUT'), 
    (2, 5, '2024-10-29', 'IN'), 
    (1, 15, '2024-10-28', 'OUT'), 
    (6, 6, '2024-10-27', 'IN'), 
    (9, 8, '2024-10-26', 'OUT'), 
    (4, 1, '2024-10-25', 'IN'), 
    (5, 10, '2024-10-24', 'OUT'), 
    (8, 4, '2024-10-23', 'IN'), 
    (7, 20, '2024-10-22', 'OUT'), 
    (10, 25, '2024-10-21', 'IN'), 
    (3, 50, '2024-10-20', 'OUT'), 
    (2, 2, '2024-10-19', 'IN'), 
    (1, 30, '2024-10-18', 'OUT'), 
    (4, 5, '2024-10-17', 'IN'), 
    (6, 3, '2024-10-16', 'OUT'), 
    (5, 15, '2024-10-15', 'IN'), 
    (8, 10, '2024-10-14', 'OUT'), 
    (7, 60, '2024-10-13', 'IN'), 
    (9, 20, '2024-10-12', 'OUT'), 
    (10, 35, '2024-10-11', 'IN'), 
    (2, 10, '2024-10-10', 'OUT'), 
    (3, 300, '2024-10-09', 'IN');


INSERT INTO Products (ProductName, CategoryID, SupplierID, StockLevel, Price)
VALUES 
    ('Wireless Mouse', 1, 1, 120, 25.00),
    ('Gaming Keyboard', 1, 2, 80, 75.00),
    ('Office Chair', 2, 3, 200, 150.00),
    ('Standing Desk', 2, 4, 50, 250.00),
    ('Notebook', 3, 5, 500, 3.00),
    ('Printer', 1, 1, 30, 200.00),
    ('Smartphone', 1, 2, 100, 500.00),
    ('Bluetooth Speaker', 4, 3, 75, 40.00),
    ('Headphones', 4, 4, 120, 60.00),
    ('External Hard Drive', 1, 5, 60, 100.00),
    ('HD Monitor', 1, 1, 40, 300.00),
    ('Graphics Tablet', 1, 2, 30, 150.00),
    ('USB Flash Drive', 1, 3, 400, 15.00),
    ('LED Desk Lamp', 4, 4, 200, 25.00),
    ('Backpack', 3, 5, 150, 50.00),
    ('Coffee Maker', 4, 1, 100, 80.00),
    ('Vacuum Cleaner', 4, 2, 60, 150.00),
    ('Bookshelf', 2, 3, 70, 120.00),
    ('Laptop', 1, 4, 50, 1000.00),
    ('Tablet', 1, 5, 80, 400.00),
    ('Electric Kettle', 4, 1, 150, 30.00),
    ('Blender', 4, 2, 100, 40.00),
    ('Microwave Oven', 4, 3, 20, 100.00),
    ('Refrigerator', 4, 4, 15, 800.00),
    ('Treadmill', 7, 5, 20, 1200.00),
    ('Yoga Mat', 7, 1, 300, 25.00),
    ('Basketball', 7, 2, 150, 20.00),
    ('Soccer Ball', 7, 3, 200, 25.00),
    ('Tennis Racket', 7, 4, 80, 60.00),
    ('Running Shoes', 7, 5, 120, 100.00),
    ('Shampoo', 8, 1, 300, 10.00),
    ('Toothpaste', 8, 2, 400, 5.00),
    ('Body Lotion', 8, 3, 150, 12.00),
    ('Face Wash', 8, 4, 200, 8.00),
    ('T-Shirt', 6, 5, 500, 20.00),
    ('Jeans', 6, 1, 300, 40.00),
    ('Jacket', 6, 2, 100, 80.00),
    ('Socks', 6, 3, 600, 5.00),
    ('Hat', 6, 4, 150, 15.00),
    ('Sunglasses', 6, 5, 200, 30.00),
    ('Textbook', 3, 1, 100, 60.00),
    ('Novel', 3, 2, 150, 15.00),
    ('Comic Book', 3, 3, 200, 10.00),
    ('Cookbook', 3, 4, 80, 25.00),
    ('Children\'s Book', 3, 5, 120, 20.00),
    ('Desk Organizer', 3, 1, 300, 15.00),
    ('File Cabinet', 2, 2, 50, 200.00),
    ('Whiteboard', 2, 3, 70, 100.00),
    ('Easel', 2, 4, 30, 150.00),
    ('Conference Table', 2, 5, 20, 400.00);


INSERT INTO Products (ProductName, CategoryID, SupplierID, StockLevel, Price)
VALUES 
    ('Smartwatch', 1, 1, 70, 200.00),
    ('Wireless Earbuds', 1, 2, 100, 150.00),
    ('Projector', 1, 3, 30, 600.00),
    ('Camera', 1, 4, 40, 800.00),
    ('Tripod', 1, 5, 90, 50.00),
    ('E-Reader', 1, 1, 50, 120.00),
    ('Power Bank', 1, 2, 200, 30.00),
    ('Surge Protector', 1, 3, 120, 20.00),
    ('Wireless Router', 1, 4, 80, 100.00),
    ('Smart Light Bulb', 1, 5, 150, 25.00),
    ('Office Desk', 2, 1, 60, 250.00),
    ('Bookcase', 2, 2, 50, 180.00),
    ('Filing Cabinet', 2, 3, 30, 150.00),
    ('Office Partition', 2, 4, 40, 300.00),
    ('Reception Desk', 2, 5, 15, 500.00),
    ('Paper Shredder', 2, 1, 70, 100.00),
    ('Wall Clock', 2, 2, 200, 20.00),
    ('Whiteboard Markers', 3, 3, 400, 5.00),
    ('Highlighters', 3, 4, 500, 3.00),
    ('Pens', 3, 5, 600, 2.00),
    ('Paper Clips', 3, 1, 1000, 0.50),
    ('Stapler', 3, 2, 150, 10.00),
    ('Glue Sticks', 3, 3, 300, 1.50),
    ('Drawing Pad', 3, 4, 400, 10.00),
    ('Watercolor Set', 3, 5, 200, 25.00),
    ('Cutting Mat', 3, 1, 100, 15.00),
    ('Paint Brushes', 3, 2, 150, 12.00),
    ('Electric Drill', 4, 3, 60, 150.00),
    ('Saw', 4, 4, 40, 120.00),
    ('Hammer', 4, 5, 80, 25.00),
    ('Wrench Set', 4, 1, 50, 60.00),
    ('Screwdriver Set', 4, 2, 100, 40.00),
    ('Plier Set', 4, 3, 70, 50.00),
    ('Laser Level', 4, 4, 30, 100.00),
    ('Toolbox', 4, 5, 90, 80.00),
    ('Fitness Tracker', 7, 1, 100, 150.00),
    ('Dumbbell Set', 7, 2, 40, 200.00),
    ('Resistance Bands', 7, 3, 200, 25.00),
    ('Punching Bag', 7, 4, 30, 120.00),
    ('Foam Roller', 7, 5, 150, 20.00),
    ('Water Bottle', 7, 1, 300, 15.00),
    ('Protein Powder', 7, 2, 80, 50.00),
    ('Sports Shoes', 7, 3, 60, 100.00),
    ('Bicycle Helmet', 7, 4, 90, 80.00),
    ('Golf Clubs', 7, 5, 20, 400.00),
    ('Camping Tent', 7, 1, 30, 200.00),
    ('Sleeping Bag', 7, 2, 40, 100.00),
    ('Hiking Backpack', 7, 3, 50, 150.00),
    ('Portable Stove', 7, 4, 30, 80.00),
    ('Flashlight', 7, 5, 200, 30.00);


UPDATE Suppliers
SET SupplierName = CASE
    WHEN SupplierName = 'Supplier A' THEN 'Costco (General Goods)'
    WHEN SupplierName = 'Supplier B' THEN 'Staples (Office Supplies)'
    WHEN SupplierName = 'Supplier C' THEN 'Best Buy (Electronics)'
    WHEN SupplierName = 'Supplier D' THEN 'IKEA (Furniture)'
    WHEN SupplierName = 'Supplier E' THEN 'Nike (Sports Goods)'
END;

INSERT INTO Suppliers (SupplierName, ContactInfo)
VALUES
    ('Walmart (General Goods)', 'support@walmart.com'),
    ('Target (Retail Goods)', 'support@target.com'),
    ('Amazon (Online Marketplace)', 'support@amazon.com'),
    ('Home Depot (Hardware)', 'support@homedepot.com'),
    ('Adidas (Sports Goods)', 'support@adidas.com'),
    ('Costco (Wholesale)', 'support@costco.com'),
    ('Best Buy (Electronics)', 'support@bestbuy.com'),
    ('IKEA (Furniture)', 'support@ikea.com'),
    ('Nike (Athletic Gear)', 'support@nike.com'),
    ('Samsung (Electronics)', 'support@samsung.com'),
    ('Apple (Tech Products)', 'support@apple.com'),
    ('Sony (Consumer Electronics)', 'support@sony.com'),
    ('Lenovo (Computers)', 'support@lenovo.com'),
    ('Dell (IT Equipment)', 'support@dell.com'),
    ('HP (Printers and Laptops)', 'support@hp.com'),
    ('Staples (Office Supplies)', 'support@staples.com'),
    ('Canon (Cameras and Printers)', 'support@canon.com'),
    ('LG (Appliances and Electronics)', 'support@lg.com'),
    ('Under Armour (Sportswear)', 'support@underarmour.com'),
    ('Puma (Footwear)', 'support@puma.com'),
    ('Reebok (Athletic Wear)', 'support@reebok.com'),
    ('Unilever (Consumer Goods)', 'support@unilever.com'),
    ('Procter & Gamble (Personal Care)', 'support@pg.com'),
    ('Kroger (Grocery)', 'support@kroger.com'),
    ('Whole Foods (Organic Food)', 'support@wholefoods.com'),
    ('Samsung (Appliances)', 'support@samsung.com'),
    ('Asus (Computers)', 'support@asus.com'),
    ('Microsoft (Software)', 'support@microsoft.com'),
    ('Google (Technology)', 'support@google.com'),
    ('Facebook (Tech Services)', 'support@facebook.com'),
    ('Tesla (Electric Vehicles)', 'support@tesla.com'),
    ('Toyota (Automobiles)', 'support@toyota.com'),
    ('Honda (Vehicles)', 'support@honda.com'),
    ('Ford (Trucks)', 'support@ford.com'),
    ('Chevrolet (Cars)', 'support@chevrolet.com'),
    ('PepsiCo (Beverages)', 'support@pepsico.com'),
    ('Coca-Cola (Drinks)', 'support@coca-cola.com'),
    ('Nestle (Food and Drinks)', 'support@nestle.com'),
    ('Heinz (Condiments)', 'support@heinz.com'),
    ('General Mills (Cereals)', 'support@generalmills.com'),
    ('Colgate (Dental Care)', 'support@colgate.com'),
    ('Johnson & Johnson (Health Products)', 'support@jnj.com'),
    ('Pfizer (Pharmaceuticals)', 'support@pfizer.com'),
    ('Moderna (Biotech)', 'support@moderna.com'),
    ('Boeing (Aerospace)', 'support@boeing.com'),
    ('Lockheed Martin (Defense)', 'support@lockheedmartin.com'),
    ('SpaceX (Aerospace)', 'support@spacex.com'),
    ('Intel (Microchips)', 'support@intel.com'),
    ('AMD (Graphics Processors)', 'support@amd.com');




