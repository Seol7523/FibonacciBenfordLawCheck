# FibonacciBenfordLawCheck

n 진법에서 피보나치 수열의 벤포드 규칙의 성립 여부를 확인하는 프로그램입니다.

## 벤포드 규칙이란?

> 벤포드의 법칙(Benford's law)은 실세계에서 존재하는 많은 수치 데이터의 10진법 값에서 수의 첫째 자리의 확률 분포를 관찰한 결과, 첫째 자리 숫자가 작을 확률이 크다는 법칙이다.
> 출처 - 위키백과<벤포드의 법칙>

![벤포드의 규칙을 보여주는 사진](https://github.com/Seol7523/FibonacciBenfordLawCheck/blob/master/results/result(Base10_10000).png)

위의 그래프는 10진법에서 피보나치 수열의 10000번째 수까지의 총 10000개의 숫자의 가장 첫자리가 1에서 9까지일 확률을 나타낸 그래프입니다.

그런데 과연 10진법이 아닌 8진법, 16진법, 아니 n 진법에서도 성립할까요?

수학적인 증명은 어려우니 전 컴퓨터로 증명해 보았습니다.

## 결과

>![8진법](https://github.com/Seol7523/FibonacciBenfordLawCheck/blob/main/results/result(Base8_10000).png)
> 8진법에서의 그래프

> ![20진법](https://github.com/Seol7523/FibonacciBenfordLawCheck/blob/main/results/result(Base20_10000).png)
> 20진법에서의 그래프

성립한다는 것을 알 수 있다.

## 수학적인 것들

벤포드 법칙이 성립하는 경우 n진법에서 d의 확률은 아래의 수식과 같다.

> ![수식](https://github.com/Seol7523/FibonacciBenfordLawCheck/blob/main/results/answer.gif)
> 수식

위의 예시에서 8진법에서 1의 확률은 

![수식에 대입하면](https://github.com/Seol7523/FibonacciBenfordLawCheck/blob/main/results/base8.gif)

위의 예시에서 20진법의 1의 확률은

![수식에 대입하면](https://github.com/Seol7523/FibonacciBenfordLawCheck/blob/main/results/base20.gif)

잘 일치함을 볼 수 있다.
