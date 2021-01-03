import csv
import matplotlib.pyplot as plt
import numpy as np

abril = 0
maio  = 0
junho = 0
julho = 0
agosto = 0

setembro = 0
outubro = 0
novembro  = 0

with open('covid19-rio.csv', 'r', encoding = "ISO-8859-1") as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')

    for coluna in leitor:
        if('2020-04-30' in str(coluna[0])):                        
            abril+=int(coluna[3])   
        if('2020-05-31' in str(coluna[0])):            
            maio+=int(coluna[3])    
        if('2020-06-30' in str(coluna[0])):            
            junho+=int(coluna[3])      
        if('2020-07-31' in str(coluna[0])):            
            julho+=int(coluna[3])          
        if('2020-08-31' in str(coluna[0])):            
            agosto+=int(coluna[3])
        if('2020-09-30' in str(coluna[0])):            
            setembro+=int(coluna[3])
        if('2020-10-31' in str(coluna[0])):            
            outubro+=int(coluna[3])
        if('2020-11-30' in str(coluna[0])):            
            novembro+=int(coluna[3])        

    maio = maio - abril   
    junho = junho - maio - abril    
    julho = julho - junho - maio - abril
    agosto = agosto - julho - junho - maio - abril

    setembro = setembro - agosto - julho - junho - maio - abril
    outubro = outubro - setembro - agosto - julho - junho - maio - abril
    novembro = novembro - outubro - setembro - agosto - julho - junho - maio - abril
    
    periodo1 = [junho, julho, agosto, setembro]
    periodo2 = [outubro, novembro]

    mediaPeriodo1 = round((junho + julho + agosto + setembro) / 3)  
    varianciaPeriodo1 = np.var(periodo1)
    desvioPadraoPeriodo1 = np.std(periodo1)


    mediaPeriodo2 = round((outubro + novembro) / 3)   
    varianciaPeriodo2 = np.var(periodo2)
    desvioPadraoPeriodo2 = np.std(periodo2)

    print('------------------ PERIODO 1 ------------------')
    print('MEDIA: ', round(mediaPeriodo1))
    print('VARIÂNCIA: ', round(varianciaPeriodo1))
    print('DESVIO PADRÃO: ', round(desvioPadraoPeriodo1))
    print('\n')
    print('------------------ PERIODO 2 ------------------')
    print('MEDIA: ', round(mediaPeriodo2))
    print('VARIÂNCIA: ', round(varianciaPeriodo2))
    print('DESVIO PADRÃO: ', round(desvioPadraoPeriodo2))


    meses = ['junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro']
    valores = [junho, julho, agosto, setembro, outubro, novembro]

    plt.title('Casos de coronavírus no RJ')
    plt.ylabel('Quantidade de casos')
    plt.xlabel('Meses')
    plt.plot(meses, valores)
    plt.show()