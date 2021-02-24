import pandas as pd
import numpy as np

train_data = pd.read_csv("./Kaggle/Titanic/Titanic_data/train.csv")
test_data = pd.read_csv("./Kaggle/Titanic/Titanic_data/test.csv")

print(train_data.shape) #(891, 12)
print(test_data.shape)  #(418, 11)

'''
print(train_data.columns)
print(test_data.columns)

- train_data - 12 columns
'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 
'Age', 'SibSp','Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'

- test_data - 11 columns
'PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 
'SibSp', 'Parch','Ticket', 'Fare', 'Cabin', 'Embarked'

No Survived columns in test_data.



print(train_data.info())
print(test_data.info())

- train_data
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   PassengerId  891 non-null    int64
 1   Survived     891 non-null    int64
 2   Pclass       891 non-null    int64
 3   Name         891 non-null    object
 4   Sex          891 non-null    object
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64
 7   Parch        891 non-null    int64
 8   Ticket       891 non-null    object
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object
 11  Embarked     889 non-null    object


- test_data
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   PassengerId  418 non-null    int64
 1   Pclass       418 non-null    int64
 2   Name         418 non-null    object
 3   Sex          418 non-null    object
 4   Age          332 non-null    float64
 5   SibSp        418 non-null    int64
 6   Parch        418 non-null    int64
 7   Ticket       418 non-null    object
 8   Fare         417 non-null    float64
 9   Cabin        91 non-null     object
 10  Embarked     418 non-null    object

'''

