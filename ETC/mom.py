import pandas as pd

load_fish = pd.read_excel('C:/Users/sangwoo/Desktop/조건별학생조회.xls')
# print(load_fish)

# '성명'열 만 뽑기
name = load_fish['성명']
# 이름만 추출해서 list 만들기
names = []
for i in name:
    names.append(i)

print(names) # 475명 확인


data = pd.read_excel('C:/Users/sangwoo/Desktop/상우테스트.xlsx')
print('전체데이터:')
print(data)
print(data.iloc[:,3].isnull().sum()) # 이름자료들

df = data.dropna(subset=['성명'])
# print('결측치제거')
print(df)


work = []
for i in names:
    name_data = df[df.iloc[:,3].str.contains(i)]
    df1 = name_data.values.tolist()
    work.append(df1)
print(work)

done = sum(work,[])

answer = pd.DataFrame(done)
print(answer)

answer.to_excel('C:/Users/sangwoo/Desktop/엄마작업.xlsx')