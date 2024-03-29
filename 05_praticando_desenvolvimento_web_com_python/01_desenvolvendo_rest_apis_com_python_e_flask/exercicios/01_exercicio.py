"""
    - Desenvolva uma API que gerencie um cadastro de tarefas.

    - A API terá uma lista de tarefas que deverá ter os seguintes campos:
        id, responsável, tarefa e status.

    - A API deverá permitir listar todas as tarefas e também incluir novas
        tarefas.

    - A API deverá permitir consultar uma tarefa através do ID, alterar o
        status de uma tarefa e também excluir uma tarefa.

    - Nenhuma outra alteração deverá ser permitida além do status da tarefa.    
"""


from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
import json

app = Flask(__name__)

tasks = [
    {
        'id':'0',
        'responsavel':'Roberth',
        'tarefa': 'Criar API',
        'status':'Nao concluida'
    },
    {
        'id':'1',
        'responsavel':'Larissa',
        'tarefa':'Fazer bolo',
        'status':'Nao concluida'
    }
]


# Retorna todas as tarefas
@app.route('/task', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


# Retorna a tarefa com o id especifico
@app.route('/task/<string:task_id>', methods=['GET'])
def get_task(task_id):
    # Retorna a task, para task em tasks se task com tal id for igual ao id passado como argumento
    task = [task for task in tasks if task['id'] == task_id]

    # Retorna a task do id especifico, o index 0 é passado especificamente
    # por que a lista deve conter apenas o elemento do id especifico  
    return jsonify(task[0])


# Cria uma nova task, incluindo à na lista de taks existentes
@app.route('/task', methods=['POST'])
def task_create():

    # Elemento que será incluído na lista de tasks
    task = {
        'id': str(len(tasks)),
        'responsavel': request.json['responsavel'],
        'tarefa': request.json['tarefa'],
        'status': request.json['status']
    }

    # Adicionando a task na lista de tasks
    tasks.append(task)

    # retornando a task que foi criada e incluida
    return jsonify(task)

@app.route('/task/<string:task_id>', methods=['PUT'])
def task_update(task_id):
    # Retorna a task, para task em tasks se task com tal id for igual ao id passado como argumento
    task = [task for task in tasks if task['id'] == task_id]

    # Se status estiver na requisição json e na instancia, então faça, task na posicao 0
    # no campo status recebe a requisicao json em status
    if 'status' in request.json and isinstance(request.json['status'], str):
        task[0]['status'] = request.json['status']

    # retorna a task modificada
    return jsonify(task[0])

@app.route('/task/<string:task_id>', methods=['DELETE'])
def task_delete(task_id):
    # Retorna a task, para task em tasks se task com tal id for igual ao id passado como argumento
    task = [task for task in tasks if task['id'] == task_id]

    # Deleta a task encontrada pela variavel task que é correspondente ao ID de entrada
    tasks.remove(task[0])

    # Retorna mensagem dizendo que a task foi deletada com sucesso
    return jsonify({'message':'Task deletada com sucesso.'})


if __name__ == '__main__':
    app.run()