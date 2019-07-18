#Workshop

#1. 양의 정수 x를 입력 받아 제곱근의 근사값을 반환하는 함수를 작성하세요. sqrt() 사용 금지

def sqqrt(a) :    
    b1 = 1   
    b2 = (b1+a)/2
    while(round(b1, 8) != round(b2, 8)) :      
        cal = (b1 + b2)/2
        if a < cal **2 :
            b2 = cal
        if a > cal **2 :
            b1 =cal           
    print(round(b1,8), a**0.5)

sqqrt(float(input()))


#print(a, b1, b2)
