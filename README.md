<img width="1643" height="1854" alt="image" src="https://github.com/user-attachments/assets/875449d9-9d43-4a8f-b74c-0ffb9e175859" />

<video src="./video.mp4" controls></video>

# Nikkey — Descubra seu Elemento Japonês (Flask)

Aplicação web em Flask que:

- Cadastra usuários e salva em JSON.
- Faz login usando sessão de usuário.
- Gera um “cartão” com um elemento da cultura japonesa escolhido aleatoriamente a cada tentativa (dados em JSON).
- Cria uma URL estável para compartilhar o resultado (parâmetro `e` fixa o índice do elemento sorteado).
- Interface com Tailwind CSS via CDN.

Este projeto foi criado como exercício de Programação Web III e serve como base para explorar rotas Flask, templates Jinja, sessões e persistência em arquivos.

## Stack Técnica

- Backend: Python 3.10+ com Flask 3.x
- Templates: HTML + Jinja2 (pasta `paginas/`)
- Estilos: Tailwind CSS (CDN)
- Persistência: JSON em `data/usuarios.json` e `data/elementos.json`
- Sessão: cookie de sessão Flask (`SECRET_KEY`)
- Assets estáticos: `assets/` (servidos pela rota `/assets/<arquivo>`)

## Estrutura do Projeto

```
.
├─ app.py                   # App Flask e rotas
├─ requirements.txt         # Dependências
├─ paginas/                 # Templates (Jinja)
│  ├─ inicio.html
│  ├─ entrada.html          # Página de login e, se logado, área para gerar cartão
│  ├─ cadastro.html         # Formulário de cadastro (POST → /cadastro)
│  └─ cartao.html           # Cartão com elemento sorteado (usa Jinja)
├─ data/
│  ├─ usuarios.json         # Usuários cadastrados (criado automaticamente)
│  └─ elementos.json        # Base de elementos japoneses
├─ assets/                  # Imagens, vídeos etc. (ex.: logo)
└─ README.md
```

## Rotas

- `GET /` → Página inicial (`paginas/inicio.html`).
- `GET|POST /entrar`, `/entrada`, `/elemento` →
  - GET: mostra `entrada.html`.
  - POST: valida login (email+senha) em `data/usuarios.json` e inicia sessão.
- `GET|POST /cadastro` →
  - GET: mostra formulário de cadastro.
  - POST: salva `{nome, email, senha, created_at}` em `data/usuarios.json` e redireciona para `/entrar`.
- `GET /cartao` → Requer sessão. Sorteia elemento de `elementos.json` e renderiza `cartao.html` com:
  - `nome`: lido de `?nome=` (se presente) ou do usuário logado.
  - `elemento`: objeto com `titulo`, `subtitulo`, `descricao`, `icone`.
  - Se `?e=` não existir ou for inválido, o backend sorteia um índice e redireciona para `/cartao?nome=...&e=IDX` para a URL ficar compartilhável.
- `GET /sair` → Encerra a sessão e redireciona para `/entrar`.
- `GET /assets/<path>` → Serve arquivos da pasta `assets/`.

## Elementos Japoneses (dinâmicos)

- Os dados ficam em `data/elementos.json`. Caso o arquivo não exista, o backend cria um padrão.
- Cada item tem: `titulo`, `subtitulo`, `descricao`, `icone`.
- O `icone` é mapeado para um emoji no `paginas/cartao.html` (via Jinja):
  - `paper-airplane` → 🕊️ (Tsuru)
  - `flower` → 🌸 (Sakura)
  - `shield-check` → 🛡️ (Samurai)
  - `gate` → ⛩️ (Torii)
  - `fish` → 🐟 (Koi)
  - `tree` → 🪴 (Bonsai)
  - `sparkles` → 🍣 (Sushi)
  - `drum` → 🥁 (Taiko)
  - Qualquer outro → 🎌

Você pode editar `elementos.json` para adicionar/alterar elementos (apenas mantenha as chaves). Se adicionar novos valores em `icone`, inclua o mapeamento no template do cartão, se quiser um emoji específico.

## Compartilhamento de Resultado

- `paginas/cartao.html` usa a Web Share API se disponível; caso contrário, copia o link da página para a área de transferência.
- O link é estável por conter o parâmetro `e` (índice do elemento). Assim, quem receber o link verá o mesmo cartão.

## Segurança (importante)

- Este projeto armazena a senha em texto plano no JSON para simplicidade educacional. Em produção, utilize hashing seguro (por exemplo, `werkzeug.security.generate_password_hash`) e um banco de dados adequado.
- Defina `SECRET_KEY` para uma chave forte em produção.

## Como criar e ativar um ambiente virtual (venv)

Pré‑requisito: Python 3.10+ instalado.

Windows (PowerShell):

```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux (bash/zsh):

```
python3 -m venv .venv
source .venv/bin/activate
```

Para sair do venv:

```
deactivate
```

## Como rodar o projeto

1) Ative o venv (ver seção acima).

2) Instale dependências:

```
pip install -r requirements.txt
```

3) (Opcional) Configure variáveis de ambiente:

```
# Windows (PowerShell)
$env:SECRET_KEY = "uma-chave-secreta-segura"

# macOS/Linux
export SECRET_KEY="uma-chave-secreta-segura"
```

4) Inicie o servidor de desenvolvimento:

```
python app.py
```

Abra em: `http://localhost:5000/`

## Fluxo de Uso

- Acesse `/cadastro` e crie sua conta.
- Vá para `/entrar` e faça login.
- Em `/entrar` (logado), informe um nome (opcional) e clique em “Gerar cartão aleatório”.
  - Se o nome não for informado, o backend usa o nome do usuário logado.
- Em `/cartao`, compartilhe o link (já com `?e=` fixando o elemento).

## Formatos dos JSONs

Exemplo `data/usuarios.json`:

```json
[
  {
    "nome": "Fulana",
    "email": "fulana@example.com",
    "senha": "123456",
    "created_at": "2025-01-01T12:00:00Z"
  }
]
```

Exemplo `data/elementos.json` (um item):

```json
{
  "titulo": "Origami Tsuru",
  "subtitulo": "Tsuru de Origami",
  "descricao": "Você representa paciência, esperança e realização de desejos...",
  "icone": "paper-airplane"
}
```

## Dicas de Desenvolvimento

- Templates ficam em `paginas/` e podem usar Jinja normalmente (`{{ ... }}`, `{% ... %}`).
- Para alterar o visual, edite os HTMLs; Tailwind entra por CDN.
- Para adicionar novos elementos, edite `data/elementos.json`.
- Para depurar, rode `python app.py` com `debug=True` (padrão no arquivo).

## Problemas comuns

- Porta ocupada: altere a porta em `PORT` (env) ou no `app.run`.
- Erros de acentuação: garanta que os arquivos estejam em UTF‑8.
- JSON corrompido: valide o conteúdo (vírgulas e aspas). Em último caso, apague o arquivo para o app recriar (no caso de `elementos.json`).



