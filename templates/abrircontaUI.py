import time
import streamlit as st
from views import View


class AbrirContaUI:
    def main():
      st.header("Abrir conta no sistema")
      AbrirContaUI.inserir()
        
    def inserir():
      nome = st.text_input("Informe o nome")
      email = st.text_input("Informe o e-mail")
      fone = st.text_input("Informe o fone")
      senha = st.text_input("Informe a senha")
      if st.button("Inserir"):
        View.cliente_inserir(nome, email, fone, senha)
        st.success("Conta criada com sucesso")
        time.sleep(2)
        st.rerun()