CREATE TABLE userStatus(
    user_id INTEGER,
    blocked BOOLEAN,
    primary key  (user_id),
    FOREIGN KEY  (user_id) references users (user_id)
);
