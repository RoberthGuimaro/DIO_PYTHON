# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

# Criando nosso DataFrame
df = pd.read_excel("AdventureWorks Sales.xlsx")

# Visualizando as 5 primeiras linhas
df.head()

# Quantidade de linhas e colunas
df.shape

# Verificando o tipo das colunas
df.dtypes

# Qual a Receita Total?
df["Valor Venda"].sum()

# Qual o custo total?
# Criando a coluna custo
df["custo"] = df["Custo Unitario"].mult(df["Quantidade"])

# Verificando a primeira linha da tabela
# Para saber se a coluna 'custo' foi criada
df.head(1)

# Qual o custo total? Retornando apenas duas
# casas decimais
round(df["custo"].sum(), 2)

# Agora que temos a receita e custo total,
# podemos achar o lucro total.
# Vamos criar uma coluna de lucro que
# sera Receita - Custo.
df["lucro"] = df["Valor Venda"] - df["custo"]

# Verificando a primeira linha da tabela
# Para saber se a coluna 'lucro' foi criada
df.head(1)

# Total do lucro, arredondado para duas casas decimais
round(df["lucro"].sum(), 2)

# Criando uma coluna com total de dias para enviar o
# produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

# Verificando a primeira linha da tabela
# Para saber se a coluna 'Tempo_envio' foi criada
df.head(1)

# Agora queremos saber a média do tempo de envio
# para cada Marca, e para isso precisamos transformar
# a coluna Tempo_envio em numérica

# Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

# Verificando a primeira linha da tabela
# Para saber se a coluna 'Tempo_envio' está correta
df.head(1)

# Verificando o tipo da coluna 'Tempo_envio'
df["Tempo_envio"].dtype

# Media de tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()

# Missing Values

# Verificando se temos valores nulos
df.isnull().sum()

# Lucro por ano e marca?
# Vamos agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

# Formata o tipo float para apenas duas casas decimais
pd.options.display.float_format = '{:20,.2f}'.format

# Resetando o Index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

# Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

# Gráfico total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sorte_values(
    ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

# Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df["Tempo_envio"].describe()

# Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"])

# Histograma
plt.hist(df["Tempo_envio"])

# Tempo mínimo de envio
df["Tempo_envio"].min()

# Tempo máximo de envio
df["Tempo_envio"].max()

# Identificando o Outlier
df[df["Tempo_envio"] == 20]

# Salvando alteração na base, passando o parametro
# index = False, para que o index das linhas não
# sejam salvos.
df.to_csv("df_vendas_novo.csv", index=False)