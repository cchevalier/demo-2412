# demo contacts
contacts = [('john', 'doe'), 
            ('jane', 'doe'), 
            ('jean', 'dupont'), 
            ('marie', 'durand'),
            ('carlos', 'none'),
            ('mike', 'smith')
           ]
for c in contacts:
    print(c)


from helpers_sqlite3 import *
from sql_requests import *


ma_base_donnees = "contacts.db"
conn = ouvrir_connection(ma_base_donnees)


supprimer_table(conn, sql_supprimer_table_personnes)
creer_table(conn, sql_creer_table_personnes)


inserer_donnees(conn, sql_inserer_personnes, contacts)


mes_contacts = lire_donnees(conn, sql_lire_personnes)
print(mes_contacts)
