# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

# [1,2,3,4]	    1
# [1,2,7,6,4]	4

# [1,2,4]를 이용해서 7을 만들 수 있습니다.

# [1,2,4]를 이용해서 7을 만들 수 있습니다.
# [1,4,6]을 이용해서 11을 만들 수 있습니다.
# [2,4,7]을 이용해서 13을 만들 수 있습니다.
# [4,6,7]을 이용해서 17을 만들 수 있습니다.

from itertools import combinations
import math

com_list = []


def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):  # 2부터 x의 제곱근까지의 숫자 (시간을 줄이기 위한 제곱근까지의 수)
        if x % i == 0:  # 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True


def solution(nums):
    answer = 0

    comb = list(combinations(nums, 3))
    for i in comb:
        sum_comb = sum(i)
        com_list.append(sum_comb)

    for y in com_list:
        if primenumber(y) is True:
            answer += 1

    return answer