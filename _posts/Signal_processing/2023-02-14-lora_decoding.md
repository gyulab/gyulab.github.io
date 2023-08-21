---
layout: post
title:  "LoRa/CSS Decoding: Gray indexing, Deinterleaving, and De-randomizing in data decoding"
date:   2023-02-14T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---

![alt text]({{ site.baseurl }}/assets/images/general_research/69.PNG "image"){:.profile}<br>
The LoRa receiver performs synchronization, frequency-offset estimation, and compensation prior to demodulation. Gray coding, de-interleaving, de-whitening, and Hamming decoding are carried out to recover the information as described in the figure above. In this post, we will discuss the concept of those decoding processes in general and how they apply to the LoRa decoding process.

# Gray coding
![alt text]({{ site.baseurl }}/assets/images/general_research/6.PNG "image"){:.profile}<br>

A gray coding is a mapping between a symbol in any numeric representation to a binary sequence. The particularity of the obtained binary sequence is that adjacent symbols in the original representation only differ by one bit in the gray representation. This property of a gray codes make them very useful in many wireless communication modulations where it is more likely to misinterpret a symbol by an adjacent one than another random one. It is noteworthy that in the case of CSS modulation it is not the white noise that causes this misinterpretation between adjacent symbols but the carrier and sampling frequency offset. In the case of LoRa, the symbols can be seen as integers between 0 and 2^SF − 1 and by making usage of gray coding to map them to binary strings, we increase the performance of the forward error correction mechanisms capable of correcting one erroneous bit in a codeword.<br>


Unfortunately, it is possible to create different binary string sequences respecting the conditions to be considered as a gray code. Furthermore it is just a mapping between decimal numbers and binary string, meaning that once we have found a sequence of 2^SF binary string differing by only one bit, we can still define any of them to by mapped to 0. Finally the direction of mapping of the following symbol can also be chosen freely. This leads to 2 ∗ 2^SF possibilities for every possible gray sequence. The method used in was a brute force approach, which found out that the method of the figure 2.4 is used. <br><br>
![alt text]({{ site.baseurl }}/assets/images/general_research/7.PNG "image"){:.profile}<br>
> Important Note: The standard gray code being used is given by Cn = Bn XOR (Bn >> 1) where Bn is the left MSB binary representation of n. On top of the mapping using this gray code, a shift of -1 is used, i.e., v = (v0 − 1) XOR ((v0 − 1) >> 1).

  
- In MATLAB<br>
Read the following document to understand the <a href="https://www.mathworks.com/help/comm/ref/bin2gray.html">bin2gray</a> function.<br>
<script src="https://gist.github.com/gyulab/b757d0c18d5d4d0dbc6f744b5d7f65f7.js"></script>
<br>
  
- In Python<br>
<script src="https://gist.github.com/gyulab/aa8a11f9440eff532411433bcd71abbf.js"></script>
<br>

We can note that the gray coding doesn’t occur in the conventional order but in reverse which still holds the property that one adjacent symbol mistake leads only to one bit being wrong. The figure 2.5 present the binary values obtained after gray encoding of the received LoRa symbols line by line. The white and black square are respectively ones and zeros.<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/8.PNG "image"){:.profile}<br>


# Interleaving and De-interleaving
![alt text]({{ site.baseurl }}/assets/images/general_research/26.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;Interleaving is a technique used to improve the performance of error correction codes by breaking the correlation between errors caused by noise or fading. It works by spreading the bits of a codeword across multiple symbols, so that if a symbol is corrupted, the errors will be distributed across multiple codewords rather than concentrated in one. This increases the effectiveness of the error correction code, but also increases the latency of the communication. Interleaving can also be used to improve the robustness of data transmitted over a noisy channel.<br>

&nbsp;&nbsp;&nbsp;&nbsp;For instance, LoRa signal applies diagonal interleaving instead of conventional row-line interleaving. The Figure (a) shows the column-major order row-line interleaving of eight symbols. For row-line interleaving, the LSBs (bi,1) of the eight symbols are assembled into a byte. From Section 3 we know that the LSBs of a symbol are more fragile than the most signiicant bits (MSBs) of the symbol. From the perspective of FEC, it is a bad design to group fragile bits together. Figure 9(b) shows diagonal interleaving used in LoRa. Diagonal interleaving distributes the fragile LSBs into diferent bytes and is more robust. We then manipulate the transmitted packets to derive the detailed diagonal mapping.<br>

&nbsp;&nbsp;&nbsp;&nbsp;As an example, we send packets with SF = 8 and CR = 4/8 in implicit header mode. Thus, the interleaving block is an 8 × 8 block as shown in Figure 9(b). First, we assume the FEC used in CR = 4/8 is the standard (7,4) Hamming code with one bit extension. Therefore, after Gray coding and Whitening, the codeword for nibble 0000 is 00000000, and the codeword for 1111 is 11111111. Suppose the sending bytes are all zeros except that the fourth byte is 0x0F, we observe b11 = b22 = · · · = b88 = 1 in Figure 9(b). Therefore the main diagonal represents the fourth byte 0x0F. The one bin shift problem mentioned in Gray coding relects here that we cannot always get eight ones in a block if we directly apply the standard Gray coding. Shifting the mapping by one solves this problem and perfectly matches our following decoding process. By changing the all-1 data bits in the transmitted packet, we can derive the entire mapping for interleaving as shown in Figure9(b). For other parameters, the deinterleaving process is similar. The only diference is that the block size becomes 4/CR × SF.<br>


<br>
> Important Note: From these patterns, we can finally extract the following general interleaving formula: I(i,j) = D(j,(i−(j+1)%SF))where I is the interleaved matrix and D the deinterleaved one.

![alt text]({{ site.baseurl }}/assets/images/general_research/27.PNG "image"){:.profile}<br>

  
- Simple snippet in cpp code<br>
<script src="https://gist.github.com/gyulab/da3eae1e719987c6b474f1702b083840.js?theme=dark"></script>
<br>
<br>

# Whitening and De-whitening (De-randomizing)

![alt text]({{ site.baseurl }}/assets/images/general_research/28.PNG "image"){:.profile}<br>

&nbsp;&nbsp;&nbsp;&nbsp;Whitening (Randomizing) is a technique that uses XORing bits with a pseudo-random sequence to remove the DC-bias from transmitted data. Unlike Manchester coding, it maintains the same data rate, but does not guarantee the removal of DC-bias, only a high probability of doing so.<br>

&nbsp;&nbsp;&nbsp;&nbsp;LoRa chip datasheet (Semtech. Data Sheet SX1276/77/78/79, Rev. 7, 2020) mentions that the whitening sequence in FSK mode is generated by a Linear Feedback Shift Register (LFSR). We guess that there also exists a LFSR generating the whitening sequence for LoRa mode. We apply Berlekamp-Massey algorithm on the whitening sequences of the two decoding orders to obtain the corresponding LFSR. <br>


<br>
> Important Note: The whitening is based around the 9-bit LFSR polynomial x^9+x^5+1. With this structure, the least significant bit (LSB) at the output of the LFSR is XORed with the most significant bit (MSB) of the data.

![alt text]({{ site.baseurl }}/assets/images/general_research/31.PNG "image"){:.profile}<br>

  
- Simple snippet<br>
<script src="https://gist.github.com/gyulab/79d92b0ad2f3f5a0c5df0abcd70bd981.js?theme=dark"></script>
<br>


<br><br>

<b>[References]</b>
1. Tapparel Joachim, Complete Reverse Engineering of LoRa PHY: https://www.epfl.ch/labs/tcl/wp-content/uploads/2020/02/Reverse_Eng_Report.pdf
2. Zhenqiang Xu, Pengjin Xie, Shuai Tong, and Jiliang Wang. 2022. From Demodulation to Decoding: Towards Complete LoRa PHY Understanding and Implementation. ACM Trans. Sen. Netw. Just Accepted (July 2022). https://doi.org/10.1145/3546869
3. Ghanaatian, R., Afisiadis, O., Cotting, M., & Burg, A. (2019). Lora Digital Receiver Analysis and Implementation. ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). doi:10.1109/icassp.2019.8683504
4. https://www.youtube.com/watch?v=MsMkiTcc_w0
   

