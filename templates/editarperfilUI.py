import time
import streamlit as st
import pandas as pd
from views import View

class EditarPerfilUI:
    def main():
        st.header("Editar Perfil")
        EditarPerfilUI.editar()
        
    def editar():
       
        for clientes in View.cliente_listar():
            if clientes.get_id() == st.session_state["cliente_id"]:
              nome = st.text_input("Informe o novo nome", clientes.get_nome())
              email = st.text_input("Informe o novo e-mail", clientes.get_email())
              fone = st.text_input("Informe o novo fone", clientes.get_senha())
              senha = st.text_input("Informe a nova senha")
        if st.button("Atualizar"):
          id = clientes.get_id()
          View.cliente_atualizar(id, nome, email, fone, senha)
          st.success("Atualizado com sucesso")
          time.sleep(2)
          st.rerun()

          