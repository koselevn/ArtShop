-- Create the database
CREATE DATABASE ArtGallery;
USE ArtGallery;

-- Create the authors table
CREATE TABLE authors (
    autor_id INT AUTO_INCREMENT PRIMARY KEY,
    autor_full_name VARCHAR(255) NOT NULL,
    autor_description TEXT,
    autor_contact VARCHAR(255),
    autor_password VARCHAR(255)
);

-- Create the category table
CREATE TABLE category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

-- Create the paintings table
CREATE TABLE paintings (
    p_id INT AUTO_INCREMENT PRIMARY KEY,
    p_name VARCHAR(255) NOT NULL,
    p_img_link VARCHAR(255),
    p_description TEXT,
    p_price DECIMAL(10, 2),
    category_id INT,
    autor_id INT,
    FOREIGN KEY (category_id) REFERENCES category(category_id),
    FOREIGN KEY (autor_id) REFERENCES authors(autor_id)
);

-- Create the client table
CREATE TABLE client (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_full_name VARCHAR(255) NOT NULL,
    client_phone_number VARCHAR(20),
    client_country VARCHAR(100),
    client_city VARCHAR(100),
    client_area VARCHAR(100),
    client_address VARCHAR(255),
    client_apartment VARCHAR(50),
    client_index VARCHAR(20)
);

-- Create the order table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    p_id INT,
    client_id INT,
    FOREIGN KEY (p_id) REFERENCES paintings(p_id),
    FOREIGN KEY (client_id) REFERENCES client(client_id)
);
