from flask import Flask, render_template, request
import pickle
import numpy as np

## These are changes
## These are changes

model=pickle.load(open('attrition_adaboost_pickle_model.pkl','rb'))

app = Flask(__name__)
@app.route('/output',methods=['POST'])
def predict():
    Age=int(request.form['Age'])
    bt=int(request.form['BusinessTravel'])
    BusinessTravel_Travel_Rarely=0
    BusinessTravel_Travel_Frequently=0
    if bt==0:
        BusinessTravel_Travel_Rarely=1
    elif bt==1:
        BusinessTravel_Travel_Frequently=1
    else:
        BusinessTravel_Travel_Rarely=0
        BusinessTravel_Travel_Frequently=0
    
    d=int(request.form['Department'])
    Department_Sales=0
    Department_Research_Development=0
    if d==0:
        Department_Sales=1
    elif d==1:
        Department_Research_Development=1
    else:
        Department_Sales=0
        Department_Research_Development=0

    DistanceFromHome=int(request.form['DistanceFromHome'])

    Education=int(request.form['Education'])
    
    ef=int(request.form['EducationField'])
    EducationField_Life_Sciences=0
    EducationField_Other=0
    EducationField_Medical=0
    EducationField_Marketing=0
    EducationField_Technical_Degree=0
    if ef==0:
        EducationField_Life_Sciences=1
    elif ef==1:
        EducationField_Other=1
    elif ef==2:
        EducationField_Medical=1   
    elif ef==3:
        EducationField_Marketing=1  
    elif ef==4:
        EducationField_Technical_Degree=1         
    else:
        EducationField_Life_Sciences=0
        EducationField_Other=0
        EducationField_Medical=0
        EducationField_Marketing=0
        EducationField_Technical_Degree=0

    EnvironmentSatisfaction=int(request.form['EnvironmentSatisfaction'])

    g=int(request.form['Gender'])
    Gender=1
    if g==0:
        Gender=0       
    else:
        Gender=1

    DailyRate=int(request.form['DailyRate'])

    HourlyRate=int(request.form['HourlyRate'])

    MonthlyRate=int(request.form['MonthlyRate'])
    
    MonthlyIncome=int(request.form['MonthlyIncome'])
    
    JobInvolvement=int(request.form['JobInvolvement'])
    
    JobLevel=int(request.form['JobLevel'])
    
    jr=int(request.form['JobRole'])
    JobRole_Sales_Executive=0
    JobRole_Research_Scientist=0
    JobRole_Laboratory_Technician=0
    JobRole_Manufacturing_Director=0
    JobRole_Manager=0
    JobRole_Sales_Representative=0
    JobRole_Research_Director=0
    JobRole_Human_Resources=0
    if jr==0:
        JobRole_Sales_Executive=1
    elif jr==1:
        JobRole_Research_Scientist=1
    elif jr==2:
        JobRole_Laboratory_Technician=1   
    elif jr==3:
        JobRole_Manufacturing_Director=1  
    elif jr==4:
        JobRole_Manager=1
    elif jr==5:
        JobRole_Sales_Representative=1
    elif jr==6:
        JobRole_Research_Director=1
    elif jr==7:
        JobRole_Human_Resources=1
    else:
        JobRole_Sales_Executive=0
        JobRole_Research_Scientist=0
        JobRole_Laboratory_Technician=0
        JobRole_Manufacturing_Director=0
        JobRole_Manager=0
        JobRole_Sales_Representative=0
        JobRole_Research_Director=0
        JobRole_Human_Resources=0   
    
    JobSatisfaction=int(request.form['JobSatisfaction'])   

    ms=int(request.form['MaritalStatus'])
    MaritalStatus_Married=0
    MaritalStatus_Single=0
    if ms==0:
        MaritalStatus_Married=1
    elif ms==1:
        MaritalStatus_Single=1
    else:
        MaritalStatus_Married=0
        MaritalStatus_Single=0

    NumCompaniesWorked=int(request.form['NumCompaniesWorked'])
    
    ot=int(request.form['OverTime'])
    OverTime_Yes=1
    if ot==0:
        OverTime_Yes=0      
    else:
        OverTime_Yes=1

    PercentSalaryHike=int(request.form['PercentSalaryHike'])
    
    PerformanceRating=int(request.form['PerformanceRating'])    
    
    RelationshipSatisfaction=int(request.form['RelationshipSatisfaction'])
    
    StockOptionLevel=int(request.form['StockOptionLevel'])
    
    TotalWorkingYears=int(request.form['TotalWorkingYears'])
    
    TrainingTimesLastYear=int(request.form['TrainingTimesLastYear'])
    
    WorkLifeBalance=int(request.form['WorkLifeBalance'])
    
    YearsAtCompany=int(request.form['YearsAtCompany'])
    
    YearsInCurrentRole=int(request.form['YearsInCurrentRole'])
    
    YearsSinceLastPromotion=int(request.form['YearsSinceLastPromotion'])
    
    YearsWithCurrManager=int(request.form['YearsWithCurrManager'])
    
    pred = model.predict([[Age, DailyRate, DistanceFromHome, Education, EnvironmentSatisfaction, HourlyRate, JobInvolvement, JobLevel, JobSatisfaction, MonthlyIncome, MonthlyRate, NumCompaniesWorked, PercentSalaryHike,	PerformanceRating,	RelationshipSatisfaction,	StockOptionLevel,	TotalWorkingYears,	TrainingTimesLastYear,	WorkLifeBalance,	YearsAtCompany,	YearsInCurrentRole,	YearsSinceLastPromotion,	YearsWithCurrManager,	BusinessTravel_Travel_Frequently,	BusinessTravel_Travel_Rarely,	Department_Research_Development,	Department_Sales,	EducationField_Life_Sciences,	EducationField_Marketing,	EducationField_Medical,	EducationField_Other,	EducationField_Technical_Degree,	Gender,	JobRole_Human_Resources,	JobRole_Laboratory_Technician,	JobRole_Manager,	JobRole_Manufacturing_Director,	JobRole_Research_Director,	JobRole_Research_Scientist,	JobRole_Sales_Executive,	JobRole_Sales_Representative,	MaritalStatus_Married,	MaritalStatus_Single,	OverTime_Yes]])
    
    return render_template('result.html',prediction=pred)

@app.route('/')
def home():
	return render_template('index.html')

if __name__=='__main__':
	app.run()