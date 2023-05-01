import psycopg2
from psycopg2 import extras
import configparser
import pandas as pd

# Load data into postgresql
#   - connect to postgresql
#   - create table
#   - insert data into table
#   - close connection

def load_data(df):
    """Load data into postgresql

    Args:
        df (pandas.DataFrame): dataframe
    """

    # Load config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    db_host = config['postgresql']['host']
    db_port = config['postgresql']['port']
    db_name = config['postgresql']['dbname']
    db_user = config['postgresql']['user']
    db_password = config['postgresql']['password']

    # Connect to postgres
    conn = psycopg2.connect(
        host=db_host, 
        port=db_port, 
        database=db_name, 
        user=db_user, 
        password=db_password)
    cur = conn.cursor()

    # drop table 
    table_name = 'customers'
    drop_table_query = f'DROP TABLE IF EXISTS {table_name};'

    # create table
    table_name = 'customers'
    schema = '''id int, first_name varchar(255), 
                last_name varchar(255),
                email varchar(255),
                email_domain varchar(255),gender varchar(255),
                ip_address inet'''
    
    create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({schema});'
    cur.execute(create_table_query)

    # insert data into table
    values = [tuple(x) for x in df.to_numpy()]
    insert_query = f"INSERT INTO {table_name} ({','.join(df.columns)}) VALUES %s"
    try:
        extras.execute_values(cur, insert_query, values)
        conn.commit()
        print("execute_values() done")

        # test to see if data is inserted
        cur.execute(f'SELECT COUNT(*) FROM {table_name};')
        print(cur.fetchall())
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        return 1
    
    # close connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    df = pd.DataFrame()
    # create test data = id 
    df['id'] = [1, 2, 3]
    # create test data  - first name
    df['first_name'] = ['John', 'Jane', 'Joe']
    # create test data - last name
    df['last_name'] = ['John', 'Jane', 'Joe']
    # create test data - email
    df['email'] = ['John@gmail.com', 'Jane@gmail.cc', 'Joe@gm98[].com']
    # create test data - gender
    df['gender'] = ['Male', 'Female', 'Male']
    # create test data - ip_address
    df['ip_address'] = ['34.148.232.131', '192.168.0.255', '34.148.232.139']
    # create test data - email_domain
    df['email_domain'] = ['gmail.com', 'gmail.cc', 'gm98[].com']

    load_data(df)