# src/main.py

from task_manager import TaskManager

def print_menu():
    """Exibe o menu principal de opções para o usuário."""
    print("\n--- Gerenciador de Tarefas TechFlow ---")
    print("1. Adicionar Nova Tarefa")
    print("2. Listar Todas as Tarefas")
    print("3. Atualizar Status da Tarefa")
    print("4. Excluir Tarefa")
    print("5. Sair")
    print("---------------------------------------")

def main():
    """Função principal que executa o loop da aplicação."""
    manager = TaskManager()
    
    # Adicionando tarefas iniciais para demonstração
    manager.add_task("Planejar rota de entrega para o cliente A")
    manager.add_task("Realizar manutenção preventiva no veículo B")

    while True:
        print_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            description = input("Digite a descrição da nova tarefa: ")
            try:
                task = manager.add_task(description)
                print(f"Tarefa '{task.description}' adicionada com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif choice == '2':
            tasks = manager.list_tasks()
            if not tasks:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("\n--- Lista de Tarefas ---")
                for task in tasks:
                    print(task)

        elif choice == '3':
            try:
                task_id = int(input("Digite o ID da tarefa para atualizar: "))
                new_status = input("Digite o novo status (ex: Em Progresso, Concluído): ")
                if manager.update_task_status(task_id, new_status):
                    print("Status atualizado com sucesso!")
                else:
                    print("Erro: Tarefa com o ID informado não encontrada.")
            except ValueError:
                print("Erro: O ID da tarefa deve ser um número.")

        elif choice == '4':
            try:
                task_id = int(input("Digite o ID da tarefa para excluir: "))
                if manager.delete_task(task_id):
                    print("Tarefa excluída com sucesso!")
                else:
                    print("Erro: Tarefa com o ID informado não encontrada.")
            except ValueError:
                print("Erro: O ID da tarefa deve ser um número.")

        elif choice == '5':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()