---
layout: post
title: OFDM demodulation with synchronization techniques- CFO and Equalization
date:   2023-08-12T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---

![alt text]({{ site.baseurl }}/assets/images/general_research/68.PNG "image"){:.profile}<br>

OFDM systems are very sensitive towards  synchronization error. Synchronization of an OFDM signal is required to find the symbol timing and carrier frequency offset (CFO). Before demodulation of subcarriers, either from explicit training data or using cyclic prefix of the OFDM signal we can get synchronization at receiver. After demodulation of the OFDM subcarriers, information about the synchronization can be obtained from training symbols embedded into the regular data symbol pattern. The estimation of synchronization error can be performed depending on the type of the training data. Orthogonal Frequency Division Multiplexing (OFDM) is a multi-carrier modulation technique that has significantly impacted modern data transmission. By distributing data bits across multiple subcarriers, OFDM transforms communication methods, effectively addressing challenges such as multipath propagation.<br>

The materials below are helpful to comprehend this post:<br>
<iframe src="https://drive.google.com/file/d/1uOm2mTfnvMKewzKpfGH8Wp4wkvNYGfEf/preview" type="application/pdf" style="width:100%; height:600px;" frameborder="0"></iframe><br>
<a href="https://wirelesspi.com/timing-synchronization-in-ofdm-systems/" target="_blank">Timing Synchronization in OFDM Systems</a><br>
<a href="https://drive.google.com/file/d/1UXBKSiIWQODTCLaJvZ2M2YlT8f9Wmre1/preview" target="_blank">Time and Frequency Synchronization in OFDM System</a><br>

I have arranged some useful notes to organize OFDM synchronization and demodulation in the following note:<br>
<iframe src="https://drive.google.com/file/d/1AEJol-bRUNF_ENH5fEIbjCvCcVrMa12E/preview" type="application/pdf" style="width:100%; height:600px;" frameborder="0"></iframe><br>

Now, we will discuss the code implementation of the OFDM synchronization process. <br>

# DCM Autocorrelation and Find Peak
![alt text]({{ site.baseurl }}/assets/images/general_research/67.PNG "image"){:.profile}<br>
DCM (Delay-Conjugate Multiply) autocorrelation in OFDM improves signal quality by reducing fading effects caused by multipath propagation. It's evaluated by delaying, conjugating, and multiplying received subcarriers, then measuring their correlation. This process enhances reliability and reduces errors in wireless communication systems. The code below calculates DCM Autocorrelation and Maximum Likelihood peak values:<br>
<script src="https://gist.github.com/gyulab/d0c4216e798fadd68379bc43a3680f01.js"></script>

# CFO Estimation
CFO (Carrier Frequency Offset) estimation in OFDM is necessary to correct frequency discrepancies between transmitted and received signals, caused by factors like Doppler shifts. Accurate CFO estimation prevents subcarrier misalignment and interference.<br>
To evaluate CFO:<br>
1. Use pilot symbols (known data) in OFDM frames.
2. Measure phase difference between received and expected pilot symbols.
3. Calculate CFO from phase difference.
4. Compensate CFO to align subcarriers and maintain signal integrity.
5. CFO estimation ensures reliable data recovery in dynamic wireless environments.<br>
The following code estimates and compensates CFO by following the aforementioned sequences:<br>
<script src="https://gist.github.com/gyulab/2896b3287e7a3891220f8a72ad1bdd89.js"></script>

# LS Equalization
LS (Least Squares) equalization in OFDM is essential for mitigating channel distortions and improving signal quality. It's needed to counteract the effects of multipath fading and frequency-selective channels. The following figures describes the method of LS Equalization:<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/70.PNG "image"){:.profile}<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/71.PNG "image"){:.profile}<br>
To evaluate LS equalization:<br>
1. Collect pilot symbols (known data) transmitted in OFDM frames.
2. Measure the received pilot symbols' values.
3. Construct a channel response matrix.
4. Apply the LS algorithm to calculate equalization coefficients.
5. Use equalization coefficients to enhance data recovery from distorted subcarriers.
The following code is for the LS-Equalization process as aforementioned sequences:<br>
<script src="https://gist.github.com/gyulab/2bcc8608479706c8329571d8fb854882.js"></script>


# References
- Paramita, Saswati. (2014). Time and Frequency Synchronization in OFDM System. International Journal of Advanced Computer Research. 4. 856-865.
- T. Schmidl and D. Cox, "Robust frequency and timing synchronization for OFDM," IEEE Trans. Commun., vol. 45, Dec. 1997
- https://www.eit.lth.se/fileadmin/eit/courses/eit140/ofdm_synch.pdf
- https://wirelesspi.com/timing-synchronization-in-ofdm-systems
- https://www.sharetechnote.com/html/Communication_Equalizer.html
