"""
    Utilizando a biblioteca
        Esta biblioteca dispõe de ferramentas simples e eficientes
        para análise preditiva de dados, é reutilável em diferentes
        situações, possuí código aberto, sendo acessível a todos e
        foi construída sobre os pacotes NumPy, SciPy e matplotilib.
"""

"""
    Scikit-learn
        Neste exemplo iremos criar uma massa de dados com 200
        observações, com apenas uma variável preditora, que será
        a variável target, que será a y. Para isso indicamos os
        parâmetros n_samples = 200 e n_features = 1. O parâmetro
        noise define o quão dispersos os dados estrão um dos outros
"""

"""
    Scikit-learn - etapa 01
    from sklearn.datasets import make_regression
    gerando uma massa de dados:
    x, y = make_regression(n_samples=200, n_features=1, noise=30)
"""

"""
    Utilizaremos o pacote matplotlib, com o módulo pyplot e a função
    scatter(), que criará o gráfico, e função show() que exibira a tela.

    import matplotlib.pyplot as plt

    mostrando no gráfico

    plt.scatter(x,y)
    plt.show()
"""

"""
    Comos os dados gerados, já podemos iniciar a criação de nosso modelo
    de machine learning.
    Para isso utilizaremos o módulo linear_model, e a função LinearRegression().

    from sklearn.linear_model import LinearRegression
    Criação do modelo
    modelo = LinearRegression()
"""

"""
    Após esta execução, o objeto modelo que acabamos de criar está pronto para
    receber os dados que darão origem ao modelo. Como não indicamos nenhum
    parâmetro específico na função, estamos utilizando suas configurações padrão.

    Agora precisamos apenas apresentar os dados ao modelo, e para isso temos o
    método fit(). Na dodumentação da função podemos conferir todos os métodos
    que ela possui.
"""

"""
    Scikit-learn - Etapa 02
    Após está etapa, nosso modelo de machine learn está pronto e podemos utilizá-lo
    para prever dados desconhecidos. Simplificando este primeiro entendimento, vamos
    apenas visualizar a reta de regressão linear que o modelo gera, com os mesmos dados
    que criaram o modelo. Para isso iremos utilizar o método predict(), indicando que
    queremos aplicar a previsão nos valores de x. O resultado do método será uma previsão
    de y para cada valor de x apresentado.

    modelo.predict(x)
"""

"""
    A função plot() do pacote pyplot gera uma reta com os dados apresentados. como já
    temos os dados de x e y, basta indicá-los na função. Assim, primeiramente montamos
    novamente o gráfico de x e y original com a função scatter(), e somamos a ele a reta
    de

    plt.scatter(x, y)
    plt.plot(x, modelo.predict(x), color='red', linewidth=3)
    plt.show()
"""