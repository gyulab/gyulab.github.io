---
layout: post
title:  "Isolation Technique"
date:   2020-01-13T14:25:52-05:00
author: Gyujun Jeong
categories: Research@HSNL
---
![alt text]({{ site.baseurl }}/assets/images/mosfet/i1.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;CMOS is an abbreviation for Complementary MOS, which is a MOS device with two different types of MOS elements placed in one wafer: n-channel MOS and p-channel MOS. When the two types of devices are placed on one substrate, various problems such as leakage current and latch-up occur. Today, let's talk about isolation techniques that separate these elements.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/i2.jpg "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/i3.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;First, let's find out why isolation is necessary. In the figure above, a leakage current path is illustrated, and isolation is required to prevent such a leakage current. Looking at the second figure, the space required for isolation is reduced while reducing the size of the device, so it can be seen that isolation also requires various technologies.
<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/i4.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Various techniques for performing isolation are introduced. You can think of it as the latest technology as you go down from top to bottom. Now let's look at each technology.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/i5.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;A diffusion isolation utilizing reverse biased diode. It was used in Bipolar Transistor and is currently used as isolation through well.
![alt text]({{ site.baseurl }}/assets/images/mosfet/i6.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;It is isolation using Oxide and is a technology used in the early days of MOS development. However, due to various disadvantages, the LOCOS technique or trench isolation to be introduced next is used.
![alt text]({{ site.baseurl }}/assets/images/mosfet/i7.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;The LOCOS technique is an abbreviation for LOCal Oxidation of Si, which is today's method to organize old data, but in reality, in the current nano process, LOCOS will be described later, but it is not used now due to side effects such as Bird's Beak.
![alt text]({{ site.baseurl }}/assets/images/mosfet/i8.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;The word 'trench' of trench isolation stands for the <a href="https://en.wikipedia.org/wiki/Trench">trench</a> for trench coats. Although the process is complicated, it is one of the most widely used techniques today because it can dramatically increase packing density.



![alt text]({{ site.baseurl }}/assets/images/mosfet/i9.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Let's find out more about the LOCOS process introduced earlier.
![alt text]({{ site.baseurl }}/assets/images/mosfet/i11.jpg "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/i10.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;The order of the LOCOS process is as illustrated in the figure above, and in the last figure, it is possible to observe the bending of oxide while growing field oxide.
![alt text]({{ site.baseurl }}/assets/images/mosfet/i12.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;This bending phenomenon is called Bird's Beak because it resembles a bird's beak, which lowers the active area of the device and acts as a limiting factor for LOCOS process.
![alt text]({{ site.baseurl }}/assets/images/mosfet/i13.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;To solve this Bird's Bake phenomenon, various techniques such as SWAMI, SPOT, OSELO, and FUROX were utilised.



![alt text]({{ site.baseurl }}/assets/images/mosfet/i14.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Now let's learn about Trench Isolation.


![alt text]({{ site.baseurl }}/assets/images/mosfet/i15.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Let's find out the application techniques using Trench Isolation. STI is the Shallow Trench Isolation, which uses Moderate Trench to isolate Bipolar or preempt latch-up of CMOS. And to make DRAM's trench capacitor, use Deep trench. Each classification is divided into 1um and 3um as a starting point.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/i16.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;STI(Shallow Trench Isolation) Process

![alt text]({{ site.baseurl }}/assets/images/mosfet/i17.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;When Etching the trench, a round trench is preferred. In order to make a trench round, it is necessary to go through an advanced dry-etching technique and a high-temperature thermal oxidation process. The high-temperature thermal oxidation process reduces stress, which reduces leakage current.

![alt text]({{ site.baseurl }}/assets/images/mosfet/i18.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Using the silicon on insulator (SOI) and STI seen in the previous posting, more effective isolation is possible. It is a technique used in a process of 0.13um or less.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/i19.jpg "image"){:.profile}
