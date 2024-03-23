"""Temos 3 etapas
    1 Extract
    2 Transform
    3 Load
"""

""" 
    1 - Extract
    Processo de extração dedados consiste em se comunicar com
    outros sistemas ou bancos de dados para capturar os dados
    que serão insridos no destino, seja uma Staging Area ou
    outro sistema.
"""

"""
    2 - Transform
    O processo de transformação de dados é composto por várias
    etapas: padronização, limpeza, qualidade. Dados vindos de 
    sistemas diferentes tem padrões diferentes seja de nomenclatura
    ou mesmo de tipos de dados (varchar2 Oracle ou Varchar Sql Server).
"""

"""
    3 - Load
    O processo de load é a etapa final onde os dados são lidos das áreas
    de staging e preparação de dados, carregados no Data Warehouse ou
    Data Mart Final.
"""

"""
    Garantia significativa de qualidade dos dados
    A Ferramentas de ETL, através de sequẽncias de operações e instruções
    tem condições de solucionar prolemas de maior complexidade.
"""

"""
    Funcionalidade de execução
    Uma ferramenta de ETL já possui suas funções especificas, sendo
    necessárias apenas a atenção no fluxo de dados.
"""

"""
    Desenvolvimento das cargas
    Mesmo que o usuário não seja técnico poderá desenvolver uma rotina
    de carga em uma ferramenta de ETL, devido a facilidade e rapidez
    para codificação.
"""

"""
    Manuteção das cargas
    As tarefas de manutenão de rotina de carga são mais simples de realizar
    em relacão à manutenção de código.
"""

"""
    Metainformação
    Os metadados(informações úteis para identificar, localizar, entender e gerenciar
    os dados) são gerados e mantidos de forma automática com a ferramenta, evitando
    problemas de geração de informações incorretas na finalização do processo.
"""

"""
    Perfomance
    Os métodos mais usados para trabalhar com grandes volumes conseguem extrair,
    transformar e carregar dados com maior velocidade e menos recursos, como gravações
    em bloco e operações não logadas.
"""

"""
    Transferência
    Ferramentas de ELT podem ser deslocadas de um servidor mais facilmente ou distribuídas
    entre vários servidores.
"""

"""
    Conectividade
    A conexão de uma ferramenta de ETL com múltiplas fontes de dadosé transparente. Caso
    sejam precisas mais fontes como o SAP, VSAM, Mainframe ou qualquer outra, basta a
    aquisição do conector sem a necessidade de codificar um.
"""

"""
    Reinicialização
    Ferramantas possuem a capacidade de reiniciar a carga onde pararam sem a necessidade
    de codificação.
"""

"""
    Segurança e Estabilidade
    É possível articular melhor a segurança tornando-a mais modulas, dividindo as finalidades
    (criação de cargas, execução de cargas, agendamentos, etc.)
"""