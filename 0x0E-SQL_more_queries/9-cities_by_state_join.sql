-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id AS id, states.name AS name, states.name AS name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY id ASC;
