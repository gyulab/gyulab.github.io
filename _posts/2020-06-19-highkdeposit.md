---
layout: post
title:  "High-K Deposition Methods"
date:   2020-06-16T14:26:52-05:00
author: Gyujun Jeong
categories: Academics
---

<br>
&nbsp;&nbsp;&nbsp;&nbsp;기존의 oxide인 SiO2를 형성하기 위해서는, 열처리를 통해 oxide를 기르는 것과 같이 간단한 방법으로 절연막을 형성할 수 있었다. 하지만 High-K material을 이용하게 되면서, 기본적으로 High-k 물질은 SiO2와 다르게Silicon으로 이루어진 물질이 아니기 때문에, deposition에 각별한 주의가 필요하게 된다. 우수한 전기적 특성을 가지기 위해 거의 완벽에 가까운 thickness uniformity와 interfacial, bulk property들이 요구된다. 이러한 요구 조건을 만족하는 것은 oxidation보다는 deposition이 더 적합하며, 그 종류에는 수업시간에 배운 ALD, CVD, PEALD, PECVD, PVD부터 Molecular Beam Epitaxy, Ion-Beam Assisted Deposition, Sol-gel deposition 등이 있다. 그 중, 현재 High-K Material의 deposition에서 가장 많이 사용하는 ALD (Atomic layer deposition)에 대해 자세히 다룰 것이고, CVD, PVD 및 다른 deposition에 대해서는 간단하게 알아보도록 할 것이다.

<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/dm1.PNG "image"){:.profile}
<br>
1. ALD Process<br>
&nbsp;&nbsp;&nbsp;&nbsp;ALD process에서 가장 중요한 점은, CVD와는 다르게 precursor와 reactant gas를 같은 시간에 넣지 않는 것이다. 각 공정 사이에 잔여 precursor나 reactant gas를 purge를 통해 원천적으로 둘의 reaction을 막기 때문에, gas phase reaction, 즉 homogeneous reaction을 막음으로써 ideal한 film uniformity를 얻을 수 있다. 또 하나의 ALD의 중요한 점은 바로 Surface-Self limited reaction이라는 점이다. 만약 모든 surface reaction이 끝났다면, surface에서의 reaction은 추가적으로 일어나지 않는다. 공정 사이클을 반복하면 한 cycle당 gas들은 mono, 혹은 submono (e.g., 60% film thickness)을 형성하게 된다.
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;ALD Process의 장점은 매우 다양하다. 먼저 thickness control을 수 Å 단위로 할 수 있어 Gate dielectric deposition에 아주 적합하다. 또한, ALD 공정에서 필요한 온도가 섭씨 400도 이하 (front-end 뿐만 아니라 backend process도 가능한 온도) 이므로, metal component가 있는 high-k deposition에 매우 적합하다. Step coverage, wafer uniformity 또한 CVD와 PVD에 비해 매우 우수하다. 하지만 impurity의 측면에서는 ALD의 precursor가 carbon을 incorporate하기 때문에 단점으로 작용할 수 있다.
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;이제 High-K dielectric의 ALD process 순서에 대해서 알아보도록 하자. HfO2 deposition을 위한 Precursor에는 수업시간에 배운 Al2O3 Deposition의 TMA (Tri-methyl aluminum)과 비슷하게 TEMAH (Tetrakis(ethylmethylamino) Hafnium) 를 사용할 수도 있지만, 위의 Figure 7에서는 HfCl4, 즉 Metal Halide precursor를 사용하였다. HfO2 deposition에 쓰일 수 있는 precursor의 종류는 아주 다양하다. 
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;이후 기판의 reactive site와 반응하면서, 기판에 Precursor가 붙게 된다. 어느 정도 reaction이 되면, surface self-limiting에 의해 더 이상 반응하지 않는 지점이 발생하고, growth rate saturation이 발생한다. 하지만 여기서 만약 homogeneous reaction이 발생하면 growth rate에 slope가 생기게 되고, 이러한 CVD-like behavior가 deposition의 quality를 결정하는 factor로 작용한다. Homogeneous reaction은 film uniformity를 저해시키고 impurity를 발생시키므로 최대한 suppress하는 것이 중요하다. 이후 excess precursor와 byproduct를 Argon이나 Nitrogen으로 purge를 시킨다. 다음으로 reactant인 H2O 등을 precursor로 covered된 표면에 주입을 한 후 다시 purge를 하면, 위의 그림과 같이 Hf monolayer가 증착되게 된다.
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/dm2.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;ALD process에서 눈여겨 보아야 할 대표적인 issue에는process temperature가 있다. 오른쪽의 figure는 process temperature에 따른 growth rate를 나타낸다. 먼저 activation energy limited 부분을 보면, process 온도가 너무 낮으면 surface의 reaction rate가 낮아져 growth rate가 낮아진다. 이 문제를 해결하기 위해서는 PE-ALD 방법을 사용하는데, Thermal energy뿐만 아니라 plasma enhanced가 되면 추가적인 에너지를 가지게 되면서, 낮은 온도에서도 precursor가 activated되어 reaction을 가능하게 할 수 있다. (Plasma를 통해 radical을 형성하여 ligand를 없애거나 surface를 activate할 수 있다.) Condensation limited는 practically하게는 잘 일어나지 않는 현상이다. 반대로 Process temperature를 너무 높이게 되면, desorption과 decomposition limited process문제가 나타나게 된다. desorption limited는 분해가 dominant한 region이라 growth rate가 감소한다. Decomposition limited는 CVD-like film deposition을 가져오기 때문에, suppressed되어야하는 상황이다. 따라서 위의 diagram에서 ALD process window region 안에서 process를 진행해야 perfect한 self-limiting이 가능하게 되어 최적화된 ALD process를 진행할 수 있다.
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/dm3.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;실제로 ALD를 진행하면, 그림과 같이 처음 수 cycle에서는 deposition이 되지 않는 영역이 있는데, 이 부분을 incubation cycle이라고 부르며, wafer가 OH radical 등의 reactive site를 만들기 위한 initialization region이라고 생각할 수 있다.
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;ALD process는 특유의 uniformity 및 step coverage와 같은 우수한 품질로 인해, High-K dielectric deposition 뿐만 아니라 DRAM, Flash 및 AR가 중요한 입체 구조 트랜지스터인 FinFET, GAA와 같은 최신 공정에서 Key Technique로 작용하고 있다.
<br>
<br>
2.	CVD (Chemical Vapor Deposition) Process<br>
&nbsp;&nbsp;&nbsp;&nbsp;High-k material의 CVD의 경우, metal을 포함하는 precursor가 직접 가열된  실리콘의 표면과 반응하여 decomposition과 deposition이 이루어진다. ALD에서 사용된 대부분의 chemical을 사용할 수 있으나, HFCl4와 같은 metal halide의 경우에는 decomposition temperature가 너무 높아 CVD process에서는 잘 쓰지 않는다. 또한, CVD에서는temperature gradient 등으로 인해 flow rate 등이 좌우되기 때문에, ALD에 비해 상대적으로 좋은uniformity를 가질 수 없다는 점을 고려해야 한다. 그럼에도 CVD Process를 사용하는 가장 큰 이유는 Mass production이 가능하다는 것이다. ALD의 경우 layer-by-layer로 deposition하기 때문에, throughput이 좋지 않다. 하지만 CVD의 경우 (특히 LPCVD의 경우) 많은 양의 deposition을 한꺼번에 처리할 수 있기 때문에 throughput이 우수하다. 
<br><br>&nbsp;&nbsp;&nbsp;&nbsp;기본적으로 CVD에는 AP (Atmospheric Pressure), LP (Low Pressure), PE(Plasma Enhanced), HDPCVD(High Density Plasma)가 있으나, High-k material에서의 CVD는 보통 LPCVD나 PECVD Process를 이용한다. LPCVD와 PECVD를 이용하는 이유에 대해 알아보고자 한다. CVD process는 sequential한 process를 가지므로, 제일 느린 rate가 deposition rate를 결정한다. 따라서CVD process는 다음과 같은 두 가지의 reaction regime을 가진다. 고온에서는 Mass-transport limited, 저온에서는 surface reaction limited reaction이다. Mass transport rate는 flow rate와 연관되어 있고, surface reaction rate는 temperature uniformity와 관계가 있는데, 실제로는 flux rate를 uniform하게 만드는 것이 훨씬 어렵기 때문에, process point를 보통 surface reaction rate limited로 맞추게 된다. LPCVD의 경우, high temperature이지만 low pressure이기 때문에, transport point가 바뀌기 때문에 Surface reaction limited mode이다. 따라서 step coverage 및 uniformity가 우수하여, LPCVD가 APCVD보다 deposition에 유리하다. 또한 PECVD의 경우 PEALD와 마찬가지로 상대적으로 더 낮은 온도에서 deposition을 가능하게 하기 때문에, 보통 metal을 포함하는 High-K deposition에 유리하다.
<br>
<br>
3.	PVD Process<br>
&nbsp;&nbsp;&nbsp;&nbsp;PVD는 evaporation이나 sputtering 등 기판에 물리적 방법으로 physical vapor를 deposit시키는 방법이다. PVD process는 precursor type (volatile or stable)에 구애받지 않고 deposition이 가능하며, 상온에서 고온까지 넓은 범위의 기판 온도에서 모두 가능하므로, thermal limit가 없는 것 또한 장점이다. 보통 Evaporation의 경우 정확도가 상당히 떨어지기 때문에, 주로 sputtering deposition 방법을 사용한다.
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/dm4.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;먼저 Sputtering gas (Ar plasma)에 bias를 걸어 주어 sputtering target인 metal에 bombarding을 진행한다. 우리는 HfO2와 같은 dielectric을 sputtering해야 하기 때문에, argon atom에 에너지를 주기 위해 RF input을 가해야 한다. Ar plasma (양이온)은 상대적으로 무겁기 때문에 RF signal에도 거의 움직이지 않지만, electron particle들은 상대적으로 RF signal을 따르게 되며, 이로 인한 Potential difference가 target dielectric에 형성된다. 이를 통해 target dielectric이 기판에 deposit될 수 있게 된다.
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;여태까지 보았던 High-K dielectric deposition 방법의 operation condition과 dielectric의 quality를 비교해 보도록 하자.
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/dm5.PNG "image"){:.profile}
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;각각의 process마다 장단점이 있기 때문에 어떠한 공정이 가장 좋다고 할 수는 없다. 엔지니어들은 각자의 공정 환경 및 만들고자 하는 소자의 종류에 따라 다양한 공정 조건을 선택한다. 예를 들어, CVD의 경우 ALD에 비해 높은 온도와 낮은 dielectric quality를 가지지만, throughput의 관점에서는 매우 우수하다. 또한, PVD의 경우 room temperature에서 process가 가능하다는 장점이 있다.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;Electrical performance 측면에서는 ALD가 대체로 우수하다고 할 수 있다. 20 이상의 높은 dielectric constant와 얇은 interfacial layer 두께 (tIL), 낮은 EOT와 interfacial state(Dit), leakage current과 높은 electron mobility를 가진다. 이는 현재 대부분의 High-K dielectric deposition에서 ALD를 사용하는 이유이기도 하다.
