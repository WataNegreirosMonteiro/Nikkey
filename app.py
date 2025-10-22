from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session


BASE_DIR = Path(__file__).parent.resolve()
PAGINAS_DIR = BASE_DIR / "paginas"
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"
USERS_JSON = DATA_DIR / "usuarios.json"
ELEMENTS_JSON = DATA_DIR / "elementos.json"


def create_app() -> Flask:
    app = Flask(__name__, template_folder=str(PAGINAS_DIR))
    app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

    # -------------- Utilidades de persistência --------------
    DATA_DIR.mkdir(exist_ok=True)

    def load_users():
        if not USERS_JSON.exists():
            return []
        try:
            with USERS_JSON.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def save_user(user: dict):
        users = load_users()
        users.append(user)
        with USERS_JSON.open("w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

    def find_user(email: str, senha: str):
        email_l = (email or "").strip().lower()
        senha_s = (senha or "").strip()
        for u in load_users():
            if (u.get("email", "").lower() == email_l) and (u.get("senha", "") == senha_s):
                return u
        return None

    # Elementos japoneses (carregado de JSON; cria padrão se ausente)
    DEFAULT_ELEMENTS = [
        {
            "titulo": "Origami Tsuru",
            "subtitulo": "Tsuru de Origami",
            "descricao": "Você representa paciência, esperança e realização de desejos. Como mil tsurus, você traz sonhos realizados.",
            "icone": "paper-airplane"
        },
        {
            "titulo": "Sakura",
            "subtitulo": "Flor de Cerejeira",
            "descricao": "Beleza efêmera e renovação. Você inspira novos começos e aprecia o momento presente.",
            "icone": "flower"
        },
        {
            "titulo": "Samurai",
            "subtitulo": "Caminho do Bushidô",
            "descricao": "Honra, coragem e disciplina. Você enfrenta desafios com determinação e propósito.",
            "icone": "shield-check"
        },
        {
            "titulo": "Torii",
            "subtitulo": "Portal Sagrado",
            "descricao": "Transição e espiritualidade. Você busca significado e abre caminhos para o sagrado em sua vida.",
            "icone": "gate"
        },
        {
            "titulo": "Carpa Koi",
            "subtitulo": "Força e Perseverança",
            "descricao": "Resiliência e sorte. Você segue contra a corrente e transforma obstáculos em crescimento.",
            "icone": "fish"
        },
        {
            "titulo": "Bonsai",
            "subtitulo": "Arte da Paciência",
            "descricao": "Cuidado e equilíbrio. Você cultiva o potencial, respeitando o tempo e a natureza.",
            "icone": "tree"
        },
        {
            "titulo": "Sushi",
            "subtitulo": "Harmonia de Sabores",
            "descricao": "Criatividade e precisão. Você combina simplicidade e elegância para criar experiências memoráveis.",
            "icone": "sparkles"
        },
        {
            "titulo": "Taiko",
            "subtitulo": "Tambor Japonês",
            "descricao": "Energia e ritmo. Você contagia as pessoas ao seu redor com força e entusiasmo.",
            "icone": "drum"
        }
    ]

    def ensure_elements_file():
        if not ELEMENTS_JSON.exists():
            with ELEMENTS_JSON.open("w", encoding="utf-8") as f:
                json.dump(DEFAULT_ELEMENTS, f, ensure_ascii=False, indent=2)

    def load_elements():
        ensure_elements_file()
        with ELEMENTS_JSON.open("r", encoding="utf-8") as f:
            return json.load(f)

    # -------------- Rotas de páginas --------------
    @app.route("/")
    def inicio():
        return render_template("inicio.html")

    @app.route("/entrar", methods=["GET", "POST"]) 
    @app.route("/entrada", methods=["GET", "POST"]) 
    @app.route("/elemento", methods=["GET", "POST"]) 
    def entrada():
        erro = None
        if request.method == "POST":
            email = request.form.get("email")
            senha = request.form.get("senha")
            user = find_user(email, senha)
            if user:
                session["user"] = {k: user[k] for k in ("nome", "email") if k in user}
                return redirect(url_for("entrada"))
            else:
                erro = "E-mail ou senha inválidos."
        usuario = session.get("user")
        return render_template("entrada.html", usuario=usuario, erro=erro)

    @app.route("/cadastro", methods=["GET", "POST"])
    def cadastro():
        if request.method == "POST":
            nome = (request.form.get("nome") or "").strip()
            email = (request.form.get("email") or "").strip().lower()
            senha = (request.form.get("senha") or "").strip()

            if nome and email and senha:
                save_user({
                    "nome": nome,
                    "email": email,
                    "senha": senha,
                    "created_at": datetime.utcnow().isoformat() + "Z",
                })
                return redirect(url_for("entrada"))
        return render_template("cadastro.html")

    @app.route("/cartao")
    def cartao():
        import random
        if not session.get("user"):
            return redirect(url_for("entrada"))
        nome = (request.args.get("nome") or session.get("user", {}).get("nome") or "").strip()
        elementos = load_elements()
        try:
            idx = int(request.args.get("e"))
        except Exception:
            idx = None
        if idx is None or idx < 0 or idx >= len(elementos):
            idx = random.randrange(len(elementos))
            return redirect(url_for("cartao", nome=nome, e=idx))
        elemento = elementos[idx]
        return render_template("cartao.html", nome=nome, elemento=elemento, idx=idx)

    @app.route("/sair")
    def sair():
        session.clear()
        return redirect(url_for("entrada"))

   
    @app.route("/assets/<path:filename>")
    def assets(filename):
        return send_from_directory(ASSETS_DIR, filename)

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
