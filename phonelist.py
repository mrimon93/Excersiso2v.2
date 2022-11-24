import psycopg2
print("Hello Muzammil, this is from Github") 
print("Welcome to the phone list, the following commands are available:")
print("LIST, ADD, DELETE, QUIT")

def SQL_Connection():
    dbconn = psycopg2.connect(
        host="localhost",
        database="Phonelistdv",
        user="postgres",
        password="Monasogsql@12")
    return dbconn
def read_phonelist(conn,):
    connection = SQL_Connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(conn, name, phone):
    connection = SQL_Connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.execute("COMMIT;")
    cur.close()
    print(f"{name} added!")
def delete_phone(conn, name):
    connection = SQL_Connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
    print(f"{name} deleted!")
def save_phonelist(conn):
    connection = SQL_Connection()
    cur = conn.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()
while True: ## REPL - Read Execute Print Loop/Read Execute Program Loop
            ##https://codewith.mu/en/tutorials/1.1/repl
    cmd = input("Command: ")
    if cmd == "LIST":
        listrow = read_phonelist(dbconn)
        for row in listrow:
            print(row[0] + "\t" + row[1])
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        add_phone(SQL_Connection(), name, phone)
    elif cmd == "DELETE":
        name = input("  Name: ")
        delete_phone(SQL_Connection(), name)
    elif cmd == "QUIT":
        save_phonelist(SQL_Connection())
        print("Committing all changes to the database and quitting! Good bye!")
        exit()
