SELECT b.name AS Employee
FROM Employee a
LEFT JOIN Employee b
ON (a.id = b.managerId)
WHERE b.salary > a.salary
