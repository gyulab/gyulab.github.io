---
layout: post
title:  "LoRa/CSS demodulation using de-chirp and FSK demodulation"
date:   2023-02-25T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---

![alt text]({{ site.baseurl }}/assets/images/general_research/37.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;Typically, LoRa detection is achieved in two steps: (i) first, the signal is de-chirped, then (ii) typical FSK demodulation is applied. De-chirping is achieved by mixing the received LoRa symbol with an inverted chirp (down-chirp) with no frequency offset. Since the demodulator has no prior knowledge of the transmit symbols, the de-chirping signal utilizes γ(0) = −B/2. Hence, the resulting signal is given as follows:<br>
<center>$$
s(t) = \sqrt{\frac{E_b}{N_0}} \sqrt{SF} \exp\left(j2\pi mδ_f t\right){}
$$
</center>
<br>
which is a typical M-ary FSK signal. Each symbol is now represented with a frequency shift of mδf, where δf is the bandwidth divided by the number of steps. In LoRa, it happens that this value is equivalent to the symbol rate as follows, δf = 1/T.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Now that the symbol is modulated using FSK, we can use conventional FSK demodulation methods to detect the symbol. Here, we utilized Non-coherent detection, attained by using energy detection in the frequency domain, where the maximum PSD peak location indicates the extracted symbol, formulated as follows:<br>
<center>$$
\hat{m}_{n-coh} = \frac{1}{δ_f}argmax[[R(f)] − 0.5]
$$
</center>
<br>
where R(f) is implemented as the fast Fourier transform (FFT) of the FSK signal, R(f) = FFT{r(t)}.
<br>
&nbsp;&nbsp;&nbsp;&nbsp;Based on this, we can implement the LoRaWan-like demodulator as follows. Note that this is simple snippets.<br>
<script src="https://gist.github.com/gyulab/5f53d28e4dc56e6195da004598742dbe.js"></script>

&nbsp;&nbsp;&nbsp;&nbsp;To de-chirp the signal, we start by cross-correlating it with a reference downchirp. This is done using <code>np.convolve</code> with mode <code>'valid'</code>. The index where the maximum correlation is achieved corresponds to the timing of the received data, which we obtain using <code>data_index = argmax(crosscorr_result)</code>. We then perform an FFT on each dechirped data and proceed with symbol-to-bit mapping as described earlier.

<br><br>

<b>[References]</b>
1. Liando, Jansen & Jg, Amalinda & Tengourtius, Agustinus & Li, Mo. (2019). Known and Unknown Facts of LoRa: Experiences from a Large-scale Measurement Study. ACM Transactions on Sensor Networks. 15. 1-35. 10.1145/3293534. 
2. Tapparel Joachim, Complete Reverse Engineering of LoRa PHY: https://www.epfl.ch/labs/tcl/wp-content/uploads/2020/02/Reverse_Eng_Report.pdf
3. Kosta Dakic et al, LoRa Signal Demodulation Using Deep Learning, a Time-Domain Approach
4. Zhenqiang Xu et al, From Demodulation to Decoding: Toward Complete LoRa PHY Understanding and Implementation
