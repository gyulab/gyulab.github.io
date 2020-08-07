---
layout: post
title:  "Scattering Reduction using Volume Inversion Phenomenon"
date:   2020-08-07T14:28:52-05:00
author: Gyujun Jeong
categories: Academics
---
![alt text]({{ site.baseurl }}/assets/images/gyulab/sm1.jpg "image"){:.profile}
<br>
&nbsp; &nbsp; &nbsp; &nbsp;이전 포스팅에서 가장 widely하게 이용되는 Mobility Enhancement Technique인 Strain Engineering에 대해서 알아보았다. 이번 포스팅에서는 반도체를 만들 때 가장 기초가 되는 Wafer를 이용하여 Mobility를 향상시키는 기술에 대해서 알아보고자 한다.
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/sm2.png "image"){:.profile}
<br>

&nbsp; &nbsp; &nbsp; &nbsp;Wafer orientation과 관련하여 배운 흥미로운 내용들에 대해 잠깐 정리해보고자 한다. (111) orientation은 그림과 같이 unit area당 가장 많은 atom이 들어갈 수 있다. 반대로 (100) orientation은 unit area당 가장 적은 atom이 들어갈 수 있다. 하지만 (111) orientation은 surface에 dangling bond가 많아 interface trap을 형성하여 surface quality를 저하시킨다. CMOS process는 surface current flow를 기반으로 만들기 때문에, (100) wafer에서 fabrication을 해야 한다. 반면 Bipolar Transistor process의 경우 subjacent한 current flow를 가지므로, surface current이 중요하지 않다. 따라서 모든 orientation 모두 가능하지만, Czochralski method로 가장 쉽고 싸게 만들 수 있는 (111) wafer를 사용한다. 여담으로, Wafer 모양으로 orientation을 알 수 있다. Primary flat을 기준으로 secondary flat이 90도를 이루고 있으면 (100) wafer이고, 45도 각도를 이루고 있으면 (111) wafer이다.
<br><br>
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/sm3.png "image"){:.profile}
<br>

&nbsp; &nbsp; &nbsp; &nbsp;이제 Wafer orientation으로 moility를 향상시키는 방법에 대해 알아보자. Orientation에 따라 electron과 hole carrier의 mobility가 달라지는데, 아래 figure로부터 (110)에서 (100) orientation으로 갈수록 mobility가 향상되고, hole은 (100) orientation에서 (110) orientation으로 갈수록 mobility가 향상되어서, 두 carrier 사이에 trade-off 관계가 있음을 알 수 있다.
<br>
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/sm4.png "image"){:.profile}
<br>
&nbsp; &nbsp; &nbsp; &nbsp;이러한 경향성으로 인해, (100)에서 (110)으로 갈수록 NMOS의 drain current는 감소하고, PMOS의 drain current는 증가하게 된다. 이러한 표면 방향에 따라 캐리어의 mobility가 변화하는 요인에는 각 면에서의 effective mass와 surface roughness scattering의 차이 때문인 것으로 알려져 있다. 
<br>
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/sm5.png "image"){:.profile}
<br>

&nbsp; &nbsp; &nbsp; &nbsp;Wafer orientation 뿐만 아니라 MOS의 channel orientation도 mobility에 영향을 주게 된다. 위의 Figure를 보게 되면, (100) wafer orientation을 가진 기판에서 제작된 <100>, <110> channel 방향을 갖는 MOSFET에 대해, electron의 mobility의 경우 channel orientation에 거의 영향을 받지 않지만, hole mobility의 경우 특히 낮은 Electric field region에서 <110> channel orientation에서 improve되었다는 것을 알 수 있다. (110) wafer orientation을 가진 기판에서 제작된 경우를 보면, electron은 <100> channel에서, hole은 <110> channel orientation에서 mobility 향상을 obtain 할 수 있었다.
<br><br>
&nbsp; &nbsp; &nbsp; &nbsp;정리하자면, electron mobility는 (100) wafer와 channel orientation에서 성능이 improve되어 NMOS의 성능이 가장 좋고, hole mobility는 (110) wafer와 channel orientation에서 성능이 inprove되어 PMOS의 성능이 가장 좋다는 것을 알 수 있다. 이에 기반하여, 2005년 IBM에서는 기존의 동일 orientation을 가지는 wafer에서의 CMOS process에서, NMOS와 PMOS의 orientation을 각각 달리 하여 fabrication하는 Hybrid orientation 기술을 발표했다.


<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/wo6.png "image"){:.profile}
<br>

&nbsp; &nbsp; &nbsp; &nbsp;위의 Figure를 보게 되면, 3.1.에서 알아보았던 eSiGe와 tensile stressed liner, 즉 intentional한 stress enhancement또한 적용이 되어 있음을 알 수 있다.
<br>
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/wo7.png "image"){:.profile}
<br>
&nbsp; &nbsp; &nbsp; &nbsp;결과적으로, (100)면에서 NMOS를, (110)에서 PMOS를 fabrication할 경우, PMOS와 hole mobility의 향상을 얻을 수 있다는 것을 알 수 있다.
<br>


<br>
&nbsp; &nbsp; &nbsp; &nbsp;이 방법에도 단점은 존재한다. 다른 orientation에서 process를 진행하게 되면, 기본적으로 다른 orientation의 wafer를 같이 붙이므로 mismatch와 같은 side effect가 발생하여 reliability 문제가 가장 큰 문제가 될 것이다. 또한, (100) orientation에 비해 (110) wafer는 interface trap density가 높아지기 때문에, device의 크기를 더 작게 하면 오히려 더 치명적인 factor로 작용할 수 있다. 논문의 저자 또한 이 process는 32nm dimension이하에서의 trap density에 대해서는 고려하지 않았다고 언급하였다.

<br>
<br>
[Reference]<br>
[1] Chang, L., Leong, M., Yang, M., Chang, L., Leong, M., & Yang, M. (2004). CMOS Circuit Performance Enhancement by Surface Orientation Optimization. IEEE Transactions on Electron Devices, 51(10), 1621–1627.doi:10.1109/ted.2004.834912 <br>
[2] P. Gaubert et al., "Relation Between the Mobility, 1/f Noise, and Channel Direction in MOSFETs Fabricated on (100) and (110) Silicon-Oriented Wafers, IEEE TED, 2010.<br>
[3] H. Nakamura et al., "Effects of Selecting Channel Direction in Improving Performance of Sub-100 nm MOSFETs Fabricated on (110) Surface Si Substrate, Japanese Journal of Applied Physics, 2004.
