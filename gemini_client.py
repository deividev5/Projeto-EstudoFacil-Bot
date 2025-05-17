import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega a chave da API a partir do .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configura a API Gemini com a chave
genai.configure(api_key=GEMINI_API_KEY)

# Instancia o modelo de IA (versão rápida)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Função que cria o prompt e obtém a resposta do modelo IA
def gerar_plano_estudos(tipo_ensino, materias, dias):
    prompt = f"""
Você é uma IA chamada EstudoFácil Bot 😄  
Ajude um estudante que está cursando **{tipo_ensino}** a organizar seus estudos nas matérias: {materias}.  

📅 O plano deve durar **{dias} dias**.  

- Divida o conteúdo por **dias**, com título grande: `📆 Dia X`.  
- Deixe **espaço entre os blocos e frases** (use linhas em branco e `  `).  
- Em cada dia, liste os blocos de estudo usando Pomodoro (25min estudo / 5min pausa).  
- Após os blocos, adicione uma **dica motivacional** para o dia, separada.  
- Use **formatação Markdown**: títulos, listas com marcadores, **negrito**, emojis.  
- Comece com uma saudação calorosa e feliz. Diga ao aluno que você está aqui para ajudar!  
"""

    # Gera o conteúdo com base no prompt acima
    response = model.generate_content(prompt)
    return response.text  # Retorna o markdown gerado
