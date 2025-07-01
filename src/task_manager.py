# src/task_manager.py

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


class TaskManager:
    """
    Gerencia todas as operações de tarefas (CRUD).
    Mantém uma lista de tarefas e o controle do próximo ID disponível.
    """
    def __init__(self):
        self._tasks = {}  # Usando um dicionário para acesso rápido por ID.
        self._next_id = 1

    def add_task(self, description: str) -> Task:
        """
        Adiciona uma nova tarefa à lista.

        Args:
            description (str): A descrição da tarefa.

        Returns:
            Task: O objeto da tarefa criada.
        """
        if not description:
            raise ValueError("A descrição não pode ser vazia.")
            
        new_task = Task(self._next_id, description)
        self._tasks[self._next_id] = new_task
        self._next_id += 1
        return new_task

    def list_tasks(self) -> list:
        """Retorna uma lista de todas as tarefas cadastradas."""
        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Task | None:
        """
        Busca uma tarefa pelo seu ID.

        Args:
            task_id (int): O ID da tarefa a ser buscada.

        Returns:
            Task or None: O objeto da tarefa, se encontrado, senão None.
        """
        return self._tasks.get(task_id)

    def update_task_status(self, task_id: int, new_status: str) -> bool:
        """
        Atualiza o status de uma tarefa existente.

        Args:
            task_id (int): O ID da tarefa a ser atualizada.
            new_status (str): O novo status da tarefa.

        Returns:
            bool: True se a atualização foi bem-sucedida, False caso contrário.
        """
        task = self.get_task(task_id)
        if task:
            task.status = new_status
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Exclui uma tarefa do sistema.

        Args:
            task_id (int): O ID da tarefa a ser excluída.

        Returns:
            bool: True se a exclusão foi bem-sucedida, False caso contrário.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False