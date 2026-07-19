import logging
import os
import time

import pandas as pd
from sqlalchemy import create_engine

os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/.logs',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
    filemode='a',
)

engine = create_engine('sqlite:///inventory.db')


def ingest_db(df, table_name, engine):
    '''Ingest data into the database.'''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


def load_raw_data():
    '''Load the raw CSV files from the data folder into the database.'''
    start = time.time()
    for file_name in os.listdir('data'):
        if file_name.endswith('.csv'):
            df = pd.read_csv(os.path.join('data', file_name))
            logging.info(f'Ingesting {file_name} in db')
            ingest_db(df, file_name[:-4], engine)
    end = time.time()
    total_time = (end - start) / 60
    logging.info('----------------Ingestion Complete-----------------')
    logging.info(f'Total time taken: {total_time:.2f} minutes')


if __name__ == '__main__':
    load_raw_data()
