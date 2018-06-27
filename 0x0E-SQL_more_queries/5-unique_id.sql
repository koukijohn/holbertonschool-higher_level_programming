-- This is a script that creates the table unique_id on our MySQL server.
CREATE TABLE IF NOT EXISTS `unique_id`(id INT DEFAULT 1 UNIQUE, name
VARCHAR(256));
