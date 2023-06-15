import ConsultaBD as bd
import Alerta as A
from datetime import datetime

def main():
    bd.Consulta()
    Menu=int(input('\nIngerese 1 si quiere ver la simulacion de la alerta\n'
                    'Ingrese 2 si quiere ingresar las fechas\n'
                    'Ingrese 3 si quiere ver el promedio de la Humedad \n'
                   ))
    datitos=bd.Consulta()# traigo la lista de datos.
    if Menu==1:#este es el menu de la alerta
        for i in datitos:#  i es el indice 
            print(datitos[i]['temperatura'])#print de checkeos
            if i>1:
                if datitos[i-1]['temperatura']-datitos[i]['temperatura']>=3: #compara en este caso una temperatura
                    print('Esto seria una alerta')
                    A.aviso(datitos,i)
                    
                elif datitos[i-1]['humedad']-datitos[i]['humedad']>5: #compara en este caso una humedad 
                    print('Esto seria una alerta')
                    A.aviso(datitos,i)
                    
                elif datitos[i-1]['presion']-datitos[i]['presion']>800: #compara en este caso una humedad 
                    print('Esto seria una alerta')
                    A.aviso(datitos,i)    

    elif Menu == 2:# este es la seleccion de la fecha de inicio y de final
        print (f"En la base simulamos datos desde el {datitos[1]['fecha']} hasta el {datitos[len(datitos)]['fecha']}")
        while True:
            try:
                fechainicio=str(input('\nIngrese Fecha Inicio con el siguiente formato (DDMMYY)\n'))
                fechafin=str(input('\nIngrese Fecha Fin con el siguiente formato (DDMMYY)\n'))
                datetime.strptime(fechainicio, '%d%m%y')
                datetime.strptime(fechafin, '%d%m%y') #verificacion del formato que ingreso el usuario(es el que se usa en la base de datos)
                break
            except ValueError:
                print('Ingrese la fecha con el formato que corresponde')
                
        CantidadDeLecturas=0
        for i in datitos:
            FechaStr=str(datitos[i]['fecha'])
            if (fechainicio>=FechaStr[0:5] or FechaStr[0:5]>=fechainicio) and FechaStr[0:5]<=fechafin:
                CantidadDeLecturas=CantidadDeLecturas+1
        print ("La cantidad de mediciones tomadas de presion es: ",CantidadDeLecturas)
    
    elif Menu == 3: #aca usamos el promedio
        archivo=open("PromHumedad.txt","r") #leemos el promedio
        print('El promedio de la Humedad es: ',archivo.read()) #Leemos y mostramos el contenido del archivo que guardamos en consulta BD
        archivo.close()
        
main()