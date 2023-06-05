---
layout: post
title:  "Automatic detection of center frequency of 8PSK modulated signal"
date:   2023-06-02T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---
![alt text]({{ site.baseurl }}/assets/images/general_research/57.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;In the realm of digital communication systems, 8PSK (8-Phase Shift Keying) modulation plays a crucial role in achieving higher data rates and improved spectral efficiency. 8PSK (8-Phase Shift Keying) is a digital modulation scheme used in communication systems to transmit data over radio frequency or optical channels. It is an extension of the binary PSK modulation, where instead of two phase states (0 and π), it uses eight equally spaced phase states around a unit circle (0, π/4, π/2, 3π/4, π, 5π/4, 3π/2, and 7π/4). The eight possible phase states allow for encoding a larger number of bits per symbol compared to binary PSK modulation. This results in higher data transmission rates and increased spectral efficiency. Its utilization can be found in satellite communication, digital broadcasting, wireless LANs, mobile communication systems, and digital modems, among others.<br>

![alt text]({{ site.baseurl }}/assets/images/general_research/54.PNG "image"){:.profile}<br>

&nbsp;&nbsp;&nbsp;&nbsp;Detecting the highly accurate center frequency of an 8PSK signal is essential for precise demodulation and reliable data recovery. It enables accurate phase detection, symbol recovery, and carrier frequency estimation. It also ensures optimal interference rejection, spectral efficiency, and compatibility with receiving systems. Deviations in the center frequency can lead to errors, degraded performance, and interference with neighboring signals. Overall, accurate center frequency detection is vital for achieving high-quality demodulation and maximizing the effectiveness of 8PSK communication systems.<br>
&nbsp;&nbsp;&nbsp;&nbsp;To accurately detect the center frequency of an 8PSK signal, a careful analysis of the 8th power spectrum becomes essential. This article explores the process of identifying two distinct peaks in the 8th power spectrum and leveraging their spacing to determine the center frequency of an 8PSK signal.<br>

# Understanding the 8th Power Spectrum
&nbsp;&nbsp;&nbsp;&nbsp;The power spectrum is a valuable tool for analyzing the spectral characteristics of a signal. In the context of 8PSK signals, the 8th power spectrum exhibits distinct peaks that provide key insights into the underlying modulation scheme. Each peak in the 8th power spectrum corresponds to the frequency associated with a specific phase state of the 8PSK signal. By examining these peaks, we can infer important information about the signal, including the center frequency. For instance, the 4th power spectrum of a QPSK signal below reveals a multitude of distinct peaks, each corresponding to a specific phase state of the modulation scheme.<br>

![alt text]({{ site.baseurl }}/assets/images/general_research/55.PNG "image"){:.profile}<br>

&nbsp;&nbsp;&nbsp;&nbsp;Theoretically, when observing the m-th power spectrum of an m-ary PSK modulated signal, such as the 8th power spectrum of 8PSK or the 4th power spectrum of 4PSK, we expect to observe distinct peaks, as illustrated in the following figure:<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/58.PNG "image"){:.profile}<br>

# Identifying the Distinct Peaks
&nbsp;&nbsp;&nbsp;&nbsp;To detect the center frequency of an 8PSK signal, we focus on identifying two distinct peaks in the 8th power spectrum. These peaks are separated by a distance equal to twice the baud rate of the signal. By leveraging this property, we can accurately determine the center frequency. The baud rate represents the rate at which symbols are transmitted, and its doubling in this context ensures that we capture the phase transitions necessary for reliable detection.<br>

![alt text]({{ site.baseurl }}/assets/images/general_research/59.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;To track the carrier one first needs to at least roughly estimate the frequency of the signal. This is easy for MSK and OQPSK at least. It consists of producing a nonlinearity and then performing a FFT (Fast Fourier Transform). Simply squaring the audio signal and taking the FFT results in the following figure. As can be seen there is no peak where the carrier is. However, there are two peaks evenly spaced around where the carrier would be. Taking the average of the two peaks you obtain the carrier frequency of the transmission. Here, the difference between the two peaks are 10500bps, hence the baud rate is 5250 baud.



&nbsp;&nbsp;&nbsp;&nbsp;However, The spectrum of an 8PSK signal is more challenging to detect distinct peaks compared to BPSK and QPSK due to the increased number of phase states, which results in a higher density of peaks and a greater likelihood of overlapping frequencies in the power spectrum, as you can see in the below figure:<br>

![alt text]({{ site.baseurl }}/assets/images/general_research/56.PNG "image"){:.profile}<br>

&nbsp;&nbsp;&nbsp;&nbsp;Due to the lack of clear peak identification, manually selecting peaks in the spectrum of an 8PSK signal is nearly impossible. To overcome this challenge, it is crucial to focus on identifying relatively distinct peaks that are separated by a distance equal to twice the baud rate of the signal. This approach ensures reliable detection of the desired peaks in the spectrum.<br>


# Calculating the Center Frequency
&nbsp;&nbsp;&nbsp;&nbsp;Once the two distinct peaks in the 8th power spectrum are identified by program, we can calculate the center frequency of the 8PSK signal. The center frequency is determined by finding the middle point between the frequencies associated with the two peaks. This approach leverages the fact that the two peaks are evenly spaced around the center frequency.<br>


# Impairments in Digital Communication
<b><a href="https://www.gaussianwaves.com/2013/11/symbol-timing-recovery-for-qpsk-digital-modulations/">Symbol Timing Recovery for QPSK</a></b>: This article will help you a lot to comprehend the contents below.<br>

&nbsp;&nbsp;&nbsp;&nbsp;Demodulating a PSK (Phase Shift Keying) signal involves several steps, including matched filtering, symbol timing synchronization, carrier frequency synchronization, carrier phase synchronization, and equalization. Each step plays a crucial role in extracting the transmitted information accurately. Let's elaborate on each of these steps:<br>

1. Matched Filtering:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Matched filtering is the first step in demodulating a PSK signal. It involves convolving the received signal with a matched filter that has a response matched to the shape of the transmitted pulse. Matched filtering helps improve the signal-to-noise ratio and enhances the detection of the symbols.<br>

2. Symbol Timing Synchronization:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Symbol timing synchronization is essential for accurately sampling the received signal at the symbol boundaries. It involves estimating the optimal sampling instants to correctly demodulate the symbols. Timing synchronization ensures that each symbol is sampled precisely, minimizing timing errors and improving the overall demodulation performance.<br>

![alt text]({{ site.baseurl }}/assets/images/general_research/60.PNG "image"){:.profile}<br>

3. Carrier Frequency Synchronization:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Carrier frequency synchronization is necessary to compensate for any frequency offset between the received signal and the local oscillator at the receiver. By estimating and correcting the frequency offset, carrier frequency synchronization ensures that the receiver is operating at the correct frequency, allowing for accurate demodulation of the PSK signal.<br>

4. Carrier Phase Synchronization:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Carrier phase synchronization involves estimating and compensating for any phase offset between the received signal and the local oscillator. Accurate carrier phase synchronization is crucial because PSK modulation relies on precise phase differences between symbols. By aligning the carrier phase, the receiver can correctly decode the symbol information embedded in the phase shifts.<br>

5. Equalization:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Equalization is performed to combat the effects of channel distortion, such as multipath fading and intersymbol interference. It aims to restore the received signal to its original form by compensating for the channel-induced distortions. Equalization techniques help mitigate the adverse effects of the channel and improve the accuracy of symbol demodulation.<br>

&nbsp;&nbsp;&nbsp;&nbsp;By going through these steps of matched filtering, symbol timing synchronization, carrier frequency synchronization, carrier phase synchronization, and equalization, the demodulation process for a PSK signal becomes robust and reliable. Each step addresses specific challenges introduced by the channel and ensures accurate recovery of the transmitted information.<br>

Here is the example code to accomplish above impairment steps:
<script src="https://gist.github.com/gyulab/707ee779e53743116ba0d7f58ebef64f.js"></script>

# Detecting Center Frequency of 8PSK
&nbsp;&nbsp;&nbsp;&nbsp;I have implemented MATLAB codes to perform the aforementioned task, allowing for the accurate identification of relatively distinct peaks in the spectrum of an 8PSK signal based on the specified criteria.<br>
<script src="https://gist.github.com/gyulab/c7ff0970a9d326dca8c5e629ac5122e2.js"></script>

# Application and Importance
&nbsp;&nbsp;&nbsp;&nbsp;Accurate detection of the center frequency in an 8PSK signal holds significant implications in various communication applications. In satellite communication systems, it allows for optimal frequency allocation and spectrum management, ensuring efficient and reliable data transmission. In digital broadcasting, identifying the center frequency enables precise channel tuning and reception. Additionally, in wireless LANs and mobile communication systems, detecting the center frequency of 8PSK signals facilitates efficient data transmission, enabling faster and more reliable wireless connectivity.<br>

# Conclusion
&nbsp;&nbsp;&nbsp;&nbsp;Detecting the center frequency of an 8PSK signal is a crucial step in various communication systems. By analyzing the 8th power spectrum and identifying two distinct peaks with a spacing equal to twice the baud rate, we can accurately determine the center frequency. This approach allows for optimal frequency allocation, spectral efficiency, and reliable data transmission in applications ranging from satellite communication to wireless networks. Understanding the intricacies of the 8th power spectrum and its role in center frequency detection empowers engineers and researchers in their pursuit of efficient and robust communication systems.<br>

# References
1. Tatu, S. & Moldovan, E. & Brehm, Gailon & Wu, Ke & Bosisio, Renato. (2002). Ka-band direct digital receiver. Microwave Theory and Techniques, IEEE Transactions on. 50. 2436 - 2442. 10.1109/TMTT.2002.804646. 
2. Kolumban, Geza & Krebesz, Tamas & Lau, Francis. (2012). Theory and Application of Software Defined Electronics: Design Concepts for the Next Generation of Telecommunications and Measurement Systems. IEEE Circuits and Systems Magazine - IEEE CIRCUITS SYST MAG. 12. 8-34. 10.1109/MCAS.2012.2193435. 
3. https://www.mathworks.com/help/comm/ug/modulate-and-demodulate-8-psk-signal.html
4. https://www.eecs.umich.edu/courses/eecs555/lect06.pdf
5. https://core.ac.uk/reader/42776140
6. https://jontio.zapto.org/hda1/oqpsk.html
