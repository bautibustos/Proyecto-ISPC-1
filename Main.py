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
  datos[f'{id_registro}']=[]
  datos[''].append({
					#"id":(f"ID {idgame[cont]}"),
					"title": titulo[i],
					"platform": plat[i],
					"photo": imagen[i],
					"link": f"{link[i]} ",
					"description":desc[i]
					})
  diccionario={id_registro,Fecha,Temperatura,Humedad,Presion}
  print(diccionario)
cursor.close()
cnx.close()