def Consulta():
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
    datos[f"{id_registro}"]={
            "fecha": Fecha,
            "temperatura": int(Temperatura),
            "presion": int(Presion),
            "humedad": int(Humedad),
            }

  #print(datos)
  #print (datos["1"]["fecha"][8:10]) #Hora
  #print (datos["1"]["fecha"][:8]) #Fecha

  cursor.close()
  cnx.close()
  return datos