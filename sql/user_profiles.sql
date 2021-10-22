DROP TABLE user_profiles;

CREATE TABLE user_profiles(
    profile_id SERIAL,
    profile_name VARCHAR(255),
    primary key (profile_id)
);

INSERT INTO user_profiles (profile_name) VALUES
    ('Estudiante'),
    ('Creador'),
    ('Colaborador')
;
