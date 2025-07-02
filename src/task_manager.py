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
        """Retorna uma representação textual amigável da tarefa."""
        return f"ID: {self.task_id} | Descrição: {self.description} | Status: {self.status}"



class TaskManager:
    """
    Gerencia todas as operações de tarefas (CRUD).
    
    Esta classe é o coração do sistema, responsável por adicionar,
    listar, atualizar e deletar tarefas, garantindo a integridade dos dados.
    """
    def __init__(self):
        # Usando um dicionário para acesso rápido por ID. O(1) em vez de O(n) de uma lista.
        self._tasks = {}
        # Garante que cada tarefa terá um ID único que nunca se repete.
        self._next_id = 1

    def add_task(self, description: str) -> Task:
        """
        Cria e adiciona uma nova tarefa ao sistema.

        Args:
            description (str): A descrição textual da tarefa.

        Returns:
            Task: O objeto da tarefa que foi criada.
        
        Raises:
            ValueError: Se a descrição estiver vazia.
        """
        if not description:
            raise ValueError("A descrição não pode ser vazia.")
            
        new_task = Task(self._next_id, description)
        self._tasks[self._next_id] = new_task
        self._next_id += 1
        return new_task

    def list_tasks(self) -> List[Task]:
        """Retorna uma lista com todas as tarefas cadastradas."""
        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Union[Task, None]:
        """
        Busca uma tarefa específica pelo seu ID.

        Args:
            task_id (int): O ID da tarefa a ser encontrada.

        Returns:
            Union[Task, None]: O objeto da tarefa se encontrada, senão None.
        """
        return self._tasks.get(task_id)

    def update_task_status(self, task_id: int, new_status: str) -> bool:
        """
        Atualiza o status de uma tarefa existente.

        Args:
            task_id (int): O ID da tarefa a ser atualizada.
            new_status (str): O novo status para a tarefa.

        Returns:
            bool: True se a tarefa foi encontrada e atualizada, False caso contrário.
        """
        task = self.get_task(task_id)
        if task:
            task.status = new_status
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Exclui uma tarefa do sistema com base no seu ID.

        Args:
            task_id (int): O ID da tarefa a ser deletada.

        Returns:
            bool: True se a tarefa foi encontrada e deletada, False caso contrário.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False