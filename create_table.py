def create_table() -> None:
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS Phones (
        phoneId INTEGER PRIMARY KEY,
        contactName varchar(255),
        phoneValue varchar(255)
        );
        """
    cur.execute(sql)

    con.commit()
    con.close()
