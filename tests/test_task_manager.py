# tests/test_task_manager.py

import unittest
from src.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    """Suite de testes para a classe TaskManager."""

    def setUp(self):
        """
        Configura um ambiente de teste limpo antes de cada teste.
        Este método é executado antes de cada 'test_*'.
        """
        self.manager = TaskManager()

    def test_add_task(self):
        """Testa se uma tarefa é adicionada corretamente."""
        task = self.manager.add_task("Testar funcionalidade de adição")
        self.assertEqual(len(self.manager.list_tasks()), 1)
        self.assertEqual(task.description, "Testar funcionalidade de adição")
        self.assertEqual(task.status, "A Fazer")

    def test_add_task_with_empty_description(self):
        """Testa se o sistema impede a criação de tarefas com descrição vazia."""
        with self.assertRaises(ValueError):
            self.manager.add_task("")

    def test_delete_task(self):
        """Testa a exclusão de uma tarefa."""
        task = self.manager.add_task("Tarefa para deletar")
        self.assertTrue(self.manager.delete_task(task.task_id))
        self.assertEqual(len(self.manager.list_tasks()), 0)

    def test_delete_non_existent_task(self):
        """Testa se a exclusão de uma tarefa inexistente falha graciosamente."""
        self.assertFalse(self.manager.delete_task(999))

    def test_update_task_status(self):
        """Testa a atualização do status de uma tarefa."""
        task = self.manager.add_task("Tarefa para atualizar")
        self.manager.update_task_status(task.task_id, "Concluído")
        updated_task = self.manager.get_task(task.task_id)
        self.assertEqual(updated_task.status, "Concluído")

if __name__ == '__main__':
    unittest.main()