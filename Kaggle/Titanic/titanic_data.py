import pandas as pd
import numpy as np
import re

train_data = pd.read_csv("./Kaggle/Titanic/Titanic_data/train.csv")
test_data = pd.read_csv("./Kaggle/Titanic/Titanic_data/test.csv")

#print(train_data.shape) #(891, 12)
#print(test_data.shape)  #(418, 11)

'''
- Colums info -
PassengerId : 승객 번호
Survived    : 생존여부 (1: 생존, 0: 사망)
Pclass      : 승선권 클래스 (1: 1st, 2: 2nd, 3: 3rd)
Name        : 승객 이름
Age         : 승객 나이
Sex         : 승객 성별
SibSp       : 동반한 형제자매, 배우자 수
Parch       : 동반한 부모, 자식 수
Ticket      : 티켓의 고유 넘버
Fare        : 티켓의 요금
Cabin       : 객실 번호
Embarked    : 승선한 항구명(C: Cherbourg, Q: Queenstown, S: Southampton)


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


print(pd.isnull(train_data).sum())

PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2

print(pd.isnull(test_data).sum())

PassengerId      0
Pclass           0
Name             0
Sex              0
Age             86
SibSp            0
Parch            0
Ticket           0
Fare             1
Cabin          327
Embarked         0

Train_data - 177 Age, 687 Cabin and 2 Embarked nun values.
Test_data - 86 Age, 1 Fare and 327 Cabin nun values.

'''

# Fill age null values

all_sex = pd.concat([train_data["Sex"], test_data["Sex"]], axis=0)


print(all_sex)
print(train_data["PassengerId"])

# print(pd.Series.value_counts(train_data["Name"]))

# 호칭을 뽑기 위한 정규식
pat = re.compile('[\w]+, ([\w]+)')
# 이름에서 호칭을 뽑기위한 함수 정의
def find_name_title(x):
    return pat.findall(x)[0]

#이름 내용을 호칭으로 변경해버리기
train_name_data = train_data['Name'].apply(find_name_title)
test_name_data = test_data['Name'].apply(find_name_title)
first_name = pd.concat([test_name_data, test_name_data], axis=0)
'''
print(pd.Series.value_counts(first_name))
Mr        480   남자
Miss      156   결혼하지 않은 여자
Mrs       144   결혼한 여자
Master     42   석사
Rev         4   신부
Col         4   대령(군인)
Dona        2   귀부인
Ms          2   알리고 싶지 않아함
Dr          2   박사, 의사
'''
# print(train_name_data)
# print(test_name_data)