---
layout: post
title:  "Problems and Solutions for the High-K Materials"
date:   2020-06-18T14:28:52-05:00
author: Gyujun Jeong
categories: Academics
---

<br>
&nbsp;&nbsp;&nbsp;&nbsp;이전 포스팅까지 알아본 것과 같이, 같은 장점이 있는 High-K dielectric도 다양한 이유로 인해 사용에 어려움이 있었다. 대표적으로 다음과 같은 문제점들이 있었고, 자세한 내용은 후술하도록 한다.

<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/pk1.PNG "image"){:.profile}
<br>

1.	Silicon interface 상태 문제:  Silicon 위에 High-K layer deposition을 진행하게 되면, 그 high-K layer가 실리콘을 제대로 passivate하지 못하게 된다. 따라서 interface trap 및 charge가 많아지게 되고 performance degradation이 발생하게 된다.<br><br>
2.	Silicon의 Metal에 의한Contamination 발생: High-K layer는 metal oxide가 많기 때문에, metal atom들이 silicon내부에 deep trap을 형성하여 문제를 야기하였다.<br><br>
3.	당시 사용하던 Gate electrode였던 Poly-Si와의 호환성 문제:  당시 65nm technology node에서는 polysilicon gate를 사용하였는데, 45nm 공정으로 넘어가면서 High-K dielectric을 사용하려고 하니 다양한 side effect들이 발생하였다. 대표적으로, Poly-Si gate와 High-K dielectric을 같이 사용하게 되면 work-function 문제 (Fermi Level Pinning)가 발생하였다. <br><br>
4.	Device reliability문제:  Metal oxide는 SiO2에 비해서 bandgap이 작기 때문에,  dielectric layer가 high electric field 또는radiation에 노출되었을 때, 전자가 쉽게 큰 에너지를 받아 high-k layer의 bandgap을 넘게 되어 의도치 않은 current flow가 발생한다.<br><br>
5.	Process에서의 문제: Metal oxide 공정 시 여러 화학 물질과 공정 환경에서 SiO2보다 상대적으로 잘 견디지 못한다. 이는 기존 공정과의 호환성에 문제가 되었다. SiO2를 대체할 High-K material은 기존의 deposition, etching, annealing, cleaning 공정을 모두 견딜 수 있는 물질이어야 한다.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;이러한 문제들이 SiO2를 High-K 물질로 대체하는 데 큰 걸림돌이 되었다. 이 중 poly-Si gate와 high-k dielectric을 같이 사용할 때 발생하는 문제에 대해서 먼저 다루어보고자 한다.

<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/pk2.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;Polysilicon을 gate로 사용한 MOS device의 경우, polysilicon을 doping하여 gate의 work function를 바꾸는데, 만약 high-k dielectric을 oxide로 사용하였을 경우 gate의 work function이 쉽게 바뀌지 않게 된다. 이러한 현상의 가장 큰 이유는 ‘Fermi Level Pinning’이다. 일반적으로 Metal electrode 쪽의 Fermi level에 의해서 work function이 변하는데, poly-Si와High-K가 붙게 되면, Silicon-Metal(Hf) 결합에 의해 polysilicon의 work function이 Silicon의 Conduction Band 근처에 고정이 된다. 그 결과, threshold voltage가 작동 가능한 범위를 벗어나 매우 커지는 문제가 발생하게 된다. 예를 들어, 일반적인 NMOS의 Vth는 0.25~0.6V, PMOS의 Vth는 -0.25~-0.6V 범위에서 형성이 되어야 하는데, High-K와 Poly-Si를 같이 쓰게 되면, PMOS의 경우 Vth가 -1.4V 이하로 내려가게 되면서 Vth가 너무 커져서 channel 부분의 doping modification만으로 조절이 어려워진다. 이러한 문제는 CMOS에 high-k를 oxide로 사용하는데 큰 장애가 되었다. 이를 해결하기 위해서 gate 전극을 metal gate electrode 로 교체하게 된다. 자세한 내용은 조금 더 밑에서 다루어보고자 한다. 
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;High-K layer를 사용하면서 발생된 또 하나의 주요 문제로 Mobility degradation이 있다. 아래의 그림과 같이 공정 중에 발생하는 다양한 요인으로 인해서 때문에 carrier의 mobility가 감소하여 performance가 하락하게 된다.
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/pk3.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;위의 그림에서 poly-Si gate와 high-k layer 사이의 fixed charge에 의한 요인과 phase-separation crystallization에 의해서 발생하는 mobility degradation의 정도는 다음 Figure 와 같다. Fixed charge로 인한 degradation은 낮은 E-field region에서 매우 심각하게 나타난다. 추가적으로, Phase-separation crystallization이란 amorphous인 high-k layer 중 어느 부분이 crystallization되어 유전율 값이 변해 성능에 변화를 주는 요인을 뜻한다. Ion implantation 단원에서 배웠듯이, amorphous layer에서는 결정체에서 일어나는channeling effect가 덜 일어나게 된다. 만약 crystallization이 되면, electron이나 Boron같은 작은 물질들은 결정 구조 사이로 이동이 가능하게 되는 Channeling effect가 일어나게 되어, 물질이 저장할 수 있는 전하량으로 생각할 수 있는 유전율의 변화가 발생하게 되는 것이다.
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/pk4.PNG "image"){:.profile}
<br>

&nbsp;&nbsp;&nbsp;&nbsp;현재 사용되는 gate dielectric 물질을 HfO2 based dielectric이다. 이 물질은 k=22정도의 큰 유전율을 갖고 있고, thermal stability가 좋다. 다양한 기술들을 통해 위에서 언급한 high-k layer의 단점들을 완화시켜 poly-Si가 아닌 metal gate와 함께 사용하여 1세대 high-k layer에 사용될 수 있었다. 하지만, High-K layer를 1nm 이하 (sub-1nm EOT process) 로 줄이는 데는 다시 다양한 문제가 발생하였다. 
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;우선 gate 와 HfO2 사이의 oxygen diffusion으로 인한 interface quality degradation 문제와 gate work function 문제가 있다. 이러한 HfO2와 Si 사이에서 생기는 다양한 문제를 해결하기 위해서는 interfacial layer인 SiON (Silicon Oxynitride) 을 HfO2와 Si 사이 삽입해 줘야 한다. 하지만 이 layer의 삽입으로 인해 전체적인 EOT가 증가하여 mobility가 떨어진다. 기술이 발전함에 따라 EOT를 줄여야 하지만 그러기 위해서는 이 interfacial layer를 줄여야 하는데, 얇은 interfacial layer를 더 줄이게 되면 또 문제가 발생하는 악순환이 반복되게 된다. 또한, interfacial layer와 HfO2 또는 Si 사이에서 생길 수 있는 interface state, fixed charge, dipole 등이 interface quality를 나쁘게 한다. 위와 같은 다양한 문제들이 EOT를 줄이는데 큰 걸림돌이 되었다. 이를 해결하기 위해서 HfO2를 대신하여 Nitrided Hf Silicate를 사용하는 방법이 있다. 이에 관련하여서는 조금 뒤에서 다루어보고자 한다.


<br><br><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;위에서 언급한 대부분의 High-K dielectric의 문제점은 Gate 물질을 Poly-Si에서 Metal로 바꾸면서 해결되었다. 먼저 metal gate를 사용함으로써 해결된 문제점들을 알아보고자 한다.
<br><br>
1.	Gate Depletion<br>
Poly-silicon gate는 기본적으로 silicon이기 때문에 high-doping을 했다고 할지라도 depletion이 생길 수 밖에 없다. 이러한 gate의 depletion은 EOT를 높이고 inversion region의 capacitance를 줄이는 단점으로 작용한다. Metal gate를 사용하게 되면 이러한 depletion을 없앨 수 있다.<br><br>
2.	Dopant Penetration<br>
Poly-Si gate의 경우 high-doping으로 인해 dopant들이 oxide나 silicon으로 penetrate할 수 있다. 이렇게 되면 device의 performance degradation을 초래하게 되는데, metal gate를 사용하면 이러한 문제를 해결할 수 있다.<br><br>
3.	Low Resistance<br>
Polysilicon은 기본적으로 반도체이기 때문에, 아무리 high-doping을 했다고 할지라도 metal에 비해서는 resistance가 높을 수 밖에 없다. 따라서 metal gate를 사용하면 저항을 현저하게 줄일 수 있다.<br><br>
4.	Fermi Level Pinning<br>
앞서 보았던 것과 같이, Poly-Si/High-k stack에서는 Si-Hf bonding에 의해 work function modification이 발생한다. 하지만 metal gate를 사용하면 gate work function이 고정되어 잘 조절할 수 없는 fermi level pinning 문제 또한 해결 가능하다.<br><br>
5.	Surface Phonon based Mobility Degradation<br>
Poly-Si와 다르게 metal은 carrier (electron)이 매우 abundant하기 때문에, 이러한 carrier들이 surface phonon에 의한 vibration을 막을 수 있다. 다시 말해,  channel region의 mobility degradation을 막을 수 있다. 아래 Figure 18을 보게 되면 mobility가 향상되었음을 보여준다. 여기서의 metal gate는 TiN이다.

<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/pk6.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;이러한 Metal Gate를 deposit하기 위해서, 우리는 앞서 보았던 High-K deposition 공정과는 또 다른 공정을 필요로 한다. 금속은 annealing 등 열처리 과정에 민감하게 반응하기 때문에, High-K dielectric을 deposit하는 것 뿐만 아니라, Metal Gate의 deposit 방법도 달라져야 하는 overcome method가 필요하기 때문이다. High K dielectric과 Metal Gate를 같이 사용하는 공정을 HK/MG Process라고 하며, 이러한process에 대해서 간단하게 다루어보고자 한다. HK/MG process는 metal gate의 공정 순서에 따라서 gate first와 gate last로 나눌 수 있다. 
<br>
<br>
1.	Gate First HK/MG Process<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/pk7.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;Gate First HK/MG는 먼저 기판 위에 high-k layer를 증착시키고, 그 위에 metal gate와 poly-Si를 증착시킨다. 여기서 metal gate는 1.3.절에서 이야기했던 것처럼, 절연막과의 좋은 contact property와  gate work-function을 결정짓기 위해 최대한 정확한 deposition이 필요하다. 좋은 quality로 증착을 위해서 느린 속도로 deposition을 해야 하는데, 수율(yield)을 높이기 위해서 일정 높이까지만 metal gate를 증착시키고 나머지 gate는 poly-Si로 빠르게 채운다. 그 다음 Source/Drain region을 형성하기 위한 ion implantation과 annealing 공정을 진행한다.
<br>
<br>
2.	Gate last HK/MG Process
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/pk8.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;Gate-first process의 경우, metal의 melting point가 낮아 gate공정이 끝난 후 annealing을 진행할 때metal gate에 손상이 발생하는 치명적인 단점이 존재하였다. 따라서 이를 해결하기 위해 처음 annealing 전 dummy gate, 즉 실제 쓰일 gate를 올리기 전에 gate의 위치를 잡아주는 역할을 하는 가짜 게이트를 먼저 만들고 annealing을 한 후, 실제로 쓰일 gate를 마지막에 처리함으로써 thermal stress를 받지 않은 상태의 pure metal을 사용하는 방법이 나오게 되었다. 이러한 process를 gate last process라고 한다. 이 공정은 matal gate를 교체하는 공정이라고 해서 RMG (Replacement Metal Gate) 공정이라고도 불린다. Gate last HK/MG는 먼저 기판 위에 high-k layer를 증착시킨 후, dummy gate (poly-Si)를 증착시킨다. 그 뒤, source/drain 형성을 위한 ion implantation 공정과 annealing을 진행한다. 이후 dummy gate를 없애고, metal gate를 증착시킨 뒤 텅스텐(W)으로 남은 부분을 채운다. 이 방법은 gate first 공정보다 process step이 복잡하고 비싸지만, dummy gate에 thermal stress가 가해지기 때문에 thermal budget을 줄일 수 있고, 더 나은 quality의 metal gate를 얻을 수 있다. 또한, Work function controllability와 carrier mobility를 얻을 수 있다는 장점이 있다.
<br>
<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/pk9.PNG "image"){:.profile}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;하지만 Gate last process만으로는 45nm에서 32nm node로 넘어가기에는 역부족이었다.  High-K last process가 나오게 된 배경은 gate last process가 나왔던 배경과 유사하다. Gate last process의 경우 high-k를 deposit시킨 상태에서 annealing 과정을 거치고 그 후 gate를 올렸으므로 high-k 부분에 thermal stress가 가해지고 팽창이 일어나므로 EOT가 커져 carrier penetration이 발생하였다. High-k last 공정을 통해, EOT를 줄일 수 있었고, 이에 따른 defect도 줄일 수 있게 되었다.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;Gate/High K last process는 substrate 위에 poly-Si를 증착시킨 후, S/D 형성을 위한 etching 후 ion implantation과 annealing을 진행한다. 이후 poly-Si를 없애고, high-k layer와 metal gate를 증착시킨 후 텅스텐으로 남은 부분을 채운다. 이렇게 하면 S/D formation 이후 high-k lager와 metal gate를 deposit하기 때문에, 앞서 설명한 두 공정보다 더 좋은 quality의 high-k layer 형성이 가능하다. 하지만 process complexity와 cost가 상당히 올라가게 되는 단점이 있다.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;HK/MG process는 2007년 Intel에서 45nm 공정에 처음 도입하였고, TSMC와 삼성과 같은 파운드리 회사들이 그 뒤를 이어 32nm 공정에 도입하였다. 초기 TSMC를 제외한 삼성과 파운드리 회사들은 Gate first 방식을 채택하였는데, 공정 과정이 단순하고 cost가 싼 장점이 있었다. 하지만 좋지 않은 quality로 인해 leakage current가 발생하게 되었다. TSMC와 Intel은 gate last HK/MG 공정을 채택하였는데, quality는 좋지만, 비싸고 복잡한 공정 등이 단점으로 떠올랐다. 현재는 삼성을 비롯한 다양한 파운드리 회사들도 gate last process 공정을 채택하고 있다.<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;추가적으로 우리가 1.3.절에서 다루어 본 것과 같이, sub-1nm EOT process에서는 tunneling current를 방지하기 위해서 SiON interface layer를 사용했어야 했는데, 이렇게 layer를 넣게 되면 또 다시 EOT가 증가하는 악순환이 반복되었다. 이를 해결하기 위하여 Hafnium Silicate를 고온(약 섭씨 1100도)의 Nitride ambient에서 PNA(Post Nitridation Annealing) 공정을 통해 적은 leakage current를 가지는 0.81nm-EOT HfSiON Gate dielectric (Nitrided Hafnium Silicate) 를 사용할 수 있게 되었다. (Seiji, 2006) 아래 Figure 22를 보게 되면, 0.81nm의 아주 얇은 EOT에서도 0.7A/cm2정도의 낮은 leakage current와 SiO2 2nm EOT와 비슷한 mobility를 가진다는 것을 알 수 있다.

<br>
![alt text]({{ site.baseurl }}/assets/images/gyulab/pk10.PNG "image"){:.profile}
<br>
<br>
<br>


[Reference]<br>
[1] Lee, B. H., Oh, J., Tseng, H. H., Jammy, R., & Huff, H. (2006). Gate stack technology for nanoscale devices. Materials Today, 9(6), 32–40. doi:10.1016/s1369-<br>
[2] Bersuker, G., Park, C. S., Barnett, J., Lysaght, P. S., Kirsch, P. D., Young, C. D., … Ryan, J. T. (2006). The effect of interfacial layer properties on the performance of Hf-based gate stack devices. Journal of Applied Physics, 100(9), 094108.doi:10.1063/1.2362905 <br>
[3] Inoue, T., Yamamoto, Y., Koyama, S., Suzuki, S., & Ueda, Y. (1990). Epitaxial growth of CeO2layers on silicon. Applied Physics Letters, 56(14), 1332–1333.doi:10.1063/1.103202 
<br>[4] S. A. Campbell et al., "MOSFET transistors fabricated with high permitivity TiO/sub 2/ dielectrics," in IEEE Transactions on Electron Devices, vol. 44, no. 1, pp. 104-109, Jan. 1997, doi: 10.1109/16.554800.
<br>[5] Wilk, G. D., Wallace, R. M., & Anthony, J. M. (2001). High-κ gate dielectrics: Current status and materials properties considerations. Journal of Applied Physics, 89(10), 5243–5275. doi:10.1063/1.1361065 
<br>[6] Lee, B. H., Jeon, Y., Zawadzki, K., Qi, W.-J., & Lee, J. (1999). Effects of interfacial layer growth on the electrical characteristics of thin titanium oxide films on silicon. Applied Physics Letters, 74(21), 3143–3145.doi:10.1063/1.124089 
<br>[7] Hiratani, M., Saito, S., Shimamoto, Y., & Torii, K. (2002). Effective Electron Mobility Reduced by Remote Charge Scattering in High-κ Gate Stacks. Japanese Journal of Applied Physics, 41(Part 1, No. 7A), 4521–4522. doi:10.1143/jjap.41.4521 
<br>[8] M. T. Bohr et al., “The High-K solution”, IEEE Spectr., vol. 44. no. 10. pp. 29-35. 2007.
<br>[9] R. Chau, S. Datta, M. Doczy, B. Doyle, J. Kavalieros and M. Metz, "High-/spl kappa//metal-gate stack and its MOSFET characteristics," in IEEE Electron Device Letters, vol. 25, no. 6, pp. 408-410, June 2004, doi: 10.1109/LED.2004.828570.
<br>[10] Auth, C. (2008). 45nm high-k + metal gate strain-enhanced CMOS transistors. 2008 IEEE Custom Integrated Circuits Conference.doi:10.1109/cicc.2008.4672101 
<br>[11] H. Ohta et al., "High performance 30 nm gate bulk CMOS for 45 nm node with /spl Sigma/-shaped SiGe-SD," IEEE InternationalElectron Devices Meeting, 2005. IEDM Technical Digest., Washington, DC, 2005, pp. 4 pp.-240, doi: 10.1109/IEDM.2005.1609316.
<br>[12] Mukhopadhyay, A. B., Musgrave, C. B., & Sanz, J. F. (2008). Atomic Layer Deposition of Hafnium Oxide from Hafnium Chloride and Water. Journal of the American Chemical Society, 130(36), 11996–12006.doi:10.1021/ja801616u 
<br>[13] Chang J. (2005) High-k Gate Dielectric Deposition Technologies. In: Huff H., Gilmer D. (eds) High Dielectric Constant Materials. Springer Series in Advanced Microelectronics, vol 16. Springer, Berlin, Heidelberg
