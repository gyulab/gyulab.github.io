---
layout: post
title:  "FinFET Fabrication Process"
date:   2020-06-19T14:28:52-05:00
author: Gyujun Jeong
categories: Academics
---

<br>
&nbsp;&nbsp;&nbsp;&nbsp;일반적으로 device의 크기가 작아질수록 성능이 향상되고 소비전력과 cost 또한 감소한다. 하지만 소자의 크기가 20nm 이하 수준으로 매우 작아짐에 따라 source-drain 간 physical distance가 짧아지고, 이는 곧 device의 gate가 channel에 대한 controllability를 잃게 되는 원인이 되었다. MOSFET의 채널 길이가 매우 짧아져 2D planar structure의 MOS로는 더 이상 leakage current나 drain current를 control하기 어려워졌다. 따라서 gate를 여러 개 사용하여 channel에 흐르는 전류를 더 잘 제어할 수 있는 방법을 연구하기 시작하였다. 그에 따라, 채널 길이가 짧은 만큼 비례하여 증가하는 Short Channel Effect를 막기 위하여 기존의 MOS와 다른 3D structure의 소자들이 개발되기 시작하였다. 22nm 구조를 위한 device structure 중 가장 유명한 것은 바로 FinFET이다. FinFET의 이름은 device의 channel 구조가 물고기의 지느러미 (fin) 처럼 형성되어 있다는 점에서 붙여진 이름이다. 

<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/ff1.png "image"){:.profile}
<br> 

&nbsp;&nbsp;&nbsp;&nbsp;FinFET 소자는 크게 Bulk-FinFET과 SOI-FinFET으로 구분할 수 있다. SOI랑 Silicon-on-insulator의 약자로, Silicon-insulator-silicon와 같이 layered substrate를 사용함으로써 parasitic capacitance를 줄여주고device간의 isolation을 향상시켜주는 역할을 한다. 그림을 보게 되면 SOI-FinFET은 Oxide 위에 fin이 만들어져 substrate와 완벽하게 isolated 되어 있지만, Bulk-FinFET은 fin이 substrate bulk와 연결되어 있다는 것을 알 수 있다. Bulk의 performance 자체는 좋지만, SOI는 Vth나 소자의 on 속도와 관련 있는 Subthreshold Swing 특성, 그리고 인접 device와의 isolation을 주기 때문에, SOI가 더 preferred된 FinFET이라고 할 수 있다. 하지만, SOI 기판의 특성으로 인하여 비용의 문제점과 채널의 역할을 하는 핀 부분과 실리콘 바디 부분이 oxide층으로 인하여 절연되어 있기 때문에, device 구동 시 채널의 열을 쉽게 방출하지 못하는 열전도 문제도 존재한다.
두 종류의 FinFET을 구분한 이유는 두 종류의 FinFET의 fabrication process flow에 약간의 차이가 있기 때문이다. 먼저 Bulk-FinFET의 공정에 대해서 알아본 후, SOI-FinFET 공정에 대해 알아보도록 하자. 
기본적으로, FinFET의 공정은 기존 2D MOSFET과 크게 다르지 않다. 하나의 Gate와 S, D을 만들면 된다. 하지만 차이점도 존재한다. MOS와의 차이점은 실리콘 기판 위에 3D 구조의 bar 모양 (Fin) 을 만들어야 한다. Gate 전극을 channel 근처에 감싸는 형태로 만들어서 drive current 특성을 향상시키고 leakage current를 감소시킬 수 있다.

<br>
<br>
- Bulk-FinFET Process Flow
 
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/ff2.png "image"){:.profile}
<br> 



1. Substrate & Lithography<br>
&nbsp;&nbsp;&nbsp;&nbsp;p-substrate 위에 Hard mask (e.g., Silicon Nitride)와 PR 패턴을 만들어 올린다. 하지만 실제 공정은 간단하지만은 않다. 솟아 오른 지느러미 모양의 채널인 핀을 만드는 과정에 있어서LER (Line Edge Roughness)과 같은 문제가 발생한다. 이는 핀의 패턴 형성을 위한 Lithography 공정 중 생기는 현상으로, 매우 짧은 핀을 만들 때 핀의 표면이 울퉁불퉁한 모양으로 형성되게 된다. 게다가 이 현상은 확률적으로 발생하는 현상(Stochastic process) 이라 같은 공정이라 할지라도 생산된 device 각각의 성능이 달라지는 문제점이 발생한다. 이러한 문제점은 나중에 device를 이용하여 회로를 구성할 때에 구성된 circuit이 정상적으로 작동하지 않게 될 수 있어 큰 문제가 될 수 있다. 
 
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/ff3.png "image"){:.profile}
<br> 

&nbsp;&nbsp;&nbsp;&nbsp;이러한 문제를 해소하기 위해, FinFET공정에서는 더 정교한 lithography를 요구한다. Fin Patterning에서 가장 중요한 technique는 Spacer Lithography (Double Patterning) 라고 할 수 있다. Double Patterning의 방법에는 LELE(Litho-Etch-Litho-Etch)와 SADP(Self-Aligned Double Patterning)가 있는데, SADP는 처음 기초 패턴을 한 번 형성한 후, 여러 번 etching을 통해 패턴을 미세화하는 작업이고, LELE는 Lithography와 etching을 번갈아 하면서 패턴을 2번 나누어서 그린다. LELE가 패턴을 2번 그릴 수 있으므로 더 정교하지만 비싸서 메모리에서는 주로 SADP를 사용한다. 10nm 공정에서는 SAQP(Quadraple-)과 LELELE로 더욱 미세화되었다.


<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/ff4.png "image"){:.profile}
<br> 

&nbsp;&nbsp;&nbsp;&nbsp;SADP 공정 방법에 대해서 조금 자세히 알아보고자 한다. 위의 Figure은 Spacer Lithography 방법을 나타낸다. 먼저 1장에서 보았던 Poly-Si Dummy Gate와 같이, 사용하지 않는 희생층(sacrificial layer)를 증착하고 patterning한다. 이후 Spacer를 만들기 위해 mask를 증착 후 etch-back을 하여 3번 모양처럼 만든다. 마지막으로 sacrificial layer를 etch를 통해 없앤다. (현재는SiO2 spacer를 표면에서 mobility가 좋아 step coverage가 우수한 TEOS를 활용한 ALD를 통해 형성한다.) 이 방법을 이전 페이지와 같이 여러 개의 fin을 통해 만들게 되면, n번째 lithography를 시행했을 때 2^n개의 line을 만들 수 있게 된다. Fin pitch 또한 pattern layer의 ½만큼의 값을 가지게 될 것이다. 즉, 이 방법을 통해 처음 lithography를 통해서 50nm 선폭을 만들고, 2번째 lithography를 통해 25nm의 선폭을 만들 수 있게 된 것이다.
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;이러한 spacer lithography 기술은 크게 2가지의 이점이 있다. 첫 번째로는 한 번의 lithography 과정을 통해 여러 개의 fin pitch를 만들 수 있다. 앞에서 언급했던 것과 같이, n번째 litho 공정을 하게 되면, 아래 Figure와 같이 2^n개의 line을 만들 수 있게 된다.
 
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/ff5.png "image"){:.profile}
<br> 

&nbsp;&nbsp;&nbsp;&nbsp;또 하나의 장점으로는 앞서 언급한 Fin Edge Roughness를 개선할 수 있다. 실험적으로Spacer Lithography의 표준편차가 기존의 conventional한 lithography보다 더 작기 때문이다. 앞서 보았듯이 Edge Roughness 현상은 Stochastic한 process여서, 표준편차를 줄임으로써 Edge의 Roughness함을 개선할 수 있었다.

 
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/ff6.png "image"){:.profile}
<br> 

&nbsp;&nbsp;&nbsp;&nbsp;특히 10나노급 FinFET 공정에서는, Lithography 장비 또한 기존의 KrF (λ=248nm,0.18um 공정 이상), ArF ( λ=193nm) 과 같은 light source보다 더 파장이 짧은 장비를 사용해야 한다. 더 미세한 그림을 그리기 위해서는 더 얇은 샤프를 사용해야 하는 것과 비슷하다고 생각할 수 있다. 예를 들어서, 삼성의 7nm 공정에서는 파장이 13.5nm인 네덜란드의ASML EUV 장비를 도입하였다.
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;20nm급 FinFET 공정에서는 ArF light source를 사용할 수 있는데, 이때 lithography 장비의 huge jump (ArF -> EUV)를 compensate하기 위해 Mask pattern을 살짝 더 크게 만들어서 corner diffraction을 고려해서 원하는 패턴을 새기는OPC(Optical Proximity Correction)나 더 나은 resolution을 얻기 위한 phase shifting 과 같은 mask engineering, 그리고 Resolution을 낮추어 더 미세한 pattern을 새기기 위해,
<br>Resolution R=k_1  λ/NA = k_1  λ/nsinα<br>
&nbsp;&nbsp;&nbsp;&nbsp;위 식에 의해 NA를 높일 수 있는 방법, 즉 굴절률이 높은 물에서 lithography을 진행하는 immersion lithography 과 같은 다양한 lithography engineering도 함께 사용된다.

2. Fin Etch<br>
&nbsp;&nbsp;&nbsp;&nbsp;Fin들은 고도의 anisotropic etch (Degree of anisotropy A=1), 즉 밑으로 directional한 etch를 통해 만들어진다. Isotropic etching이 발생하게 되면 직각 모양의 Fin을 제대로 만들 수 없게 된다. 따라서 LAM research에서 설명해주신 것과 같이, selectivity와 anisotropic 특성이 모두 높은 ion-enhanced etching 공정을 사용한다. Ion-enhanced etching의 성능이 좋은 이유는 SiF4를 plasma bombardment로 분해를 시켜 F etch가 enhance되며, surface에 damage를 주어서 Si가 깨지면서 불소와 결합을 용이하게 하여 reactivity를 높이기 때문이다.
SOI와 다르게 bulk wafer는 stop layer가 없기 때문에, etch process는 시간에 따라 이루어져야 한다. 즉, 저절로 limit되지 않는다. 22nm process에서의 일반적인 dimension criterion은 보통 fin의 넓이는 10~15nm(Channel length의 2/3 이하) 정도이고, 높이는 넓이의 2배 이상(Channel length의 4/3 이상) 정도로 만들어진다.
<br><br>&nbsp;&nbsp;&nbsp;&nbsp;22nm 세대에서는 파운드리 업체마다 핀의 모양이 약간씩 다름을 알 수 있었다. Intel은 Tapered Fin 모양이고, IBM과 TSMC는 Rectangular fin모양을 채택하였다. 인텔에서 Tapered Fin 모양을 채택한 이유는 Corner Effect를 개선하기 위함이다. Corner Effect란 gate가 채널을 감싸듯이 형성되기 때문에 Fin의 모퉁이 부분이 gate의 영향을 가장 크게 받는다고 생각할 수 있고, 이로 인해 gate전압이 threshold voltage에 미치지 않은 상태에서 코너에서만 미리 inversion layer가 발생하는 현상이다. 즉, 미리 형성된 inversion layer로 인하여 예상치 못할 때에 device가 켜지게 되어 소자의 OFF상태에 대한 특성을 악화시키게 된다. 따라서, 이러한 문제를 해결하기 위해 Intel에서는 Tapered 핀을 채택했다고 한다. 
<br><br>
3. Oxide Deposition<br>
&nbsp;&nbsp;&nbsp;&nbsp;
각각의 Fin을 서로 isolate하기 위해, High AR (Aspect Ratio)로 oxide를 deposit해야 한다.
<br><br>
4. Planarization<br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Oxide가 CMP (Chemical Mechanical Polishing)으로 planarized된다. 여기서 Hard mask가 stop layer로 작용한다.
<br><br>

5. Recess Etch<br>
&nbsp;&nbsp;&nbsp;&nbsp;
Fin의 측면을 isolation시키기 위해 oxide film을 recess하기 위한 etch가 진행된다.
<br><br>
6. Gate Oxide<br>
&nbsp;&nbsp;&nbsp;&nbsp;
Fin의 꼭대기 부분에 channel과 gate electrode의 isolation을 위해 gate oxide가 thermal oxidation (현재는 ALD)을 통해 deposit된다. 그림에는 나와있지 않지만, Fin이 여전히 oxide 하부에 있기 때문에, Fin 밑쪽 부분에 high-dose angled implant를 함으로써 dopant junction을 만들고, isolation을 마무리한다. 
<br><br>
7. Deposition of the Gate<br>
&nbsp;&nbsp;&nbsp;&nbsp;
마지막으로 n+-doped poly-Si layer (현재는 Metal Gate)를 Fin 위에 deposit한다. 이렇게 만들면 최대 3개의 gate가 channel을 감싸는 형태를 띄게 된다. (양 측면에 각각 1개씩, gate oxide의 두께에 따라 상단에 1개) Nitride laayer를 채널 위에 깔면 위쪽 게이트의 영향을 없앨 수 있다.
<br><br>
8. Source/Drain Doping (Raised S/D Epitaxy)<br>
&nbsp;&nbsp;&nbsp;&nbsp;
		Source와 Drain을 Fin에 Doping을 한다. 하지만 일반적으로 단순하게 doping을 하지는 않는다. Short Channel Effect를 충분히 억제하기 위해서는 FinFET의 핀을 채널의 길이보다 훨씬 좁게 만들어야 한다. 따라서, 만약 S/D를 Fin위에만 도핑을 하게 된다면, S와 D 또한 매우 얇게 되어 이 부분과 contact part가 접한 면적이 매우 작게 되고. 이 지점에서의 contact resistance가 매우 높게 됨을 알 수 있다. 접촉 저항이 높으면 흐르는 전류를 막는 힘이 높다고 볼 수 있고, 이는 device performance 하락을 의미한다. 이와 비슷한 예시로, Backend process에서 contact window의 크기가 작을 때, contact resistance가 커지면서 dominant하게 작용하는 것을 배웠다. 
		<br>
&nbsp;&nbsp;&nbsp;&nbsp;따라서, 이와 같은 문제를 해결하기 위해 RSD 구조가 탄생하게 되었다. RSD구조는 S/D가 기존의 핀 영역에만 국한된 것이 아니라, 이 S/D 부분만 epitaxy성장시켜 이 영역을 gate electrode과의 접촉 면적을 넓혀 접촉 저항을 감소시키는 효과를 낸다. 정확하게는 SEG (Selective Epitaxial Growth) 를 통해 dry etch로 Fin spacer만 제거한 뒤, S와 D만 성장시키는 것이다. 그 결과로, RSD구조가 형성되어 S/D contact resistance를 감소시킬 수 있다. 하지만 이렇게 튀어 나온 S/D region이 Gate electrode와 마주보게 되어parasitic capacitance가 추가적으로 나타나는 단점이 있다.

 
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/ff7.png "image"){:.profile}
<br> 

- SOI-FinFET Process Flow
 
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/ff8.png "image"){:.profile}
<br> 
&nbsp;&nbsp;&nbsp;&nbsp;그림을 보게 되면, Bulk-FinFET과 공정이 거의 유사하다는 것을 알 수 있다. 다만, Oxide layer가 wafer 사이에 끼여 있기 때문에, etch를 할 때 이 oxide가 stop layer의 역할을 하게 되면서, 기판과 Fin이 isolate되는 형태를 가진다는 것을 알 수 있다. FinFET의 isolation을 위해서, SOI 뿐만 아니라 N과 P-bulk 사이의 latch-up을 방지하기 위해 Shallow Trench Isolation (STI) 을 사용하기도 한다.
<br><br><br><br>
[Reference]
<br>[1] D. Hisamoto, T. Kaga, Y. Kawamoto and E. Takeda, "A fully depleted lean-channel transistor (DELTA)-a novel vertical ultra thin SOI MOSFET," International Technical Digest on Electron Devices Meeting, Washington, DC, USA, 1989, pp. 833-836, doi: 10.1109/IEDM.1989.74182.
<br>[2] Colinge, J.-P. (2011). FinFETs and other multi-gate transistors. New York: Springer. 
<br>[3] Victor Moroz, “Managing FinFET design and variability analysis,” EE Times India, 2012
<br>[4] Chang, L., Leong, M., Yang, M., Chang, L., Leong, M., & Yang, M. (2004). CMOS Circuit Performance Enhancement by Surface Orientation Optimization. IEEE Transactions on Electron Devices, 51(10), 1621–1627.doi:10.1109/ted.2004.834912 
<br>[5] P. Gaubert et al., "Relation Between the Mobility, 1/f Noise, and Channel Direction in MOSFETs Fabricated on (100) and (110) Silicon-Oriented Wafers, IEEE TED, 2010.
<br>[6] H. Nakamura et al., "Effects of Selecting Channel Direction in Improving Performance of Sub-100 nm MOSFETs Fabricated on (110) Surface Si Substrate, Japanese Journal of Applied Physics, 2004.
<br>[7] Hisayo S. Momose and Sadayuki Yoshitomi, "Effects of Si Channel Orientation on MOSFET Characteristics", Intl. Conference on MIEL, 2008.
<br>[8] Q. Ouyang et al., "Investigation of CMOS Devices with Embedded SiGe Source/Drain on Hybrid Orientation Substrates, VLSI Tech., 2005.
<br>[9] Seiji Inumiya et al 2006 Jpn. J. Appl. Phys. 45 2898 
<br>[10] T. Hook, “FinFET Isolation Approaches and Ramifications: Bulk vs. SOI,” FDSOI Workshop at Hsinchu, Taiwan, April, 2013. 
<br>[11] A. Yagishita, “Process and Device Technologies for FinFET and Its Alternative Devices,” IEEE SOI Conference Short Course, Foster City, CA, October, 2009. 
<br>[12] X. Sun, T.-J. King Liu, “Spacer Gate Lithography for Reduced Variability due to Line Edge Roughness,” IEEE Transactions on Semiconductor Manufacturing, Vol.23, No.2, pp.311-315, 2010. [26] Retrieved from EECS Berkeley Lecture Notes, 2013: 
https://inst.eecs.berkeley.edu/~ee290d/fa13/LectureNotes/Lecture7.pdf
