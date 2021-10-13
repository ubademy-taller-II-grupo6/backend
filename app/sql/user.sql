DROP TABLE users;

CREATE TABLE users(
    user_id SERIAL,
    user_name VARCHAR(255) NOT NULL,
    user_lastname VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) unique NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    user_wallet Float NOT NULL,
    user_blocked  Boolean NOT NULL,
    user_profile INT NOT NULL,
    primary key (user_id),
    CONSTRAINT fk_profile
        FOREIGN KEY(user_profile)
            REFERENCES user_profiles(profile_id)
)