CREATE TABLE users(
    id int,
    name varchar NOT NULL,
    lastname varchar NOT NULL,
    email varchar NOT NULL,
    latitude varchar,
    longitude varchar,
    blocked boolean,
    primary key (id)
);