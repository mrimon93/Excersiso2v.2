import psycopg2
print("Welcome to the phone list, the following commands are available:")
print("LIST, ADD, DELETE, QUIT")
dbconn = psycopg2.connect(
    host="localhost",
    port="5433",
    database="phonedb",
    user="postgres",
    password="tmad1652")
def read_phonelist(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(conn, name, phone):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.execute("COMMIT;")
    cur.close()
    print(f"{name} added!")
def delete_phone(conn, name):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
    print(f"{name} deleted!")
def save_phonelist(conn):
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
        add_phone(dbconn, name, phone)
    elif cmd == "DELETE":
        name = input("  Name: ")
        delete_phone(dbconn, name)
    elif cmd == "QUIT":
        save_phonelist(dbconn)
        print("Committing all changes to the database and quitting! Good bye!")
        exit()