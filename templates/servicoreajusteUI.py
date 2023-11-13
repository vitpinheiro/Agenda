import time
import streamlit as st
import pandas as pd
from views import View


class ServicoreajusteUI:
  def main():
    st.header("Reajuste dos valores")
    ServicoreajusteUI.listar()


  def listar():
    servicos = View.servico_listar()
    if len(servicos) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      dic = []
      for obj in servicos: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)
      percentual = st.text_input("Informe o percentual de reajuste")
      if st.button("Reajustar"):
        View.Servico_Reajustar(float(percentual))
        st.success("Reajuste realizado com sucesso")
        time.sleep(2)

        st.rerun()

