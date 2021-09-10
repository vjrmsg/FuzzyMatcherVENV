Step1:  Create the Virtual environment for the Project "FuzzyMatcherVENV"

C:\Work_Imp\DataScience\FuzzyMatcherVENV> python -m venv C:\Work_Imp\DataScience\FuzzyMatcherVENV

Step2: Actiavate the virtual environment "FuzzyMatcherVENV"

C:\Work_Imp\DataScience\FuzzyMatcherVENV>cd Scripts

C:\Work_Imp\DataScience\FuzzyMatcherVENV\Scripts>activate

Step3: Open the code in the VisualStudio Code

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>code .

Step4: Update the template python file to create the directories for the project

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>python template.py

Step5: Update the requirements.txt with required libraries which are to be installed in the new created new environment.

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>pip  install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  -r requirements.txt

Step6: Initiate the DVC and GIT for the repositories

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>dvc init

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git init

Step7:  Add the source CSV files to DVC which is initiated.

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>dvc add data/raw/hospital_account_info.csv

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>dvc add data/raw/hospital_reimbursement.csv

Step8:  Configure the github to the environment and add the main branch

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git remote add origin https://github.com/vjrmsg/FuzzyMatcherVENV.git

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git branch -M main

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git push -u origin main

Step9:  Add the current code and commit and push to the GitHub

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git add .

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git commit -m "first commit"

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>git push -u origin main

Step10: run dvc repro -- to check the data and pipelines status 

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV>dvc repro

Step11: Installing

npm config set strict-ssl false

Allure requires Java 8 or higher; 

npm install -g allure-commandline --save-dev ...

python -m pytest csvfilecheck.py --alluredir ./reports --ignore-mandatory
python -m pytest Riedl_FuzzyMatcher_1_unittest.py --alluredir ./tests/reports --ignore-mandatory

-- The Allure Framework is a flexible and lightweight open source multi-language test reporting tool. It provides clear graphical reports and allows everyone involved in the development process to extract a maximum of information from the everyday software testing process.

(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV\tests>python -m pytest csvfilecheck.py --alluredir ./reports --ignore-mandatory

allure serve ./reports

cd
(FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV\src>python DynamoDB_CSV_Import.py ..\\data\\raw\\hospital_reimbursement.csv hospital_account_info

(FuzzyNameMatching) (FuzzyMatcherVENV) C:\Work_Imp\DataScience\FuzzyMatcherVENV\src>python RapidFuzzDemo.py