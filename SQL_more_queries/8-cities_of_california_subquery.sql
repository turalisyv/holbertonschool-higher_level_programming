-- Cities of California --

SELECT * FROM cities WHERE (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id
