import mariadb

try:
    conn = mariadb.connect(
        user = "galav",
        password = "md@123",
        host = "localhost",
        port = 3306,
        database = "college",
    )

    print("table created succesfully")
    cursor = conn.cursor()

    cursor.execute("""create table if not exists student (
           id int,
          name varchar (100),
         sec varchar(5), 
        branch varchar(10)""")

    conn.commit()
    cursor.close()

except mariadb.Error as e:
    print(" mariadb could not be connected: {e}")