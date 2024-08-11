# Hello World RAG - Comparación de Chatbots

Este proyecto demuestra cómo implementar un chatbot básico utilizando RAG (Retrieval-Augmented Generation) en Streamlit. Compara un chatbot potenciado por RAG con un chatbot estándar, utilizando datos ficticios de un menú de restaurante.

## Estructura del Proyecto

- `app.py`: Código principal de la aplicación Streamlit.
- `menu.txt`: Archivo de texto que contiene el menú del restaurante.
- `requirements.txt`: Archivo con las dependencias de Python necesarias.

## Requisitos

- Python 3.7 o superior
- Cuenta de OpenAI con una clave API válida

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu-usuario/Hello_World_RAG.git
   cd Hello_World_RAG
   ```

2. **Crea un entorno virtual y actívalo**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura tu clave API de OpenAI**:
   
   - Abre el archivo `app.py`.
   - Sustituye `"tu-api-key-aqui"` por tu clave API de OpenAI.

5. **Ejecuta la aplicación**:

   ```bash
   streamlit run app.py
   ```

6. **Carga el archivo `menu.txt`** cuando se te solicite en la interfaz de la aplicación.

## Uso

Puedes hacer preguntas sobre el menú del restaurante en los dos chats. El chat con RAG utiliza la técnica de recuperación para mejorar las respuestas, mientras que el chat estándar responde sin utilizar los datos del menú.

## Ejemplos de Preguntas

- "¿Cuál es la especialidad del chef?"
- "¿Qué bebida recomiendan para acompañar el risotto?"
- "¿Qué postres ofrecen que no sean tan dulces?"

## Contribución

Si tienes sugerencias o mejoras, no dudes en hacer un fork del repositorio y enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.
