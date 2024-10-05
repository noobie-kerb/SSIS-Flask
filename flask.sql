CREATE DATABASE IF NOT EXISTS ccc181_flask
USE ccc181_flask;
CREATE TABLE College (
    college_code VARCHAR(10) PRIMARY KEY,
    college_name VARCHAR(25)
);

CREATE TABLE Program (
    program_code VARCHAR(10) PRIMARY KEY,
    program_name VARCHAR(50),
    college VARCHAR(10),
    FOREIGN KEY (college) REFERENCES College(college_code)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

CREATE TABLE Student (
    student_id VARCHAR(9) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    program VARCHAR(10),
    year tinyint,
    gender VARCHAR(20),
    FOREIGN KEY (program) REFERENCES Program(program_code)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);
