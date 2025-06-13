import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCzlx3Pn72I-0JK9MJjakRacThXgpr48F8")

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

st.title("🍲 Gerador de Receitas com IA")

# 1. Ingredientes principais
ingredientes = st.text_area("Digite os ingredientes principais (separados por vírgula):", placeholder="ex: frango, tomate, cebola, arroz")

# 2. Tipo de culinária
tipo_culinaria = st.selectbox("Escolha o tipo de culinária:", ["Qualquer uma", "Italiana", "Brasileira", "Asiática", "Mexicana"])

# 3. Nível de dificuldade
nivel_dificuldade = st.slider("Nível de dificuldade:", 1, 5, 3)

# 4. Restrição alimentar
possui_restricao = st.checkbox("Possui Restrição Alimentar?")
restricao = ""
if possui_restricao:
    restricao = st.text_input("Digite a restrição alimentar:", placeholder="ex: sem glúten, vegetariana, sem lactose")

# 5. Botão para gerar receita
if st.button("🍴 Sugerir Receita"):
    if not ingredientes.strip():
        st.warning("Por favor, insira pelo menos um ingrediente.")
    else:
        # 6. Construindo o prompt
        restricao_str = f"Considere também a seguinte restrição alimentar: {restricao}." if possui_restricao and restricao else ""
        prompt = (
            f"Sugira uma receita do tipo {tipo_culinaria.lower()} com nível de dificuldade {nivel_dificuldade} "
            f"(sendo 1 muito fácil e 5 desafiador). Deve usar principalmente os seguintes ingredientes: {ingredientes}. "
            f"{restricao_str} Apresente o nome da receita, uma lista de ingredientes adicionais se necessário, "
            f"e um breve passo a passo do preparo."
        )

        # 7. Enviando para o Gemini
        try:
            response = model.generate_content(prompt)
            st.subheader("🍽️ Receita Sugerida:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Ocorreu um erro ao gerar a receita: {e}")
