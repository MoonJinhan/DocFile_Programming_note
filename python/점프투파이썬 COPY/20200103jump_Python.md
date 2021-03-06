# 20200104 예외 처리



프로그래밍을 하다보면 진짜 수많은 오류가 발생하게 된다. 이때, 어떤 오류들은 무시를 하고 싶다. 가령 내가 예전에 프로젝트를 하다가 무시를 하고 싶은 오류가 있었다. 어떤 오류였냐 하면, 형태소 분석기 중에 코모란이라는 것이 있다. 이 녀석은 분석 성능과 속도가 최상은 아니지만 좋은 편이다. 게다가 코드 한줄만 들어가면, 형태소 분석또한 쉽게 되니 아주 편하게 쓸수있다. 

하지만 1가지 오류(?)가 있다. 글에서 한 줄 자체를 띄는 부분이 있으면, 분석을 멈추게된다. 가끔은 하루에 수천건을 분석하는 경우가 있는데, 이런 경우에는 아주 맘이 복잡해진다. 그래서 나는 try except fianlly 문을 썼다. 한 줄을 띄어넘으면 오류가 뜬다. 이 오류를 패스를 하게 만들어 준 것이다. 그래서 다행스럽게 그 코드는 쓸만한 코드가 되었다. 하지만, 가장 좋은 것은 오류가 없는 것이다. =)

위에서 나의 예제를 가지고와서 어떤 경우에 예외처리를 하고 싶은지 말해보았다. 이번에는 어떻게 만드는 것인지 알아보자. 아주 처음 자바로 이 구조를 보았을 때에는 이해하지 못했지만, 파이썬으로 보니, 한결 수월하다.



### try , except 문

```
try:
	....
except[발생 오류[as 오류 메세지 변수]]:
	...
```

try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

except 구문을 자세히 살펴보자.

> except [발생 오류 [as 오류 메시지 변수]]:

위 구문을 보면 [ ] 기호를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이다. 즉 except 구문은 다음 3가지 방법으로 사용할 수 있다.

#### **1. try, except만 쓰는 방법**

```
try:
    ...
except:
    ...
```

이 경우는 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.

#### **2. 발생 오류만 포함한 except문**

```
try:
    ...
except 발생 오류:
    ...
```

이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행한다는 뜻이다.

#### **3. 발생 오류와 오류 메시지 변수까지 포함한 except문**

```
try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...
```

이 경우는 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다.

이 방법의 예를 들어 보면 다음과 같다.

```
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
```

위처럼 4를 0으로 나누려고 하면 ZeroDivisionError가 발생하여 except 블록이 실행되고 변수 e에 담기는 오류 메시지를 다음과 같이 출력한다.



### 여러개의 오류처리하기

try문 안에서 여러 개의 오류를 처리하기 위해 다음 구문을 사용한다.

```
try:
    ...
except 발생 오류1:
   ... 
except 발생 오류2:
   ...
```

즉 0으로 나누는 오류와 인덱싱 오류를 다음과 같이 처리할 수 있다.

```
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
```

a는 2개의 요솟값을 가지고 있기 때문에 `a[3]`는 `IndexError`를 발생시키므로 "인덱싱할 수 없습니다."라는 문자열이 출력될 것이다. 인덱싱 오류가 먼저 발생했으므로 `4/0`으로 발생되는 `ZeroDivisionError` 오류는 발생하지 않았다.

이전에는 어떻게 하면 여러개를 처리할 수 있을까? 고민만 하다가 말았는데, 꽤나 유용하다.



#### 또 다른 방법

```
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
```

프로그램을 실행하면 "list index out of range" 오류 메시지가 출력될 것이다.



다음과 같이 `ZerroDivisionError`와 `IndexError`를 함께 처리할 수도 있다.

```
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
```

2개 이상의 오류를 동시에 처리하기 위해서는 위와 같이 괄호를 사용하여 함께 묶어 처리하면 된다.











