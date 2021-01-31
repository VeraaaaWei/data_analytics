create table weblinks(
id SERIAL primary key,
name varchar(255) not null,
url varchar (255) not null,
description varchar(255));

INSERT INTO weblinks (url, name)
VALUES ('www.google.com',  'Google'),
('www.amazon.com', 'Amazon'),
('www.ign.com', 'IGN'),
('www.cuny.edu', 'CUNY');

SELECT * FROM weblinks;

CREATE TABLE copy_weblinks (LIKE weblinks);
SELECT * FROM copy_weblinks;

update weblinks
SET description = 'university' 
where id =17;
SELECT * FROM weblinks;

UPDATE weblinks
SET description = 'Website for your shopping needs'
WHERE name LIKE 'Amazon%'
SELECT * FROM weblinks;

UPDATE weblinks
SET description = 'url';
SELECT * FROM weblinks;

UPDATE weblinks
SET description = 'Empty Description';
SELECT * FROM weblinks;

delete from weblinks
where id = 7;
select * from weblinks
order by id;



