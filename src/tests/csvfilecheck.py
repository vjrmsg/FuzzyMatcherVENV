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

@allure.story('Testing hospital_account_info CSV File')
@allure.feature('Testing path of the hospital_account_info CSV file and Extension')
@allure.testcase("hospital_account_info CSV Test Case")
@pytest.fixture(scope='module')
@dt.working_directory(__file__)
@allure.step("Validate the hospital_account_info CSV file existence")
@allure.severity(allure.severity_level.MINOR)
def df():
    return pd.read_csv('C:\\Work_Imp\\DataScience\\FuzzyMatcherVENV\\data\\raw\\hospital_account_info.csv')


@allure.story('Testing hospital_reimbursement CSV File')
@allure.feature('Testing path of the hospital_reimbursement CSV file and Extension')
@allure.testcase("hospital_reimbursement CSV Test Case")
@pytest.fixture(scope='module')
@dt.working_directory(__file__)
@allure.step("Validate the hospital_reimbursement CSV file existence")
@allure.severity(allure.severity_level.MINOR)
def df1():
    return pd.read_csv('C:\\Work_Imp\\DataScience\\FuzzyMatcherVENV\\data\\raw\\hospital_reimbursement.csv')
    

@allure.step("Validate the hospital_account_info csv columns")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.mandatory
def test_columnsha(df):
    dt.validate(df.columns,{'Account_Num','FacilityName','Address','City','State','ZIPCode','County Name','Phone Number','Hospital Type','Hospital Ownership'})

@allure.step("Validate the hospital_reimbursement CSV  columns")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.mandatory
def test_columnshr(df1):
    dt.validate(df1.columns,{'Provider_Num','ProviderName','ProviderStreetAddress','ProviderCity','ProviderState','ProviderZipCode','Total Discharges','Average Covered Charges','Average Total Payments','Average Medicare Payments'})
   
    
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

@allure.step("Verify the Facility Name column")
@allure.severity(allure.severity_level.MINOR)
def test_Facility_Name(df):
    dt.validate.regex(df['FacilityName'],r'^[a-zA-Z0-9()]')

@allure.step("Verify the City column")
@allure.severity(allure.severity_level.MINOR)
def test_city(df):
    dt.validate.regex(df['City'],r'^[a-zA-Z]')

@allure.step("Verify the State column")
@allure.severity(allure.severity_level.MINOR)
def test_State(df):
    #dt.validate(df['State'],int)
    dt.validate.regex(df['State'],r'^[a-zA-Z]')

@allure.step("Verify the ZIP Code column")
@allure.severity(allure.severity_level.MINOR)
def test_Zip_Code(df):
    dt.validate(df['ZIPCode'],int)
#'','','',''
@allure.step("Verify the County Name column")
@allure.severity(allure.severity_level.MINOR)
def test_County_Name(df):
    dt.validate.regex(df['County Name'],r'^[a-zA-Z]')

@allure.step("Verify the Phone Number column")
@allure.severity(allure.severity_level.MINOR)
def test_Phone_Number(df):
    dt.validate.regex(df['Phone Number'],r'^[0-9+)(]')

@allure.step("Verify the Hospital Type column")
@allure.severity(allure.severity_level.MINOR)
def test_Hospital_Type(df):
    dt.validate.regex(df['Hospital Type'],r'^[a-zA-Z]')

@allure.step("Verify the Hospital Ownership column")
@allure.severity(allure.severity_level.MINOR)
def test_Hospital_Ownership(df):
    dt.validate.regex(df['Hospital Ownership'],r'^[a-zA-Z]')

if __name__=='__main__':
    from datatest import main
    pytest.main()    
