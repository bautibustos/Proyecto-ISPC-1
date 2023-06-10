def aviso(datitos,i):
    import mysql.connector
    cnx = mysql.connector.connect(user='root', password='FernetFree2023',
                                host='127.0.0.1',
                                database='sensores',
                                use_pure=False)
    cursor = cnx.cursor()
    """
    utlimodato = ("SELECT * FROM alerta ORDER BY id_alerta DESC LIMIT 1")
    # Ejecutar la consulta
    cursor.execute(utlimodato)

    # Obtener el resultado
    resultado = cursor.fetchone()
    print(resultado)
    """
    query = f"INSERT INTO alerta (id_alerta,Fecha, id_registro) VALUES (0,{datitos[i]['fecha']},{i})"
    #val = (f"{datitos[i]['fecha']}", f"{i}")
    
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()