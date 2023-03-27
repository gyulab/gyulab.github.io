---
layout: post
title:  "LoRa Signal and CSS Modulation for IoT device communication"
date:   2022-10-14T14:28:52-05:00
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

- By the way, what does the word ‘Chirp’ mean?<br>
&nbsp;&nbsp;&nbsp;&nbsp;Oxford Languages: typically of a small bird, utter a short, sharp, high-pitched sound<br>
&nbsp;&nbsp;&nbsp;&nbsp;In engineering: Compressed High Intensity Radar Pulse<br>

- Key parameter: Spreading Factor (SF)
&nbsp;&nbsp;&nbsp;&nbsp;SF(Spreading Factor): Bits per symbol (5<SF<13)<br>
&nbsp;&nbsp;&nbsp;&nbsp;Suppose we transmit the siganl with consistnt BW..<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Low SF: Short symbol duration -> Tough Identification -> High SNR required<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;High SF: Long symbol duration -> Easy identification -> Low SNR affordable<br>
&nbsp;&nbsp;&nbsp;&nbsp;i.e., Symbol duration increases -> Energy per bit increases -> Remote transmission available<br>
<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/3.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;Read the following link to elaborate idea of SF: <a href="https://www.rfwireless-world.com/Terminology/What-is-difference-between-Chip-and-Chirp-in-LoRaWAN.html">What is difference between Chip and Chirp in LoRaWAN, LoRa?</a><br>
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
