# Workshop 2

## Problem

### 1번문제

```python
#1. 두 개의 정수 n과 m이 주어질 때, 반복문을 사용하여 별(*) 문자를 이용해
#가로의 길이가 n, 세로의 길이가 m인 사각형을 출력하시오.

n = 5
m = 9
result=''
for k in range(m):
    for i in range(n):
        result += '*'
    result += '\n'    
print(result)
#결과값
*****
*****
*****
*****
*****
*****
*****
*****
*****
```

### 2번문제

```python
#2.과목명과 점수가 담긴 딕셔너리가 있을 때, 평균 점수를 출력하시오.

student = {'python' : 80, 'algorithm' : 99, 'django' : 89, 'flask' : 83}
sum1 = 0
for i in student.values():
    sum1 += i
print(sum1/len(student))

#결과값
87.75
```



### 3번문제

```python
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
for 
A = {'A' : len(a), 'B' : len(b), 'AB' : len(ab), 'O' : len(o)}
print(A)
#결과값
{'A': 3, 'B': 3, 'AB': 3, 'O': 3}
```

