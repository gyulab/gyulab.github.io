---
layout: post
title:  "Fixed point conversion to read out signal file"
date:   2022-12-02T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---

![alt text]({{ site.baseurl }}/assets/images/general_research/12.PNG "image"){:.profile}<br>

&nbsp;&nbsp;&nbsp;&nbsp;Fixed-point conversion is the process of converting a floating-point number to a fixed-point number. A fixed-point number has a fixed number of digits to the right of the decimal point, while a floating-point number can have a variable number of digits.<br>

&nbsp;&nbsp;&nbsp;&nbsp;In MATLAB, the numerictype function can be used to define a numeric data type with a specified word length and fraction length, which can then be used in the reinterpretcast function to convert a floating-point number to a fixed-point number.<br>

&nbsp;&nbsp;&nbsp;&nbsp;There are several reasons why fixed-point conversion is used in digital signal processing and other numerical applications:<br>

1. Fixed-point numbers take up less memory than floating-point numbers, making them more efficient for embedded systems and other devices with limited memory.

2. Fixed-point numbers can be processed more quickly than floating-point numbers by specialized digital signal processing hardware, such as digital signal processors (DSPs).

3. Fixed-point numbers are more predictable and can be more accurate than floating-point numbers, especially in embedded systems and other applications where precision is critical.

4. Using fixed-point numbers can also make it easier to implement mathematical algorithms that are difficult to implement with floating-point numbers.
<br>

&nbsp;&nbsp;&nbsp;&nbsp;The videos below is the good material to understand fixed point conversion.<br>
<center><iframe width="95%" height="315" src="https://www.youtube.com/embed/kUNVW-mal0A" frameborder="0" allowfullscreen></iframe></center><br>


&nbsp;&nbsp;&nbsp;&nbsp;So, How could we read out the signal file to a processable bit-file? The MATLAB and Python codes below convert the signal file in the fixed point with binary point scaling, the word length of w, and fraction length of f as a big-endian order.
<br>
  
- In MATLAB<br>
Read the following document to understand the <a href="https://www.mathworks.com/help/fixedpoint/ref/embedded.numerictype.html">numerictype</a>
and <a href="https://www.mathworks.com/help/fixedpoint/ref/reinterpretcast.html?s_tid=doc_ta#d124e162564">reinterpretcast</a><br>

<script src="https://gist.github.com/gyulab/fe4be0a81a473eda5a344d1ad5779c5c.js"></script>
<br>
  
- In Python<br>

<script src="https://gist.github.com/gyulab/c5c47615111e88463c299d5658c6a8c2.js"></script>


<br><br>

<b>[References]</b>
1. https://www.researchgate.net/figure/Representation-of-floating-point-and-fixed-point-numbers_fig1_348825339
2. https://www.analog.com/en/technical-articles/fixedpoint-vs-floatingpoint-dsp.html
