import ConsultaBD as bd

def main():
    datitos=bd.Consulta()
    #print(datitos)

    for i in datitos:#  i es el indice 
        print(datitos[i]['temperatura'])
        print(i+1)
        if datitos[i]['temperatura']-datitos[int(i)+1]['temperatura']>=3:
            print('aaaaa')
main() 