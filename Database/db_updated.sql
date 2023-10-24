CREATE DATABASE  IF NOT EXISTS `chatbotdb`;
USE `chatbotdb`;

DROP TABLE IF EXISTS `categories`;

CREATE TABLE `categories` (
  `idcategories` int NOT NULL,
  `catergories_name` varchar(45) NOT NULL,
  PRIMARY KEY (`idcategories`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table `categories`

INSERT INTO `categories` (`idcategories`, `catergories_name`)
VALUES
  (1, 'Skincare'),
  (2, 'Makeup'),
  (3, 'Haircare'),
  (4, 'Fragrances'),
  (5, 'Nail Care'),
  (6, 'Bath and Body'),
  (7, 'Mens Grooming'),
  (8, 'Organic and Natural'),
  (9, 'Sunscreen and SPF'),
  (10, 'Beauty Tools');
  
select * from categories

LOCK TABLES `categories` WRITE;
UNLOCK TABLES;

-- Table structure for table `orders`

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `idorders` int NOT NULL AUTO_INCREMENT,
  `orderDate` date DEFAULT NULL,
  `order_totAmount` decimal(2,0) NOT NULL,
  `shipping_address` varchar(45) DEFAULT NULL,
  `order_status` varchar(25) DEFAULT NULL,
  `ordersdetails` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`idorders`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table `orders`

INSERT INTO `orders` (`orderDate`, `order_totAmount`, `shipping_address`, `order_status`, `ordersdetails`)
VALUES
  ('2023-10-23', 50, '123 Beauty Street, Cityville', 'Pending', 'Skincare products'),
  ('2023-10-22', 75, '456 Beauty Lane, Townsville', 'Shipped', 'Makeup and Fragrances'),
  ('2023-10-21', 30, '789 Glamour Road, Beautyville', 'Delivered', 'Haircare essentials'),
  ('2023-10-20', 60, '101 Cosmetics Avenue, Beautytown', 'Pending', 'Nail Care items'),
  ('2023-10-19', 40, '222 Spa Street, Cosmetictown', 'Shipped', 'Bath and Body products'),
  ('2023-10-18', 90, '333 Grooming Drive, Mansville', 'Delivered', 'Men orders Grooming supplies'),
  ('2023-10-17', 55, '444 Organic Road, Naturaltown', 'Pending', 'Organic and Natural items'),
  ('2023-10-16', 70, '555 Sunscreen Boulevard, SPFville', 'Shipped', 'Sunscreen and SPF products'),
  ('2023-10-15', 35, '666 Beauty Tools Lane, Toolstown', 'Delivered', 'Beauty Tools and Accessories'),
  ('2023-10-14', 25, '777 Skincare Street, Clearskinville', 'Shipped', 'Skincare and Makeup');
  
UPDATE orders
SET ordersdetails = 'Men orders Grooming supplies'
WHERE idorders= 6;

select * from orders;

LOCK TABLES `orders` WRITE;
UNLOCK TABLES;

-- Table structure for table `products`

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `idproducts` int NOT NULL,
  `product_name` varchar(45) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `price` decimal(2,0) NOT NULL,
  `brand` varchar(45) DEFAULT NULL,
  `categoryID` int DEFAULT NULL,
  PRIMARY KEY (`idproducts`),
  KEY `categoriesID_idx` (`categoryID`),
  CONSTRAINT `categoriesID` FOREIGN KEY (`categoryID`) REFERENCES `categories` (`idcategories`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table `products`
INSERT INTO `products` (`idproducts`, `product_name`, `description`, `price`, `brand`, `categoryID`)
VALUES
  (1, 'Moisturizing Cream', 'Hydrating cream for soft skin', 20, 'BeautyBrand', 1),
  (2, 'Lipstick - Red Velvet', 'Long-lasting red lipstick', 10, 'MakeupMaster', 2),
  (3, 'Shampoo - Nourishing', 'Strengthens and nourishes hair', 15, 'HairHealth', 3),
  (4, 'Perfume - Floral Bliss', 'Elegant floral fragrance', 30, 'ScentedLux', 4),
  (5, 'Nail Polish - Rose Quartz', 'Glossy rose nail color', 8, 'NailGlam', 5),
  (6, 'Bath Bomb Set', 'Relaxing bath bombs for self-care', 25, 'BathBliss', 6),
  (7, 'Mens Beard Oil', 'Softens and conditions beard', 18, 'ManlyGroom', 7),
  (8, 'Organic Face Mask', 'All-natural facial mask', 12, 'PureBeauty', 8),
  (9, 'Sunscreen SPF 30', 'Sun protection for the face', 15, 'SunSafe', 9),
  (10, 'Beauty Blender', 'Makeup blending sponge', 5, 'MakeupEssentials', 10),
  (11, 'Exfoliating Scrub', 'Gentle exfoliation for smooth skin', 12, 'BeautyGlow', 1),
  (12, 'Eyeshadow Palette - Natural Tones', 'Versatile eyeshadow palette', 18, 'MakeupMagic', 2),
  (13, 'Conditioner - Color-Protect', 'Preserves color-treated hair', 14, 'HairColorPro', 3),
  (14, 'Cologne - Citrus Burst', 'Fresh and zesty citrus scent', 28, 'CitrusScent', 4),
  (15, 'Nail Art Kit', 'Create stunning nail designs', 10, 'NailArtPro', 5),
  (16, 'Luxury Bathrobe', 'Plush bathrobe for ultimate comfort', 35, 'BathLux', 6),
  (17, 'Beard Grooming Kit', 'Complete beard care set', 22, 'BeardStyle', 7),
  (18, 'Organic Lip Balm', 'Nourishing lip balm', 5, 'PureLips', 8),
  (19, 'Sun Hat with UV Protection', 'Stylish sun hat for sun safety', 20, 'SunStyle', 9),
  (20, 'Makeup Brush Set', 'Professional makeup brush collection', 30, 'MakeupArtistry', 10);

select * from products;

LOCK TABLES `products` WRITE;
UNLOCK TABLES;

-- Table structure for table `promotions`

DROP TABLE IF EXISTS `promotions`;

CREATE TABLE `promotions` (
  `idcategoryID` int NOT NULL AUTO_INCREMENT,
  `promotion_name` varchar(45) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `discount_value` decimal(2,0) DEFAULT NULL,
  `categoryIDcol` varchar(45) DEFAULT NULL,
  `productID` int DEFAULT NULL,
  PRIMARY KEY (`idcategoryID`),
  KEY `productID_idx` (`productID`),
  CONSTRAINT `productID` FOREIGN KEY (`productID`) REFERENCES `products` (`idproducts`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table `promotions`
INSERT INTO `promotions` (`promotion_name`, `start_date`, `end_date`, `discount_value`, `categoryIDcol`, `productID`)
VALUES
  ('Summer Sale', '2023-06-01', '2023-06-30', 15, NULL, 1),
  ('Holiday Discounts', '2023-11-15', '2023-12-31', 10, NULL, 2),
  ('Haircare Special', '2023-07-10', '2023-08-10', 20, NULL, 3),
  ('Fragrance Festival', '2023-09-01', '2023-09-30', 25, NULL, 4),
  ('Nail Polish Promo', '2023-08-15', '2023-09-15', 30, NULL, 5),
  ('Spa Essentials', '2023-05-01', '2023-06-15', 10, NULL, 6),
  ('Grooming Discounts', '2023-07-20', '2023-08-20', 15, NULL, 7),
  ('Natural Beauty Sale', '2023-04-01', '2023-05-15', 20, NULL, 8),
  ('Sun Protection Deal', '2023-06-15', '2023-07-15', 15, NULL, 9),
  ('Makeup Brushes Special', '2023-10-01', '2023-10-31', 10, NULL, 10);
  
ALTER TABLE `promotions`
DROP COLUMN `categoryIDcol`;

select * from promotions;

LOCK TABLES `promotions` WRITE;
UNLOCK TABLES;

SELECT * FROM categories;
SELECT * FROM orders;
SELECT * FROM products;
SELECT * FROM promotions;


