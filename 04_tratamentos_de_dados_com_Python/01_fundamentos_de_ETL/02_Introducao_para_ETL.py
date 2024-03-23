""" Mas o que é uma ELT? 

ETL é um tipo de data integration em três etapadas (extração, tranformação,
carregamento) usado para combinar dados de diversas fontes. Ele é comumente
utilizado para construir um data warehouse

"""

""" 
Extract

Importar  dados de diversos tipos e formatos como:
    Pasta de trabalho,
    Diversos banco de dados,
    CSV,
    TXT,
    JSON,
    etc.

Transform
    Colunas, linhas
    Tipos de Dados
    Mesclar, acrescentar
    Listas, tabelas

Load
    Para o modelo de dados
    
"""

""" 
    ETLs, são ferramentas de software cuja função é a extração
    de dados de diversos sistemas, tranformação desses dados
    conforme regras de negócios e por fim o carregamento dos 
    dados geralmente para um Data Mart e/ou Data Warehouse
"""

"""
    Nesse processo, os dados são retirados (extract) de um
    sistema-fonte, converitidos (transform) em um formato que
    possa ser analisado, e armazenados (load) em nuvem ou outro
    sistema. Extract, Load, Transform (ELT) é uma abordagem
    alternativa, embora relacionada, projetada para jogar o
    processamento para o banco de dados, de modo a primorar
    a performance.
"""

"""
    Existem muitas ferramentas de ETL disponíveis no mercado
    como: IBM information Server (Data Stage), o Oracle Data
    Integrator (ODI), o Informatica power Center, o Microsoft
    Integration Services (SSIS). Existem também um conjunto de
    ferramentas de ETC Open Source como o PDI - Pentaho Data
    Integrator e Talend ETL.
"""

"""
    O processo de extração, transformação e carregamento (ETL)
    abrange alguns passos importantes. Como exemplo, podemos considerar
    um Banco de dados de Clientes Eseciais com todas as informações
    essesnciais 
"""

"""
    No mapeamento, a extração de origem deve conter a especificação da
    identidade e seus atributos detalhados, tudo armazenado numa zona
    temporária. Quando forem efetuadas as análises e filtragens dos dados,
    a nova versão poderá ser comparada com a cópia da versão prévia.
"""

"""
    A transformação inclui limpeza, racionalização e complementação dos registros.
    O processo de limpeza removerá erros e padronizará as informações. O processo
    de complementação inplicará no acréscimo dados.
"""

