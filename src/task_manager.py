# src/task_manager.py

from typing import Union, List

class Task:
    """
    Representa uma única tarefa no sistema.
    Cada tarefa tem um id, uma descrição e um status.
    """
    def __init__(self, task_id: int, description: str, status: str = "A Fazer"):
        self.task_id = task_id
        self.description = description
        self.status = status

    def __repr__(self):
        """Retorna uma representação textual da tarefa."""
        return f"ID: {self.task_id} | Descrição: {self.description} | Status: {self.status}"


# <-- ALTERAÇÃO AQUI: Duas linhas em branco separam as classes -->


class TaskManager:
    """
    Gerencia todas as operações de tarefas (CRUD).
    Mantém uma lista de tarefas e o controle do próximo ID disponível.
    """
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    # <-- ALTERAÇÃO AQUI: Uma linha em branco separa os métodos -->
    def add_task(self, description: str) -> Task:
        """
        Adiciona uma nova tarefa à lista.
        """
        if not description:
            raise ValueError("A descrição não pode ser vazia.")
            
        new_task = Task(self._next_id, description)
        self._tasks[self._next_id] = new_task
        self._next_id += 1
        return new_task

    def list_tasks(self) -> List[Task]:
        """Retorna uma lista de todas as tarefas cadastradas."""
        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Union[Task, None]:
        """
        Busca uma tarefa pelo seu ID.
        """
        return self._tasks.get(task_id)

    def update_task_status(self, task_id: int, new_status: str) -> bool:
        """
        Atualiza o status de uma tarefa existente.
        """
        task = self.get_task(task_id)
        if task:
            task.status = new_status
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Exclui uma tarefa do sistema.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False