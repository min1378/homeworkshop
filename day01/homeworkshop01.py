#homework1
#1. Python에서 사용할 수 없는 식별자 예약어 를 찾아 작성하세요.
# import keyword
# print(keyword.kwlist)


# #2.파이썬에서 float 는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다.
# #(floating point rounding error)
# #따라서 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

# # 1)abs <= 1e-10 과 같이 오차범위 설정하여 비교
# a = 0.1 * 3
# b = 0.3
# print(abs(a-b) <= 1E-10)

# # 2)sys 모듈을 통해 처리하는 방법
# import sys

# a = 0.1 * 3
# b = 0.3
# print(abs(a-b) <= sys.float_info.epsilon)

# # 3) math 모듈을 통해 처리

# import math

# a = 0.1 * 3
# b = 0.3

# print(math.isclose(a,b))

# #3.이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) 을 작성하세요.

# print('이것은 줄바꿈입니다. \n 1) 줄바꿈')
# print('이것은 탭입니다 \t 2) 탭')
# print('이것은 역슬래시입니다. 3) \\')

# #4. 안녕 철수야 를 String Interpolation 을 사용하여 출력하세요.

# name = '철수'
# # 1) %-formatting 활용
# print('안녕, %s야' %name)

# # 2) str.format() 활용
# print('안녕, {}야'.format(name))

# # 3) f-string() 활용
# print(f'안녕, {name}야')

# #5. 다음 중 형변환시 오류가 발생하는 것은?
# print(str (1))
# print(int('30'))
# print(int(5))
# print(bool('50'))
# print(int('3.5'))


#workshop1

# #1. 두 개의 정수 n 과 m 이 주어집니다 . 
# # 반복문을 사용하지 않고 별 (*) 문자를 이용해 가로의 길이가 n, 
# # 세로의 길이가 m 인 직사각형 형태를 출력해보세요.

n = 5
m = 9
print((('*' * n) + '\n')*m)
# print('*','\0'*(n-4),'*')
# print('*','\0'*(n-4),'*')
# print('*','\0'*(n-4),'*')
# print('*','\0'*(n-4),'*')
# print('*','\0'*(n-4),'*')
# print('*','\0'*(n-4),'*')
# print('*','\0'*(n-4),'*')
# print('*' * n)

print('"C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다." 나는 생각했다.'"'cd를 써서 git bash로 들어가봐야지'")

#3. 다음과 같은 이차방정식이 있을 때 근을 찾는 수식을 파이썬 코드를 이용하여 출력해보시오.

#x^2 + 4x + 21
a = 1
b = 4
c = 21 
d = b^2-4*a*c
solution1 = (-b + d**0.5)/(2*a)
solution2 = (-b - d**0.5)/(2*a)
print(solution1, solution2)