import subprocess

def test_divisors_100():
    # divisors.py를 실행하고 출력값을 얻음
    result = subprocess.run(["python3", "divisors.py", "100"], capture_output=True, text=True)
    output = result.stdout.strip()
    
    # 예상 출력값
    expected_output = "1 2 4 5 10 20 25 50 100"
    
    # 결과 비교
    assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"
    print("test1 passed")

if __name__ == "__main__":
    test_divisors_100()
