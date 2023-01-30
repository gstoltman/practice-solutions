SELECT b.email
FROM (SELECT email, COUNT(id) AS total
        FROM Person a
        GROUP BY email) b
WHERE total > 1
