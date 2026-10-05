import streamlit as st

st.title("Transformador de texto")

texto = st.text_area("Escribe un texto:")
palabra_anterior = st.text_input("Palabra que quieres reemplazar:")
palabra_nueva = st.text_input("Palabra nueva:")

resultado = texto
mensaje = ""

columna1, columna2, columna3 = st.columns(3)
columna4, columna5, columna6 = st.columns(3)

if columna1.button("Quitar espacios extra"):
    resultado = texto.strip()
    while "  " in resultado:
        resultado = resultado.replace("  ", " ")
    mensaje = "Se eliminaron los espacios extra."

if columna2.button("Quitar espacios iniciales/finales"):
    resultado = texto.strip()
    mensaje = "Se quitaron los espacios del inicio y del final."

if columna3.button("Quitar todos los espacios"):
    resultado = texto.replace(" ", "")
    mensaje = "Se quitaron todos los espacios."

if columna4.button("Mayúsculas"):
    resultado = texto.upper()
    mensaje = "El texto se convirtió a mayúsculas."

if columna5.button("Minúsculas"):
    resultado = texto.lower()
    mensaje = "El texto se convirtió a minúsculas."

if columna6.button("Invertir el texto"):
    resultado = texto[::-1]
    mensaje = "El texto se invirtió."

st.subheader("Resultado")
st.text_area("Texto transformado:", resultado, height=180)

if mensaje != "":
    st.write(mensaje)

st.subheader("Cantidad")
if texto != "":
    cantidad_palabras = len(texto.split())
    cantidad_caracteres = len(texto)
    cantidad_lineas = len(texto.split("\n"))

    st.write("Palabras:", cantidad_palabras)
    st.write("Caracteres:", cantidad_caracteres)
    st.write("Líneas:", cantidad_lineas)
else:
    st.write("Escribe un texto para ver sus cantidades.")
