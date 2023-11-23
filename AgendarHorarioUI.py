import streamlit as st
import pandas as pd
from views import View
import time

class AgendarHorarioUI:
  def main():
    st.header("Agendar horário semanal")
    AgendarHorarioUI.agendar()

  def agendar():
    horarios = View.agenda_listarsemana()
    if len(horarios) == 0:
      st.write("Nenhum horário disponível essa semana")
    else:  
      dic = []
      for obj in horarios:
        if not obj.get_id_cliente():
          dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)
      horario = st.selectbox("Escolha o horário", horarios)
      servico = st.selectbox("Escolha o serviço", View.servico_listar())
      if st.button("Agendar"):
          id = st.session_state["cliente_id"]
          View.agenda_cliente(id, horario, servico)
          st.success("Horário agendado com sucesso")
      
