CREATE TABLE profiles(
    profile_id SERIAL,
    profile_name VARCHAR(255),
    primary key (profile_id)
);

CREATE TABLE userProfiles(
    user_id INTEGER,
    profile_id INTEGER,
    PRIMARY KEY (user_id,profile_id),
    FOREIGN KEY  (user_id) references users (user_id),
    FOREIGN KEY  (profile_id) references profiles (profile_id)
);

INSERT INTO profiles (profile_name) VALUES
    ('Estudiante'),
    ('Creador'),
    ('Colaborador')
;


DROP TABLE profiles