import boto3
import pytest
import allure
import pandas as pd
import datatest as dt
from datatest import (
    Missing,
    Extra,
    Invalid,
    Deviation,
)

@allure.story('Testing CSV File')
@allure.feature('Testing path of the CSV file and Extension')
@allure.testcase("CSV Test Case")
@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def df():
    return pd.read_csv('C:\\Work_Imp\\DataScience\\FuzzyMatcherVENV\\data\\raw\\hospital_account_info.csv')
    

@allure.step("Validate the columns")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.mandatory
def test_columns(df):
    dt.validate(df.columns,{'Account_Num','Facility Name','Address','City','State','ZIP Code','County Name','Phone Number','Hospital Type','Hospital Ownership'})
    
    
@allure.step("Verify the address column")
@allure.severity(allure.severity_level.MINOR)
def test_Address(df):
    dt.validate.regex(df['Address'],r'^[a-zA-Z0-9#(),]')
    pass

@allure.step("Verify the Account_Num column")
@allure.severity(allure.severity_level.MINOR)
def test_Account_Num(df):
    dt.validate(df['Account_Num'],int)
    #dt.validate.regex(df['Account_Num'],r'^[0-9]')    

def test_Facility_Name(df):
    dt.validate.regex(df['Facility Name'],r'^[a-zA-Z0-9()]')

def test_city(df):
    dt.validate.regex(df['City'],r'^[a-zA-Z]')

def test_State(df):
    #dt.validate(df['State'],int)
    dt.validate.regex(df['State'],r'^[a-zA-Z]')

def test_Zip_Code(df):
    dt.validate(df['ZIP Code'],int)
#'','','',''
def test_County_Name(df):
    dt.validate.regex(df['County Name'],r'^[a-zA-Z]')

def test_Phone_Number(df):
    dt.validate.regex(df['Phone Number'],r'^[0-9+)(]')

def test_Hospital_Type(df):
    dt.validate.regex(df['Hospital Type'],r'^[a-zA-Z]')

def test_Hospital_Ownership(df):
    dt.validate.regex(df['Hospital Ownership'],r'^[a-zA-Z]')

if __name__=='__main__':
    from datatest import main
    pytest.main()    
