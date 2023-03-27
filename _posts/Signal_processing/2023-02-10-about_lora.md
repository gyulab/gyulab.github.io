---
layout: post
title:  "LoRa PHY and Chirp Spread Spectrum(CSS) for IoT device communication"
date:   2023-02-10T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---
<b>1. Overview of LoRa</b><br>
![alt text]({{ site.baseurl }}/assets/images/general_research/1.PNG "image"){:.profile}<br>

&nbsp;&nbsp;&nbsp;&nbsp;LoRa (Long Range) is a proprietary wireless communication technology that is used for long-range communication and low-power, low-data-rate applications. LoRa is based on the spread spectrum technique and uses a frequency-hopping spread spectrum (FHSS) approach to transmit data over long distances.

<br><br>
<b>2. LoRa Modulation</b><br>
![alt text]({{ site.baseurl }}/assets/images/general_research/2.PNG "image"){:.profile}<br>
- Employs CSS(Chirp Spread Spectrum modulation)<br>
&nbsp;&nbsp;&nbsp;&nbsp; Chirp: Signals with constantly increasing(Up-) or decreasing(Down-) frequency<br>
&nbsp;&nbsp;&nbsp;&nbsp; Usually up-chirp utilized on LoRa Mod<br>

- Key parameter: Spreading Factor (SF)<br>
SF(Spreading Factor): Bits per symbol (5<SF<13)<br>
The SF satisfies SF = B · T , where B is bandwidth and T is chirp period. There are at most SF cyclically shifted up-chirp symbols given a specific SF. An up-chirp can be represented as the following formula:<br>
<center>$$
chirp(t; f0) = Aexp[j2πf0+ \frac{B}{2T} t)t]
$$</center>
<br>

The higher the SF, the longer the time on air, resulting in higher energy per bit.
<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/3.PNG "image"){:.profile}<br>


&nbsp;&nbsp;&nbsp;&nbsp;A LoRa symbol is a cyclic shift in frequency that is controlled by chirping rates represented with a spreading factor (SF), which determines the symbol’s spreading over time. A normalized up-chirp LoRa signal is expressed as follows:<br>
<center>$$
s(t) = \sqrt{\frac{E_b}{N_0}} \sqrt{SF} \exp\left(j2\pi[\gamma(m) + \beta t/2\right)_{mod B} - \frac{B}{2}]t.
$$
</center>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;The frequency offset, γ(m), and chirp slope, β, are obtained from m, the symbol being modulated, B, the transmission bandwidth, and Ts, the symbol time. The SF has a range of SF ∈ {6, 7, 8, 9, 10, 11, 12}, while the bandwidth B ∈ {125, 250, 500} kHz. The chirp rate has a slope of fhigh − flow = B/Ts.


![alt text]({{ site.baseurl }}/assets/images/general_research/36.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;An example of a LoRa chirp is shown in the above figure, which depicts the spectrogram of a LoRa symbol, highlighting the cyclic frequency shift. Each symbol represents M = 2^SF bits according to the LoRa modulation convention.<br>
&nbsp;&nbsp;&nbsp;&nbsp;With these knowledges, we can make chirp generator program for given domain as follows:<br>
<script src="https://gist.github.com/gyulab/c2c829eb765c6fb3e9e24549e11ad3c1.js"></script>


<br>
<b>3. LoRa Waveform Structure</b><br>
![alt text]({{ site.baseurl }}/assets/images/general_research/4.PNG "image"){:.profile}<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/5.PNG "image"){:.profile}<br>
- Preamble -> (Sync) -> SFD -> (Header) -> Data<br>
&nbsp;&nbsp;&nbsp;&nbsp;Preamble: Sync detection, i.e., Start point of the signal<br>
&nbsp;&nbsp;&nbsp;&nbsp;Sync: Frame sync, utilized after demodulation - bit analysis<br>
&nbsp;&nbsp;&nbsp;&nbsp;SFD(Start Frame Delimiter): Identifier, i.e., Delimiter, Down-chirp<br>
&nbsp;&nbsp;&nbsp;&nbsp;Data: CSS-Modulated data, varying start frequency <br>




<br><br>

<b>[References]</b>
1. Liando, Jansen & Jg, Amalinda & Tengourtius, Agustinus & Li, Mo. (2019). Known and Unknown Facts of LoRa: Experiences from a Large-scale Measurement Study. ACM Transactions on Sensor Networks. 15. 1-35. 10.1145/3293534. 
2. Tapparel Joachim, Complete Reverse Engineering of LoRa PHY: https://www.epfl.ch/labs/tcl/wp-content/uploads/2020/02/Reverse_Eng_Report.pdf
3. https://lora.readthedocs.io/en/latest/
4. Modulation, 2015. LoRa Modulation Basics, Rev.2., https://www.semtech.com/uploards/documents/an1200.22.pdf
5. Kosta Dakic et al, LoRa Signal Demodulation Using Deep Learning, a Time-Domain Approach
