---
layout: post
title:  "반도체의 Scaling Trend (CMOS)"
date:   2020-01-02T14:25:52-05:00
author: Gyujun Jeong
categories: Issues
---

![alt text]({{ site.baseurl }}/assets/images/mosfet/s1.png "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;지난 시간까지 Device를 작게 만드는 이유와, 작게 만들 때 발생하는 Short Channel Effect를 알아 보았다. 수율 면으로나 성능 면으로나 소자를 더욱 작게 만드는 것은 중요하나, 점점 작게 만듬으로써 비이상적인 특성들이 나타나기 시작하고(SCE), 정상적인 스위칭이 불가능해지게 된다. 이 Short Channel Effect를 극복하기 위한 기술을 이번 시간에 알아보도록 하자.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/s2.png "image"){:.profile}

<br>

&nbsp;&nbsp;&nbsp;&nbsp;1971년, 강대원 박사의 MOSFET 트랜지스터 개발 이후, 10 마이크로미터의 Channel 길이로 시작한 반도체 산업은 세월이 지나 현재 2019년, 삼성, 하이닉스, TSMC와 같은 굴지의 기업들이 5nm 공정까지의 개발을 성공하게 된다. 세계적인 반도체 기업인 Intel은 2019년 12월, 기술 컨퍼런스에서 2027년까지 1nm 공정을 개발하는 것을 목표로 한 Roadmap을 공개하게 된다. 오늘은 빨간색으로 표시한 250, 130, 90, 45 나노 공정에 들어간 기술에 대하여 알아 보도록 하자. 
<br>
(2012년과 2021년에 다르게 색칠해 놓은 FinFET과 GAAFET의 경우 저번 포스팅에서 다루었으므로 저번 포스팅을 참고하도록 하자: https://gyulab.github.io//issues/2019/12/23/finfet.html)
<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/m2.PNG "Profile Picture"){:.profile}
 
&nbsp;&nbsp;&nbsp;&nbsp;이제 FET에 대하여 알아보자. FET이랑 Field Effect Transistor의 약자로, 앞에서 본 MOS구조에 2개의 Terminal (Source, Drain)을 달고, 이 Terminal에 Voltage를 걸어 줘서 (=Field Effect 형성) Current의 흐름을 제어 및 증폭 (=Transistor 역할) 이 가능하다. 즉, Voltage-Controlled Current Source(VCCS)가 되는 것이다.
<br>

 
![alt text]({{ site.baseurl }}/assets/images/mosfet/m3.PNG "Profile Picture"){:.profile}
<br>
  
&nbsp;&nbsp;&nbsp;&nbsp; Accumuation, Depletion, Inversion에 관한 내용이다. 위의 도표를 보면 이해가 가능할 것이다.

<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/m4.PNG "Profile Picture"){:.profile}

<br>
 
&nbsp;&nbsp;&nbsp;&nbsp; MOS의 C-V characteristics이다. Accumulation에서의 Capacitance는 오직 Oxide charge만 존재하므로, Cox만 계산하면 된다. Depletion Region의 경우, Space charge region에 추가적인 dQ가 형성이 되어, 추가적인 Capacitance가 Series로 들어가게 되고, Curve가 내려간다. 이후 Inversion mode에서는 dQ가 surface에 extremely close한 layer에 추가가 되어 추가적인 Capacitance가 발생하지 않으므로 Cox만 발생하게 되어 curve가 다시 올라가게 된다. High Frequency에서는 Inversion layer에 dQ가 너무 빨리 스위칭되어서 response가 불가능해지고, 이에 따라 Space charge region에 보상적으로 dQ가 추가되어, deep depletion 이 발생하여 curve가 더 내려가게 된다.

<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/m5.PNG "Profile Picture"){:.profile}

<br>
 
&nbsp;&nbsp;&nbsp;&nbsp;MOS의 I-V characteristics이다. 처음에는 Id가 linear하게 올라가다가, Vde가 증가하게 되면서 Drain에 걸리는 전압차가 줄어들게 되어 Drain의 inversion charge density가 줄어들게 되고, 이에 따라 channel conductance가 감소하여 I-V slope가 점점 감소하게 된다. Vds가 Vgs-Vt가 될 때 saturation이 발생하며, 이 때의 inversion charge는 0이 되어 pinch-off가 발생한다. 이후, Vds가 더 커짐에 따라 pinch-off가 source쪽으로 이동하게 된다. 오른쪽의 그림은 MOS의 Enhancement mode와 Depletion mode를 나타내는데, Enhancement mode는 normally off device이고, Depletion mode는 normally on device로, off 하기 위해서는 minus Vg를 걸어서 G oxide에 SCR를 induce하여, n-channel region의 두께를 reduce해야 한다.

다음 시간에는 Non-ideal한 몇 가지 effects에 대하여 알아보도록 하자.
