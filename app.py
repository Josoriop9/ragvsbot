import streamlit as st
import openai
from annoy import AnnoyIndex
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde .env
load_dotenv()

# Configuración de la API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para cargar y procesar el archivo de menú
def load_menu(uploaded_file):
    menu_items = []
    if uploaded_file is not None:
        lines = uploaded_file.read().decode("utf-8").splitlines()
        for line in lines:
            category, item = line.split(": ")
            menu_items.append(f"{item} ({category})")
    return menu_items


# Interfaz en Streamlit
st.title("Comparación RAG vs Chatbot Estándar")

# Subir el archivo de menú
uploaded_file = st.file_uploader("Sube un archivo de texto con el menú", type="txt")

# Cargar los datos del menú
documents = load_menu(uploaded_file)

if documents:
    # Crear vectorizador TF-IDF y construir el índice Annoy
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(documents)
    f = X.shape[1]
    index = AnnoyIndex(f, 'angular')

    for i in range(X.shape[0]):
        index.add_item(i, X[i].toarray()[0])

    index.build(10)

    def retrieve(query):
        query_vec = vectorizer.transform([query]).toarray()[0]
        nearest = index.get_nns_by_vector(query_vec, 1)
        return documents[nearest[0]]

    def generate_text_rag(prompt):
        retrieved_doc = retrieve(prompt)
        combined_input = f"{retrieved_doc}\n\n{prompt}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": combined_input}
            ]
        )
        return response['choices'][0]['message']['content'].strip()

    def generate_text_standard(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()

    col1, col2 = st.columns(2)

    with col1:
        st.header("Chat con RAG")
        query_rag = st.text_input("Pregunta al Chat con RAG", key="rag")
        if query_rag:
            response_rag = generate_text_rag(query_rag)
            st.write(response_rag)

    with col2:
        st.header("Chat Estándar")
        query_standard = st.text_input("Pregunta al Chat Estándar", key="standard")
        if query_standard:
            response_standard = generate_text_standard(query_standard)
            st.write(response_standard)
else:
    st.write("Por favor, sube un archivo de texto para continuar.")
