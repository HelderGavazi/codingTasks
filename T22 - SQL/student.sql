-- Create the Student table
CREATE TABLE IF NOT EXISTS Student (
    STU_NUM CHAR(6) PRIMARY KEY,
    STU_SNAME VARCHAR(15),
    STU_FNAME VARCHAR(15),
    STU_INITIAL CHAR(1),
    STU_STARTDATE DATE,
    COURSE_CODE CHAR(3),
    PROJ_NUM INT
);

-- Insert rows into the Student table
INSERT INTO Student (STU_NUM, STU_SNAME, STU_FNAME, STU_INITIAL, STU_STARTDATE, COURSE_CODE, PROJ_NUM)
VALUES
('01', 'Snow', 'Jon', 'E', '2014-04-05', '201', 6),
('02', 'Stark', 'Arya', 'C', '2017-07-12', '305', 11),
('03', 'Lannister', 'Jamie', 'C', '2012-09-05', '101', 2),
('04', 'Lannister', 'Cercei', 'J', '2012-09-05', '101', 2),
('05', 'Greyjoy', 'Theon', 'I', '2015-12-09', '402', 14),
('06', 'Tyrell', 'Margaery', 'Y', '2017-07-12', '305', 10),
('07', 'Baratheon', 'Tommen', 'R', '2019-06-13', '201', 5);

-- Select all records with a COURSE_CODE of 305
SELECT * FROM Student
WHERE COURSE_CODE = '305';

-- Change the course code to 304 for the student whose student number is 07
UPDATE Student
SET COURSE_CODE = '304'
WHERE STU_NUM = '07';

-- Delete the row of the person named Jamie Lannister, who started on 5 September 2012, whose course code is 101 and project number is 2
DELETE FROM Student
WHERE STU_SNAME = 'Lannister'
  AND STU_FNAME = 'Jamie'
  AND STU_STARTDATE = '2012-09-05'
  AND COURSE_CODE = '101'
  AND PROJ_NUM = 2;

-- Change the PROJ_NUM to 14 for all those students who started before 1 January 2016 and whose course code is at least 201
UPDATE Student
SET PROJ_NUM = 14
WHERE STU_STARTDATE < '2016-01-01'
  AND COURSE_CODE >= '201';

-- Drop the Student table entirely
DROP TABLE Student;
