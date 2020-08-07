---
layout: post
title:  "Scattering Reduction using Volume Inversion Phenomenon"
date:   2020-08-07T14:28:52-05:00
author: Gyujun Jeong
categories: Academics
---
![alt text]({{ site.baseurl }}/assets/images/gyulab/sm1.jpg "image"){:.profile}
<br>
&nbsp; &nbsp; &nbsp; &nbsp;이전 포스팅까지 Carrier Mobility Enhancement를 위한 2가지 method를 알아보았다. 이번 시간에 알아볼 Scattering Mechanism Reduction은 재료공학에 대한 이해도가 있어야 이해할 수 있지만, 간단하게 먼저 소개해보고자 한다.<br><br>

&nbsp; &nbsp; &nbsp; &nbsp;전하가 Field를 받아 움직이는 속도인 drift velocity와 Field 간의 비례상수가 mobility이다. 따라서 mobility가 클수록 전자나 전공이 더 빠르게 움직이므로 반도체 공정에서 매우 중요한 물리량이라는 것을 이야기해왔다.<br><br>

&nbsp; &nbsp; &nbsp; &nbsp;하지만 이러한 mobility는 scattering mechanism에 의해 제한되게 된다. Scattering이란 electron이나 hole이 이동 중 Si Lattice나 ionized impurity 등에 의해 carrier의 움직임이 제한을 받게 되는 현상이고, 이로 인해 mobility degradation이 발생하게 된다. Scattering mechanism에는 아주 다양한 종류가 있지만, 가장 대표적인 2가지 종류의 scattering에 대해서 먼저 간단하게 알아보고자 한다.<br><br>

&nbsp; &nbsp; &nbsp; &nbsp;첫 번째로는 Phonon (Lattice) Scattering이 있다. 온도에 의해 thermal energy를 받게 되면, lattice에 있는 atom들이 vibration을 하게 되며, 온도가 높아지면 이러한 vibration이 더 커지게 된다. 즉, lattice scattering에 의한 mobility degradation은 온도 상승에 의해 커진다고 할 수 있다. 이 scattering mechanism은 주로 고온, High E-field의 regime에서 mobility degradation factor로 작용하게 된다.<br><br>

&nbsp; &nbsp; &nbsp; &nbsp;두 번째로는 Coulomb (Impurity) Scattering이 있다. Impurity들은 electron이나 hole을 내 놓은 후, 고정된 ion의 형태로 존재한다. 따라서 carrier들이 움직이게 되면 이러한 ion들과의 coulomb force에 의해 mobility가. 낮아지게 된다. 이러한 impurity scattering은 lattice scattering과 다르게 온도가 높아질수록 mobility 감소가 줄어들게 된다. 이 mechanism은 주로 저온, Low E-field, low inversion charge의 regime에서 mobility degradation factor로 작용하게 된다.<br>

<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/sm2.png "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/gyulab/sm3.png "image"){:.profile}
<br>

&nbsp; &nbsp; &nbsp; &nbsp;먼저 Phonon scattering을 없애는 방법을 알아보도록 하자. 2단원에서 알아보았던 FinFET과 같은 multigate device를 사용하면 phonon scattering을 현저하게 낮출 수 있다. 그 원리는 바로 multigate device의 특성인 ‘volume inversion’ 에 있다. Si의 두께가 20nm 수준으로 감소하고 multigate structure가 되면서, 2개의 potential well 사이의 interaction이 발생한다. 이 condition에서, inversion layer가 silicon과 dielectric의 계면에만 발생하는 것이 아니라 거의 silicon 전체에 형성이 되게 된다. 즉, Si/Dielectric interface에 더 이상 carrier들이 묶여있지 않고 Silicon 전체로 퍼져나가게 되는 것이다. 이는 oxide와 interface charge와의 scattering을 줄여줌으로써, phonon scattering을 줄여주고, mobility enhancement를 가져오게 된다. 사실 volume inversion이 mobility를 enhance하는 방법이고, phonon scattering reduction은 volume inversion에 따른 결과이기는 하나, 서로 연관성이 있다는 것을 보여주기 위해 여기에 작성하게 되었다.
<br>
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/sm4.png "image"){:.profile}
<br>
<br>
&nbsp; &nbsp; &nbsp; &nbsp;Volume inversion으로 phonon scattering을 낮추는 방법에 대한 단점으로는, device의 크기가 수 원자 크기 정도로 작아짐으로써 발생하는 양자역학적 문제들이 발생한다. Volume inversion이 발생하는 곳 부근에서 Quantum Confinement Effect가 발생하여, Bandgap이 커지는 효과가 일어나게 되고 (Blue-shift 같은 현상), threshold voltage가 커지게 된다. [34][35] 이와 같은 양자역학적인 문제들을 추가로 고려하여 공정 조건을 다시 설계해야 한다는 단점이 있다. 또한, Volume inversion을 obtain하기 위해서는 multi-gate structure를 만들어야 하는데, 이러한 structure를 만들기 위해서는 Planar structure보다 공정의 복잡도가 올라가 cost가 올라간다는 단점이 있다.<br><br>

&nbsp; &nbsp; &nbsp; &nbsp;Coulomb Scattering은 앞서 discuss 했던 것 과 같이, inversion charge concentration과 E-field의 세기가 낮은 region에서 main scattering mechanism으로 작용한다. 이러한 coulomb scattering을 낮추기 위해서는 High-K dielectric을 사용하면 된다. High-K dielectric을 사용할 경우, SiO2와 비교하였을 때 coulomb perturbation potential이 감소하는 효과를 가져온다는 것을 실험적으로 알 수 있었다. [1] 이 방법에 대한 단점은 1.3.절에서 알아보았던 High-K dielectric의 problem인 mobility degradation과 Fermi level pinning등과 동일하며, 이러한 문제들은 HK/MG process로 대부분 해결할 수 있었다.
<br>

![alt text]({{ site.baseurl }}/assets/images/gyulab/sm5.png "image"){:.profile}
<br>
&nbsp; &nbsp; &nbsp; &nbsp;Scattering reduction으로 mobility를 증가시킨 비교적 최신 연구도 찾을 수 있었다. 2018년, N. Huo, et al. 연구진들은 CVD-grown monolayer MoS2 FET에서 ALD process를 이용한 Hafnia (HfO2) cover를 통해서 coulomb scattering과 phonon scattering을 억제함으로서 훨씬 더 improved 된 mobility를 얻을 수 있었다고 한다. [2]


<br>
<br>
[Reference]<br>
[1] Jiménez-Molinos, F., Gámiz, F., & Donetti, L. (2008). Coulomb scattering in high-κ gate stack silicon-on-insulator metal-oxide-semiconductor field effect transistors. Journal of Applied Physics, 104(6), 063704. doi:10.1063/1.2975993 <br>
[2] Huo, N., Yang, Y., Wu, Y.-N., Zhang, X.-G., Pantelides, S. T., & Konstantatos, G. (2018). High carrier mobility in monolayer CVD-grown MoS2 through phonon suppression. Nanoscale, 10(31), 15071–15077.doi:10.1039/c8nr04416c 
