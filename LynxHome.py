from StreamLitHelper import StreamLitHelper as slhelp
import streamlit as st
import pandas as pd
from Widgets import Widgets as wg

# streamlit run LynxHome.py

st.header("Lynx Home")
database_filepath_alpha = "C:\\Matthew IC Copy For Test\\Database\\LillyLynxDatabase_Alpha_231018.db"
database_filepath_bravo = "C:\\Matthew IC Copy For Test\\Database\\LillyLynxDatabase_231017.db"
table_name = 'RunInfo'
data_alpha = slhelp.load_data(slhelp, database_filepath=database_filepath_alpha, table_name=table_name)
data_bravo = slhelp.load_data(slhelp, database_filepath=database_filepath_bravo, table_name=table_name)
combined_data = pd.concat([data_alpha, data_bravo], axis=0)

home_tab, mix_tab, norm_tab = st.tabs(['Home', 'DNA Mixing', 'Normalization'])

with home_tab:
    wg.display_metrics_line(self=wg, data=combined_data, method_name=None)
    wg.display_runs_by_day(self=wg, data=combined_data, method_name=None)

with mix_tab:
    method_name = "Biologica_DNA_Miniprep_Mixing_V3,0(MJR)"
    wg.display_metrics_line(self=wg, data=combined_data, method_name=method_name)
    wg.display_runs_by_day(self=wg, data=combined_data, method_name=method_name)

with norm_tab:
    method_name = "Biologica_Normalization_V3,0(MJR)"
    wg.display_metrics_line(self=wg, data=combined_data, method_name=method_name)
    wg.display_runs_by_day(self=wg, data=combined_data, method_name=method_name)
