import pandas as pd
import matplotlib.pyplot as plt

# Lista com os arquivos e seus respectivos semestres
arquivos = [
    ('Floripa_2019.1.csv', '2019_1'),
    ('Floripa_2019.2.csv', '2019_2'),
    ('Floripa_2020.1.csv', '2020_1'),
    ('Floripa_2020.2.csv', '2020_2'),
    ('Floripa_2021.1.csv', '2021_1'),
    ('Floripa_2021.2.csv', '2021_2'),
    ('Floripa_2022.1.csv', '2022_1'),
    ('Floripa_2022.2.csv', '2022_2'),
    ('Floripa_2023.1.csv', '2023_1'),
    ('Floripa_2023.2.csv', '2023_2')  
]


dfs={}

for arquivo, nome in arquivos:
    dfs[nome]=pd.read_csv(arquivo,on_bad_lines='skip',sep=';')

concatdfs=pd.concat(dfs,axis=0,ignore_index=True)

concatdfs['Data']=pd.to_datetime(concatdfs['Data'],dayfirst=True)

concatdfs['Dia']=concatdfs['Data'].dt.day
concatdfs['Mês']=concatdfs['Data'].dt.month
concatdfs['Ano']=concatdfs['Data'].dt.year

def mensal():
    medias=[]

    concatdfs['Vel. Vento (m/s)']=concatdfs['Vel. Vento (m/s)'].str.replace(',','.')
    concatdfs['Vel. Vento (m/s)']=pd.to_numeric(concatdfs['Vel. Vento (m/s)'], errors = 'coerce')
    for mês in range(1,13):

        media=concatdfs[concatdfs['Mês']==mês]['Vel. Vento (m/s)'].mean()
        medias.append((mês,media))



    tabela=pd.DataFrame(medias, columns=['Mês', 'Velocidade Média (m/s)'])

    print(tabela)

    plt.figure(figsize=(10,6))
    plt.plot(tabela['Mês'], tabela['Velocidade Média (m/s)'], marker='o', linestyle='-',color='b')
    plt.title('Velocidade Média por mês')
    plt.xlabel('Meses')
    plt.ylabel('Velocidade Média (m/s)')
    plt.grid(True)
    plt.show()

def anual():
    anuais=[]
    concatdfs['Vel. Vento (m/s)']=concatdfs['Vel. Vento (m/s)'].str.replace(',','.')
    concatdfs['Vel. Vento (m/s)']=pd.to_numeric(concatdfs['Vel. Vento (m/s)'], errors = 'coerce')
    for ano in range (2019,2024):
        media1=concatdfs[concatdfs['Ano']==ano]['Vel. Vento (m/s)'].mean()
        anuais.append((ano,media1))
    
    tabela2=pd.DataFrame(anuais, columns=['Ano', 'Velocidade Média (m/s)'])

    print(tabela2)

    plt.figure(figsize=(10,6))
    plt.plot(tabela2['Ano'], tabela2['Velocidade Média (m/s)'], marker='o', linestyle='-', color='b')
    plt.xlabel('Ano')
    plt.ylabel('Velocidade Média (m/s)')
    plt.grid(True)
    plt.show()

anual()