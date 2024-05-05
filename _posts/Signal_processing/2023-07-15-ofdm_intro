---
layout: post
title:  "Introduction of OFDM (Orthogonal Frequency Division Multiplexing)"
date:   2023-07-15T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---

![alt text]({{ site.baseurl }}/assets/images/general_research/61.PNG "image"){:.profile}<br>
Orthogonal Frequency Division Multiplexing (OFDM) is a multi-carrier modulation technique that has significantly impacted modern data transmission. By distributing data bits across multiple subcarriers, OFDM transforms communication methods, effectively addressing challenges such as multipath propagation.<br>

# Advantages of OFDM
![alt text]({{ site.baseurl }}/assets/images/general_research/62.PNG "image"){:.profile}<br>
OFDM effectively addresses the challenge of multipath propagation, a common issue in wireless communication. Unlike traditional single-carrier systems, where multipath signals can lead to Intersymbol Interference (ISI), OFDM's use of orthogonal subcarriers prevents such problems.<br>
The division of data into parallel subcarriers allows OFDM to handle multipath propagation adeptly. Even if some subcarriers experience fading or interference due to multipath effects, the overall impact on the data stream remains minimal. This inherent capability eliminates ISI, ensuring data accuracy and communication reliability.<br>

Moreover, OFDM offers enhanced spectral efficiency and interference resilience. Its ability to divide a broad frequency band into numerous narrow subcarriers facilitates efficient spectrum utilization, enabling higher data rates and accommodating multiple users simultaneously.<br>
OFDM's capacity to mitigate multipath effects and provide robust data transmission has solidified its role as a pivotal technology in modern wireless communication systems. As we delve deeper into the mechanics of OFDM, we will uncover the principles that underlie its transformative impact on data transmission.<br>

# Orthogonality: The Foundation of OFDM's Efficiency
Orthogonal Frequency Division Multiplexing (OFDM) derives its name from a fundamental concept in mathematics and signal processing—orthogonality. This concept plays a key role in OFDM's ability to efficiently transmit data across multiple carriers, enabling robust and high-throughput communication.<br>
The orthogonality of subcarriers in OFDM brings several key advantages:<br>
- Interference Mitigation: Since the carriers are orthogonal, they do not overlap in frequency, reducing the chances of intercarrier interference. This is particularly advantageous in environments with multipath propagation, as it helps maintain data integrity and communication quality.

- Efficient Spectrum Utilization: The absence of interference enables carriers to be closely spaced without causing mutual interference. This efficient packing of carriers within the available spectrum enhances the spectral efficiency of OFDM, allowing for higher data rates and accommodating multiple users or data streams simultaneously.

- Simplified Equalization: Orthogonality simplifies the process of equalization at the receiver end. Equalization is the technique used to correct distortions and phase shifts that can occur during transmission. In OFDM, since carriers do not interfere with each other, the equalization process becomes less complex and more accurate.


# OFDM Modulation and Demodulation: Unveiling the FFT Process
![alt text]({{ site.baseurl }}/assets/images/general_research/63.PNG "image"){:.profile}<br>
Orthogonal Frequency Division Multiplexing (OFDM) relies on a process of modulation and demodulation, driven by Fast Fourier Transforms (FFTs). <br>
1. Frequency Domain Encoding: At the heart of OFDM lies data coding in the frequency domain. Each data bit, denoted as b0, b1, b2, and so forth up to bN-1, is transformed into a symbol. These symbols are then sent through an Inverse Fast Fourier Transform (IFFT), transitioning them from the frequency domain to the time domain.
2. IFFT: A Transformative Conversion: The IFFT, or Inverse Fast Fourier Transform yields the frequency-to-time conversion. One symbol at a time, the IFFT processes the encoded data, yielding a stream of time-domain data points: d0, d1, d2, d3, and so on up to dN-1.
3. Parallel to Serial Conversion: To ready the time-domain data for transmission, a Parallel to Serial (P/S) converter takes the individual time-domain samples and arranges them sequentially. This stream of time-domain samples, d0, d1, d2, and so forth, forms the core of the signal to be transmitted.
4. Transmission and Reception: The transmit phase involves sending the time-domain samples of one symbol, d0, d1, d2, and so on. At the receiving end, the time-domain samples, d0’, d1’, and others, are collected.
5. Serial to Parallel Conversion: For further processing, the Serial to Parallel (S/P) converter takes the received time-domain samples, d0’, d1’, d2’, and arranges them in parallel.
6. Demodulation through FFT: The final step in the journey is demodulation. Here, the Fast Fourier Transform (FFT) steps in. It processes the parallel time-domain samples, d0’, d1’, d2’, and others, and performs a rapid conversion back to the frequency domain.
7. Finding the Encoded Data: As a result of the FFT, the encoded data bits resurface: b0’, b1’, b2’, and onwards up to bN-1’. These bits hold the key to the original information, revealing the encoded data in the frequency domain.


# Integrating the Cyclic Prefix: Countering Time Dispersion

![alt text]({{ site.baseurl }}/assets/images/general_research/64.PNG "image"){:.profile}<br>
An essential aspect of Orthogonal Frequency Division Multiplexing (OFDM) is the utilization of a "cyclic prefix" (CP). This element plays a crucial role in mitigating the effects of time dispersion within the communication channel.<br>
The cyclic prefix acts as a time-domain buffer that enhances robustness in the presence of varying propagation delays and channel complexities. During symbol transitions, the cyclic prefix introduces time guards, counteracting transient distortions through overlap-save conversion.<br>
Two primary functions highlight the importance of the cyclic prefix:
- Transient Management: The cyclic prefix accommodates the residual decay of the previous symbol, avoiding interference with the current symbol.
- Interference Suppression: The cyclic prefix also prevents the initial transient from affecting the ongoing symbol, ensuring uninterrupted communication.

# Challenges and Solutions in OFDM: Carrier Frequency Offset (CFO) and Peak-to-Average Power Ratio (PAPR)
Orthogonal Frequency Division Multiplexing (OFDM) revolutionized data transmission, but it isn't immune to challenges. Two critical issues are Carrier Frequency Offset (CFO) and Peak-to-Average Power Ratio (PAPR). Here, we delve into these hurdles and the strategies that address them.

![alt text]({{ site.baseurl }}/assets/images/general_research/65.PNG "image"){:.profile}<br>
1. Carrier Frequency Offset (CFO): CFO, or deviations in carrier frequency, can distort OFDM's orthogonality. As a result, subcarriers lose their perfect alignment, causing intercarrier interference. The culprit is often Doppler shifts due to relative motion between transmitter and receiver, or local oscillator inaccuracies.<br>
Introducing known pilot or training symbols within the OFDM frame enables accurate estimation of the CFO. By observing the shifts in these symbols, the receiver can calculate and compensate for the carrier frequency offset, thereby restoring orthogonality.
![alt text]({{ site.baseurl }}/assets/images/general_research/66.PNG "image"){:.profile}<br>
2. Peak-to-Average Power Ratio (PAPR): PAPR refers to the disparity between the highest and average power levels of an OFDM signal. High PAPR strains power amplifiers, leading to inefficiency and distortion, affecting overall performance.
Solutions for PAPR are discussed below:<br>
- Clipping: Truncate the signal peaks beyond a certain threshold. While effective, this method may introduce in-band distortion and out-of-band emissions.
- Peak Windowing: Apply a windowing function to the time-domain signal to distribute power more evenly. This technique reduces PAPR but might compromise bit error rate (BER) performance.
- Forward Error Correction (FEC) Coding: Encoding data with FEC adds redundancy, mitigating the impact of PAPR-induced errors.
- Scrambling: Scramble the data prior to transmission, spreading out the high-amplitude peaks. This strategy reduces the likelihood of extreme peaks.

# References
1. http://bwrcs.eecs.berkeley.edu/Classes/EE225C/Lectures/Lec16_ofdm.pdf
2. https://courses.engr.illinois.edu/ece463/fa2018/Lectures/ECE463_fa18_Lec9.pdf
3. https://rfmw.em.keysight.com/wireless/helpfiles/89600b/webhelp/subsystems/wlan-ofdm/content/ofdm_basicprinciplesoverview.htm
