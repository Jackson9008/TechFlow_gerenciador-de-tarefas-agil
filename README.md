# Projeto de Engenharia de Software: Gerenciador de Tarefas TechFlow

Este repositório representa o projeto prático "Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade", desenvolvido para a disciplina de Engenharia de Software da UniFECAF. 

## 1. Objetivo e Escopo do Projeto 

**Contexto:** A TechFlow Solutions, uma empresa de software, foi contratada por uma startup de logística para desenvolver um sistema de gerenciamento de tarefas. O objetivo é criar uma ferramenta que permita à startup acompanhar seu fluxo de trabalho, priorizar tarefas essenciais e monitorar o desempenho da equipe em tempo real. 

**Escopo Inicial:**
* Implementar uma funcionalidade de CRUD (Create, Read, Update, Delete) para o gerenciamento de tarefas. 
* Permitir a criação de tarefas com um ID único, descrição e status.
* Permitir a visualização de todas as tarefas cadastradas.
* Permitir a atualização do status de uma tarefa existente (ex: de "A Fazer" para "Concluído").
* Permitir a exclusão de uma tarefa.

## 2. Metodologia Adotada 

A metodologia ágil escolhida para este projeto foi o **Kanban**. A escolha se justifica pela necessidade de flexibilidade e visualização clara do fluxo de trabalho, características essenciais para uma startup de logística com demandas dinâmicas.

Um quadro Kanban foi criado na aba "Projects" deste repositório, contendo as seguintes colunas:
* **A Fazer (To Do):** Tarefas planejadas que ainda não foram iniciadas.
* **Em Progresso (In Progress):** Tarefas que estão sendo desenvolvidas ativamente.
* **Concluído (Done):** Tarefas finalizadas e entregues.

## 3. Instruções para Execução do Sistema 

Para executar o sistema de gerenciamento de tarefas em seu ambiente local, siga os passos abaixo.

1.  **Pré-requisitos:**
    * Python 3.x instalado.
    * Git instalado.

2.  **Clonar o Repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/TechFlow_Task_Manager.git](https://github.com/seu-usuario/TechFlow_Task_Manager.git)
    cd TechFlow_Task_Manager
    ```

3.  **Executar a Aplicação:**
    ```bash
    python src/main.py
    ```
    O sistema será iniciado no terminal, apresentando um menu interativo para gerenciar as tarefas.

## 4. Simulação de Mudança no Escopo 

### Justificativa da Mudança 

Após uma reunião de feedback com o cliente (a startup de logística), foi identificada a necessidade de **adicionar um campo de prioridade** às tarefas. A equipe de logística precisa diferenciar rapidamente entregas urgentes de tarefas administrativas. A falta dessa funcionalidade estava impactando a capacidade de resposta a eventos críticos.

A mudança foi considerada de alto valor e baixo custo de implementação, alinhada aos princípios ágeis de adaptação a novos requisitos.

### Impacto no Kanban 
Para refletir essa mudança, as seguintes tarefas foram adicionadas ao quadro Kanban na coluna **"A Fazer"**:
* *Feature: Adicionar campo 'prioridade' à classe Tarefa.*
* *Feature: Atualizar função de criação para incluir prioridade.*
* *Feature: Exibir prioridade na listagem de tarefas.*
* *Test: Criar teste para validar a funcionalidade de prioridade.*
* *Docs: Atualizar README e diagramas UML com o novo campo.*
