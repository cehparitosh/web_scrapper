import sqlite3
def connect():
    conn = sqlite3.connect("oyo.db")
    conn.execute("CREATE TABLE IF NOT EXISTs DELHI_HOTELS(NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")
    print("Table created Successfully")
    conn.close()
def insert():
    conn = sqlite3.connect("oyo.db")
    in_table = "INSERT INTO DELHI_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES (?,?,?,?,?)"
    conn.execute(in_table, values)
    conn.commit()
    conn.close()
def show():
    conn = sqlite3.connect("oyo.db")
    cur = conn.cursor()
    sel = "SELECT * FROM DELHI_HOTELS"
    conn.execute(sel)
    t_data = cur.fetchall()
    for record in t_data:
        print(record)
    conn.close()
