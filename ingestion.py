import pyodbc
import pandas as pd 


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

    ## Charger les données des ficgiers CSV
    df_lieux = pd.read_csv('data/lieux.csv')
    df_people = pd.read_csv('data/people.csv')

    ## Transformer la forme de la date pour s'adapter au type DATE de SQL Server
    df_people.rename(columns = {'date-naissance':'date_naissance'}, inplace = True)
    df_people['date_naissance'] = pd.to_datetime(df_people.date_naissance)

    ## Requête pour insérer les données dans les tables "lieux" et "people"
    try:
        for row in df_lieux.itertuples():
            cursor.execute('''
                        INSERT INTO lieux (commune, departement, region)
                        VALUES (?,?,?)
                        ''',
                        row.commune, 
                        row.departement,
                        row.region
                        )

        for row in df_people.itertuples():
            cursor.execute('''
                        INSERT INTO people (prenom, nom, date_naissance, commune)
                        VALUES (?,?,?,?)
                        ''',
                        row.prenom, 
                        row.nom,
                        row.date_naissance,
                        row.commune
                        )
        conn.commit()
    except pyodbc.Error as e:
        print(f"L'erreur est: '{e}'")
        exit(1)

    conn.close()


if __name__ == "__main__":
    main()