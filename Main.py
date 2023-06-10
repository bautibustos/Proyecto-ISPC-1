import mysql.connector

cnx = mysql.connector.connect(user='root', password='FernetFree2023',
                              host='127.0.0.1',
                              database='sensores',
                              use_pure=False)
cursor = cnx.cursor()
query = ("SELECT * FROM registro")
cursor.execute(query)

datos={}
for (id_registro,Fecha,Temperatura,Humedad,Presion) in cursor: 
  datos[id_registro]=[]
  datos[id_registro].append({
					"temperatura": Temperatura,
					"presion": Presion,
					"humedad": Humedad,
					})
  diccionario={id_registro,Fecha,Temperatura,Humedad,Presion}
  print(diccionario)
cursor.close()
cnx.close()