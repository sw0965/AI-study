# 문제
# 네오와 프로도가 숫자놀이를 하고 있습니다.
# 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 조건
# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.
#    1478 → "one4seveneight"
#    234567 → "23four5six7"
#    10203 → "1zerotwozero3"

# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나,
# 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다.
# s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.
# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

def solution(s):

    ls = []
    cnt = 0

    str_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    str_int = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    dic = {y : x for x, y in enumerate(str_num)}

    for i in range(1, len(s) + 1):
        if s[cnt:i] in str_num:
            num = dic.get(s[cnt:i])
            ls.append(str(num))
            cnt = i

        elif s[cnt:i] in str_int:
            ls.append(s[cnt:i])
            cnt = i

    answer = int("".join(ls))

    return answer

s = "2three45sixseven"
# print(solution(s))
#
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
def solution2(s):
    answer = s
    for key, value in num_dic.items():
        print(key, value)
        answer = answer.replace(key, value)
    return int(answer)

print(solution2(s))

# str_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# str_int = ['0','1','2','3','4','5','6','7','8','9']
# # for i, y in enumerate(str_num):
# #     print(i,y)
#
# dic = {y : x for x, y in enumerate(str_num)}
# # print(dic)
# # print(dic.get('zero'))
#
# cnt = 0
#
# for i in range(1, len(s)+1):
#     if s[cnt:i] in str_num:
#         num = dic.get(s[cnt:i])
#         c.append(str(num))
#         cnt = i
#
#     elif s[cnt:i] in str_int:
#         c.append(s[cnt:i])
#         cnt = i
#
# answer = int("".join(c))
