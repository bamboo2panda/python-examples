import psycopg2


#connect to db
con = psycopg2.connect(
    host = "0.0.0.0",
    database = "postgres",
    user = "postgres",
    password = "mysecretpassword",
    port = "5432")


#cursor
cur = con.cursor()

#execute query

#insert row 
#cur.execute("insert into employee (id, name) values (%s, %s)", (4, "Jessy"))

cur.execute("select id, name from employee")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]}, name {r[1]}")


#commit changes
con.commit()
#close cursor
cur.close()
#close connection
con.close()