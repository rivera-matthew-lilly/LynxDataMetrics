import streamlit as st
from StreamLitHelper import StreamLitHelper as slhelp

class Widgets:

    def display_metrics_line(self, data, method_name):
        dna_mixing_prod_runs = slhelp.get_production_run_count(self=slhelp, data=data, target_column_name="methodname", target_value=method_name)
        dna_mixing_success_runs = slhelp.get_successful_run_count(self=slhelp, data=data, target_column_name="methodname", target_value=method_name)
        successful_rate = round(((dna_mixing_success_runs/dna_mixing_prod_runs) * 100))

        st.markdown(":orange[Data span:] " + str(slhelp.get_first_prod_date(self=slhelp, data=data)) + " - " + str(slhelp.get_last_prod_date(self=slhelp, data=data)))

        col1, col2, col3 = st.columns(3)
        col1.metric(label=":green[Production Runs]", value=dna_mixing_prod_runs, delta=None)
        col2.metric(label=":green[Successful Runs]", value=dna_mixing_success_runs, delta=None)
        col3.metric(label=":green[Success Rate]", value=str(successful_rate) + "%", delta=None)

    def display_runs_by_day(self, data, method_name):
        st.divider()
        st.subheader('Runs Per Day')
        slhelp.days_per_week_hist(slhelp, data=data, method_name=method_name)