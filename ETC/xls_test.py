import pandas as pd

# 데이터 불러오기
data = pd.read_excel('C:/Users/sangwoo/Desktop/test.xlsx') 
# df = pd.DataFrame(data)
df = data.values.tolist()
# print(data.shape)

# 신입생 데이터 불러오고 신입생들 이름 리스트로 치환
name_list = ['코코몽', '초코', '고구려'] 
# print(df)


ls = []

for i in name_list:
    name_data = data[data.iloc[:,1].str.contains(i)]
    df1 = name_data.values.tolist()
    ls.append(df1)
# print(ls)

# 리스트 합치기
a = sum(ls, [])
print(a)

#형식 바꿔주기
answer = pd.DataFrame(a)
print(answer)


answer.to_excel('C:/Users/sangwoo/Desktop/answer.xlsx')


    # ls.append(name_data)
    # print(ls)

#     a = pd.DataFrame(name_data)
#     # print(a)
# # print(name_data)
# print(a)

# print(a)
# answer = pd.DataFrame([ls])
# answer.reset_index().drop()
# print(answer)
# print(ls)
# print(name_data)

'''
answer = pd.DataFrame([ls])
print(answer)
'''
