import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database='phonebook',
    user='postgres',
    password='1234',
    port='5433'
)
cur = config.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    level INTEGER NOT NULL,
    score INTEGER NOT NULL);
""")

cur.execute("""
INSERT INTO users (username, level, score) 
VALUES ('Rina', 0, 0), ('Shuaq', 0, 0);
""")

config.commit()

cur.close()
config.close()