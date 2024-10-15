import openai
import random
import os

# Configura tu clave API
openai.api_key = os.getenv('OPENAI_API_KEY')

# Lista de frases célebres
FRASES_CELEBRES = [
    "La vida es lo que te pasa mientras estás ocupado haciendo otros planes. – John Lennon",
    "El éxito es aprender a ir de fracaso en fracaso sin desesperarse. – Winston Churchill",
    "Lo que no te mata te hace más fuerte. – Friedrich Nietzsche",
    "En medio de la dificultad reside la oportunidad. – Albert Einstein",
    "La felicidad no es hacer lo que uno quiere, sino querer lo que uno hace. – Jean Paul Sartre",
    "El único modo de hacer un gran trabajo es amar lo que haces. – Steve Jobs",
    "El conocimiento es poder. – Francis Bacon"
]

def obtener_frase_aleatoria():
    """
    Selecciona una frase célebre al azar de la lista.
    """
    return random.choice(FRASES_CELEBRES)

def obtener_respuesta_gpt(mensaje_usuario):
    """
    Esta función interactúa con la API de OpenAI para obtener una respuesta del modelo GPT-3.5-turbo
    utilizando el endpoint correcto de chat (v1/chat/completions).
    """
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # O "gpt-4" si tienes acceso
        messages=[
            {"role": "system", "content": "Eres un chatbot que responde siempre con frases célebres."},
            {"role": "user", "content": mensaje_usuario}
        ],
        max_tokens=100,
        temperature=0.7
    )

    # Obtener el texto de la respuesta
    texto_respuesta = respuesta['choices'][0]['message']['content']
    return texto_respuesta
