CREATE TABLE users (
user_id INT PRIMARY KEY,
username VARCHAR(100)
);

CREATE TABLE problems (
problem_id INT PRIMARY KEY,
title VARCHAR(255),
description TEXT
);

CREATE TABLE submissions (
submission_id INT PRIMARY KEY,
user_id INT,
problem_id INT,
code TEXT,
status VARCHAR(50)
);
