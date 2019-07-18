# Homework3

## 1번문제

```python
#1. Python에서 기본으로 사용할 수 있는 Built in function 5개를 찾아서 작성하세요.
print(dir(__builtins__))

#결과값

['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

## 2번문제

```python
#2. 다음과 같이 함수가 정의되어 있다. 보기 중, 오류가 발생하는 코드를 고르시오.
def ssafy(name, location = '서울') :
    print(f'{name}의 지역은 {location}입니다.')

ssafy(location='대전', name='철수')
ssafy('길동', location='광주')
ssafy(name='허준', '구미')

#ssafy(name='허준', '구미')
                        ^
#SyntaxError: positional argument follows keyword argument

3번에서 오류가 발생한다. 왜냐하면 ssafy에서 입력받는 location은 키워드 인자를 사용하였는데 이는 위치 인자를 활용할 수 없기 때문이다. 그렇기 때문에 오류가 발생한다.

# 키워드 인자는 앞으로 가야함!!

```



## 3번문제

```python
#3. 다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.

def my_func(a,b):
    c = a + b
    print(c)
result = my_func(4,7)
print(result)

#결과값
11
None


프린트 해본결과 None값이 들어 있는 것을 확인할 수 있다.
그 이유는 my_func함수는 return 값이 없기 때문에 None 값을 반환한다.
```



## 4번문제

```python

```



## 5번문제

```python

```

