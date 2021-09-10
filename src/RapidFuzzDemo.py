import rapidfuzz as fuzz
import pandas as pd
from pathlib import Path
import fuzzymatcher
import rapidfuzz
from rapidfuzz import process,fuzz,utils
import openpyxl

#print(rapidfuzz.fuzz.partial_ratio("this is a test", "12"))
input_file_master = '..\\data\\raw\\hospital_account_info.csv'
input_file_to_match_with_master = '..\\data\\raw\\hospital_reimbursement.csv'
df_left =  pd.read_csv(input_file_master)
df_right = pd.read_csv(input_file_to_match_with_master)

actual_comp = []
similarity = []
provider_mapping = {provider: utils.default_process(provider) for provider in df_left.FacilityName}
provider_address_mapping={provider: utils.default_process(provider) for provider in df_left.Address}
provider_city_mapping={provider: utils.default_process(provider) for provider in df_left.City}
provider_state_mapping={provider: utils.default_process(provider) for provider in df_left.State}


for providername in df_right.ProviderName:
    _,score, comp = process.extractOne(
        utils.default_process(providername),
        provider_mapping,
        processor=None)
    actual_comp.append(comp)
    similarity.append(score)

df_right['FacilityName'] = pd.Series(actual_comp)
df_right['similarity']=pd.Series(similarity)

actual_comp1 = []
similarity1 = []

for provideraddress in df_right.ProviderStreetAddress:
    _,score1, comp1 = process.extractOne(
        utils.default_process(provideraddress),
        provider_address_mapping,
        processor=None)
    actual_comp1.append(comp1)
    similarity1.append(score1)

df_right['Address'] = pd.Series(actual_comp1)
df_right['similarity']=pd.Series(similarity1)

actual_comp3 = []
similarity3 = []

for providercity in df_right.ProviderCity:
    _,score3, comp3 = process.extractOne(
        utils.default_process(providercity),
        provider_city_mapping,
        processor=None)
    actual_comp3.append(comp3)
    similarity3.append(score3)
df_right['City'] = pd.Series(actual_comp3)
df_right['similarity']=pd.Series(similarity3)

actual_comp2 = []
similarity2 = []

for providerstate in df_right.ProviderState:
    _,score2, comp2 = process.extractOne(
        utils.default_process(providerstate),
        provider_state_mapping,
        processor=None)
    actual_comp2.append(comp2)
    similarity2.append(score2)

df_right['State'] = pd.Series(actual_comp2)
df_right['similarity']=((pd.Series(similarity2)+pd.Series(similarity1)+pd.Series(similarity3)+pd.Series(similarity))/4)

if __name__ == "__main__" :

    print(df_right[['Provider_Num','ProviderName','ProviderStreetAddress','ProviderCity','ProviderState','FacilityName','Address','City','State','similarity']].head(10))
    MatchedResults=df_right[['Provider_Num','ProviderName','ProviderStreetAddress','ProviderCity','ProviderState','FacilityName','Address','City','State','similarity']].head(10)
    MatchedResults.to_excel('..\\data\\processed\\MatchedResults.xlsx')

    
#lookup = df_left['Account_Num']


