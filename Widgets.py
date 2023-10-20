import streamlit as st
from StreamLitHelper import StreamLitHelper as sthelp

class Widgets:

    def display_metrics_line(self, data, method_name):
        if method_name is None:
            dna_mixing_prod_runs = sthelp.get_production_run_count(self=sthelp, data=data, target_column_name=None, target_value=None)
            dna_mixing_success_runs = sthelp.get_successful_run_count(self=sthelp, data=data, target_column_name=None, target_value=None)
            successful_rate = round(((dna_mixing_success_runs/dna_mixing_prod_runs) * 100))

            st.markdown(":orange[Data span:] " + str(sthelp.get_first_prod_date(self=sthelp, data=data)) + " - " + str(sthelp.get_last_prod_date(self=sthelp, data=data)))

            col1, col2, col3 = st.columns(3)
            col1.metric(label=":green[Production Runs]", value=dna_mixing_prod_runs, delta=None)
            col2.metric(label=":green[Successful Runs]", value=dna_mixing_success_runs, delta=None)
            col3.metric(label=":green[Success Rate]", value=str(successful_rate) + "%", delta=None)
        else:
            dna_mixing_prod_runs = sthelp.get_production_run_count(self=sthelp, data=data, target_column_name="methodname", target_value=method_name)
            dna_mixing_success_runs = sthelp.get_successful_run_count(self=sthelp, data=data, target_column_name="methodname", target_value=method_name)
            successful_rate = round(((dna_mixing_success_runs/dna_mixing_prod_runs) * 100))

            st.markdown(":orange[Data span:] " + str(sthelp.get_first_prod_date(self=sthelp, data=data)) + " - " + str(sthelp.get_last_prod_date(self=sthelp, data=data)))

            col1, col2, col3 = st.columns(3)
            col1.metric(label=":green[Production Runs]", value=dna_mixing_prod_runs, delta=None)
            col2.metric(label=":green[Successful Runs]", value=dna_mixing_success_runs, delta=None)
            col3.metric(label=":green[Success Rate]", value=str(successful_rate) + "%", delta=None)

    def display_runs_by_day(self, data, method_name):
        st.divider()
        st.subheader('Runs By Day')
        if method_name is None:
            sthelp.runs_by_day_hist(sthelp, data=data ,method_name=None)
        else:
            sthelp.runs_by_day_hist(sthelp, data=data, method_name=method_name)
        
    def display_runs_by_hour(self, data, method_name):
        st.divider()
        st.subheader("Runs by Hour")
        if method_name is None:
            sthelp.runs_by_hour_hist(self=sthelp, data=data, method_name=None)
        else:
            sthelp.runs_by_hour_hist(self=sthelp, data=data, method_name=method_name)