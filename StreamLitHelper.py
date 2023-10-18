import sqlite3
import pandas as pd
import streamlit as st

class StreamLitHelper:

    def load_data(self, database_filepath, table_name):
        DATE_COLUMN = 'datetime'
        conn = sqlite3.connect(database_filepath)
        query = f"SELECT * FROM {table_name}"
        data = pd.read_sql_query(query, conn)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        conn.close()
        return data
    
    def days_per_week_hist(self, data, method_name):
        if method_name is None: 
            data = data[(data['productionmode'] == 'true')]
            data['day_of_week'] = data['datetime'].dt.dayofweek 
            day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            histogram = data['day_of_week'].value_counts().reindex(range(5), fill_value=0)
            histogram.index = pd.Categorical(histogram.index, categories=range(5), ordered=True)
            histogram = histogram.sort_index()
            day_names_dict = dict(enumerate(day_names))
            histogram.index = histogram.index.map(day_names_dict)
            st.bar_chart(histogram)
        else:
            data = data[(data['methodname'] == method_name) & (data['productionmode'] == 'true')]
            data['day_of_week'] = data['datetime'].dt.dayofweek 
            day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            histogram = data['day_of_week'].value_counts().reindex(range(5), fill_value=0)
            histogram.index = pd.Categorical(histogram.index, categories=range(5), ordered=True)
            histogram = histogram.sort_index()
            day_names_dict = dict(enumerate(day_names))
            histogram.index = histogram.index.map(day_names_dict)
            st.bar_chart(histogram)

    def get_production_run_count(self, data, target_column_name, target_value):
        if target_column_name is None and target_value is None:
            count = len(data[(data['productionmode'] == 'true')])
        else: 
            count = len(data[(data['productionmode'] == 'true') & (data[target_column_name] == target_value)])
        return count

    def get_successful_run_count(self, data, target_column_name, target_value):
        if target_column_name is None and target_value is None:
            count = len(data[(data['productionmode'] == 'true') & (data['successfulrun'] == 'true')])
        else:
            count = len(data[(data['productionmode'] == 'true') & (data['successfulrun'] == 'true') & (data[target_column_name] == target_value)])
        return count
    
    def get_first_prod_date(self, data):
        data = data[(data['productionmode'] == 'true')]
        data = data.sort_values(by='datetime')
        data['dates'] = data['datetime'].dt.date
        first_prod_date = data.iloc[0]['dates']
        return first_prod_date
    
    def get_last_prod_date(self, data):
        data = data[(data['productionmode'] == 'true')]
        data = data.sort_values(by='datetime')
        data['dates'] = data['datetime'].dt.date
        first_prod_date = data.iloc[-1]['dates']
        return first_prod_date
    

    
    # depreciated
    # def get_column_names(self, database_filepath, table_name) -> []:
    #     conn = sqlite3.connect(database_filepath)
    #     cursor = conn.cursor()
    #     query_command = f"PRAGMA table_info({table_name});"
    #     cursor.execute(query_command)
    #     column_names = [row[1] for row in cursor.fetchall()]
    #     conn.close
    #     return column_names
    
    # def get_unique_values(self, database_filepath, table_name, column_name):
    #     conn = sqlite3.connect(database_filepath)
    #     cursor = conn.cursor()
    #     query_command = f"SELECT DISTINCT {column_name} FROM {table_name};"
    #     cursor.execute(query_command)
    #     unique_values = [row[0] for row in cursor.fetchall()]
    #     conn.close
    #     return unique_values
    
    # def get_production_run_count(self, database_filepath, table_name, target_column_name, target_value):
    #     conn = sqlite3.connect(database_filepath)
    #     cursor = conn.cursor()
    #     query_command = f"SELECT COUNT(*) FROM {table_name} WHERE ProductionMode = 'true' AND {target_column_name} = '{target_value}'";
    #     cursor.execute(query_command)
    #     count = cursor.fetchone()[0]
    #     conn.close()
    #     return count
    
    # def get_successful_run_count(self, database_filepath, table_name, target_column_name, target_value):
    #     conn = sqlite3.connect(database_filepath)
    #     cursor = conn.cursor()
    #     query_command = f"SELECT COUNT(*) FROM {table_name} WHERE SuccessfulRun = 'true' AND {target_column_name} = '{target_value}'";
    #     cursor.execute(query_command)
    #     count = cursor.fetchone()[0]
    #     conn.close()
    #     return count

    