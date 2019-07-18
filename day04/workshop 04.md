# Workshop4

## Problem

### 1번문제

```python
#1. 양의 정수 x를 입력 받아 제곱근의 근사값을 반환하는 함수를 작성하세요. sqrt() 사용 금지

def sqqrt(a) :    
    b1 = 1 # 부등호의 왼쪽 초기값   
    b2 = (b1+a)/2 #부등호의 오른쪽 초기값
    while(round(b1, 8) != round(b2, 8)) :  #최소값과 최대값이 8자리 반올림했을때 같을때 까지 반복한다.    
        cal = (b1 + b2)/2 #이분법을 cal에 저장
        if a < cal **2 : #만약에 a가 cal^2보다 작다면
            b2 = cal #cal을 최대값에 넣음
        if a > cal **2 : #만약에 a 가 cal^2보다 크다면
            b1 =cal #cal을 최소값에 넣음            
    print(round(b1,8), a**0.5) #출력

sqqrt(float(input()))
# 결과값
$ python test04.py
141
11.87434209 11.874342087037917

student@M702 MINGW64 ~/homeworkshop/day04 (master)
$ python test04.py
2
1.41421356 1.4142135623730951
```

### 2번문제

```python

```



### 3번문제

```python

```

