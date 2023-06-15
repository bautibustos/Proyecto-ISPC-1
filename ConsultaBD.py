def Consulta():
  import mysql.connector

  cnx = mysql.connector.connect(user='root', password='FernetFree2023',
                                host='127.0.0.1',
                                database='sensores',
                                use_pure=False)
  cursor = cnx.cursor()
  query = ("SELECT * FROM registro")
  cursor.execute(query)
  
  
  datos={}#definimos el diccionario
  prom = 0
  for (id_registro,Fecha,Temperatura,Humedad,Presion) in cursor:# llenamos de datos el diccionario 
    datos[int(id_registro)]={
            "fecha": Fecha,
            "temperatura": int(Temperatura),
            "presion": int(Presion),
            "humedad": int(Humedad),
            }
    prom = prom+Humedad
    
  ######## sacar promedio de la humedad ##########
  consulta = "SELECT * FROM registro ORDER BY id_registro DESC LIMIT 1" #hago una consulta al ultimo registro de la bd
  cursor.execute(consulta)#ejecuto la consulta
  CantidadRegistros = cursor.fetchone()[0]#retorna una tupla y le pido el item 0 (id_registro)
  archivo=open("PromHumedad.txt","w")
  archivo.write(str(prom/CantidadRegistros))#escribimos el resultado de la division y lo guaardamos en el txt
  archivo.close()
      
  cursor.close()
  cnx.close()
  return datos

#Consulta()