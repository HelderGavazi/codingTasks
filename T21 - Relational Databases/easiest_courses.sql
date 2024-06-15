SELECT first_name, Course.course_name
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Student.mark >= 70;
