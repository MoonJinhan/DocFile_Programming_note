#<<<<연습문제>>>
#Q1 흥길동 씨의 과목별 점수는 다음과 같다. 홍길동씨의 평균 점수를 구해보자

# ko = 80
# en = 75
# ma = 55

# print((ko+en+ma)/3)

#Q2자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해보자

# if 13%2 == 0 :
#     print('짝수')
# else:
#     print('홀수')

#Q3홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
#04주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.

# jumin = "881120-1068234"
# list(jumin)
# print(jumin[:6])
# print(jumin[7:])
# print(jumin[7])

#Q5다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.

# a="a:b:c:d"
# print(a)
# print(a.replace(":","#"))

#Q6[1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.
# b=[1, 3, 5, 4, 2]
# #b.sort()
# b.reverse()
# print(b)

#Q7['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
# sen = ['Life', 'is', 'too', 'short']
# print(sen[0]+" "+sen[1]+" "+sen[2]+" "+sen[3])

#Q8(1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.

# a=(1,2,3)
# b=(4)
# print(a+b)

#Q9 다음과 같은 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.

# a['name'] = 'python'
# a[('a',)] = 'python'
# a[[1]] = 'python'
# a[250] = 'python'

# 2번째 빈칸이 있기 때문에, 거짓이 성립이 되므로.

#Q10딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자

# a = {'A':90, 'B':80, 'C':70}
# print(a.pop('B'))

#Q11 a 리스트에서 중복 숫자를 제거해 보자.
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# a.remove(1)
# a.remove(1)
# a.remove(2)
# a.remove(3)
# a.remove(3)
# a.remove(4)
# print(a)

#Q12
#<<<<변수>>>>
#리스트를 복사하는 방법
# a=[1,2,3]
# b=a[:]
# a[1]=4
# print(a)
# print(b)

# from copy import copy

# a=[1,2,3]
# b=[1,2,3]
# # b=copy(a)
# # print(b)
# print(b is a)
#<<<<bool>>>>
# if [1]:
#     print("참")
# else:
#     print("거짓")
# # a=True
# b=False

# print(type(a))
# print(1==1)

#<<<<dic>>>>
# print(())
# grade ={'pey':10,'julliet':99}
# print(grade.keys())
# print(list((grade.keys())))

# print(grade['pey'])

# a={1:'a',2:'b'}
# print(a[1])

#<<<<list>>>>
# s1=set([1,2,3,4])
# l1 =list(s1)
# print(l1)
# print(l1[0])

# s2 = set("moonjinhan")
# l2 = list(s2)
# print(l2)

# print(l2[0])

# import moduel_test as mod1

# print(mod1.add(3,4))
# print(mod1.sub(4,3))

import moduel_test as mod1

print(mod1.add(2,3))
print(mod1.PI)

a = mod1.Math()
print(a.solv(2))
print(mod1.solv(2))