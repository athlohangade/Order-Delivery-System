-- Clear existing database
-- DELETE FROM Customer;
-- DELETE FROM Address;
-- DELETE FROM DeliveryExecutive;
-- DELETE FROM Product;
-- DELETE FROM Orders;
-- DELETE FROM Delivery;
-- DELETE FROM OrderDetails;
-- DELETE FROM Cart;

-- INSERT INTO Customer VALUES ('C00000', 'Jon', 'Snow','js@gmail.com', 'bingo123', '7412963023', '5930370418');
-- INSERT INTO Customer VALUES ('C00001', 'Jeremy', 'Resse', 'jr@gmail.com', 'qwertyui123', '9784565458', '7903621220');
-- INSERT INTO Customer VALUES ('C00002', 'Mike', 'Crawford', 'mc@gmail.com', 'asdfghjkl', '7009324204', '9700932420');
-- INSERT INTO Customer VALUES ('C00003', 'Burton', 'Bush','bb@gmail.com', 'zxcvbnml', '6277237235', '8627723723');
-- INSERT INTO Customer VALUES ('C00004', 'Jery', 'Muny', 'jm@gmail.com', 'poiuytre', '6123557156', '6123557156');
-- INSERT INTO Customer VALUES ('C00005', 'Malcolm', 'West', 'mw@gmail.com', 'lkjhgfds', '9772390147', '7723901474');
-- INSERT INTO Customer VALUES ('C00006', 'Mikel', 'Spany','ms@gmail.com', 'mnbvcxza', '9699625732', '8699625732');
-- INSERT INTO Customer VALUES ('C00007', 'Charles', 'Hevel','ch@gmail.com', 'vitmitloni', '7654896251', '7654896251');
-- INSERT INTO Customer VALUES ('C00008', 'John', 'Russo', 'jr@gmail.com', 'coepsngr', '8631892372', '9631892372');
-- INSERT INTO Customer VALUES ('C00009', 'Travis', 'Ferd', 'tf@gmail.com', 'pictaundh', '7689625166', '7689625166');
-- INSERT INTO Customer VALUES ('C00010', 'Jarvis', 'Loan', 'jl@gmail.com', 'dapodibodh', '9638923918', '6389239187');

INSERT INTO Product VALUES ('MOB-000000', 'Razor Red', 'Mobile', '22999', '4.5', 'RAZR', '515');
INSERT INTO Product VALUES ('MOB-000001', 'Redmi 6 Pro', 'Mobile', '14999', '3.5', 'Xiaomi', '310');
INSERT INTO Product VALUES ('MOB-000002', 'Galaxy S9', 'Mobile', '27999', '4.0', 'Samsun', '130');
INSERT INTO Product VALUES ('MOB-000003', 'OnePlus 7T', 'Mobile', '36999', '4.2', 'OnePlus', '815');
INSERT INTO Product VALUES ('MOB-000004', 'Honor 8x', 'Mobile', '19999', '3.6', 'Honor', '220');

INSERT INTO Product VALUES ('LAP-000000', 'HP Pavilion x360', 'Laptop', '95000', '3.1', 'HP', '188');
INSERT INTO Product VALUES ('LAP-000001', 'Acer Aspire 3', 'Laptop', '24590', '4.0', 'Acer', '155');
INSERT INTO Product VALUES ('LAP-000002', 'HP 14 Pentium Gold', 'Laptop', '85499', '4.8', 'HP', '142');
INSERT INTO Product VALUES ('LAP-000003', 'Lenovo V145-15AST', 'Laptop', '45999', '3.2', 'Lenovo', '125');
INSERT INTO Product VALUES ('LAP-000004', 'Dell Inspiron 15 358', 'Laptop', '32999', '2.4', 'Dell', '120');

INSERT INTO Product VALUES ('BOK-000000', 'Intro to Linux', 'Book', '1000', '3.8', 'Tata McGraw', '120');
INSERT INTO Product VALUES ('BOK-000001', 'Rich Dad Poor Dad', 'Book', '150', '3.5', 'Texas', '105');
INSERT INTO Product VALUES ('BOK-000002', 'The Alchemist', 'Book', '250', '4.4', 'NYT', '200');
INSERT INTO Product VALUES ('BOK-000003', 'Raging Winds', 'Book', '600', '4.1', 'Khan', '170');
INSERT INTO Product VALUES ('BOK-000004', 'Thomas Calculus', 'Book', '700', '2.5', 'Mohini Publishers', '160');

INSERT INTO Product VALUES ('SPT-000000', 'Football', 'Sport', '800', '3.5', 'Arsenal', '150');
INSERT INTO Product VALUES ('SPT-000001', 'Badminton Racquet', 'Sport', '4500', '3.5', 'Yonex', '510');
INSERT INTO Product VALUES ('SPT-000002', 'Cricket Bat', 'Sport', '1600', '4.5', 'MRF', '220');
INSERT INTO Product VALUES ('SPT-000003', 'Tennis Ball', 'Sport', '600', '3.8', 'Spox', '320');
INSERT INTO Product VALUES ('SPT-000004', 'Carrom Board', 'Sport', '450', '4.2', 'Rewapuin', '510');

INSERT INTO Product VALUES ('CLT-000000', 'Blazer', 'Clothing', '8000', '4.5', 'Raymond', '100');
INSERT INTO Product VALUES ('CLT-000001', 'Mens Shirt', 'Clothing', '800', '3.5', 'Arrow', '100');
INSERT INTO Product VALUES ('CLT-000002', 'Casual T-Shirt', 'Clothing', '400', '3.9', 'Flying Machine', '100');
INSERT INTO Product VALUES ('CLT-000003', 'V-Neck Shirt', 'Clothing', '350', '3.4', 'Alfredo', '100');
INSERT INTO Product VALUES ('CLT-000004', 'Shorts', 'Clothing', '850', '3.8', 'Puma', '100');
