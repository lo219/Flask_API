import pandas as pd
from sqlalchemy import create_engine

def create_database_from_csv(db_name, table_name, db_type, csv_file_path):
    connection_string = db_type + ':///' + dbname
    engine = create_engine(connection_string)
    #connection = engine_connect()
    with open(csv_file_path, 'r') as file:
        csv_df = pd.read_csv(file)
    csv_df.to_sql(table_name, con=engine, index=True, index_lable='id'. if_exists='replace')
