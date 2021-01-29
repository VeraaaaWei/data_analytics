CREATE TABLE Claimmmsss (
Claim_ID_Number VARCHAR(50) PRIMARY KEY,
Claim_Receipt_Date TIMESTAMP,
Claim_Description VARCHAR(255),
Claimant_Birth_Date TIMESTAMP,
Law_Suit_Indicator VARCHAR(50),
Claimant_First_Name VARCHAR(50),
Claimant_Last_Name VARCHAR(50),
Policy_Number VARCHAR(50),
Claimant_Occupation VARCHAR(50),
Loss_Date TIMESTAMP,
Claim_Amount VARCHAR(50),
Claim_Paid_Amount VARCHAR(50),
Claim_Paid_Date VARCHAR(50));
SELECT * FROM Claimmmsss;

CREATE TABLE Customeerr(
Customer_ID_Number int PRIMARY KEY,
Customer_Type VARCHAR(50),
Customer_First_Name VARCHAR(50),
Customer_Last_Name VARCHAR(50),
Business_Name VARCHAR(50),
Address_Street_Name_Line_One VARCHAR(255),
Address_Street_Name_Line_Two VARCHAR(255),
Address_City VARCHAR(50),
Address_State VARCHAR(50),
Address_Postal_Code INT,
Address_Type VARCHAR(50),
Customer_Birth_Date VARCHAR(50),
Risk_Score INT);
SELECT * FROM Customeerr;

CREATE TABLE Policys1(
Policy_Number VARCHAR(50),
Customer_ID_Number int,
Policy_Effective_Date TIMESTAMP,
Policy_Expiration_Date TIMESTAMP,
Policy_Limit int,
Policy_Type VARCHAR(50),
Currency_Type VARCHAR(50),
Premium_Cost int);
SELECT * FROM Policys1;

CREATE TABLE Reserves1(
Customer_ID_Number int ,
Policy_Number VARCHAR(50),
Reserved_Amount int,
Reserved_Date TIMESTAMP );
SELECT * FROM Reserves1;

INSERT INTO Claimmmsss (
Claim_ID_Number, 
Claim_Receipt_Date,	
Claim_Description,
Claimant_Birth_Date,
Law_Suit_Indicator,
Claimant_First_Name,
Claimant_Last_Name,
Policy_Number, 
Claimant_Occupation, 
Loss_Date, 
Claim_Amount, 
Claim_Paid_Amount, 
Claim_Paid_Date)
VALUES ('C123450000',	
		'2020/12/5', 
		'Automobile accident',
		'1975/8/1', 
		'N',	
		'Joe', 
		'Smith',
		'P987654321',
		'Physician', 
		'2020/12/4',
		'5000',
	    '/',
	    '/');
INSERT INTO Claimmmsss (
Claim_ID_Number, 
Claim_Receipt_Date,	
Claim_Description,
Claimant_Birth_Date,
Law_Suit_Indicator,
Claimant_First_Name,
Claimant_Last_Name,
Policy_Number, 
Claimant_Occupation, 
Loss_Date, 
Claim_Amount, 
Claim_Paid_Amount, 
Claim_Paid_Date)
VALUES ('C123441000',
		 '2019/8/5',
		 'Automobile accident',	
		 '1975/8/1',
		 'N',
		 'Joe',
		 'Smith',
		 'P987654321',
		 'Physician',
		 '2019/8/2',
		 '7600',
		 '7100',
		 '2019/9/5'
		);
INSERT INTO Claimmmsss (
Claim_ID_Number, 
Claim_Receipt_Date,	
Claim_Description,
Claimant_Birth_Date,
Law_Suit_Indicator,
Claimant_First_Name,
Claimant_Last_Name,
Policy_Number, 
Claimant_Occupation, 
Loss_Date, 
Claim_Amount, 
Claim_Paid_Amount, 
Claim_Paid_Date)
VALUES ('C123440000',
		'2020/10/15',
		'Robbery',
		'1986/3/20',
		'N',
		'Mary',
		'Roberts',
		'P987654111',
		'Not provided',
		'2020/10/1',
		'25000',
		'20000',	
		'2020/11/5');
INSERT INTO Claimmmsss (
Claim_ID_Number, 
Claim_Receipt_Date,	
Claim_Description,
Claimant_Birth_Date,
Law_Suit_Indicator,
Claimant_First_Name,
Claimant_Last_Name,
Policy_Number, 
Claimant_Occupation, 
Loss_Date, 
Claim_Amount, 
Claim_Paid_Amount, 
Claim_Paid_Date)
VALUES('C345478900',
	   '2020/7/13',
	   'Property',
	   '1990/5/27',
	   'N',
	   'Aditya',
	   'Reddy',
	   'P987654222',
	   'Business Owner',
	   '2020/7/12',
	   '10000',
	   '8000',
	   '2020/8/12');
SELECT * FROM Claimmmsss;

INSERT INTO Customeerr(
Customer_ID_Number,
Customer_First_Name,
Customer_Last_Name,
Customer_Type,	
Business_Name,
Address_Street_Name_Line_One,
Address_Street_Name_Line_Two,
Address_City,
Address_State,
Address_Postal_Code,
Address_Type,
Customer_Birth_Date,
Risk_Score)
VALUES('777543325',
	   'Mary',
	   'Roberts',
	   'Individual',
	   ' ',
	   '123 Main Street',
	   ' ',
	   'Chicago',
	   'Illinois',
	   '60007',
	   'Residential',
	   '1986/3/20',
	   '75'),
	   ('777543800',
		'Joe',
		'Smith',
		'Individual',
		' ',
		'123 Park Avenue',
		' ',
		'New York',
		'New York',
		'10017',
		'Residential',
		'1963/2/27',
		'70'),
		('776983401',
		 'Aditya',
		 'Reddy',
		 'Business',
		 'ABC Systems',
		 '222 Hyde Street',
		 'Floor 2',
		 'San Francisco',
		 'California',
		 '94123',
		 'Business',
		 'no data', 
		 '50');
SELECT * FROM Customeerr;

INSERT INTO Policys1(Customer_ID_Number,
					 Policy_Number,
					 Policy_Effective_Date,
					 Policy_Expiration_Date,
					 Policy_Limit,
					 Policy_Type,
					 Currency_Type,
					 Premium_Cost)
VALUES ('777543800', 'P987654321','2020/2/11',	'2021/2/11',	'500000',	'Automobile',	'USD',	'2600'),
('777543800', 'P987654321',	'2019/2/11',	'2020/2/11',	'500000',	'Automobile',	'USD',	'2300'),
('777543800', 'P987654321',	'2018/2/11',	'2019/2/11',	'500000',	'Automobile',	'USD',	'2150'),
('777543800', 'P987654321',	'2017/2/11',	'2018/2/11',	'500000',	'Automobile',	'USD',	'2100'),
('777543325', 'P987654111',	'2020/3/15',	'2021/3/15',	'5000000','Excess/Umbrella',	'USD',	'5500'),
('776983401', 'P987654222',	'2020/6/15',	'2020/6/15',	'3000000','Property',	'USD',	'10000');
SELECT * FROM Policys1;

INSERT INTO Reserves1(Customer_ID_Number,	Policy_Number,	Reserved_Amount,	Reserved_Date)
VALUES(
'777543325',	'P987654111',	'5000',	'2020/3/15'),
('776983401',	'P987654222',   '7000',	'2020/6/15'),
('777543800',	'P987654321',	'1500',	'2017/2/11'),
('777543800',	'P987654321',	'1500',	'2018/2/11'),
('777543800',	'P987654321',	'1500',	'2019/2/11');
SELECT * FROM Reserves1;

SELECT*
FROM Reserves1
WHERE (Reserved_Amount > 5000)

SELECT*
FROM Policys1
WHERE (Customer_ID_Number = 777543800)

SELECT*
FROM Policys1
WHERE (Customer_ID_Number = 777543800 AND Premium_Cost >2500)

SELECT*
FROM Policys1
WHERE (Customer_ID_Number = 777543800 OR Premium_Cost >2500)

SELECT Loss_Date
FROM Claimmmsss
WHERE(Claimant_First_Name = 'Joe')
