import sys

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
    # 명령줄 인수에서 숫자를 입력받음
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        divisors = find_divisors(number)
        # 약수들을 공백으로 구분하여 출력
        print(" ".join(map(str, divisors)))
