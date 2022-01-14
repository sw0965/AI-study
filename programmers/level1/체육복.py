# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다.
# 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
# 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
# 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

#전체 학생의 수 n,
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.


def solution(n, lost, reserve):
    before_borrow = range(n)
    print(before_borrow)
    answer = 0
    return answer


n = 5
lost = [2,  4]
reserve = [1, 3]

# 전체 인원중 도둑맞지 않은 아이들 찾기
non_stolen = [x for x in range(1, n+1) if x not in lost]
print('도둑안당한 아이들', non_stolen)



# 옷 갯수 확인하기 (자기꺼 제외한 빌려줄 수 있는 옷)
reserve = [x for x in reserve if x in non_stolen]
print('옷 여부', reserve)





#
# check_cloths = [x for x in reserve if x in lost]    # 2벌 챙긴애중에 도둑맞은애 찾기
#
# count_cloths = [x for x in reserve if x not in check_cloths]    #
#
# print(check_cloths)
# print(count_cloths)
#
#
# cloths = count_cloths * 2
# print(cloths)
# # for i in cloths:


# check_cloth = [x for x in cloths if x not in lost]
# print(cloths)
# print(check_cloth)


'''
one = [x for x in range(1, 5+1) if x not in lost]
print('도둑맞은애 제외', one)

one = [x for x in one if x not in reserve]
print('자기 옷만 챙긴애', one)

cloths = one+(reserve*2)
# print(one)
print("옷 여부 상태", cloths)
'''
# reserve = (reserve * 2) + ()
# print(reserve)

'''all = [i for i in range(1, n+1)]
print(all)
for m in lost:

    all.remove(m)
print(all)

p_borrow = {}
student = 0
b_range = []
borrow = 0
for i in lost:

    # print(i)
    borrow_down = i-1
    borrow_up = i+1
    if borrow_up <= n and borrow_down > 0:
        p_borrow[i] = [borrow_down, borrow_up]

live = []
print('총인원', n)
print('잃어버린 애들', lost)
print('빌려줄수 있는 애들', reserve)
print('-------------------------------')

for j in p_borrow:
    print('잃어버린 애들이 입을수 있는 사이즈들', p_borrow)
    # print('g',j)
    for k in reserve:
        print('빌려주는 애', k)
        if k in p_borrow[j]:
            # print('빌려줄애 찾은애', k)
            # live = live.append[j]
            p_borrow[j] = []
            reserve.append(j)


result = all + reserve

print(p_borrow)
print(all)
print('체육활동 가능한 사람들', reserve)
print('체육활동 가능한 사람들', len(reserve))

print('결과: ', list(set(result)))'''

# print(j)
# print(live)
# print(b_range)


# all_students_list.remove([i for i in lost])
#
# print(all_students_list)

