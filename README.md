C:\Work_Imp\DataScience\FuzzyMatcherVENV>cd Scripts

C:\Work_Imp\DataScience\FuzzyMatcherVENV\Scripts>activate

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>code .

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>python template.py


(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>pip  install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  -r requirements.txt


(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>dvc init

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git init

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>dvc init

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>dvc add data/raw/hospital_account_info.csv

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>dvc add data/raw/hospital_reimbursement.csv

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git remote add origin https://github.com/vjrmsg/FuzzyMatcherVENV.git

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git branch -M main

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git push -u origin main

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git add .

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git commit -m "first commit"

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git push -u origin main

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>dvc repro

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV\src>python DynamoDB_CSV_Import.py ..\\data\\raw\\hospital_reimbursement.csv hospital_account_info

npm config set strict-ssl false

Allure requires Java 8 or higher; 

npm install -g allure-commandline --save-dev ...

python -m pytest csvfilecheck.py --alluredir ./reports --ignore-mandatory
python -m pytest Riedl_FuzzyMatcher_1_unittest.py --alluredir ./reports --ignore-mandatory

-- The Allure Framework is a flexible and lightweight open source multi-language test reporting tool. It provides clear graphical reports and allows everyone involved in the development process to extract a maximum of information from the everyday software testing process.

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV\tests>python -m pytest csvfilecheck.py --alluredir ./reports --ignore-mandatory

>allure serve ./reports




