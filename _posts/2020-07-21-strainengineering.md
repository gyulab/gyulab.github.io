---
layout: post
title:  "Strain Engineering: Enhancing Carrier Mobility"
date:   2020-07-21T14:28:52-05:00
author: Gyujun Jeong
categories: Academics
---
![alt text]({{ site.baseurl }}/assets/images/gyulab/se0.jpeg "image"){:.profile}
<br>
&nbsp; &nbsp; &nbsp; &nbsp;사람들은 항상 더 빠른 chip을 얻기 위해 노력하였다. Backend process에서 배웠듯이, 비록 Aluminum에 비해서 Copper를 실리콘 공정에 사용하기가 매우 어려웠지만, 더 빠른 칩을 위해서 Damascene 공법을 통해 결국 Copper를 사용할 수 있게 만들었다. 이처럼, 소자의 성능을 향상시키기 위해 많은 노력을 기울여왔다. 그 중 mobility를 향상시키면, drain current가 향상이 되고, chip의 속도가 향상된다는 점에서, mobility enhancement에 대해서 많은 연구가 이루어졌다. 이러한 mobility enhancement 에 대한 방법과, 이 방법으로 나오게 된 새로운 문제들에 대하여 알아볼 것이다.
<br><br>
&nbsp; &nbsp; &nbsp; &nbsp;Strain engineering는 실리콘 기반의 mobility enhancement 방법 중 가장 널리 쓰이는 방법이다. Device에 intentional한 stress를 가해 carrier의 mobility를 향상시켜 on current를 증가시키려는 시도라고 생각할 수 있다. Stress를 가한다는 의미는, carrier들이 이동하는 어떤 공간에 특정한 압력 등의 효과를 주어 carrier가 더 빨리 이동하도록 하게 함을 말한다. 격자 구조를 약간 눌러서, 늘린 방향으로 힘을 받아 mobility를 향상시킨다고 생각할 수 있다. 
<br><br>
&nbsp; &nbsp; &nbsp; &nbsp;물리전자에서, 우리는 carrier mobility를 Drude’s Model를 이용해 μ=qτ/m^* 과 같이 간단하게 구해 보았다. Strain engineering으로 carrier의 scattering time τ와 effective mass m^* 모두 improve할 수 있다. 외부의 Stress를 받은 Si 결정의 lattice constant가 바뀌면서 Bandgap structure도 변하게 되고, 이에 따라 DOS와 m^*이 바뀌게 된다. 
<br><br>
&nbsp; &nbsp; &nbsp; &nbsp;이러한 stress 효과는 크게 두 가지로 분류할 수 있는데, CMOS 전체, 즉 NMOS와 PMOS 모두에게 carrier mobility 향상을 불러오도록 하는 것과 electron/hole 각각의 mobility 향상을 불러오도록 하는 것이다. 전자를 biaxial stress, 후자를 uniaxial stress라고 부른다.
<br><br>
&nbsp; &nbsp; &nbsp; &nbsp;먼저 biaxial stress방법은〖Si〗_(1-x) 〖Ge〗_x를 사용하는 것이다. 이 방법은 저마늄의carrier mobility는 Si에 비해 매우 높다는 특성을 이용한 것이다. Electron mobility의 경우 3배, Hole의 경우 4배 더 높다. 따라서, Si와 alloy하게 혼합하여 쓸 경우 두 종류의 carrier 모두 mobility를 향상시킬 수 있다. 하지만 biaxial한 방법은 높은 electric field를 야기하기 때문에, PMOS의 hole mobility의 감소를 불러 일으킨다. 또한 biaxial한 방법은 lattice mismatch, dislocation과 같은 문제점을 가지고 있기 때문에 application에 어려움이 있다.
<br><br>
&nbsp; &nbsp; &nbsp; &nbsp;Uniaxial stress 방법은 두 가지로 분류된다. 하나는 NMOS에 가하는 tensile stress (잡아 당기기) 이고, 하나는 PMOS에 가하는 compressive stress (누르기)이다. 


<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/se1.png "image"){:.profile}
<br>

<br>
&nbsp; &nbsp; &nbsp; &nbsp;PMOS에 가해지는 compressive stress란 Si에 비해 원자와 격자 구조의 크기가 큰 Ge를 혼합하여 source, drain에 사용하는 것으로, channel이 양 방향으로 줄어드는 stress를 가해준다. 원자들 간의 공간이 줄어들기 때문에, PMOS의 hole들의 mobility가 향상되는 효과를 나타낸다. 이를 eSiGe (embedded-SiGe) 공정이라고 부른다. 또한 SiGe를 쓰게 되면 hole의 Schottky barrier를 낮출 수 있어 전류를 더 잘 흐르게 만들 수 있었다. 〖Si〗_(1-x) 〖Ge〗_x alloy의 lattice constant는 다음과 같이 superposition과 같은 형태로 간단하게 구할 수 있다.
<br>
α_(〖Si〗_(1-x) 〖Ge〗_x )=(1-x) α_Si+xα_Ge
<br>
&nbsp; &nbsp; &nbsp; &nbsp;Ge의 lattice constant는 5.646Å이고, Si는 이보다 작은5.431Å를 가지고 있어서, 둘을 alloy로 만들면 Si에 비해서 격자상수가 커지게 된다.
<br>


<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/se2.png "image"){:.profile}
<br>

<br>
&nbsp; &nbsp; &nbsp; &nbsp;SiGe와 Si의 lattice mismatch는 channel의 compressive stress를 주며, 이러한 x방향의 compressive stress는 hole의 mobility를 향상시킨다.
<br><br>
&nbsp; &nbsp; &nbsp; &nbsp;반대로NMOS에 가해지는 tensile stress에 대해 알아보자면, Si에 비해 원자와 격자 구조의 크기가 작은 Carbon을 혼합하여 source, drain에 사용함으로써 채널이 양 방향으로 늘어날 수 있는 stress를 가해주는 것을 의미한다. 원자들 간의 공간이 늘어나기 때문에 NMOS의 electron들이 움직이는 mobility가 향상되는 효과를 나타낸다. 이 공정을 eSiC (embedded-SiC) 공정이라고 부른다.
<br><br>
&nbsp; &nbsp; &nbsp; &nbsp;하지만 mobility만을 올린다고 해서 device의 performance가 좋아지지는 않는다. 새로운 solution은 반드시 새로운 problem을 만들게 되는 BJ’s Law는 여기서도 적용이 된다. 실제로 SiGe S/D stressor가 적용된 device로 실험한 결과, 높은 온도에서 실험을 하였을 때 performance가 크게 감소하였다고 한다. 이는 lattice mismatch로 인해 Channel 계면 및 Source/Drain zone surface에 interface trap과 state가 온도가 올라감에 따라 reliability가 감소하여 device가 작동하기 어려울 정도로 증가하였다고 생각할 수 있다. [27]
<br><br>
&nbsp; &nbsp; &nbsp; &nbsp;물론 이를 해결하기 위한 solution 또한 존재한다. Problem이 존재하면 반드시 solution도 존재하기 때문이다. 방법에 대해서 간단히 설명하자면, Si와 SiGe 사이의 부분에서 dislocation이 발생하는 것이므로, 이 SiGe Buffer layer를 기점으로SiGe alloy 부분을 계속 epitaxy로 기르게 되면, Quasi-crystal region을 지나 Relaxed 된 SiGe를 얻을 수 있게 된다. 이를 virtual substrate로 활용하게 되면, low defect의 stressed wafer를 얻을 수 있게 된다. [28] <br><br>


<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/se3.png "image"){:.profile}
<br>
<br>
&nbsp; &nbsp; &nbsp; &nbsp;위의 두 가지의 대표적인 공정 방법 이외에도 SMT (Stress Memorization Technology)과 sSOI (Strained Silicon-On-Insulator) 방법 등 stress enginnering에는 매우 다양한 방법이 있다.
<br><br>
&nbsp; &nbsp; &nbsp; &nbsp;SMT의 경우 크게 Poly-Si gate에 strain을 가하는 것과 Source/Drain에 가하는 두 가지 방법이 있는데, 여기서는 Gate로 stress를 가하는 것을 알아 볼 것이다. 이 방법은 Polysilicon이 annealing 공정에서 팽창되는 효과를 사용하는 것이다. Annealing을 하면 Gate가 팽창이 되고, 이렇게 팽창된 gate는 channel을 눌러 채널에 tensile stress를 가해주는 효과를 얻을 수 있다. 마치 치약 통(Channel)을 손(Gate)으로 꽉 누리면 치약(Carrier)이 나오는 것과 같은 원리라고 생각할 수 있다. 팽창되는 압력이 채널 부분에 전달이 되면서 stress 효과를 주게 되며 이 효과를 NMOS에 사용할 수 있었다. 하지만 이 방법의 가장 치명적인 단점은 metal gate에 적용을 할 수 없다는 것이다. 앞서 discuss한 바와 같이, technology node가 낮아지면서 HK/MG process를 적용해야 하는데, Metal Gate의 경우 고온에서 annealing을 할 수 없기 때문에 사용할 수 없게 되었다.

![alt text]({{ site.baseurl }}/assets/images/gyulab/se4.png "image"){:.profile}
<br>
