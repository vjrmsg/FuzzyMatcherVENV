
from numpy import character
import pandas as pd
import datatest as dt
from datatest import (
    Missing,
    Extra,
    Invalid,
    Deviation,
)

#register_accessors()
#df=pd.read_csv('C:\\Work_Imp\\DataScience\\FuzzyMatcherVENV\\data\\raw\\hospital_reimbursement.csv')

df = pd.read_csv('C:\\Work_Imp\\DataScience\\FuzzyMatcherVENV\\data\\raw\\test.csv')
dt.register_accessors()

df.validate(character)
df.validate(str)
df.validate(int)
if __name__=='__main__':
    from datatest import main
    main() 
