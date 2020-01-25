---
layout: post
title:  "Scaling Trend of Semiconductor"
date:   2020-01-02T14:25:52-05:00
author: Gyujun Jeong
categories: Issues
---

![alt text]({{ site.baseurl }}/assets/images/mosfet/s1.png "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;지난 시간까지 Device를 작게 만드는 이유와, 작게 만들 때 발생하는 Short Channel Effect를 알아 보았다. 수율 면으로나 성능 면으로나 소자를 더욱 작게 만드는 것은 중요하나, 점점 작게 만듬으로써 비이상적인 특성들이 나타나기 시작하고(SCE), 정상적인 스위칭이 불가능해지게 된다. 이 Short Channel Effect를 극복하기 위한 기술을 이번 시간에 알아보도록 하자.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/s2.png "image"){:.profile}

<br>

&nbsp;&nbsp;&nbsp;&nbsp;1971년, 강대원 박사의 MOSFET 트랜지스터 개발 이후, 10 마이크로미터의 Channel 길이로 시작한 반도체 산업은 세월이 지나 현재 2019년, 삼성, 하이닉스, TSMC와 같은 굴지의 기업들이 5nm 공정까지의 개발을 성공하게 된다. 세계적인 반도체 기업인 Intel은 2019년 12월, 기술 컨퍼런스에서 2027년까지 1nm 공정을 개발하는 것을 목표로 한 Roadmap을 공개하였다. 오늘은 빨간색으로 표시한 250, 130, 90, 45 나노 공정에 들어간 기술에 대하여 알아 보도록 하자. 
<br>
&nbsp;&nbsp;&nbsp;&nbsp;(2012년과 2021년에 다르게 색칠해 놓은 FinFET과 GAAFET의 경우 저번 포스팅에서 다루었으므로 저번 포스팅을 참고하도록 하자: https://gyulab.github.io//issues/2019/12/23/finfet.html)
<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/s3.png "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/s4.gif "image"){:.profile}

<br>

&nbsp;&nbsp;&nbsp;&nbsp;각 나노 공정을 살펴보기 전에, 반도체 업계에서 가장 많이 알려진 법칙이 있다. 세계적인 반도체 기업인 Intel의 공동설립자인 Gordon Moore가 제시한 무어의 법칙이다. 이는 반도체 집적회로의 성능이 24개월마다 2배로 증가한다는 법칙이다. 즉, 2년마다 2배의 성능이 향상된다고 생각할 수 있다. 
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;하지만, 점점 Scaling의 한계에 봉착하기 시작했다. 2번째 그림과 같이 channel length를 작게 하면, 오른쪽 그림과 같이 Tunneling이 발생하여 더 이상 소자가 제 기능을 하지 못하는 현상이 발생하게 된다. 설사 가능하다 하더라도 cost의 문제로 인해 포기를 해야 한다는 의견이 나오고 있다. Moore의 법칙이 더 이상 valid하지 않다와 아직까지는 valid하다는 의견이 분분하다.



<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/m10.PNG "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/s5.png "image"){:.profile}
<br>
  
&nbsp;&nbsp;&nbsp;&nbsp; 저번 시간에 봤던 Short Channel Effect이다. 수율 면으로나 성능 면으로나 소자를 더욱 작게 만드는 것은 중요하나, 점점 작게 만듬으로써 Channel이 짧아지게 되고, 이로 인해 Threshold Voltage가 Roll up되게 되며, Switching을 해야 할 때도 open이 되어 트랜지스터로써의 역할을 수행할 수 없는 결과가 발생하게 된다. 이제 각 나노공정별로 어떻게 Short Channel Effect를 극복했는지 알아보도록 하자.
<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/s6.png "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/s7.png "image"){:.profile}
<br>
 
&nbsp;&nbsp;&nbsp;&nbsp; 250nm 공정은 1996년 상용화가 시작된 공정으로, 1987년 일본의 NEC Research Team의 Kasai라는 공학자가 처음 demostrate에 성공하였다. Kasai는 다음과 같은 방법을 통해 Short Channel Effect를 극복하였다.
<br>
1. poly-Si Gate
2. Shallow S/D junctions
3. BF2+ implant
4. RTA (Rapid Thermal Annealing)
5. Thin Gate oxide (refer to Vt roll up formula)<br>
<br>
논문의 그래프를 보게 되면, RTA, 즉 고온으로 장시간 유지시킨 후 급속 냉각하는 열처리(annealing)을 한 것이 하지 않은 것보다 Vt roll up이 획기적으로 줄었다는 것을 알 수 있다.<br>
<br>
IBM의 Bijan Davari는 250nm dual-gate CMOS의 구조를 논문에 게재하였다. 소자의 구조는 2번째 그림과 같다.

<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/s8.png "image"){:.profile}

<br>
 
&nbsp;&nbsp;&nbsp;&nbsp;130nm 공정은 2001년 Fujitsu, IBM 등의 기업에 의해 상용화가 시작된 공정으로, 1990년 IBM의 T.J. Watson 연구센터의 Bijan Davari 연구진이 개발을 성공하였다. 이 공정에서의 Key points는 바로 SOI, 즉 Silicon-On-Insulator 기법을 이용한 것이다. 이 방법을 통해 기판으로 빠져나가는 leak current를 줄일 수 있었고, 기생 축전용량을 획기적으로 줄일 수 있었다. 또한 MOS 소자에서 알아본 Latch-up 문제를 해결할 수 있었다. 다른 factor로는 250nm 공정에 비해 더 얇은 oxide 두께 (7nm->5nm)를 사용하였다. 

<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/s9.png "image"){:.profile}

<br>

&nbsp;&nbsp;&nbsp;&nbsp; 45nm 공정부터는 아주 여러가지 문제에 직면하게 되는데, 먼저 lithography라는 포토공정에서 사용하는 빛의 파장인 193nm보다도 소자의 feature size가 작다는 문제가 있었다. 이를 보상하기 위해, 더 큰 렌즈와 Double-Patterning을 통해 조금 더 정밀한 포토리소그래피 공정을 만들 수 있었다. 
<br>
&nbsp;&nbsp;&nbsp;&nbsp; 또한, Vt roll up formula에서의 Cox를 키우기 위해서 이때까지 tox를 줄여 나갔었는데, 너무 얇은 oxide layer는 tunneling과 같은 undesirable한 effect를 초래하게 되어, 이를 보상하기 위해 유전체의 유전 상수(K)를 높혀 주는, High-K dielectric을 사용하게 되었다.
