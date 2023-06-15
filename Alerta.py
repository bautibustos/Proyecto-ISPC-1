def aviso(datitos,i):
    import mysql.connector
    cnx = mysql.connector.connect(user='root', password='FernetFree2023',
                                host='127.0.0.1',
                                database='sensores',
                                use_pure=False)
    cursor = cnx.cursor()

    query = f"INSERT INTO alerta (id_alerta,Fecha, id_registro) VALUES (0,{datitos[i]['fecha']},{i})"
   
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()