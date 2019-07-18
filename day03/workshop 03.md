# Workshop 3

## Problem

### 1번문제

```python
#1 .Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다.따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다. 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.

#1)
def palindrome(word):
    a = list(word)
    b =[0]*len(a)
    for i in range(len(a)) :
       b[len(a)-1-i]= a[i] 
    if a == b :
        return print('True')
    else :
        return print('False')


palindrome('12345654321')



#2)

def palindrome(word):
    list_word = list(word) # 5 => 2 // 4 => 2
    for i in range(len(list_word) // 2) # 몫을 구한다.
    if list_word[i] == list_word[-i-1]:
        return False
    return True


#3)
def palindrome(word):
    print(word[::-1])
    return word == word[::-1]
#결과값

True
```

### 2번문제

```python

```



### 3번문제

```python

```

