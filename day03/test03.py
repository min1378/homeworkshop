# workshop
#1 .Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다.
# 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다. 
# 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 
# palindrome(word)를 만들어보세요.


# def palindrome(word):
#     a = list(word)
#     b =[0]*len(a)
#     for i in range(len(a)) :
#        b[len(a)-1-i]= a[i] 
#     if a == b :
#         return print('True')
#     else :
#         return print('False')


# palindrome('12345654321')


# homework

#1. Python에서 기본으로 사용할 수 있는 Built in function 5개를 찾아서 작성하세요.

# print(dir(__builtins__))


#2.다음과 같이 함수가 정의되어 있다. 보기 중, 오류가 발생하는 코드를 고르시오.

# def ssafy(name, location = '서울') :
#     print(f'{name}의 지역은 {location}입니다.')

# ssafy(location='대전', name='철수')
# ssafy('길동', location='광주')
# ssafy(name='허준', '구미')

#3. 다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.

# def my_func(a,b):
#     c = a + b
#     print(c)
# result = my_func(4,7)
# print(result)