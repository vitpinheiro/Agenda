import time
import streamlit as st
import pandas as pd
from views import View



class LoginUI:
  def main():
    st.header("Faça seu login")
    LoginUI.inserir()


  def inserir():
    email = st.text_input("Informe o seu e-mail")
    senha = st.text_input("Informe a sua senha")
  
    if st.button("Login"):
      if View.Cliente_login(email, senha):
        st.success("Login realizado com sucesso")
      else:
        st.success("Usuário ou senha inválido(s)")
      time.sleep(2)

      st.rerun()