CREATE DATABASE  IF NOT EXISTS `chatbotdb`;
USE `chatbotdb`;

DROP TABLE IF EXISTS `categories`;

CREATE TABLE `categories` (
  `idcategories` varchar(5) NOT NULL default'C001',
  `catergories_name` varchar(45) NOT NULL,
  PRIMARY KEY (`idcategories`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;categoriescategories

-- Dumping data for table `categories`

INSERT INTO `categories` (`idcategories`, `catergories_name`)
VALUES
  ('C001', 'Skincare'),
  ('C002', 'Makeup'),
  ('C003', 'Haircare'),
  ('C004', 'Fragrances'),
  ('C005', 'Nail Care'),
  ('C006', 'Bath and Body'),
  ('C007', 'Mens Grooming'),
  ('C008', 'Organic and Natural'),
  ('C009', 'Sunscreen and SPF'),
  ('C0010', 'Beauty Tools');
  
select * from categories

LOCK TABLES `categories` WRITE;
UNLOCK TABLES;

-- Table structure for table `orders`

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `idorders` varchar(5) NOT NULL default'O001',
  `orderDate` date DEFAULT NULL,
  `order_totAmount` decimal(10,0) NOT NULL,
  `shipping_address` varchar(45) DEFAULT NULL,
  `order_status` varchar(25) DEFAULT NULL,
  `ordersdetails` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`idorders`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table `orders`

INSERT INTO `orders` (`idorders`,`orderDate`, `order_totAmount`, `shipping_address`, `order_status`, `ordersdetails`)
VALUES
  ('O001','2023-10-23', 500.00, '123 Beauty Street, Cityville', 'Pending', 'Skincare products'),
  ('O002','2023-10-22', 750.00, '456 Beauty Lane, Townsville', 'Shipped', 'Makeup and Fragrances'),
  ('O003','2023-10-21', 300.00, '789 Glamour Road, Beautyville', 'Delivered', 'Haircare essentials'),
  ('O004','2023-10-20', 600.00, '101 Cosmetics Avenue, Beautytown', 'Pending', 'Nail Care items'),
  ('O005','2023-10-19', 400.00, '222 Spa Street, Cosmetictown', 'Shipped', 'Bath and Body products'),
  ('O006','2023-10-18', 900.00, '333 Grooming Drive, Mansville', 'Delivered', 'Men orders Grooming supplies'),
  ('O007','2023-10-17', 550.00, '444 Organic Road, Naturaltown', 'Pending', 'Organic and Natural items'),
  ('O008','2023-10-16', 700.00, '555 Sunscreen Boulevard, SPFville', 'Shipped', 'Sunscreen and SPF products'),
  ('O009','2023-10-15', 350.00, '666 Beauty Tools Lane, Toolstown', 'Delivered', 'Beauty Tools and Accessories'),
  ('O0010','2023-10-14', 250.00, '777 Skincare Street, Clearskinville', 'Shipped', 'Skincare and Makeup');
  
UPDATE orders
SET ordersdetails = 'Men orders Grooming supplies'
WHERE idorders= 6;

select * from orders;

LOCK TABLES `orders` WRITE;
UNLOCK TABLES;

-- Table structure for table `products`

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `idproducts` varchar(5) NOT NULL default'P001',
  `product_name` varchar(45) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `price` decimal(10,0) NOT NULL,
  `brand` varchar(45) DEFAULT NULL,
  `categoryID` varchar(5) NOT NULL,
  PRIMARY KEY (`idproducts`),
  KEY `categoriesID_idx` (`categoryID`),
  CONSTRAINT `categoriesID` FOREIGN KEY (`categoryID`) REFERENCES `categories` (`idcategories`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table `products`
INSERT INTO `products` (`idproducts`, `product_name`, `description`, `price`, `brand`, `categoryID`)
VALUES
  ('P001', 'Moisturizing Cream', 'Hydrating cream for soft skin', 200.00, 'BeautyBrand', 'C001'),
  ('P002', 'Lipstick - Red Velvet', 'Long-lasting red lipstick', 100.00, 'MakeupMaster', 'C002'),
  ('P003', 'Shampoo - Nourishing', 'Strengthens and nourishes hair', 150.00, 'HairHealth', 'C003'),
  ('P004', 'Perfume - Floral Bliss', 'Elegant floral fragrance', 300.00, 'ScentedLux', 'C004'),
  ('P005', 'Nail Polish - Rose Quartz', 'Glossy rose nail color', 800.00, 'NailGlam', 'C005'),
  ('P006', 'Bath Bomb Set', 'Relaxing bath bombs for self-care', 250.00, 'BathBliss', 'C006'),
  ('P007', 'Mens Beard Oil', 'Softens and conditions beard', 180.00, 'ManlyGroom', 'C007'),
  ('P008', 'Organic Face Mask', 'All-natural facial mask', 120.00, 'PureBeauty', 'C008'),
  ('P009', 'Sunscreen SPF 30', 'Sun protection for the face', 150.00, 'SunSafe', 'C009'),
  ('P0010', 'Beauty Blender', 'Makeup blending sponge', 500.00, 'MakeupEssentials', 'C0010'),
  ('P0011', 'Exfoliating Scrub', 'Gentle exfoliation for smooth skin', 120.00, 'BeautyGlow', 'C001'),
  ('P0012', 'Eyeshadow Palette - Natural Tones', 'Versatile eyeshadow palette', 180.00, 'MakeupMagic', 'C002'),
  ('P0013', 'Conditioner - Color-Protect', 'Preserves color-treated hair', 140.00, 'HairColorPro', 'C003'),
  ('P0014', 'Cologne - Citrus Burst', 'Fresh and zesty citrus scent', 280.00, 'CitrusScent', 'C004'),
  ('P0015', 'Nail Art Kit', 'Create stunning nail designs', 100.00, 'NailArtPro', 'C005'),
  ('P0016', 'Luxury Bathrobe', 'Plush bathrobe for ultimate comfort', 350.00, 'BathLux', 'C006'),
  ('P0017', 'Beard Grooming Kit', 'Complete beard care set', 220.00, 'BeardStyle', 'C007'),
  ('P0018', 'Organic Lip Balm', 'Nourishing lip balm', 500.00, 'PureLips', 'C008'),
  ('P0019', 'Sun Hat with UV Protection', 'Stylish sun hat for sun safety', 200.00, 'SunStyle', 'C009'),
  ('P0020', 'Makeup Brush Set', 'Professional makeup brush collection', 300.00, 'MakeupArtistry', 'C0010');

select * from products;

LOCK TABLES `products` WRITE;
UNLOCK TABLES;

-- Table structure for table `promotions`

DROP TABLE IF EXISTS `promotions`;

CREATE TABLE `promotions` (
  `promotionID` varchar(5) NOT NULL default 'PR001',
  `promotion_name` varchar(45) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `discount_value` decimal(2,0) DEFAULT NULL,
  `categoryIDcol` varchar(45) DEFAULT NULL,
  `productID` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`promotionID`),
  KEY `productID_idx` (`productID`),
  CONSTRAINT `productID` FOREIGN KEY (`productID`) REFERENCES `products` (`idproducts`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table `promotions`
INSERT INTO `promotions` (`promotionID`,`promotion_name`, `start_date`, `end_date`, `discount_value`, `categoryIDcol`, `productID`)
VALUES
  ('PR001','Summer Sale', '2023-06-01', '2023-06-30', 15, NULL, 'P001'),
  ('PR002','Holiday Discounts', '2023-11-15', '2023-12-31', 10, NULL, 'P002'),
  ('PR003','Haircare Special', '2023-07-10', '2023-08-10', 20, NULL, 'P003'),
  ('PR004','Fragrance Festival', '2023-09-01', '2023-09-30', 25, NULL, 'P004'),
  ('PR005','Nail Polish Promo', '2023-08-15', '2023-09-15', 30, NULL, 'P005'),
  ('PR006','Spa Essentials', '2023-05-01', '2023-06-15', 10, NULL, 'P006'),
  ('PR007','Grooming Discounts', '2023-07-20', '2023-08-20', 15, NULL, 'P007'),
  ('PR008','Natural Beauty Sale', '2023-04-01', '2023-05-15', 20, NULL, 'P008'),
  ('PR009','Sun Protection Deal', '2023-06-15', '2023-07-15', 15, NULL, 'P009'),
  ('PR010','Makeup Brushes Special', '2023-10-01', '2023-10-31', 10, NULL, 'P0010');
  
ALTER TABLE `promotions`
DROP COLUMN `categoryIDcol`;

select * from promotions;

LOCK TABLES `promotions` WRITE;
UNLOCK TABLES;

SELECT * FROM categories;
SELECT * FROM orders;
SELECT * FROM products;
SELECT * FROM promotions;

ALTER TABLE `products`
DROP COLUMN `brand`;

UPDATE products
SET price = 200.00
WHERE idproducts = 'P001';

UPDATE products
SET price = 100.00
WHERE idproducts = 'P002';

UPDATE products
SET price = 150.00
WHERE idproducts = 'P003';

UPDATE products
SET price = 300.00
WHERE idproducts = 'P004';

UPDATE products
SET price = 800.00
WHERE idproducts = 'P005';

UPDATE products
SET price = 250.00
WHERE idproducts = 'P006';

UPDATE products
SET price = 180.00
WHERE idproducts = 'P007';

UPDATE products
SET price = 120.00
WHERE idproducts = 'P008';

UPDATE products
SET price = 150.00
WHERE idproducts = 'P009';

UPDATE products
SET price = 500.00
WHERE idproducts = 'P0010';

UPDATE products
SET price = 120.00
WHERE idproducts = 'P0011';

UPDATE products
SET price = 180.00
WHERE idproducts = 'P0012';

UPDATE products
SET price = 140.00
WHERE idproducts = 'P0013';

UPDATE products
SET price = 280.00
WHERE idproducts = 'P0014';

UPDATE products
SET price = 100.00
WHERE idproducts = 'P0015';

UPDATE products
SET price = 350.00
WHERE idproducts = 'P0016';

UPDATE products
SET price = 220.00
WHERE idproducts = 'P0017';

UPDATE products
SET price = 500.00
WHERE idproducts = 'P0018';

UPDATE products
SET price = 200.00
WHERE idproducts = 'P0019';

UPDATE products
SET price = 300.00
WHERE idproducts = 'P0020';

