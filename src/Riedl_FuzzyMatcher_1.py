import pandas as pd
from pathlib import Path
import fuzzymatcher

def fuzzymatch_csv (input_file_master,
                    input_file_to_match_with_master,
                    list_columns_to_match_of_master_file,
                    list_columns_to_match_with_master_file,
                    left_id_col,
                    right_id_col
                   ):
    """ Takes two csv files as input and compares the list of columns to return a single merged data frame along with a fuzzy match
    score.
    """
    
    df_left =  pd.read_csv(input_file_master)
    df_right = pd.read_csv(input_file_to_match_with_master)
    # Columns to match on from df_left
    left_on = list_columns_to_match_of_master_file
    # Columns to match on from df_right
    right_on = list_columns_to_match_with_master_file
    
    return fuzzymatcher.fuzzy_left_join(df_left,
                                               df_right,
                                               left_on,
                                               right_on,
                                               left_id_col='Account_Num',
                                               right_id_col='Provider_Num')


if __name__ == "__main__" :
    matched_results = fuzzymatch_csv (input_file_master = '..\\data\\raw\\hospital_account_info.csv',
                                  input_file_to_match_with_master = '..\\data\\raw\\hospital_reimbursement.csv',
                                  list_columns_to_match_of_master_file = ["FacilityName", "Address", "City", "State"],
                                  list_columns_to_match_with_master_file = ["ProviderName", "ProviderStreetAddress", "ProviderCity",   "ProviderState"],
                                  left_id_col='Account_Num',
                                  right_id_col='Provider_Num'
                                 )
    print(matched_results.head())

