from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import markdown  # Converte markdown para HTML
from gemini_client import gerar_plano_estudos  # Função que usa IA Gemini

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Rota principal ("/"), aceita GET e POST
@app.route("/", methods=["GET", "POST"])
def index():
    plano = None  # Variável que armazenará o HTML do plano (se houver)

    if request.method == "POST":
        # Coleta os dados do formulário
        ensino = request.form.get("ensino")
        materias = request.form.get("materias")
        dias = request.form.get("dias")

        # Chama a IA para gerar um plano de estudos com base nos dados
        resposta_markdown = gerar_plano_estudos(ensino, materias, dias)

        # Converte a resposta em Markdown para HTML seguro
        plano = markdown.markdown(resposta_markdown, extensions=["extra"])

    # Renderiza a página e envia o plano para o template (se houver)
    return render_template("index.html", plano=plano)

# Executa o app Flask em modo debug
if __name__ == "__main__":
    app.run(debug=True)
