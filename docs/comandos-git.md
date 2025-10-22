### 1. **O que são branches e como trocar de branches?**
**Branches** são ramificações no repositório Git que permitem trabalhar em diferentes linhas de desenvolvimento paralelamente. Cada branch é uma cópia independente do código, geralmente usada para novas funcionalidades, correções de bugs ou experimentos.

- **Como criar um branch:**
  ```bash
  git branch nome-do-branch
  ```
- **Como trocar de branch:**
  ```bash
  git checkout nome-do-branch
  ```
  Ou, em versões mais recentes do Git, use:
  ```bash
  git switch nome-do-branch
  ```
- **Criar e trocar para um novo branch em um comando:**
  ```bash
  git checkout -b nome-do-branch
  ```
  Ou:
  ```bash
  git switch -c nome-do-branch
  ```

### 2. **Como fazer share push?**
Presumo que você quis dizer **"git push"** para compartilhar alterações com um repositório remoto.

- **Comando para enviar alterações do branch atual para o repositório remoto:**
  ```bash
  git push origin nome-do-branch
  ```
- **Se o branch ainda não existe no remoto:**
  O comando acima cria o branch no repositório remoto e envia os commits.
- **Forçar o push (cuidado, pode sobrescrever alterações):**
  ```bash
  git push --force
  ```
  Use com cautela, apenas quando souber que não vai causar conflitos ou perda de dados.

### 3. **Como reescrever um commit?**
Reescrever um commit significa alterar sua mensagem ou conteúdo. Isso pode ser feito com o comando `git commit --amend`.

- **Alterar a mensagem do último commit:**
  ```bash
  git commit --amend
  ```
  Isso abre o editor para modificar a mensagem do commit.

- **Alterar o conteúdo do último commit:**
  1. Faça as alterações nos arquivos.
  2. Adicione os arquivos alterados ao staging:
     ```bash
     git add .
     ```
  3. Execute:
     ```bash
     git commit --amend
     ```
     Isso substitui o último commit pelo novo, incluindo as alterações.

- **Reescrever commits mais antigos:**
  Use o comando `git rebase -i`:
  ```bash
  git rebase -i HEAD~n
  ```
  Substitua `n` pelo número de commits que deseja editar. Escolha `edit` no editor interativo, modifique os commits e siga as instruções.

**Aviso:** Não reescreva commits já enviados a um repositório remoto compartilhado, pois pode causar conflitos para outros colaboradores.

### 4. **Diferenças entre revert e merge?**
- **Revert:**
  - Cria um novo commit que desfaz as alterações de um commit específico, mantendo o histórico intacto.
  - Útil para reverter mudanças sem apagar o histórico.
  - Exemplo:
    ```bash
    git revert <hash-do-commit>
    ```
  - Não altera commits anteriores, apenas adiciona um commit que "cancela" as mudanças.

- **Merge:**
  - Combina as alterações de um branch com outro, criando um commit de merge (se houver conflitos, eles precisam ser resolvidos).
  - Preserva todas as alterações e o histórico de ambos os branches.
  - Exemplo:
    ```bash
    git merge nome-do-branch
    ```
  - Usado para integrar mudanças, como trazer funcionalidades de um branch de desenvolvimento para o branch principal.

**Diferença principal:** `revert` desfaz alterações específicas; `merge` combina alterações de branches diferentes.

### 5. **O que é stage (staging area)?**
A **staging area** (ou área de preparação) é um estado intermediário no Git onde você seleciona quais alterações nos arquivos serão incluídas no próximo commit. Ela funciona como um "rascunho" do commit.

- **Adicionar arquivos à staging area:**
  ```bash
  git add nome-do-arquivo
  ```
  Ou, para todos os arquivos alterados:
  ```bash
  git add .
  ```
- **Verificar o status da staging area:**
  ```bash
  git status
  ```
- **Propósito:** Permite organizar commits de forma lógica, escolhendo quais mudanças incluir e quais deixar para commits futuros.

### 6. **Para que serve squash de commit?**
**Squash** é o processo de combinar vários commits em um único commit, geralmente para simplificar o histórico do repositório.

- **Como fazer squash:**
  Use o comando `git rebase -i`:
  ```bash
  git rebase -i HEAD~n
  ```
  Substitua `n` pelo número de commits a serem combinados. No editor interativo, marque os commits que deseja combinar como `squash` (ou `s`) e mantenha o primeiro como `pick`. O Git combinará os commits em um só.

- **Propósito:**
  - Reduzir o número de commits no histórico, tornando-o mais limpo e legível.
  - Útil antes de enviar um pull request, para evitar poluição no histórico com commits pequenos ou irrelevantes.
  - Exemplo: Transformar 5 commits de "correção de bugs" em um único commit "Corrigido bug X".

**Aviso:** Assim como reescrever commits, evite squash em commits já enviados a repositórios compartilhados.

### 7. **Para que serve reflog?**
O **reflog** (reference log) é um registro interno do Git que rastreia todas as alterações feitas nas referências (como branches, HEAD, etc.) no repositório local, mesmo após operações como reset ou rebase.

- **Como acessar o reflog:**
  ```bash
  git reflog
  ```
  Isso mostra uma lista de ações com seus hashes, como commits, checkouts, resets, etc.

- **Propósito:**
  - Recuperar commits "perdidos" (por exemplo, após um `git reset`).
  - Ver o histórico de movimentações no repositório.
  - Exemplo de uso para recuperar um commit:
    1. Identifique o hash do commit desejado no reflog.
    2. Use:
       ```bash
       git checkout <hash-do-commit>
       ```
       Ou crie um novo branch a partir dele:
       ```bash
       git branch novo-branch <hash-do-commit>
       ```

- **Limitação:** O reflog é local e expira após um tempo (padrão: 90 dias).

### 8. **Diferenças entre reset e clean?**
- **Reset:**
  - Altera o histórico de commits ou o estado do repositório, movendo o HEAD para um commit anterior ou desfazendo alterações no working directory/staging area.
  - Tipos:
    - **`--soft`**: Mantém as alterações no working directory e staging area, mas move o HEAD.
    - **`--mixed`** (padrão): Move o HEAD e remove as alterações da staging area, mas mantém no working directory.
    - **`--hard`**: Move o HEAD e descarta todas as alterações no working directory e staging area.
    - Exemplo:
      ```bash
      git reset --hard HEAD~1
      ```
      Desfaz o último commit e todas as alterações.

- **Clean:**
  - Remove arquivos não rastreados (untracked) e diretórios do working directory que não estão no controle de versão.
  - Não afeta commits ou o histórico.
  - Exemplo:
    ```bash
    git clean -f
    ```
    Remove arquivos não rastreados. Use `-n` para visualizar antes de excluir.
  - Para remover também diretórios:
    ```bash
    git clean -fd
    ```

**Diferença principal:** `reset` manipula o histórico de commits e alterações rastreadas; `clean` lida com arquivos não rastreados no working directory.
