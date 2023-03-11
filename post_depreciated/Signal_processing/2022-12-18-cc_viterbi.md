---
layout: post
title:  "Convolutional Codes & Viterbi Decoding by MATLAB"
date:   2022-12-18T14:28:52-05:00
author: Gyujun Jeong
categories: Research@signal
---

&nbsp;&nbsp;&nbsp;&nbsp;The documents and videos below are the good materials to study and understand the Convolutional Codes & Viterbi Decoding, from MIT 6.02 DRAFT Lecture Notes. Let's simulate various convolutional code encoders and Viterbi coding through MATLAB.
<br><br>
<b>1. Convolutional Codes</b><br>
<center><iframe width="95%" height="315" src="https://www.youtube.com/embed/kRIfpmiMCpU" frameborder="0" allowfullscreen></iframe></center><br>
<iframe src="https://ocw.mit.edu/courses/6-02-introduction-to-eecs-ii-digital-communication-systems-fall-2012/fea2b27744e25ff21846374a56ceb256_MIT6_02F12_lec06.pdf" type="application/pdf" style="width:100%; height:600px;" frameborder="0"></iframe>
<br>

<a href="https://www.mathworks.com/help/comm/ref/convenc.html" target="_blank">Mathworks convolutional code encoder description: convenc</a><br>

<b>Convolutional Code Type</b><br>
- Trellis Truncation<br>
Registers are filled with zeros initially. Terminates when the LSB of the frame enters to register.<br>
- Trellis Termination<br>
Registers are filled with zeros initially. Terminates when the LSB of the frame enters to register and refill the registers as 0. The zero-padding method is utilized in the code.<br>
- Tail Biting<br>
Registers are filled with the value of LSB of the frame and terminate when the same number enters to register, so-called 'tail-biting'. Tail-biting encoding ensures that the starting state of the encoder is the same as its ending state (and that this state value does not necessarily have to be the all-zero state). The circular viterbi algorithm (CVA) is incorporated to reduce complexity, decoding on repetitions of the LLR word, as the code below states. The documents below are helpful to understand the tail-biting concept:<br>

<a href="https://www.mathworks.com/help/comm/ug/tail-biting-convolutional-coding.html#TailBitingConvolutionalCodingExample-9" target="_blank">Mathworks tail-biting description</a><br>

<a href="https://ieeexplore.ieee.org/document/282266" target="_blank">R. V. Cox and C. E. W. Sundberg, "An efficient adaptive circular Viterbi algorithm for decoding generalized tailbiting convolutional codes," in IEEE Transactions on Vehicular Technology, vol. 43, no. 1, pp. 57-68, Feb. 1994<br>

<center><iframe width="95%" height="315" src="https://www.youtube.com/embed/nrP61KiG8fE" frameborder="0" allowfullscreen></iframe></center><br>

<b>Main code</b> <br>
<code>codedout = convenc(msg,trellis,puncpat)</code> specifies a puncture pattern, puncpat, to enable higher rate encoding than unpunctured coding.<br>

<b> Code Descriptions </b><br>
Receives an array of bits. Performs convolutional encoding on each block of a given length.

<b> Parameter descriptions</b> <br>
- <code>bit</code>: Matrix of read-out bit file<br>
- <code>len</code>: Block length, i.e., length of each block (= number of registers) being encoded, Highest order of genpoly + 1 <br>
Block length should be the multiple of k - the number of input of constraint length.<br>
e.g., <code>const_len = [5 4]</code> -> k= 2 -> Block length should be multiple of 2.
- <code>const_len</code>: Constraint length, i.e., vector of length k<br>
- <code>gen_poly</code>: Generating polynomial, k by n (k/n, k: input bit #, n: output bit #) matrix. Both octal and decimal are supported.<br>
<br>
- Sample run 1: <code>trellis = poly2trellis(3,[6 7])</code><br>
![alt text]({{ site.baseurl }}/assets/images/general_research/18.PNG "image"){:.profile}<br>
<center>Trellis Structure for Rate 1/2 Feedforward Convolutional Encoder</center><br>
<code>const_len</code> = 3,  <code>gen_poly</code> = [6 7] in octal = [110 111] in binary = [x^2+x, x^2+x^1+1] polynomials
<br>
- Sample run 2: <code>trellis = poly2trellis([5 4],[23 35 0; 0 5 13])</code><br>
![alt text]({{ site.baseurl }}/assets/images/general_research/19.PNG "image"){:.profile}<br>
<center>Trellis Structure for 2/3 Feedforward Convolutional Encoder</center><br> 
 <code>const_len</code> = [5,4],  <code>gen_poly</code> = [23 35 0; 0 5 13] in octal: input bit >= 2 -> divide row by ;
<br>

- <code>mode</code>: type of convolutional code<br>
- <code>punc</code>: Puncturing, size = multiple of n, vector of zeros(size) or ones(size)<br>
- <code>encoded_bit</code>: encoded result in binary bit<br>
<br>

<b> Code </b>
<script src="https://gist.github.com/gyulab/b790629e1804a1e4467b60b88b2ea099.js"></script><br>

<br>
<b>2. Viterbi Decoding</b><br>
<center><iframe width="95%" height="315" src="https://www.youtube.com/embed/dKIf6mQUfnY" frameborder="0" allowfullscreen></iframe></center><br>
<iframe src="https://ocw.mit.edu/courses/6-02-introduction-to-eecs-ii-digital-communication-systems-fall-2012/f398fa4a366439301b3d17e45e028952_MIT6_02F12_lec07.pdf" type="application/pdf" style="width:100%; height:600px;" frameborder="0"></iframe>
<br>
<iframe src="https://drive.google.com/file/d/1k4IPiEL9k0gHBtbEWu5XTynfB1UFTqtq/preview" type="application/pdf" style="width:100%; height:600px;" frameborder="0"></iframe>
<br>
<a href="https://www.mathworks.com/help/comm/ref/vitdec.html" target="_blank">Mathworks viterbi decoder description: vitdec</a><br>

<b>Main code</b> <br>
<code>decodedout = vitdec(codedin,trellis,tbdepth,opmode,dectype,puncpat)</code>  decodes each symbol of the punctured codedin input, where puncpat is the puncture pattern.<br>

<b> Code Descriptions </b><br>
Receives a bit file. Performs viterbi decoding on each block of given length.

<b> Parameter descriptions</b> <br>
- <code>bit, len, const_len, gen_poly, mode, punc</code>: same as the encoder<br>
- <code>tbdepth</code>: Traceback length- usually set as 5*sum(const_len) (refer to the document)
- <code>dek_bit</code>: decoded result via viterbi decoder in binary bit<br>
- <code>dectype-'hard'</code>: Decoding type: The decoder expects binary input values of 0 or 1.<br>
  
<b> Why do we use circular viterbi algorithm and permulation on tail-biting conv_mode? </b> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Tail biting convolutional codes are a type of convolutional code that are designed to be decoded using the Viterbi algorithm. In the tail biting decoding process, the encoder and decoder share the same state transition diagram and initial state, but the input and output sequences are different. To decode a tail biting code, the decoder needs to align the received sequence with the initial state of the encoder.

&nbsp;&nbsp;&nbsp;&nbsp;One way to do this is by using the circular Viterbi algorithm, which is a variant of the Viterbi algorithm that treats the received sequence as a circular buffer. This allows the decoder to align the received sequence with the initial state of the encoder by shifting the sequence left or right. After the alignment is done, the decoder needs to permute the output sequence to remove the circularity and obtain the original decoded sequence. This is done by shifting the output sequence so that the tail bits are in the correct position.<br>

<b> Code </b>
<script src="https://gist.github.com/gyulab/185c31c56a5fbe120cb508e6dc2a6c14.js"></script><br>
<br>
<br>
<b> Example 1) BER calculation of convolutional code </b><br>  
Design the convolutional encoder and the corresponding Viterbi decoder be used for channel coding where there happens a 2%-error in the 100,000 transmitted bits. <br>
![alt text]({{ site.baseurl }}/assets/images/general_research/23.PNG "image"){:.profile}<br>

- Code
<script src="https://gist.github.com/gyulab/d1f2fa6466dc11d7026e6899a36dc6ec.js"></script>
<br>
- Results Plot<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/22.PNG "image"){:.profile}<br>
  
<br>
<br>
<b> Example 2) BER calculation on QAM by Simulink </b><br>  
The Simulink model below can be used to simulate a QAM communication with a given convolutional encoder and the corresponding Viterbi decoder.<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/24.PNG "image"){:.profile}<br>
  
Here are the attributes of the Simulink model:<br>
<script src="https://gist.github.com/gyulab/08f0a1f8e99aa7184d8d2b583c77419f.js"></script>
<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/25.PNG "image"){:.profile}<br>
<br>
<br>
<b>References</b><br>
1. https://ocw.mit.edu/courses/6-02-introduction-to-eecs-ii-digital-communication-systems-fall-2012/
2. https://www.mathworks.com/help/comm/ref/vitdec.html
3. https://www.mathworks.com/help/comm/ref/convenc.html
4. Xilinx XAPP551 Viterbi Decoder Block Decoding - Trellis Termination and Tail Biting, Application Note
5. R. V. Cox and C. E. W. Sundberg, "An efficient adaptive circular Viterbi algorithm for decoding generalized tailbiting convolutional codes," in IEEE Transactions on Vehicular Technology, vol. 43, no. 1, pp. 57-68, Feb. 1994, doi: 10.1109/25.282266.
6. "MATLAB/Simulink for Digital Communication" authored by Won Y. Yang et. al
