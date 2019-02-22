import pandas as pd
from sqlalchemy import create_engine

# define variables
DB_NAME = "titanic.db"
TABLE_NAME = "titanic"
DB_TYPE = "sqlite"
CSV_FILE_PATH = "titanic.csv"


# the function
def create_database_from_csv(db_name, table_name, db_type, csv_file_path):
    connection_string = db_type + ":///" + db_name
    engine = create_engine(connection_string)
    with open(csv_file_path, "r") as file:
        csv_df = pd.read_csv(file)
    csv_df.to_sql(
        table_name, con=engine, index=True, index_label="id", if_exists="replace"
    )


# calling the function
if __name__ == "__main__":
    create_database_from_csv(DB_NAME, TABLE_NAME, DB_TYPE, CSV_FILE_PATH)