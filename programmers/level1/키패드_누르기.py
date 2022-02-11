# 이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

# 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때,
# 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

# numbers 배열의 크기는 1 이상 1,000 이하입니다.
# numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
# hand는 "left" 또는 "right" 입니다.
# "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
# 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	| "right"	| "LRLLLRLLRRL"
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	| "left"	| "LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	| "right"	| "LLRLLRLLRL"

numbers = [1,3,4,5,8,2,1,4,5,9,5]
hand = 'right'


def solution(numbers, hand):

    keys = []   # 키패드 번호
    values = [] # 키패드 일차함수 변환 값

    for point in range(1, 13):
        key = '{}'.format(point)
        keys.append(key)

    for i in [4, 3, 2, 1]:
        for j in range(1, 4):
            value = (j, i)
            values.append(value)

    dict_point = dict(zip(keys, values))    # 키패드 딕셔너리 형태로 변환 {키패드 번호:키패드 일차함수 좌표}

    result = []  # 누를 손 리스트
    now = [10, 12]  # 현재 손 위치

    for number in numbers:

        l_hand = now[0] # 현재 왼손 위치
        r_hand = now[1] # 현재 오른손 위치

        print('현재 손 번호 --- 왼손: {0}, 오른손: {1}'.format(l_hand, r_hand))
        print('입력할 키패드', number)

        # 0 번호 11번호로 바꿔주기
        if number == 0:
            number = 11

        # 왼손만 가능한 키패드
        if dict_point[str(number)][0] == 1:
            now[0] = number
            now_hand = 'L'
            result.append(now_hand)
            print('왼손으로_클릭')

        # 오른손만 가능한 키패드
        elif dict_point[str(number)][0] == 3:
            now[1] = number
            now_hand = 'R'
            result.append(now_hand)
            print('오른손으로_클릭')

        else:
            # 현재 왼손에서 들어온 키패드까지 거리 찾기 * 일차식 뺄셈 후 절댓값 *  (x1, y1) - (x2, y2)
            len_from_left = abs((dict_point[str(now[0])][0] - dict_point[str(number)][0])) + abs((dict_point[str(now[0])][1] - dict_point[str(number)][1]))

            # 현재 오른손에서 들어온 키패드까지 거리 찾기 * 일차식 뺄셈 후 절댓값 *  (x1, y1) - (x2, y2)
            len_from_right = abs((dict_point[str(now[1])][0] - dict_point[str(number)][0])) + abs((dict_point[str(now[1])][1] - dict_point[str(number)][1]))

            print('왼손부터 거리: {}'.format(len_from_left))
            print('오른손부터 거리: {}'.format(len_from_right))

            # 왼손거리가 짧을 때
            if len_from_left < len_from_right:
                now[0] = number
                now_hand = 'L'
                result.append(now_hand)
                print('왼손으로_클릭')

            # 오른손 거리가 짧을 때
            elif len_from_left > len_from_right:
                now[1] = number
                now_hand = 'R'
                result.append(now_hand)
                print('오른손으로_클릭')

            # 두 거리가 같을 경우 주 손잡이에 따라 결정
            elif len_from_left == len_from_right and hand == 'left':
                now[0] = number
                now_hand = 'L'
                result.append(now_hand)
                print('왼손으로_클릭')

            elif len_from_left == len_from_right and hand == 'right':
                now[1] = number
                now_hand = 'R'
                result.append(now_hand)
                print('오른손으로_클릭')

    answer = ''.join(result)

    return answer


answer = solution(numbers, hand)

print(answer)
