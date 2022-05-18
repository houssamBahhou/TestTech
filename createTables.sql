CREATE TABLE lieux
(
	[id_lieux] INT IDENTITY(1,1) PRIMARY KEY,
	[commune] VARCHAR(32) NOT NULL,
	[departement] VARCHAR(64) NOT NULL,
	[region] VARCHAR(64) NOT NULL
)

CREATE TABLE people
(
	[id_people] INT IDENTITY(1,1) PRIMARY KEY,
	[prenom] VARCHAR(32) NOT NULL,
	[nom] VARCHAR(32) NOT NULL,
	[date_naissance] DATE NOT NULL,
	[commune] VARCHAR(32)
)



