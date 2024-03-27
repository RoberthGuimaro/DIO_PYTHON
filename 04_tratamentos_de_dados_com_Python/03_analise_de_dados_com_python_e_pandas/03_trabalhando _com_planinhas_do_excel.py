# importando a biblioteca
import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos arquivos
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

# Juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

# Exibindo as 5 primeiras linhas
df.head()

# Exibindo as 5 últimas linhas
df.tail()

# Exibe 5 linhas aleatórias de amostra
df.sample(5)

# Verificando o tipo de dados de cada coluna
df.dtypes

# Alterando o tipo de dado da coluna LojaID para objeto(string)
df["LojaID"] = df["LojaID"].astype("object")

# Verificando o tipo de dados de cada coluna
df.types

# Verificando as 5 primeiras linhas
df.head()

# Consultando colunas com valores nulos e retornando a quantidade
df.isnull().sum()

# Substituindo os valores nulos pela média, usando o inplace para alterar em memória
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

# Consultando colunas com valores nulos e retornando a quantidade
df.isnull().sum()

# Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

# Apagando as linhas com valores nulos
df.dropna(inplace=True)

# Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)

# Removendo linhas que estejam com valores nulos em todas as colunas
df.dropna(how="all", inplace=True)

"""Criando novas colunas"""

# Criando a coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])

# Caso não existisse a coluna Qtde e precisassemos descobrir a quantidade
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

# Retornando a maior receita
df["Receita"].max()

# Retornando a menor receita
df["Receita"].min()

# nlargest, retorna as 3 maiores receitas
df.nlargest(3, "Receita")

# nsmallest, retorna as 3 menores receitas
df.nsmallest(3, "Receita")

# Agrupamento por cidade
df.groupby("Cidade")["Receita"].sum()

# Ordenando o conjunto de dados, pela receita descendente,
# mostrando os 10 primeiros resultados
df.sort_values("Receita", ascending=False).head(10)

""" Trabalhando com datas """

# Tranformando a coluna data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

# Verificando o tipo de dado de cada coluna
df.dtypes

# Transformando a coluna de data em data
df["Data"] = pd.to_datatime(df["Data"])

# Verificando o tipo de dado de cada coluna
df.dtypes

# Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()

# Criando uma nova coluna com o ano
df["Ano_venda"] = df["Data"].dt.year

# Amostra de 5 itens aleatórios da base
df.sample(5)

# Extraindo o mês e o dia
df["Ano_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

# Retornando a data mais antiga
df["Data"].min()

# Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()

# Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter

# Filtrando as vendas de 2019 do mẽs de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2018) & (df["Data"].dt.month ==3)]

# Verificando a quantidade de linhas (vendas) referentes a cada ID, do maior para o menor valor
df["LojaID"].value_counts(ascending=False)

""" Visualização de Dados """

# Gráfico de Barras na vertical
# Verificando a quantidade de linhas (vendas) referentes a cada ID, do maior para o menor valor
df["LojaID"].value_counts(ascending=False).plot.bar();

# Gráficos de barras na horizontal
# Verificando a quantidade de linhas (vendas) referentes a cada ID, do maior para o menor valor
# Se atente ao ascending
df["LojaID"].value_counts(ascending=True).plot.barh();

# Gráfico de Pizaa
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie();

# Total de vendas por cidade
df["Cidade"].value_counts()

# Adicionando um títuo e alterando o nome dos eixos
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

# Alterando a cor
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

# Alterando o estilo
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title= "Total Produtos Vendidos x Mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend();

# Selecionando apenas as vendas de 2019
df_2019 = df[df["Ano_venda"] == 2019]

# Total de produtos vendidos por mês
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "o")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend();

# Gráfico de Histograma
plt.hist(df["Qtde"], color="orangered")

# Gráfico de Dispersão
plt.scatter(x=df_2019["dia_venda"], y=df_2019["Receita"]);

# Salvando em PNG
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum.plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend();
plt.savefig("grafico_QTDE_x_MES.png")
