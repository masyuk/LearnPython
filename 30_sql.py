import pypyodbc

connection = pypyodbc.connect("Connection string")

cursor = connection.cursor()

mySQLQuery = ("""
                SELECT * 
                FROM database
            """)

cursor.execute(mySQLQuery)

result = cursor.fetchall() #выгрести все

for row in result:
    name = row[0]
    #etc.........