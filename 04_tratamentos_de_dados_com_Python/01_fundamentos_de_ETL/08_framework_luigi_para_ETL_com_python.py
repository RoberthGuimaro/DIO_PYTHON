"""
    Framework
    Luigi é um framework de execução criado pelo Spotify que cria pipelines
    de dados em Python. É um pacote Python (2.7, 3.6, 3.7 testado) que ajuda
    a construir pipelines complexos de trabalhos em lote. Ele lida com resolução
    de dependências, gerenciamento de fluxo de trabalho, visualização, tratamento
    de falhas, integração de linha de comando e muito mais.
"""

"""
    Tópicos
    Targe - Em palavras simples, um alvo contém a saída de uma tarefa. Um destino
    pode ser um local (por exemplo: um arquivo, my SQL, etc);

    Task - Tarefa é algo onde o trabalho real ocorre. Uma tarefa pode ser independente
    ou dependente é despejar os dados em um arquivo ou banco de dados. Antes de carregar
    os dados, os dados devem estar lá por qualquer meio (scraping, API, etc). Cada tarefa
    é representada como uma classe Python que contém certas funções-membro obrigatórias.
    Uma função de tarefa contém  os seguintes métodos:

    Require(): Esta função membro da classe task contém todas as instâncias de tarefas
    que devem ser executadas antes da tarefa atual.

    output(): Este método contém o destino onde a saída da tarefa será armazenada. Isso
    pode conter um ou mais objetos de destino.

    run(): Este método contém a lógica real para executar a tarefa.
"""

"""
    Instalando
    pip install luigi

    inicializando a interface grafica
    luigid
    
    acesso pelo
    localhost:8082
"""