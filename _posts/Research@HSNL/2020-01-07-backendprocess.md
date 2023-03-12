---
layout: post
title:  "Backend of IC process"
date:   2020-01-07T14:25:52-05:00
author: Gyujun Jeong
tags: Research@HSNL
---

![alt text]({{ site.baseurl }}/assets/images/mosfet/e1.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Semiconductors were manufactured through the semiconductor process introduced in the previous posting. However, semiconductors that are simply lumps of silicon do not perform their functions. Today, let's look at the backend design, which is a subsequent process.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e2.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;A frontend is a process at the Transistor level as in the previous posting method. A backend is a process of making chips with passive devices such as Interconnection or L or C.
<br>

![alt text]({{ site.baseurl }}/assets/images/mosfet/e3.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;First, we must contact the plug that will act as the electrode of the designed transistor. Let's take a closer look at this process.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e5.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;First, cut the thick oxide layer through etching.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e6.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Then, cover the titanium layer with low contact resistance.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e7.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;TiN acts as a barrier, preventing the metal to be pluggable from diffusing into oxide.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e8.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Thereafter, a tungsten (W) to serve as a plug is covered through a CVD deposition process.
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;Continuous representation of this process results in the following.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e2d.gif "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;If this process is represented by 3D structure, it will be as follows.
![alt text]({{ site.baseurl }}/assets/images/mosfet/e3d.gif "image"){:.profile}


<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e11.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Since we installed the plug, let's find out about the interconnection line that will connect these plugs organically.
<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e12.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;As shown in the figure above, the interconnect line layer can be stacked upward on 9-10 layers or more, and serves as a channel for exchanging signals between transistors.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e13.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;The most important term in this integrated circuit is RC product, which increases the delay. Delay can be minimized by adjusting R and C.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e14.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;First, how do we reduce the Capacity(C)? From a material mechanical point of view, the dielectric constant of SiO2 in general is 3.9e. Looking at SiOC reduces polarization, which reduces K. This allows the reduce of C. In another way, it is possible to reduce C by introducing Airgap.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e15.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;How can Resistance(R) can be reduced? You can use Cu or Al with the same resistance. Let's take a look at the bottom information below.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e16.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Since Al and Cu have different physical properties as described above, the metal wiring process of the two is completely different. The wiring process of aluminum is called RIE, and the wiring process of copper is called Damascene process. The term asterisked here may be unfamiliar, so let's find out.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e17.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;I summarized the terms above. Moving on to the main point, let's find out the difference between RIE and Damascene processes.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e18.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;The key difference between the two processes is in order. The RIE process forms oxide after etching, and since the Damascene process is difficult to etch as shown in the above table, there is a sequence of forming oxide, etching, and polishing the protruding part. It's easy to think that the two are in the opposite order.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e19.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Let's find out more about how to deposit the Copper. The Damascene process can be considered as an inlaid technique, and when making pottery, it uses a technique of digging grooves first, filling with other materials, baking, and grinding the surface, which also has the same process.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e20.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;The surface grinding technique is called the planarization process, and the surface can be polished through various processes such as Thremal Flow, Etch back, and CMP.

<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e22.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Among R, L, and C of passive devices, there has been no mention of L so far, so let's briefly learn how to use an inductor. Intel's Zheng researchers have been extracting papers, which can improve the quality factor by using Inductor.

<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;So far, the metalization process, i.e., metal wiring process has been investigated. Now, the remaining processes are the EDS process and the packaging process, and we'll talk about this later, and let's just briefly talk about it now.

![alt text]({{ site.baseurl }}/assets/images/mosfet/e23.jpg "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/e24.jpg "image"){:.profile}
![alt text]({{ site.baseurl }}/assets/images/mosfet/e25.jpg "image"){:.profile}

&nbsp;&nbsp;&nbsp;&nbsp;The EDS process is a yield improvement process, and the packaging process protects the chip from the outside and packages it so that signals can be exchanged. The detailed sequence can be found by looking at the picture above.


<br>
![alt text]({{ site.baseurl }}/assets/images/mosfet/e26.jpg "image"){:.profile}
&nbsp;&nbsp;&nbsp;&nbsp;Through these complex and diverse processes, one IC Chip can finally be produced.


