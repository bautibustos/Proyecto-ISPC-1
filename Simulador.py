import random, time 
import mysql.connector


timeList=[time.strftime("%d"),
          time.strftime("%m"),
          time.strftime("%y"),
          time.strftime("%H"),
          time.strftime("%M")
          ] #tiempo de la computadora actual
print(timeList)

cnx = mysql.connector.connect(user='root', password='FernetFree2023',
                                host='127.0.0.1',
                                database='sensores',
                                use_pure=False)
cursor = cnx.cursor()

utlimodato = ("SELECT * FROM registro ORDER BY id_registro DESC LIMIT 1")
    # Ejecutar la consulta
cursor.execute(utlimodato)
    # Obtener el resultado
resultado = cursor.fetchone()
id_regis=int(resultado[0])


for i in range (0,168): # 168 son las horas semanales
    id_regis=id_regis+1
    temp = random.randint(10, 12)
    humedad = random.randint(15, 20)
    presion = random.randint(800, 1000)
    fecha = str(str(timeList[0])+timeList[1]+timeList[2]+str(timeList[3])+timeList[4]) # convierto toda la lista en str
    
    query = f"INSERT INTO registro (id_registro, fecha, Temperatura, Humedad, Presion) VALUES ({id_regis},{fecha},{temp},{humedad},{presion})"
    cursor.execute(query)
    cnx.commit()
    
    timeList[3]=int(timeList[3])+1 # sumo 1 hora
    if timeList[3] == 24:#si la hora es igual 24
        timeList[0]=int(timeList[0])+1#le sumo uno al dia
        timeList[3]=0                 #lo seteo en 0 una vez q son 24
    

#pasarle la fecha una vez analizar como subir la hora 


cursor.close()
cnx.close()
