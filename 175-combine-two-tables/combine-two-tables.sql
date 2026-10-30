WITH two_tables AS (
    SELECT p.firstName, p.lastName, a.city, a.state
    FROM Person p
    LEFT JOIN Address a
    on p.personId = a.personId
)
SELECT *
FROM two_tables