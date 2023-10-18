from StreamLitHelper import StreamLitHelper as slhelp
import streamlit as st
from Widgets import Widgets as wg

# streamlit run LynxBravo.py

st.header("Lynx - Bravo")
tab1, tab2 = st.tabs(["DNA Mixing", "Normalization"])
database_filepath = "C:\\Matthew IC Copy For Test\\Database\\LillyLynxDatabase_231017.db"
table_name = 'RunInfo'
data = slhelp.load_data(slhelp, database_filepath=database_filepath, table_name=table_name)

with tab1:
    method_name = "Biologica_DNA_Miniprep_Mixing_V3,0(MJR)"
    wg.display_metrics_line(self=wg, data=data, method_name=method_name)
    wg.display_runs_by_day(self=wg, data=data, method_name=method_name)

with tab2:
    method_name = "Biologica_Normalization_V3,0(MJR)"
    wg.display_metrics_line(self=wg, data=data, method_name=method_name)
    wg.display_runs_by_day(self=wg, data=data, method_name=method_name)