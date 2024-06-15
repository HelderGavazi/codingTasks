SELECT first_name, last_name
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Course.course_code = 'DS03';
