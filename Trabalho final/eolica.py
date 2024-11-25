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
    ('Floripa_2023.2.csv', '2023_2')  # Corrigido para 2023_2
]

# Dicionário para armazenar os DataFrames
dfs = {}

# Carregar cada arquivo em um DataFrame
for arquivo, nome in arquivos:
    dfs[nome] = pd.read_csv(arquivo, on_bad_lines='skip', sep=";")  # Especificando o separador

# Realizar o merge para cada ano
concav_dfs = {}
for ano in range(2019, 2024):  # Intervalo dos anos presentes
    semestre_1 = f'{ano}_1'
    semestre_2 = f'{ano}_2'
    
    if semestre_1 in dfs and semestre_2 in dfs:
        concav_dfs[ano] = pd.concat([dfs[semestre_1], dfs[semestre_2]], axis=0)  # Corrigido para concat

# Lista para armazenar as médias de cada semestre
medias = []

# Loop para calcular as médias e armazenar
for ano, df in concav_dfs.items():
    print(df)
    # Converter os valores da coluna 'Vel. Vento (m/s)' para float
    df['Vel. Vento (m/s)'] = df['Vel. Vento (m/s)'].str.replace(',', '.')
    df['Vel. Vento (m/s)'] = pd.to_numeric(df['Vel. Vento (m/s)'], errors='coerce')
    # Remover valores NaN da coluna de velocidade do vento
    media = df['Vel. Vento (m/s)'].dropna().mean()
    medias.append((ano, media))

print(medias)
# Criar um DataFrame a partir da lista de médias
tabela = pd.DataFrame(medias, columns=['Ano', 'Velocidade Média (m/s)'])

# Mostrar a tabela
print(tabela)

# Gerar o gráfico de Velocidade Média x Semestre
plt.figure(figsize=(4, 5))
plt.plot(tabela['Ano'], tabela['Velocidade Média (m/s)'], marker='o', linestyle='-', color='b')
plt.title('Velocidade Média do Vento por Ano')
plt.xlabel('Ano')
plt.ylabel('Velocidade Média (m/s)')
plt.grid(True)
plt.show()