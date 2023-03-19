---
layout: post
title:  "Signal Processing and bit processing with Numpy"
date:   2022-09-30T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---

&nbsp;&nbsp;&nbsp;&nbsp;Numpy, one of Python's modules can be used in various fields. It is also an easy package for bit processing and matrix computation. Since the internal operation is implemented in Fortran and C, the speed is also relatively fast. This versatile package is used in bit processing and various fields in signal processing. This time, let's process the signal file by numpy module.<br><br>
FYI) Here is the link for <a href="https://numpy.org">numpy.org</a> and <a href="https://matplotlib.org/stable/">matplotlib.org</a><br>

<b>Contents of signal processing (and some linear algebras!)</b><br>
1. FFT (Fast Fourier Transform)<br>
2. Bit File readout / write example <br>
3. Gaussian Elimination<br>


<br>
<b>FFT of the signal file</b><br>

- Main Code

```python
fft.fft(a, n=None, axis=-1, norm=None)
```
Compute the one-dimensional discrete Fourier Transform. This function computes the one-dimensional n-point discrete Fourier Transform (DFT) with the efficient Fast Fourier Transform (FFT) algorithm [CT].<br>

- Example w/ Real signal<br>

<script src="https://gist.github.com/gyulab/e79a05f68201ca394bb0ac1fe95e48f0.js"></script><br>
Result plot:<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/21.PNG "image"){:.profile}<br>


<b>Bit File readout / write example </b><br>
<script src="https://gist.github.com/gyulab/f5d09d6cbe17a7a4ce00a4a1855e8d2c.js"></script><br>

<b>Gaussian Elimination</b><br>
<script src="https://gist.github.com/gyulab/097c6370a470b70170e3a5562ed7515d.js"></script>

<br><br>

<b>References</b>
1. https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html
