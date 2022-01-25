# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# 1 <= numbers의 길이 <= 9
# 0 <= numbers의 모든 원소 <= 9
# numbers의 모든 원소는 서로 다릅니다.

def solution(numbers):
    answer = -1    # -1이 왜 들어있는지 모르겠다

    answer = sum([x for x in range(0, 10) if x not in numbers]) # 0부터 10중에 numbers 에 없는거 골라서 합산해주기

    return answer

