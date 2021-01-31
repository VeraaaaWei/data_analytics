Create table videos(
video_ID serial PRIMARY KEY,
title VARCHAR(300),
length INT ,
URL VARCHAR (500)NOT NULL);

INSERT INTO videos (url, title)
VALUES ('https://www.youtube.com/watch?v=DyDfgMOUjCI',  'Bad Guy'),
('https://www.youtube.com/watch?v=EgBJmlPo8Xw', 'Everything I wanted'),
('https://www.youtube.com/watch?v=Ah0Ys50CqO8', 'You should see me in a crown ');
SELECT * FROM videos;

Create table reviewerrrr(
videos serial PRIMARY KEY,
video_ID INT,
username VARCHAR(100),
rating VARCHAR(10),
review VARCHAR(500),
FOREIGN KEY (video_ID) REFERENCES videos(video_ID));
SELECT * FROM reviewerrrr;

INSERT INTO reviewerrrr (video_ID,username,rating, review)
VALUES ('1','Kristian','/','Director: Can you drive?
Billie: No.
Director: Ill find something.'),
('1', 'Trooper','/','Billie Eilish: I’m The bad Guy.
Seth: I’m the bald guy.
Me: I’m  the sad guy.
YouTube: I’m the ad guy.'),
('2', 'Mikey','/','Billie just got her licence and she is already driving into oceans. '),
('2 ', 'Manager Raven','/','-1 year later, if you are watching this, you are a legend.');
SELECT * FROM reviewerrrr;

SELECT videos.video_ID, videos.title, videos.length, videos.URL, reviewerrrr.videos, reviewerrrr.username, reviewerrrr.rating, reviewerrrr.review
FROM videos
JOIN reviewerrrr on videos.video_ID = reviewerrrr.video_ID

