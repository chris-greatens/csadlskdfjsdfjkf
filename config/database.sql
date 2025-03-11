CREATE DATABASE sportscards;

CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

INSERT INTO categories VALUES (1, 'Sports');

CREATE TABLE IF NOT EXISTS subcategories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subcategory_name VARCHAR(100) NOT NULL
);

INSERT INTO subcategories VALUES (1, 'Baseball'), (2, 'Basketball'), (3, 'Football'), (4, 'Hockey'), (5, 'Multisport');

CREATE TABLE IF NOT EXISTS settype (
    id INT AUTO_INCREMENT PRIMARY KEY,
    settype_name VARCHAR(100) NOT NULL
);

INSERT INTO settype VALUES (1, 'Base'), (2, 'Insert');

CREATE TABLE IF NOT EXISTS releases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    release_year YEAR NOT NULL,
    release_brand VARCHAR(100) NOT NULL,
    release_name VARCHAR(100),
    category_id INT,
    subcategory_id INT,
    description VARCHAR(255),
    CONSTRAINT UC_Releases UNIQUE (release_year, release_brand, release_name)
);

CREATE TABLE IF NOT EXISTS sets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    release_id INT NOT NULL,
    set_name VARCHAR(100),
    set_type INT,
    is_autographed BOOLEAN,
    max_serial_num INT,
    description VARCHAR(255),
    CONSTRAINT UC_Sets UNIQUE (release_id, set_name, set_type)
);

CREATE TABLE IF NOT EXISTS cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    set_id INT NOT NULL,
    card_no VARCHAR(25) NOT NULL,
    card_title VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS card_players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_id INT NOT NULL,
    player_id INT NOT NULL,
    FOREIGN KEY (card_id) REFERENCES cards(id),
    FOREIGN KEY (player_id) REFERENCES players(id)
);

CREATE TABLE IF NOT EXISTS teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS card_teams ( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_id INT NOT NULL,
    team_id INT NOT NULL,
    FOREIGN KEY (card_id) REFERENCES cards(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE IF NOT EXISTS variations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    variation VARCHAR(100)
);

INSERT INTO variations (variation) VALUES ('Red Back'), ('Black Back'), ('Gray Back'), ('White Back');

CREATE TABLE IF NOT EXISTS card_variations ( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_id INT NOT NULL,
    variation_id INT NOT NULL,
    FOREIGN KEY (card_id) REFERENCES cards(id),
    FOREIGN KEY (variation_id) REFERENCES variations(id)
);

