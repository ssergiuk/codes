import sqlite3

def create_table():
    conn = sqlite3.connect("sport.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS crossfit (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("sport.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO crossfit VALUES (?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("sport.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM crossfit")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("sport.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM crossfit WHERE item=?" , (item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = sqlite3.connect("sport.db")
    cur = conn.cursor()
    cur.execute("UPDATE crossfit SET quantity = ?, price = ? WHERE item = ?", (quantity,price,item))
    conn.commit()
    conn.close()

update(11, 6, "wine Glass")


print(view())
#delete("water")
#insert("water++", 10, 5)
