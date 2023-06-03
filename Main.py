import mysql.connector

cnx = mysql.connector.connect(user='root', password='FernetFree2023',
                              host='127.0.0.1',
                              database='sensores',
                              use_pure=False)
cursor = cnx.cursor()
query = ("SELECT * FROM pepe")
cursor.execute(query)
for (idpepe,pepecol) in cursor:
  print(pepecol)
  print(idpepe)
cursor.close()
cnx.close()