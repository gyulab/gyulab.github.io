---
layout: post
title:  "Backend of IC process"
date:   2020-01-07T14:25:52-05:00
author: Gyujun Jeong
categories: Academics
---

![alt text]({{ site.baseurl }}/assets/images/mosfet/e1.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;앞선 포스팅에서 소개한 반도체 공정으로 반도체를 제작하였다. 하지만 단순히 실리콘 덩어리에 불과한 반도체는 제 기능을 수행하지 못한다. 오늘은 이후 처리과정인 Backend design에 대하여 알아보도록 하자.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e2.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;먼저 Frontend란 앞선 포스팅에서의 방법과 같이 Transistor Level에서의 공정이라면, Backend는 Interconnection이나 L, C와 같은 Passive Device로 칩을 만드는 과정이라고 생각하면 된다.
<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/e3.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;먼저 설계한 트랜지스터의 전극 역할을 해 줄 plug를 contact해야 한다. 이 공정을 자세하게 알아보자.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e5.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;먼저 두껍게 올라온 oxide layer를 에칭을 통해서 잘라준다.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e6.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;이후 접촉저항이 낮은 Titanium Layer를 올려준다.
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
&nbsp;&nbsp;&nbsp;&nbsp;이제 이 CMOS를 만들기 위한 공정을 단계별로 알아보도록 하자.
<br>


<br>

&nbsp;&nbsp;&nbsp;&nbsp;위의 CMOS 공정을 gif 파일로 나타내보면 다음과 같다.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/w17.gif "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;다음 시간에는 CMOS의 구조에 대해 자세히 알아보도록 하자. CMOS를 자세히 알기 위해서는 전자회로 지식을 알고 있어야 한다.
