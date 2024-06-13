select * from authors;
select * from category;
select * from `client`;
select * from orders;
select * from paintings;


-- Вивод первых 6 картин
select * from paintings limit 6;

-- Вывод всех категорий
select * from category;

-- Добавление категорий
DELIMITER //

CREATE PROCEDURE AddCategory(
    IN categoryName VARCHAR(255)
)
BEGIN
    -- Check if the category already exists
    IF NOT EXISTS (SELECT 1 FROM category WHERE category_name = categoryName) THEN
        -- Insert the new category if it doesn't exist
        INSERT INTO category (category_name) VALUES (categoryName);
    END IF;
END //

DELIMITER ;

CALL AddCategory('Abstractionism');



-- просмотр картин по имени
DELIMITER //

CREATE PROCEDURE SearchPaintings2(
    IN partial_name VARCHAR(255)
)
BEGIN
    SELECT *
    FROM paintings
    JOIN authors ON paintings.autor_id = authors.autor_id
    WHERE p_name LIKE CONCAT('%', partial_name, '%');
END //

DELIMITER ;

CALL SearchPaintings2('R');

-- просмотр 6 картин
DELIMITER //

DELIMITER //

CREATE PROCEDURE select6(
)
BEGIN
    SELECT *
    FROM paintings
    JOIN authors ON paintings.autor_id = authors.autor_id
    LIMIT 6;
END //

DELIMITER ;

CALL select6();

-- Добавление автора
DELIMITER //

CREATE PROCEDURE AddAuthor(
    IN full_name VARCHAR(255),
    IN description TEXT,
    IN contact VARCHAR(255),
    IN password VARCHAR(255)
)
BEGIN
    INSERT INTO authors (autor_full_name, autor_description, autor_contact, autor_password)
    VALUES (full_name, description, contact, password);
END //

DELIMITER ;

CALL AddAuthor('De Masor Actor', 'Описание Автора Описание Автора Описание Автора', '+380967777777', 'fgwy6f2');

-- Добавление картины
DELIMITER //

CREATE PROCEDURE AddPainting(
    IN pName VARCHAR(255),
    IN pImgLink VARCHAR(255),
    IN pDescription TEXT,
    IN pPrice DECIMAL(10, 2),
    IN categoryId INT,
    IN autorId INT
)
BEGIN
    -- Check if the category and author exist
    IF EXISTS (SELECT 1 FROM category WHERE category_id = categoryId) AND
       EXISTS (SELECT 1 FROM authors WHERE autor_id = autorId) THEN
        -- Insert the new painting
        INSERT INTO paintings (p_name, p_img_link, p_description, p_price, category_id, autor_id)
        VALUES (pName, pImgLink, pDescription, pPrice, categoryId, autorId);
    ELSE
        -- If the category or author does not exist, raise an error
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Category ID or Author ID does not exist';
    END IF;
END //

DELIMITER ;

CALL AddPainting('Degame Sofia g', 'img/image02.png', 'Описание картины Описание картины Описание картины Описание картины Описание картины', 1500.73, 1, 1);



-- Вывод картн по категории
DELIMITER //

CREATE PROCEDURE SearchPaintingsByCategory1(
    IN category_name VARCHAR(255)
)
BEGIN
    SELECT *
    FROM paintings
    JOIN category ON paintings.category_id = category.category_id
    JOIN authors ON paintings.autor_id = authors.autor_id
    WHERE category.category_name = category_name;
END //

DELIMITER ;

CALL SearchPaintingsByCategory1('Gothic')


-- Добавление клиента
DELIMITER //

CREATE PROCEDURE AddClient(
    IN full_name VARCHAR(255),
    IN phone_number VARCHAR(20),
    IN country VARCHAR(100),
    IN city VARCHAR(100),
    IN area VARCHAR(100),
    IN address VARCHAR(255),
    IN apartment VARCHAR(50),
    IN client_index VARCHAR(20)
)
BEGIN
    INSERT INTO client (
        client_full_name, 
        client_phone_number, 
        client_country, 
        client_city, 
        client_area, 
        client_address, 
        client_apartment, 
        client_index
    ) 
    VALUES (
        full_name, 
        phone_number, 
        country, 
        city, 
        area, 
        address, 
        apartment, 
        client_index
    );
END //

DELIMITER ;

CALL AddClient( 'Имя Клиента', '1234567890', 'Страна', 'Город', 'Район', 'Адрес 123', 'Квартира 4B', '123456' );


-- Добавление заказа по последнему добавленому клиенту
DELIMITER //

CREATE PROCEDURE AddOrder(
    IN painting_id INT
)
BEGIN
    DECLARE last_client_id INT;

    -- Получаем ID последнего добавленного клиента
    SELECT client_id INTO last_client_id
    FROM client
    ORDER BY client_id DESC
    LIMIT 1;

    -- Добавляем заказ для последнего добавленного клиента
    INSERT INTO orders (p_id, client_id)
    VALUES (painting_id, last_client_id);
END //

DELIMITER ;

CALL AddOrder(1); -- Здесь 1 - это ID картины