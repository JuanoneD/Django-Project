# Documentação do Sistema de Gerenciamento de Tarefas

Este projeto é um sistema para organizar e atribuir tarefas entre diferentes usuários.

## Funcionalidades Principais

### 1. Login e Cadastro
- Ao acessar o site, o usuário é direcionado para a tela de login.
- Caso o usuário já tenha uma conta, basta inserir suas credenciais para entrar.
- Se ainda não tiver uma conta, pode clicar em **"Criar Conta"**, onde um modal será aberto pedindo informações para o cadastro. Após isso, o usuário pode acessar o sistema.

### 2. Área de Tarefas
- Na área principal, o usuário verá suas tarefas cadastradas em forma de cards.
- Há dois botões principais:
  - **Cadastrar Tarefa**: Abre um modal para inserir o título e a descrição da tarefa. O usuário também pode atribuir a tarefa a outro usuário, inserindo o e-mail no campo indicado.
  - **Sair da Conta**: Para deslogar do sistema.

### 3. Gerenciamento de Tarefas
- As tarefas cadastradas pelo usuário podem ser editadas ou excluídas.
- Se uma tarefa for atribuída a outro usuário, ela aparecerá na tela desse usuário, mas ele não terá permissão para excluí-la.

### 4. Filtros
- Na visualização de tarefas, há filtros que permitem o usuário organizar suas tarefas por status:
  - **Pendentes**
  - **Em Desenvolvimento**
  - **Concluídas**

## Informações Adicionais

- **Login de Admin do Django**:
  - Usuário: `admin`
  - Senha: `admin`
