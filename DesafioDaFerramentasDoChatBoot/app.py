import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Carrega o modelo NLLB da Meta
model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

translator = pipeline("translation", model=model, tokenizer=tokenizer, src_lang="por_Latn", tgt_lang="eng_Latn")

st.title("Tradutor de Português para Inglês com IA")
st.write("Digite uma frase em português para traduzi-la para o inglês.")

input_text = st.text_area("Texto em português", height=150)

if st.button("Traduzir"):
    if input_text.strip() == "":
        st.warning("Por favor, digite um texto para traduzir.")
    else:
        with st.spinner("Traduzindo..."):
            result = translator(input_text, max_length=100)
            translation = result[0]['translation_text']
            st.success("Tradução:")
            st.text(translation)
