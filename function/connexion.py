import sqlite3

def connexion():
    
    # Chemin de la base de données SQLite
    db_path = 'data/bdd/trade_optimizer.db'

    # Connexion à la base de données SQLite
    conn = sqlite3.connect(db_path)

    return conn