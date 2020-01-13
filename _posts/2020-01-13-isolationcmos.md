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
![alt text]({{ site.baseurl }}/assets/images/mosfet/i6.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Oxide를 이용한 isolation으로, MOS 개발 초기에 이용된 기술이다. 하지만 다양한 단점들로 인해 다음에 소개될 LOCOS 기법이나 Trench Isolation등을 이용하게 된다.
![alt text]({{ site.baseurl }}/assets/images/mosfet/i7.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;LOCOS기법은 LOCal Oxidation of Si의 약어로, 옛날 자료를 정리하느라 오늘날의 method라고 나와 있는데, 실제로는 현재의 나노공정에서 LOCOS는 후술하겠지만 Bird's Beak과 같은 side effect들로 인하여 지금은 사용하지 않고 있다.
![alt text]({{ site.baseurl }}/assets/images/mosfet/i8.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Trench Isolation의 Trench는 트렌치 코트 할 때의 Trench, 즉 참호이다. 공정이 복잡하다는 단점이 있지만, Packing density를 획기적으로 올릴 수 있어서 오늘날 가장 많이 사용하는 기법 중 하나이다.



![alt text]({{ site.baseurl }}/assets/images/mosfet/i9.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;앞서 소개한 LOCOS 공정에 대하여 조금 더 자세하게 알아보도록 하자.
![alt text]({{ site.baseurl }}/assets/images/mosfet/i11.jpg "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/i10.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;LOCOS 공정의 순서는 위의 그림과 같은데, 마지막 그림에서 field oxide를 grow하는 과정에서 oxide가 휘는 현상을 관찰할 수 있다.
![alt text]({{ site.baseurl }}/assets/images/mosfet/i12.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;이렇게 휘는 현상을 새의 부리를 닮았다고 해서 Bird's Beak 현상이라고 부르는데, 이는 Device의 Active Area를 낮추는 효과를 가져와 LOCOS의 Limiting factor로 작용한다. 
![alt text]({{ site.baseurl }}/assets/images/mosfet/i13.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;이러한 Bird's Beak 현상을 해결하기 위하여, SWAMI, SPOT, OSELO, FUROX와 같은 다양한 기법을 사용했다.



![alt text]({{ site.baseurl }}/assets/images/mosfet/i14.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;이제 Trench Isolation에 대하여 알아보도록 하자.


![alt text]({{ site.baseurl }}/assets/images/mosfet/i15.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Trench Isolation을 이용하는 응용기법을 알아보도록 하자. STI는 Shallow Trench Isolation이고, Bipolar를 Isolate하거나 CMOS의 Latch-up을 prevent하기 위해 Moderate Trench를 이용한다. 그리고 DRAM의 Trench capacitor를 만들기 위해서는 Deep trench를 이용한다. 각각의 구분은 1um, 3um을 기점으로 구분한다. 
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/i16.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;STI(Shallow Trench Isolation) 과정이다.

![alt text]({{ site.baseurl }}/assets/images/mosfet/i17.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Trench를 Etching할 때, 둥근 trench가 선호된다. 둥글게 Trench를 만들기 위해서는 고도의 Dry-etching기법과 고온 열산화 과정을 거쳐야 한다. 고온 열산화 과정은 stress를 줄여 주고, 이는 누설 전류를 감소시킨다.

![alt text]({{ site.baseurl }}/assets/images/mosfet/i18.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;앞선 포스팅에서 본 SOI(Silicon on Insulator)와 STI를 이용하면 더욱 더 효과적인 Isolation이 가능하다. 0.13um 이하의 공정에서 사용하는 기법이다. 
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/i19.jpg "image"){:.profile}
