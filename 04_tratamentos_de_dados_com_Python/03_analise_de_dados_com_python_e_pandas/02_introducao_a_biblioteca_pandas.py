# importando a bibliteca pandas
import pandas as pd

# df é igual a dataframe, o objeto df chama a biblioteca pandas, chama o módulo 
# read_csv e seta o erro de linhas como falso, no separador definimos como ";".
df = pd.read_csv("caminho do arquivo a ser lido", error_bad_lines=False,
                 sep=";")

# Visualizando as 5 primeiras linhas do arquivo
df.head()

# Objeto recebe, objeto renomeando as colunas do arquivo
df = df.rename(columns={"country":"Pais", "continent":"continente",
                        "year":"Ano", "lifeExp":"Espectativa de Vida",
                        "pop":"Pop Total", "gdpPercap":"PIB"})

# Visualizando as 10 primeiras linhas do arquivo
df.head(10)

# Total de linhas e colunas
df.shape

# Retornando apenas os nomes das colunas
df.columns

# Tipo de dado em cada coluna
df.dtypes

# Retornando as últimas 5 linhas
df.tail()

# Retornando as últimas 15 linhas
df.tail(15)

# Informações estatisticas do conjunto de dados (arquivo)
df.describe()

# Retorna os valores unicos existentes na coluna continente
df["continente"].unique()

# Cria objeto que localiza no conjunto de dados Oceania na coluna continente
oceania = df.loc[df["continente"] == "Oceania"]

# objeto com método para ver as 5 primeiras linhas do conjunto de dados
oceania.head()

# Faz o agrupamento da coluna continente para o numero de paises utilizando
# o método nunique()
df.groupby("continente")["Pais"].nunique()

# Faz o agrupamento da coluna Ano para a espectativa média, utilizando
# o método mean()
df.groupby("Ano")["Expectativa de Vida"].mean()

# Trás a média da coluna PIB
df["PIB"].mean()

# Retorna a soma da coluna PIB
df["PIB"].sum()