SELECT p.firstName, p.lastName, a.city, a.state
FROM Person P
LEFT JOIN Address a
on p.personId = a.personId