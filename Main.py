import ConsultaBD as bd
import Alerta as A

def main():
    datitos=bd.Consulta()
    #print(datitos)

    for i in datitos:#  i es el indice 
        print(datitos[i]['temperatura'])
        if i>1:
            if datitos[i-1]['temperatura']-datitos[i]['temperatura']>=3:
                print('juro por dios que ando')
                A.aviso(datitos,i)
main()