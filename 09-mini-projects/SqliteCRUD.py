import sqlite3

conn = sqlite3.connect("college.db")

cursor = conn.cursor()

cursor.execute("""create table if not exists student (id int, 
name varchar[100],
  roll_no int ) """)

cursor.executemany( "insert into student (id, name, roll_no) values (?,?,?)",
               [ (1, "chirag",106),
               (2, "diggaj", 125),
                (3, "devang", 125)])

conn.commit()

cursor.execute("Select* from student")
rows = cursor.fetchall()

for row in rows:
    print(row)


conn.commit()
cursor.close()