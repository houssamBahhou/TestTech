--CREATE DATABASE TestTech

-- Créer la table des lieux en ajoutant une clé primaire qui s'incrémente automatiquement
CREATE TABLE lieux
(
	[id_lieux] INT IDENTITY(1,1) PRIMARY KEY,
	[commune] VARCHAR(32) NOT NULL,
	[departement] VARCHAR(64) NOT NULL,
	[region] VARCHAR(64) NOT NULL
)

-- Créer la table des personnes en ajoutant une clé primaire qui s'incrémente automatiquement
CREATE TABLE people
(
	[id_people] INT IDENTITY(1,1) PRIMARY KEY,
	[prenom] VARCHAR(32) NOT NULL,
	[nom] VARCHAR(32) NOT NULL,
	[date_naissance] DATE NOT NULL,
	[commune] VARCHAR(32)
)



