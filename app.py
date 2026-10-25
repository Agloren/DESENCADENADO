import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página y Menú lateral (Tu ficha actual)
st.set_page_config(page_title="Entrenador Calistenia", page_icon="💪")
st.sidebar.title("Mi Ficha Actual")

semana = st.sidebar.number_input("Semana del Ciclo", min_value=1, max_value=11, value=1)
nivel_flexiones = st.sidebar.selectbox("Nivel Flexiones", [1, 2, 3, 4, 5])
nivel_sentadillas = st.sidebar.selectbox("Nivel Sentadillas", [1, 2, 3, 4, 5])
nivel_dominadas = st.sidebar.selectbox("Nivel Dominadas", [1, 2, 3, 4, 5])
nivel_verticales = st.sidebar.selectbox("Nivel Verticales", [1, 2, 3, 4, 5])
nivel_core = st.sidebar.selectbox("Nivel Core", [1, 2, 3, 4, 5])

# 2. Configurar la IA de Gemini con la clave de seguridad
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Instrucciones base (Tu Framework + Tus Niveles en tiempo real)
instrucciones = f"""
Actúa como mi entrenador personal experto en calistenia. Responde de forma clara y al grano.
MANUAL DEL ENTRENADOR:
[PEGA AQUÍ TODO TU LADRILLO/FRAMEWORK DE LAS 10 SEMANAS Y EJERCICIOS]

=========================================
DATOS ACTUALES DEL USUARIO:
- Semana Actual del ciclo: Semana {semana}
- Nivel Flexiones: {nivel_flexiones}
- Nivel Sentadillas: {nivel_sentadillas}
- Nivel Dominadas: {nivel_dominadas}
- Nivel Flexiones Verticales: {nivel_verticales}
- Nivel Core: {nivel_core}
"""

# 4. Configuración del modelo (versión gratuita activa)
modelo = genai.GenerativeModel(
    model_name="gemini-flash-lite-latest",
    system_instruction=instrucciones
)

# 5. Interfaz del Chat
st.title("💪 Entrenador IA - Método Desencadenado")

# Memoria del chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes anteriores en pantalla
for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.markdown(msg["texto"])

# Caja para escribir nuevas preguntas
pregunta = st.chat_input("Ej: ¿Qué me toca entrenar hoy?")

if pregunta:
    # Mostrar y guardar lo que pregunta el usuario
    st.session_state.mensajes.append({"rol": "user", "texto": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Generar y mostrar respuesta de la IA (con detector de errores visible)
    with st.chat_message("assistant"):
        try:
            respuesta = modelo.generate_content(pregunta)
            st.markdown(respuesta.text)
            st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta.text})
        except Exception as e:
            st.error(f"Detalle exacto de Google: {e}")
