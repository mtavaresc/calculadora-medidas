import streamlit as st


st.title("Calculadora de Medidas")

st.write("Defina o valores abaixo:")
price = st.number_input("Preço do m²", .0, 1000.)
width = st.slider("Defina a Largura (em cm)", 50, 110, 80)
height = st.slider("Defina a Altura (em cm)", 50, 250, 190)

if st.button("Calcular"):
    cm2m = (width / 100) * (height / 100)
    result = cm2m * price
    st.write("")
    st.text(f"Valor Final: R$ {result:.2f}")
