# #homework02
# #1. 두 개의 정수 n과 m이 주어질 때, 반복문을 사용하여 별(*) 문자를 이용해
# #가로의 길이가 n, 세로의 길이가 m인 사각형을 출력하시오.

# n = 5
# m = 9
# result=''
# for k in range(m):
#     for i in range(n):
#         result += '*'
#     result += '\n'    
# print(result)


# #2.과목명과 점수가 담긴 딕셔너리가 있을 때, 평균 점수를 출력하시오.

# student = {'python' : 80, 'algorithm' : 99, 'django' : 89, 'flask' : 83}
# sum1 = 0
# for i in student.values():
#     sum1 += i
# print(sum1/len(student))

#3. 다음은 여러 사람의 혈액형(A, B, AB, O)에 대한 데이터이다. 반복문을 사용하여 
# key는 혈액형의 종류, value는 인원 수인 딕셔너리를 만들고 출력하시오.

blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
a, b, ab, o = [], [], [], []
for i in blood_types :
    if i == 'A' :
        a.append(i)
    elif i == 'B' :
        b.append(i)
    elif i == 'AB' :
        ab.append(i)
    elif i == 'O' :
        o.append(i)
A = {'A' : len(a), 'B' : len(b), 'AB' : len(ab), 'O' : len(o)}
print(A)

# print(A)

#homework

#1. 아래 보기 중, 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을
# 구분 하시오.

#2. range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.
# ls = []
# for i in range(1,51) :
#     if i % 2 : 
#         ls.append(i)
# print(ls)

#3. 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 딕셔너리를 만드시오.

# classroom= {'백민주' : 26, '윤성민' : 28, '하지수' : 28, '신영훈' : 26}
# print(classroom.keys())
# print(classroom.values())