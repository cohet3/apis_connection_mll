# Chatbot de Frases Célebres con OpenAI GPT

Este proyecto es un chatbot interactivo que utiliza el modelo `GPT-3.5-turbo` de OpenAI. El chatbot tiene la capacidad de responder a cualquier mensaje del usuario con frases célebres utilizando la API de OpenAI. Cada interacción es gestionada utilizando el endpoint de chat de OpenAI para obtener respuestas dinámicas y naturales.

## Funcionalidades

- **Interacción basada en chat**: El usuario puede interactuar con el chatbot escribiendo cualquier mensaje, y el chatbot responde con una frase célebre.
- **Modelo GPT-3.5-turbo**: El chatbot utiliza el modelo de chat `gpt-3.5-turbo` para generar respuestas naturales y contextuales.
- **Frases célebres**: Las respuestas generadas están diseñadas para incluir siempre una frase célebre en el contenido.

## Estructura del proyecto

- **functions.py**: Contiene la función principal `obtener_respuesta_gpt()` que interactúa con la API de OpenAI para obtener respuestas del modelo GPT.
- **main.ipynb** o **main.py**: Script interactivo que permite al usuario enviar mensajes al chatbot y obtener respuestas, utilizando las funciones definidas en `functions.py`.

## Requisitos

- Python 3.x
- [OpenAI Python Client](https://pypi.org/project/openai/)
- Clave API de OpenAI

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu-usuario/chatbot-frases-celebres.git](https://github.com/cohet3/apis_connection_mll.git
2. Navega al directorio del proyecto:
   ```bash
   cd apis_connection_mll

3. Instala las dependencias requeridas:
   ```bash
   pip install openai
4. Introduce tu APIkey:
   ```bash
   openai.api_key = 'tu_clave_api'

## Uso
1. Ejecuta el script interactivo:
    ```bash
    python main.py
2. El chatbot te dará la bienvenida y podrás interactuar con él escribiendo cualquier mensaje.

3. Para finalizar la conversación, puedes escribir salir.

Ejemplo de Interacción
Usuario: ¿Qué es el éxito?

Chatbot: El éxito es aprender de cada paso y crecer a partir de los fracasos.

Frase célebre: "El éxito es aprender a ir de fracaso en fracaso sin desesperarse. – Winston Churchill"

## Personalización
Puedes personalizar las respuestas del chatbot modificando la función obtener_respuesta_gpt() en el archivo functions.py. Cambia el contexto del chatbot o agrega más frases célebres a las respuestas.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas agregar nuevas funcionalidades o mejorar el chatbot, siéntete libre de hacer un pull request.
