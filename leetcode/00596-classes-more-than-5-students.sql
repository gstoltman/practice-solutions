SELECT b.class
FROM (SELECT class, COUNT(student) as total
    FROM Courses a
    GROUP BY class) b
WHERE total >= 5
