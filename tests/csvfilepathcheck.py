from pathlib import Path
from datatest import validate, working_directory
import csv

with working_directory(__file__):
    file_name = 'C:\\Work_Imp\\DataScience\\FuzzyMatcherVENV\\data\\raw\\hospital_account_info.txt'

def is_csv(x):
    return x.lower().endswith('.csv')

with open(file_name,newline='') as csvfile:
    reader = csv.reader(csvfile) 

    header_row = next(reader)
    validate(header_row, {'Account_Num','Facility Name','Address','City','State','ZIP Code','County Name','Phone Number','Hospital Type','Hospital Ownership'})

validate(file_name, is_csv, msg='should be a csv file')


