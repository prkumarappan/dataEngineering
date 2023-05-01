import pandas as pd
import ipaddress

# transform data from extract.py
#   - remove rows with null values
#   - remove rows with duplicate values
#   - remove rows with invalid values
#       - email
#       - ip_address

def transform_data(df):
    """Transform data from extract.py

    Args:
        df (pandas.DataFrame): dataframe
    """
        
    # remove rows with null values
    df = df.dropna()

    # remove rows with duplicate values
    df = df.drop_duplicates()

    # remove rows with invalid emails
    df = df[df['email'].str.contains('@')] # remove rows with no @
    # create new column with email domain only
    df['email_domain'] = df['email'].str.split('@').str[1]
    email_domain_regex_pattern = r'^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,}$' # domain has at least 1 dot, only containts letters and numbers and ends with at least 2 letter top level domain
    df = df[df['email_domain'].str.match(email_domain_regex_pattern)]

    # remove rows without valid ip address
    valid_ip = df['ip_address'].apply(validate_ip_address)
    df = df[valid_ip] 

    return df

# validate ip address
def validate_ip_address(ip_address):
    """Validate ip address

    Args:
        ip_address (str): ip address

    Returns:
        bool: True if valid, False otherwise
    """
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    df = pd.DataFrame()
    # create test data = id 
    df['id'] = [1, 2, 3]
    # create test data  - first name
    df['first_name'] = ['John', 'Jane', 'Joe']
    # create test data - last name
    df['last_name'] = ['John', 'Jane', 'Joe']
    # create test data - email
    df['email'] = ['John@gmail.com', 'Jane@gmail.cc', 'Joe@gm98~.com']
    # create test data - gender
    df['gender'] = ['Male', 'Female', 'Male']
    # create test data - ip_address
    df['ip_address'] = ['34.148.232.131', '192.168.0.256', '34.148.232.139']
    
    # transform data
    df = transform_data(df)
    print(df)
