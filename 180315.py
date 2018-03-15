year = 2018
month = 3
print(year, month)

print(0b10, "진수")
print("30 = ", bin(30))

print(0o10, "진수")
print("30 = ", oct(30))

print(0x10, "진수")
print("30 = ", hex(30))

# 2의 31제곱
print(type(2**31))

# 복소수 표현
x = 3 - 4j
print(type(x))
print(x.imag)           # 괄호가 없으면 x라는 객체의 속성
print(x.conjugate())    # 괄호가 있으면 x라는 객체의 멤버 함수
