import sqlite3

def create_database():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("CREATE TABLE contact(name text,number integer)")
    print("command executed")
    conn.commit()
    conn.close()



def show_all():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contact")
    items = fetchall()
    for item in items():
        print(item)

    conn.commit()
    conn.close()

def add_con(name,number):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contact VALUES(?,?),(name,number)")
    print("command executed")
    conn.commit()
    conn.close()
