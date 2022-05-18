import pyodbc
import pandas as pd 
import json

def main():
    ## Connection à la base de données TestTech SQL Server
    try:
        conn = pyodbc.connect(
            Trusted_Connected = "Yes",
            Driver = '{SQL Server}',
            Server = 'LAPTOP-IEBP4MPB\SQLEXPRESS',
            Database = "TestTech"
        )
    except pyodbc.Error as e:
        print(f"L'erreur est: '{e}'")
        exit(1)
    cursor = conn.cursor()

    ## Requête pour calculer le nombre de naissance par département
    cursor.execute('''
    SELECT lieux.departement, COUNT(people.id_people) 
    FROM people
    INNER JOIN lieux ON lieux.commune = people.commune
    GROUP BY lieux.departement
    ''')
    departements_rows = cursor.fetchall()
    departements_res = {}
    for r in departements_rows:
        departements_res[r[0]] = r[1]

    ## Requête pour calculer le nombre de naissance par région
    cursor.execute('''
    SELECT lieux.region, COUNT(people.id_people) 
    FROM people
    INNER JOIN lieux ON lieux.commune = people.commune
    GROUP BY lieux.region
    ''')
    regions_rows = cursor.fetchall()
    regions_res = {}
    for r in regions_rows:
        regions_res[r[0]] = r[1]

    cursor.close()

    ## Transformer les dictionnaires créés en JSON 
    regions_json = "./results/regions.json"
    data_region = json.dumps(regions_res, sort_keys=True, ensure_ascii=False)
    with open(regions_json,"w",encoding="utf8") as rj:
        rj.write(data_region)

    departements_json = "./results/departements.json"
    data_departement = json.dumps(departements_res, sort_keys=True, ensure_ascii=False)
    with open(departements_json,"w",encoding="utf8") as dj:
        dj.write(data_departement)


if __name__ == "__main__":
    main()