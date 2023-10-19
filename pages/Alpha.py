from StreamLitHelper import StreamLitHelper as slhelp
import streamlit as st
from Widgets import Widgets as wg
import pandas as pd

# streamlit run LynxAlpha.py

st.header("Lynx - Alpha")
database_filepath = "C:\\Matthew IC Copy For Test\\Database\\LillyLynxDatabase_Alpha_231018.db"
table_name = 'RunInfo'
data = slhelp.load_data(slhelp, database_filepath=database_filepath, table_name=table_name)


home_tab, mix_tab, norm_tab = st.tabs(['Home', 'DNA Mixing', 'Normalization'])

with home_tab:
    wg.display_metrics_line(self=wg, data=data, method_name=None)
    wg.display_runs_by_day(self=wg, data=data, method_name=None)

with mix_tab:
    method_name = "Biologica_DNA_Miniprep_Mixing_V3,0(MJR)"
    wg.display_metrics_line(self=wg, data=data, method_name=method_name)
    wg.display_runs_by_day(self=wg, data=data, method_name=method_name)

with norm_tab:
    method_name = "Biologica_Normalization_V3,0(MJR)"
    wg.display_metrics_line(self=wg, data=data, method_name=method_name)
    wg.display_runs_by_day(self=wg, data=data, method_name=method_name)