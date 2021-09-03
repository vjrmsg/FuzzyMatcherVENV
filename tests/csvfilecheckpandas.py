import pandas as pd
import datatest as dt
import allure
from datatest import (
    Missing,
    Extra,
    Invalid,
    Deviation,
)

@allure.story('Testing CSV File')
@allure.feature('Testing path of the CSV file and Extension')
@allure.testcase("CSV Test Case")
@dt.working_directory(__file__)
def setUpModule():
    global df
    df = pd.read_csv('C:\\Work_Imp\\DataScience\\FuzzyMatcherVENV\\data\\raw\\hospital_reimbursement.csv')
    dt.register_accessors()

class TestMyData(dt.DataTestCase):
    @dt.mandatory
    def test_column_names(self):
        required_names = {'Account_Num','Facility Name','Address','City','State','ZIP Code','County Name','Phone Number','Hospital Type','Hospital Ownership'}
        df.columns.validate(required_names)

        def test_Account_Num(self):
            requirement={1,2,3}
            df['C'].validate(requirement)
    
if __name__=='__main__':
    from datatest import main
    main()   
