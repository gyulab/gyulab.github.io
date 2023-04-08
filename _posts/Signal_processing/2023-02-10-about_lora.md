---
layout: post
title:  "LoRa PHY/MAC and CSS Modulation for IoT device communication"
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


<br>
<b>4. LoRaWAN MAC layer message formats (after decoding)</b><br>
![alt text]({{ site.baseurl }}/assets/images/general_research/48.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;LoRaWAN consists of End Devices and LoRa gateway. The gateway functions similar to base station of cellular network and End Devices function as mobile phones. Like other wireless network, transmission from LoRa Gateway module to End devices is known as "downlink" while transmissions from end devices to LoRa Gateway is known as "uplink".<br>

&nbsp;&nbsp;&nbsp;&nbsp;The LoRaWAN MAC layer performs following functions.<br>
- Establishes connection between MAC layer of peers (i.e. between LoRa Gateway and End device).
- The MAC layer handles transmission and reception of MAC commands and data from application layer. All the LoRaWAN MAC messages are identified based on MAC message types. This is shown in the table-1.
- MAC layer adds MHDR (MAC header) and MIC (message integrity code) at the beginning and end of MAC payload. MAC header is 1 octet in size and MIC is 4 octet in size. As mentioned MAC payload carries either MAC commands or data.
- The MAC layer data is used by PHY layer which incorporates Preamble, PHY header at the beginning and PHY header CRC and entire frame CRC at the end while constructing PHY payload at the transmit end. The reverse process i.e. stripping of preamble, PHY header and CRC is done at receive end. <br>

<b>LoRaWAN MAC commands</b><br>
Following table mentions list of LoRaWAN MAC commands with CID, transmitted by end device or gateway and their functions:<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/43.PNG "image"){:.profile}<br>

<b>LoRaWAN MAC message formats</b><br>
Following are the LoRaWAN MAC message formats at each protocol stack:<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/44.PNG "image"){:.profile}<br>

Following table mentions MAC message types with its 3 bit "MType field": <br>
![alt text]({{ site.baseurl }}/assets/images/general_research/45.PNG "image"){:.profile}<br>

- Join Request & Join Accept: These messages are used to establish connection between LoRa end device and Gateway.
- Confirmed Data Message: This message type requires to be acknowledged by its receiver.
- Unconfirmed Data Message: This message type does not require any acknowledgment.
- Proprietary : This message type is used to incorporate non standard message format functionalities.
- RFU : It means Reserved for Future Usage.

![alt text]({{ site.baseurl }}/assets/images/general_research/46.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;The figure-2 mentions LoRaWAN PHY payload and figure-3 mentioned contents of LoRaWAN MAC payload structure. For more information refer LoRaWAN specification about each of these fields.
![alt text]({{ site.baseurl }}/assets/images/general_research/47.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;MAC commands are used for network administration between server (i.e. Gateway) and end device. These commands are non visible to applications running in the LoRa server and end devices. A single data frame consists of one or multiple MAC commands(either piggybacked or transmitted as separate frame). MAC commands are segregated based on CID field of size 1 octet long. CID stands for Command IDentifier. These mac commands are used by end device or by gateway or by both.<br>

For example,<br>
- Value of 0x02 CID is used for 'LinkCheckReq' command (by End Device for transmission to Gateway)
- Value of 0x02 CID is also used for 'LinkCheckAns' (by Gateway for transmission to End device)
- Value of 0x03 CID is used by Gateway to transmit 'LinkADRReq' command.
- Value of 0x03 CID is also used by End device to transmit 'LinkADRAns' command.

<br><br>

<b>[References]</b>
1. Liando, Jansen & Jg, Amalinda & Tengourtius, Agustinus & Li, Mo. (2019). Known and Unknown Facts of LoRa: Experiences from a Large-scale Measurement Study. ACM Transactions on Sensor Networks. 15. 1-35. 10.1145/3293534. 
2. Tapparel Joachim, Complete Reverse Engineering of LoRa PHY: https://www.epfl.ch/labs/tcl/wp-content/uploads/2020/02/Reverse_Eng_Report.pdf
3. https://lora.readthedocs.io/en/latest/
4. Modulation, 2015. LoRa Modulation Basics, Rev.2., https://www.semtech.com/uploards/documents/an1200.22.pdf
5. Kosta Dakic et al, LoRa Signal Demodulation Using Deep Learning, a Time-Domain Approach
6. https://www.rfwireless-world.com/Tutorials/LoRaWAN-MAC-layer-inside.html
