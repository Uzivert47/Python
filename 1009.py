def find_last_computer(T, cases):
    results = []
    for a, b in cases:
        # a^b mod 10을 계산
        last_computer = pow(a, b, 10)
        # 만약 결과가 0이면, 10번 컴퓨터를 사용
        if last_computer == 0:
            last_computer = 10
        results.append(last_computer)
    return results

# 입력 예시
T = int(input())
cases = []
for _ in range(T):
    a, b = map(int, input().split())
    cases.append((a, b))

# 결과 출력
results = find_last_computer(T, cases)
for result in results:
    print(result)