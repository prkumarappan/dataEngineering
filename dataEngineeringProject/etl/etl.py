from extract import extract_data
from transform import transform_data
from load import load_data

# etl to extract from xlsx and load to postgres
#   - extract from xlsx
#   - transform data
#   - load to postgres

def etl(file_path):
    """Extract data from xlsx file, transform data, and load to postgres

    Returns:
        None
    """
    
    # extract data
    extract_df = extract_data(file_path)

    if extract_df is not None:
        # transform data
        transform_df = transform_data(extract_df)

        # load data to postgres
        load_data(transform_df)

if __name__ == "__main__":
    etl('./data/raw/DEM_Challenge_Section1_DATASET.xlsx')