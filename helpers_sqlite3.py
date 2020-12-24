# helpers-sqlite
import sqlite3

def ouvrir_connection(nom_bdd):
    try:
        conn = sqlite3.connect(nom_bdd)
    except sqlite3.Error as e:
        print("Erreur lors de la connection à la base de données")
        print(e)
        return None
    return conn

def supprimer_table(conn, sql_suppression_table):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_suppression_table)
        conn.commit()
    except sqlite3.Error as e:
        print("Erreur lors de la suppression de la table")
        print(e)
        return
    cursor.close()
    print("La table a été supprimée avec succès")
    
def creer_table(conn, sql_creation_table):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_creation_table)
        conn.commit()
    except sqlite3.Error as e:
        print("Erreur lors de la création de la table")
        print(e)
        return
    cursor.close()
    print("La table a été crée avec succès")
    
def executer_sql(conn, sql_code):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_code)
        conn.commit()
    except sqlite3.Error as e:
        print("Erreur lors de l'exécution du code SQL")
        print(sql_code)
        print(e)
        return
    cursor.close()
    print("Le code SQL a été exécuté avec succès")
    
def inserer_donnees(conn, sql_insertion_table, donnees):
    try:
        cursor = conn.cursor()
        for d in donnees:
            cursor.execute(sql_insertion_table, d)
        conn.commit()
    except sqlite3.Error as e:
        print("Erreur lors de l'insertion des données")
        print(e)
        return
    cursor.close()
    print("Les données ont été insérées avec succès")

def lire_donnees(conn, sql_requete):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_requete)
        conn.commit()
    except sqlite3.Error as e:
        print("Erreur lors de la lecture des données")
        print(e)
        return None
    
    data = []
    for row in cursor:
        data.append(row)
    cursor.close()
    print("Les données ont été lues avec succès")
    return data
