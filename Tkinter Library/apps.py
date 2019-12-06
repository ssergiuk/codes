import psycopg2

def conection():
    return  "conn = psycopg2.connect('dbname = 'crossfit' user = 'postgres' password = 'root' host = 'localhost' port = '5432'') cur = conn.cursor()"

def create_table():
    conn = psycopg2.connect("dbname = 'crossfit' user = 'postgres' password = 'root' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS crossy (item TEXT, quantity INTEGER, price  REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname = 'crossfit' user = 'postgres' password = 'root' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO crossy VALUES ('%s', '%s', '%s')" %(item, quantity,price)) (possible sql injection)
    cur.execute("INSERT INTO crossy VALUES (%s, %s, %s)" , (item, quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname = 'crossfit' user = 'postgres' password = 'root' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM crossy")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname = 'crossfit' user = 'postgres' password = 'root' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM crossy WHERE item = %s", (item))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("dbname = 'crossfit' user = 'postgres' password = 'root' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE crossfit SET quantity = %s, price = %s WHERE item = %s", (quantity,price,item))
    conn.commit()
    conn.close()
create_table()
print(view())
#print(view())
#delete("water")
#insert("water++", 10, 5)
