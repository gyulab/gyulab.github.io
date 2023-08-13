---
layout: post
title:  "OFDM demodulation with synchronization techniques - CFO and Equalization"
date:   2023-08-12T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---

![alt text]({{ site.baseurl }}/assets/images/general_research/68.PNG "image"){:.profile}<br>

OFDM systems are very sensitive towards  synchronization error. Synchronization of an OFDM signal is required to find the symbol timing and carrier frequency offset (CFO). Before demodulation of subcarriers, either from explicit training data or using cyclic prefix of the OFDM signal we can get synchronization at receiver. After demodulation of the OFDM subcarriers, information about the ynchronization can be obtained from training symbols embedded into the regular data symbol pattern. The estimation of synchronization error can be performed depending on the type of the training data. Orthogonal Frequency Division Multiplexing (OFDM) is a multi-carrier modulation technique that has significantly impacted modern data transmission. By distributing data bits across multiple subcarriers, OFDM transforms communication methods, effectively addressing challenges such as multipath propagation.<br>

The materials below are helpful to comprehend this post:<br>
<iframe src="https://drive.google.com/file/d/1UXBKSiIWQODTCLaJvZ2M2YlT8f9Wmre1/preview" type="application/pdf" style="width:100%; height:600px;" frameborder="0"></iframe><br>
<iframe src="https://drive.google.com/file/d/1uOm2mTfnvMKewzKpfGH8Wp4wkvNYGfEf/preview" type="application/pdf" style="width:100%; height:600px;" frameborder="0"></iframe><br>
<a href="https://wirelesspi.com/timing-synchronization-in-ofdm-systems/" target="_blank">Timing Synchronization in OFDM Systems</a><br>

I have aligned some useful notes to organize OFDM synchronization and demodulation in the following note:<br>
<iframe src="https://drive.google.com/file/d/1AEJol-bRUNF_ENH5fEIbjCvCcVrMa12E/view?usp=sharing" type="application/pdf" style="width:100%; height:600px;" frameborder="0"></iframe><br>


# References
- Paramita, Saswati. (2014). Time and Frequency Synchronization in OFDM System. International Journal of Advanced Computer Research. 4. 856-865.
- T. Schmidl and D. Cox, "Robust frequency and timing synchronization for OFDM," IEEE Trans. Commun., vol. 45, Dec. 1997
- https://www.eit.lth.se/fileadmin/eit/courses/eit140/ofdm_synch.pdf
- https://wirelesspi.com/timing-synchronization-in-ofdm-systems
