from StreamLitHelper import StreamLitHelper as slhelp
import streamlit as st

# streamlit run LynxHome.py

st.header("Lynx Home")
database_filepath = "C:\\Matthew IC Copy For Test\\Database\\LillyLynxDatabase_231017.db"
table_name = 'RunInfo'
data = slhelp.load_data(slhelp, database_filepath=database_filepath, table_name=table_name)
# if st.checkbox('Show raw data'):
    #     st.subheader('Raw data')
    #     st.write(data)
    # st.divider()

# with tab1:
#     method_name = "Biologica_DNA_Miniprep_Mixing_V3,0(MJR)"
#     dna_mixing_prod_runs = slhelp.get_production_run_count(self=slhelp, data=data, target_column_name="methodname", target_value=method_name)
#     dna_mixing_success_runs = slhelp.get_successful_run_count(self=slhelp, data=data, target_column_name="methodname", target_value=method_name)
#     successful_rate = round(((dna_mixing_success_runs/dna_mixing_prod_runs) * 100))
#     col1, col2, col3 = st.columns(3)
#     col1.metric(label="Production Runs", value=dna_mixing_prod_runs, delta=None)
#     col2.metric(label="Successful Runs", value=dna_mixing_success_runs, delta=None)
#     col3.metric(label="Success Rate", value=str(successful_rate) + "%", delta=None)

#     st.divider()
#     st.subheader('Runs Per Day')
#     slhelp.days_per_week_hist(slhelp, data=data, method_name=method_name)

# with tab2:
#     method_name = "Biologica_Normalization_V3,0(MJR)"
#     dna_mixing_prod_runs = slhelp.get_production_run_count(self=slhelp, data=data, target_column_name="methodname", target_value=method_name)
#     dna_mixing_success_runs = slhelp.get_successful_run_count(self=slhelp, data=data, target_column_name="methodname", target_value=method_name)
#     successful_rate = round(((dna_mixing_success_runs/dna_mixing_prod_runs) * 100))
#     col1, col2, col3 = st.columns(3)
#     col1.metric(label="Production Runs", value=dna_mixing_prod_runs, delta=None)
#     col2.metric(label="Successful Runs", value=dna_mixing_success_runs, delta=None)
#     col3.metric(label="Success Rate", value=str(successful_rate) + "%", delta=None)

#     st.divider()
#     st.subheader('Runs Per Day')
#     slhelp.days_per_week_hist(slhelp, data=data, method_name=method_name)