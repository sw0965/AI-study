# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다.
# 무지가 개발하려는 시스템은 다음과 같습니다.

# - 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
#    - 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
#    - 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.

# - k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
#    - 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

# 내 풀이
def solution(id_list, report, k):
    report = list(set(report))  # 같은 사람이 여러번 신고해도 1회로 적용이 되어 중복 제거를 해준다.

    count = []  # 각각 dict 형태에 넣어줄 []
    sum = []  # 신고 당한 수
    answer = []  # 답

    for i in range(len(id_list)):
        # dict.fromkeys? 이거 했는데 리스트 변경이 이루어질때 다같이 이루어져서 ..
        count.append([])
    report_info = dict(zip(id_list, count))

    for i in range(len(id_list)):
        sum.append(0)
    result = dict(zip(id_list, sum))

    for i in report:
        reporter = i.split()[0]
        reported = i.split()[1]
        report_info[reported].append(reporter)

    for i in report_info:
        # print(report_info[i])
        if len(report_info[i]) >= k:
            for j in report_info[i]:
                for y in result:
                    if j == y:
                        result[y] += 1

    for i in result:
        answer.append(result[i])

    return answer


# 다름사람 풀이
def solution2(id_list, report, k):

    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1
        print(r.split()[1])

    for r in set(report):

        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer





