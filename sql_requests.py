sql_supprimer_table_personnes = """
    DROP TABLE IF EXISTS personnes;
"""

sql_creer_table_personnes = """
    CREATE TABLE IF NOT EXISTS personnes (
    id integer primary key,
    prenom text,
    nom text not null
    );
"""

sql_inserer_personnes = """
    INSERT INTO personnes 
    (prenom, nom)
    VALUES (?, ?);
"""

sql_lire_personnes = """
    SELECT *
    FROM personnes;
"""