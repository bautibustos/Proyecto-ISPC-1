import ConsultaBD as bd
import Alerta as A

def main():
    datitos=bd.Consulta()# traigo la lista de datos.
    for i in datitos:#  i es el indice 
        print(datitos[i]['temperatura'])#print de checkeos
        if i>1:
            if datitos[i-1]['temperatura']-datitos[i]['temperatura']>=3: #compara en este caso una temperatura
                print('juro por dios que ando')
                A.aviso(datitos,i)
                
            elif datitos[i-1]['humedad']-datitos[i]['humedad']>5: #compara en este caso una humedad 
                print('juro por dios que ando')
                A.aviso(datitos,i)
main()