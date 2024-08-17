import streamlit as st
import random

def get_mensaje(sentimiento):
    """
    Esta función lee el archivo de texto correspondiente al sentimiento 
    y devuelve un mensaje aleatorio.
    """
    sentimiento = sentimiento.lower()  # Convertir a minúsculas para facilitar las comparaciones
    if sentimiento in ["triste", "mal", "mas o menos"]:
        archivo = "triste.txt"
    elif sentimiento in ["feliz", "alegre", "bien", "contenta"]:
        archivo = "feliz.txt"
    elif sentimiento in ["caliente", "hot"]:
        archivo = "caliente.txt"
    elif sentimiento in ["enojada", "molesta"]:
        archivo = "enojada.txt"
    elif sentimiento in ["tranquila", "normal"]:
        archivo = "tranquila.txt"
    elif sentimiento in ["romantica", "cursi"]:
        archivo = "romantica.txt"
    else:
        return "Lo siento, no tengo un mensaje para ese sentimiento. ¿Intentas con otro?"

    try:
        with open(archivo, 'r', encoding='utf-8') as archivo:
            cumplidos = archivo.read().splitlines()
            return random.choice(cumplidos)
    except FileNotFoundError:
        return "Lo siento, no tengo un mensaje para ese sentimiento. ¿Intentas con otro?"

# Título de la aplicación
st.title("Para mi princesa ♥")

# Campo de texto para ingresar el sentimiento
sentimiento = st.text_input("¿Cómo te sientes hoy?")

# Botón para generar el mensaje
if st.button("¡Dame un mensaje!"):
    if sentimiento:
        mensaje = get_mensaje(sentimiento)
        st.write(mensaje)
    else:
        st.write("Por favor, ingresa un sentimiento para que pueda animarte.")