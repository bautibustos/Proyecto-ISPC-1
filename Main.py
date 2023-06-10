import ConsultaBD as bd

def main():
    datitos=bd.Consulta()
    #print(datitos)

    for i in datitos:#  i es el indice 
        print(datitos[i]['temperatura'])
        if i>1:
          if datitos[i-1]['temperatura']-datitos[i]['temperatura']>=3:
            print('aaaaa')
main() 