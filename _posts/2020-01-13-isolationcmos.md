---
layout: post
title:  "Isolation Technique of CMOS"
date:   2020-01-13T14:25:52-05:00
author: Gyujun Jeong
categories: Academics
---
![alt text]({{ site.baseurl }}/assets/images/mosfet/i1.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;CMOS란 Complementary MOS의 abbreviation으로, n-channel MOS와 p-channel MOS라는 서로 다른 두 종류의 MOS 소자를 하나의 wafer 안에 놓은 MOS 소자이다. 이렇게 두 종류의 소자를 하나의 기판 위에 놓게 되면, 누설 전류나 Latch-up과 같은 다양한 문제들이 발생한다. 오늘은 이 소자들을 분리시키는 isolation technique에 대하여 알아보도록 하자.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/i2.jpg "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/i3.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;먼저 왜 isolation이 필요한지 알아보도록 하자. 위의 그림에서 누설 전류(leakage) 경로가 표시되어 있는데, 이러한 누설 전류를 막기 위해서는 isolation이 필요하다. 2번째 그림을 보면, 소자의 크기를 줄이면서 isolation을 하는데 필요한 공간이 줄어들게 되어, isolation에도 다양한 기술이 필요하다는 것을 알 수 있다.
<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/i4.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Isolation을 하기 위한 다양한 기술들이 소개되어 있다. 위에서 아래로 내려올수록 최신 기술이라고 생각하면 된다. 이제 각각의 기술에 대하여 알아보도록 하자.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/i5.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Reverse biased diode를 이용한 diffusion isolation이다. Bipolar Transistor에서 사용되었으며, well을 통한 isolation으로 현재 이용한다.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e6.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Oxide를 이용한 isolation으로, MOS 개발 초기에 이용된 기술이다. 하지만 다양한 단점들로 인해 다음에 소개될 LOCOS 기법이나 Trench Isolation등을 이용하게 된다.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e7.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;TiN은 barrier로 작용하는데, plug가 될 metal이 oxide로 diffuse되는 것을 막아준다.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e8.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;이후 CVD deposition 공정을 통해서, 플러그 역할을 할 W(텅스텐)을 씌워준다.
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;이 공정을 연속적으로 나타내면 다음과 같게 된다.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e2d.gif "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;이 공정을 3D structure로 나타내면 다음과 같게 된다.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e3d.gif "image"){:.profile}


<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e11.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Plug를 설치하였으니, 이 plug들을 유기적으로 연결해 줄 interconnection line에 대하여 알아보도록 하자.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e12.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;위의 그림과 같이, interconnect line layer는 9~10층, 혹은 그 이상으로 위로 쌓을 수 있으며, 트랜지스터 간의 신호를 주고받는 통로 역할을 수행하게 된다.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e13.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;이 집적회로에서 가장 중요한 term이 바로 RC product로, 이 RC값이 커지면 딜레이가 커지게 된다. R과 C를 조정하여 delay를 minimize할 수 있다.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e14.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;먼저 C를 어떻게 reduce할까? 소재역학적 관점에서 관찰하자면, 일반적인 SiO2의 유전율은 3.9e이다. SiOC를 보게 되면 polarization이 줄게 되는데, 이렇게 되면 K를 줄일 수 있게 된다. 이를 통해 C를 reduce할 수 있다. 또 다른 방법으로는, Airgap을 introduce하여 C를 줄일 수 있다.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e15.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;R은 어떻게 reduce할 수 있을까? Resistivity가 같은 Cu나 Al을 쓰면 된다. 더 자세하게는 아래를 한 번 살펴보자.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e16.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Al과 Cu는 각각의 물성이 위와 같이 달라서, 둘의 금속 배선 공정은 완전히 다르다. 알루미늄의 배선 과정을 RIE라고 하고, 구리의 배선과정을 Damascene process라고 한다. 여기서 별표시가 된 용어가 낯설 수 있으니 한 번 알아보도록 하자.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e17.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;위의 용어들을 정리해 보았다. 본론으로 넘어가서, RIE와 Damascene 공정의 차이를 알아보도록 하자.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e18.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;두 공정의 가장 큰 차이는 순서에 있다. RIE 공정은 에칭 이후 oxide를 형성하는데, Damascene 공정은 위의 표에서도 알 수 있듯이 etching이 어려우므로, 먼저 oxide를 형성 후 etching을 하고, 튀어나온 부분을 polish하는 순서를 가진다. 둘의 순서가 반대라고 생각하면 쉽다.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e19.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Copper를 deposit하는 방법을 조금 더 자세하게 알아보자. Damascene 공정은 상감기법을 생각하면 되는데, 도자기를 만들 때 먼저 홈을 파고, 다른 재료를 채워서 구운 뒤에 표면을 갈아내는 기법을 사용하는데, 이도 마찬가지의 공정을 가진다고 생각하면 된다.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e20.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;표면을 갈아내는 기법을 planarization process라고 하는데, Thremal Flow, Etch back, CMP와 같은 다양한 공정을 통해 표면을 polish 할 수 있다.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e22.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Passive device의 R, L, C중 지금까지 L에 대해서는 언급이 없었어서, 인덕터를 어떻게 사용하는지에 대해서 간단히 알아보도록 하자. Intel의 Zheng 연구진의 논문을 발췌해 왔는데, Inductor를 사용함으로써 Quality factor를 개선시킬 수 있다.

<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;지금까지 금속 배선 공정(Metalization)에 대해서 알아보았다. 이제 남은 공정은 EDS공정과 Packaging 공정인데, 이 부분은 추후에 다루어 보도록 하고, 오늘은 간략하게만 알아보도록 하자.

![alt text]({{ site.baseurl }}/assets/images/mosfet/e23.jpg "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/e24.jpg "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/e25.jpg "image"){:.profile}

&nbsp;&nbsp;&nbsp;&nbsp;EDS 공정은 Yield, 수율 개선 공정이고, Packaging 공정은 chip을 외부로부터 보호하고 신호를 주고받을 수 있게 패키징하는 공정이다. 자세한 Sequence는 위의 그림을 보면 알 수 있다.


<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e26.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;이러한 복잡하고 다양한 공정을 통해 마침내 하나의 IC Chip을 생산할 수 있다.


