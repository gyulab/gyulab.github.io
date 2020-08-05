---
layout: post
title:  "FinFET Doping Issue: Overcoming Shadow Effect Problem during S/D Implantation"
date:   2020-07-10T14:28:52-05:00
author: Gyujun Jeong
categories: Academics
---

<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/fd0.jpg "image"){:.profile}
<br>

&nbsp;&nbsp;&nbsp;&nbsp;Multi-gate channel은 fin의 측면에 있게 때문에, parasitic resistance를 없애기 위해서 sidewall을 따라 일정하게 도핑 되어야 한다. 하지만 이전의 FinFET 공정에서는 그림의 24번과 같이 두껍게 패터닝이 된 PR Mask를 써야 했는데, 이 PR Mask의 두께로 인해서, implant 공정이 그림에서 수직면을 기준으로 𝜃* 을 넘는 각도로 tilt되어서 진행이 된다면, 24E1과 같이 Mask 측면에 가려져 sidewall쪽의 implant가 아예 진행이 되지 않게 되어 버린다. 또한, FinFET은 Gate가 솟아 나있는 모양으로 높이를 가지기 때문에, ion implantation을 할 때 shadow effect가 발생하게 된다.<br>

<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/fd1.PNG "image"){:.profile}
<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;우리는 ion implantation 공정에서, Boron과 같이 작은 입자들이 실리콘 격자 구조를 따라 들어가버리는 channeling effect를 막기 위하여, wafer를 7도 정도 tilt하여 실리콘의 격자 구조를 조금 더 빽빽하게 만드는 방법을 사용한다는 것을 배웠다. 위의 그림에서도 26A와 같이 implant beam이 입사할 때, 7도 정도의 기울기를 가지고 implant하는 것을 알수 있다. 이를 통해 우리는 sidewall 전체에 골고루 dopant material을 implant할 수 있게 되었다고 생각했지만, tilt를 해서 implant를 하면 위에서 보았던 것처럼 PR에 의해서 shadow가 될 수 있고, fin의 한쪽 면만doping이 되게 되는, fin 모양 그 자체에 의한 shadow effect가 발생하게 되어 버린다.<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;엔지니어들은 이러한 shadow effect를 막기 위해서 여러 가지 방법을 시도해 보았다. 먼저, 위의 그림과 같이 26과 같이 우측 하방 (Figure에서 ‘26’ 방향)을 가리키는 방향으
로 implant beam을 쏘게 되면, fin의 좌측 부분을 implant할 수 있게 된다. 이후, implant 장비는 고정한 채 wafer를 180도 돌리게 되면, implant beam의 입사 방향이 좌측 하방을 가리키는 방향 (Figure에서 ‘30’ 방향)으로 바꿀 수 있게 된다. 이렇게 되면 fin의 우측 부분을 implant할 수 있게 되고, fin의 양측 모두를 implant할 수 있게 된다.<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;PR mask에 의한 shadowing effect도 해결하기 위해 많은 노력을 하였다. 그 중 하나는 fin을 가리지 않을 때까지 PR mask의 pitch (위의 Figure에서 초록색 펜으로 표시)를 늘리는 방법이다. 하지만 이 방법은 packing density를 낮추기 때문에, 애초에 집적도를 높이기 위한 노력의 일환인 FinFET의 제작 의도에 반하는 방법이므로 사용하지 않게 되었다. PR mask에 의한 shadowing effect를 근본적으로 없앨 수 있는 방법은 vertical하게 세워진 mask를 눕혀버리는 방법이다. 즉 lithography적 방법으로 이 문제를 해결하는 것이다. Mask를 위의 그림의 𝜃* 보다 더 크게, 즉 non-vertical하게 눕히게 되면, shadowing effect를 없앨 수 있게 된다.<br><br>


<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/fd2.PNG "image"){:.profile}
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/fd3.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;PR 패턴의 각도는 보통 30~60도 정도로 맞출 수 있는데, 원하는 공정에 따라 이 각도도 조절할 수 있다. 이 각도를 조절하는 방법으로는 포토레지스트의 absorption rate를 조절하면 된다. Figure 2D와 E 그래프를 보게 되면, Exposed dose가 E100인 지점에서 남은 Photoresist layer가 없어지게 된다. 여기서 Figure 2D의 slope가 더 steep하다면 expose dose가 E0(초기 dose)에서 E100으로 도달하는 시간이 더 빨라진다는 의미이며, 이는 곧 PR이 더 빨리 없어진다는 뜻이다. E0에서 E100으로의 도달 시간을 줄이기 위해서는 PR의 absorption rate를 늘려주면 된다. 더 많은 lithography source (KrF)를 수용하면서 PR이 빨리 없어지게 되고, 이에 따라 더 낮은 각도의 PR 패턴을 얻을 수 있다.
<br>
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/fd4.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;예시로, Figure 2F에서 사용된 PR에 비해 Figure 2G에서 사용된 PR의 absorption rate를 더 높은 것을 사용하여, 더 작은 각도의 mask pattern을 얻을 수 있었다.

[Reference]<br>
[1] U.S. Patent No. 20140113420A1 (2012)
