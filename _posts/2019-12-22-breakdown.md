---
layout: post
title:  "Breakdown Phenomena"
date:   2019-12-22T11:25:52-05:00
author: Gyujun Jeong
categories: Academics
---

![alt text]({{ site.baseurl }}/assets/images/mosfet/b1.png "intro"){:.profile}

<br>

&nbsp;&nbsp;&nbsp;&nbsp;Breakdown이란 다이오드에 역 바이어스 전압을 걸어주었을 때 다이오드가 견디지 못하고 전류가 크게 흐르는 현상으로, 이러한 현상이 발생하는 최소 전압을 항복전압이라고 한다.
<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/b2.png "zener"){:.profile}
 
&nbsp;&nbsp;&nbsp;&nbsp;Breakdown의 첫 번째 종류는 Zener Breakdown이다. Heavily Doped된 곳에서 발생하는 Breakdown으로, High dope일 때 Depletion region의 폭이 감소하는 효과가 나타나 에너지 밴드가 서로 가까워지는 형태를 띄게 된다. 이렇게 되면 전자가 쉽게 Penetrate가 되는, 즉 Tunneling 현상이 발생하게 된다.
<br>

 
![alt text]({{ site.baseurl }}/assets/images/mosfet/b3.png "avalanche"){:.profile}
<br>
  
&nbsp;&nbsp;&nbsp;&nbsp; Breakdown의 두 번째 종류인 Avalanche Breakdown은 Zener보다 상대적으로 lightly doped된 곳에서 발생하며, 이 Breakdown의 원리는 Impact ionization이다. Impact Ionization이란 강하게 applied 된 전계로 인해 전자가 가속이 되고, 이 가속된 전자가 Silicon 원자들의 covalent bonding에 충격을 가하면서 전자-홀 쌍을 형성하게 되고, 이러한 기작이 지수함수적으로 발생하면서 많은 양의 전류가 흐르게 된다.

<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/b4.png "versus"){:.profile}

 
&nbsp;&nbsp;&nbsp;&nbsp; 그래프에서 알 수 있듯이, 제너 항복이 Avalanche 항복보다 더 낮은 항복 전압을 가지기 때문에, 이와 같은 성질을 활용하여 Zener Diode와 같은 소자를 만든다.
<br>

<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/b5.png "avalanche"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/b6.png "avalanche"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/b7.png "avalanche"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/b8.png "avalanche"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp; Bipolar Junction Transistor에서의 Avalanche Breakdown 특성을 나타내 보았다.

<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/b9.png "punchthrough"){:.profile}

 
&nbsp;&nbsp;&nbsp;&nbsp; BJT에서의 Breakdown이 발생하는 기작인 Punch-Through 현상이다. Collector와 Base의 Space Charge Region이 Base로 점점 확장되고, 이 Region이 EB 접합과 닿게 되면 Base가 없어지고 Emitter와 Collector가 short되는 현상이 발생하게 된다. 즉, Base region이 Fully depleted, Base 전체가 공핍층이 되게 되어 Current가 급증하게 된다.
<br>



