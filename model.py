import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import AdaBoostClassifier
import pickle

data=pd.read_excel(r'C:\Users\DELL\Desktop\dev\models\employee-attrition-prediction\employee_attrition.xlsx')

data.drop(['EmployeeNumber','EmployeeCount','Over18','StandardHours'],axis=1,inplace=True)

categorical_features=[feature for feature in data.columns if data[feature].dtype=='O']
data=pd.get_dummies(data, columns=categorical_features, drop_first=True)

data.columns=['Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobSatisfaction', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'BusinessTravel_Travel_Frequently', 'BusinessTravel_Travel_Rarely', 'Department_Research_Development', 'Department_Sales', 'EducationField_Life_Sciences', 'EducationField_Marketing', 'EducationField_Medical', 'EducationField_Other', 'EducationField_Technical_Degree', 'Gender', 'JobRole_Human_Resources', 'JobRole_Laboratory_Technician', 'JobRole_Manager', 'JobRole_Manufacturing_Director', 'JobRole_Research_Director', 'JobRole_Research_Scientist', 'JobRole_Sales_Executive', 'JobRole_Sales_Representative', 'MaritalStatus_Married', 'MaritalStatus_Single', 'OverTime_Yes', 'Attrition']

X=data.iloc[:,:-1]
y=data['Attrition']

oversample = SMOTE()
smote_independent, smote_dependent = oversample.fit_resample(X, y)

ab_feature_imp = AdaBoostClassifier(n_estimators=500, learning_rate=0.1)
ab_feature_imp.fit(smote_independent, smote_dependent)

pickle.dump(ab_feature_imp,open(r'C:\Users\DELL\Desktop\dev\models\employee-attrition-prediction\attrition_adaboost_pickle_model.pkl','wb'))
model=pickle.load(open(r'C:\Users\DELL\Desktop\dev\models\employee-attrition-prediction\attrition_adaboost_pickle_model.pkl','rb'))