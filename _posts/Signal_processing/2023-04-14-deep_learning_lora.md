---
layout: post
title:  "Deep Learning-based Signal Demodulation: Paper review and Implementation"
date:   2023-04-14T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---
![alt text]({{ site.baseurl }}/assets/images/general_research/38.PNG "image"){:.profile}<br>
<b>Note: Some of the source code has been redacted for the convenience purpose.</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;Deep learning algorithms have shown significant success in various signal processing and demodulation tasks. Some commonly used deep learning algorithms for signal processing and demodulation are as follows:

- Convolutional Neural Networks (CNNs): CNNs are widely used in image processing applications but can also be applied to 1D signals such as audio and time-series data. In signal processing, CNNs can be used for tasks such as noise reduction, denoising, and filtering.

- Recurrent Neural Networks (RNNs): RNNs are commonly used in speech recognition, natural language processing, and time-series analysis. In signal processing, RNNs can be used for tasks such as speech recognition, signal prediction, and modulation classification.

- Autoencoders: Autoencoders are neural networks that can be used for unsupervised feature learning and dimensionality reduction. In signal processing, autoencoders can be used for tasks such as signal compression, denoising, and feature extraction.

&nbsp;&nbsp;&nbsp;&nbsp;In general, deep learning algorithms can be used for various signal processing and demodulation tasks such as signal classification, denoising, feature extraction, and modulation recognition. The choice of algorithm depends on the specific problem's nature and the available data.

&nbsp;&nbsp;&nbsp;&nbsp;In this section, we will explore three different approaches to detecting and demodulating LoRa signals as presented in various research papers.<br>
<br>
<b><a href="https://www.researchgate.net/publication/351449349_LoRa_Signal_Demodulation_Using_Deep_Learning_a_Time-Domain_Approach">I. Kosta Dakic et al, LoRa Signal Demodulation Using Deep Learning, a Time-Domain Approach</a></b><br>


&nbsp;&nbsp;&nbsp;&nbsp;The paper "LoRa Signal Demodulation Using Deep Learning, a Time-Domain Approach" by Kosta Dakic et al. proposes a new approach for demodulating LoRa signals using deep learning techniques. The authors observe that the existing demodulation methods for LoRa signals are computationally expensive and require a high sampling rate, which is not practical for many real-world applications. <br>
&nbsp;&nbsp;&nbsp;&nbsp;The proposed approach uses a convolutional neural network (CNN) to directly demodulate the LoRa signal in the time-domain. The CNN is trained on a large dataset of LoRa signals with different modulation indices and spreading factors, and is able to accurately estimate the symbol rate, spreading factor, and modulation index of the received signal.<br>

Here are a diagram and datasets illustrating the utilized CNN to demodulate I/Q signal of LoRa symbols:
![alt text]({{ site.baseurl }}/assets/images/general_research/39.PNG "image"){:.profile}<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/40.PNG "image"){:.profile}<br>

&nbsp;&nbsp;&nbsp;&nbsp;First, we have to generate the data giving AWGN, frequency/time offset for the noise-robust demodulation. Here are the figure and MATLAB code to generate datasets:
![alt text]({{ site.baseurl }}/assets/images/general_research/53.PNG "image"){:.profile}
<script src="https://gist.github.com/gyulab/13917ebf1f4b7a004bf3a859e4ed6f88.js"></script>
<br>
Now, let's process our data, i.e., bring the data from MATLAB and preprocess data to train our network:
<script src="https://gist.github.com/gyulab/6c74659a2a3d07495a17102ea7c070cd.js"></script>
Finally, let's implement the CNN using Tensorflow based on the paper:
<script src="https://gist.github.com/gyulab/df42521a46d4f1e6f059ce057e351b4f.js"></script>

&nbsp;&nbsp;&nbsp;&nbsp;In this code, we define the input shape of the neural network as a 2D real-valued array with size [2 × n]. Then we create a sequential model and add convolutional layers interlaced with max pooling layers. After that, we add a fully connected layer with a Softmax activation function. We compile the model with stochastic gradient descent optimizer and categorical cross-entropy loss function. Then we train the model with the training dataset and evaluate the model with the testing dataset.<br>

&nbsp;&nbsp;&nbsp;&nbsp;The authors evaluate the performance of the proposed approach on both simulated and real-world datasets, and compare it with the existing demodulation methods. The results show that the proposed approach is computationally efficient and can achieve high accuracy even in low signal-to-noise ratio (SNR) conditions.Overall, the paper presents a novel approach for demodulating LoRa signals using deep learning techniques that can improve the efficiency and accuracy of LoRa communication systems.<br>
<br>
<br>
<b><a href="https://hal.science/hal-03373813/file/Deep_Learning_based_Signal_Detection_for_Uplink_in_LoRa_like_Network.pdf">II. Angesom Ataklity Tesfay et al, Deep Learning-based Signal Detection for Uplink in LoRa-like Networks</a></b><br>

&nbsp;&nbsp;&nbsp;&nbsp;The paper "Deep Learning-based Signal Detection for Uplink in LoRa-like Networks" by Angesom Ataklity Tesfay et al. proposes a deep learning-based signal detection approach for LoRa-like networks. The authors observe that traditional signal detection approaches for LoRa-like networks have limitations in terms of accuracy and computational complexity, and that machine learning techniques can potentially improve the performance.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Unlike previous approach, the proposed approach uses two NNs: the first is based on Deep forward Neural Network (DFNN), and the second on convolutional neural network (CNN), to detect the uplink signals in the presence of interference and noise.<br>

1. Deep Forward Neural Network (DFNN) <br>
![alt text]({{ site.baseurl }}/assets/images/general_research/41.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;As indicated in Fig. 3, the detector relies on a DFNN architecture with four hidden layers. The number of nodes in each hidden layer is 8M, 4M, 2M, and M. The input is the modulus of the de-chirped received samples after the FFT, yielding M input nodes. The output is the bits of the transmitted symbol, yielding SF output nodes. The ReLU function is used as the activation function in the hidden layers. The sigmoid function is applied to map the outputs to the  interval [0, 1] in the output layer. Batch normalization (BN) is embedded in the hidden layers to prevent overfitting.<br>
Here is the implement the DFNN using Pytorch based on the paper:<br>
<script src="https://gist.github.com/gyulab/18d726f398986b1c1894194ffbd007bf.js"></script>

2. Convolutional Neural Network (CNN) <br>
![alt text]({{ site.baseurl }}/assets/images/general_research/42.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;Differently from the common feedforward architecture, CNN relies mainly on convolution operations within the socalled convolutional layers. For this architecture, the input is presented as an M ×M binary image containing the modulus plots of (4), as illustrated in Fig. 5. The M nodes at the output layer correspond to the M symbols to be detected. Here, we use a structure that includes two convolutional layers and two fully connected layers (cf. Fig. 4). We set M/4 and M/2 kernels for the first and second convolutional layers, respectively. The kernel size is set to 4 × 4 for both layers. A pooling layer follows convolution steps to reduce the feature map’s dimension while keeping the most relevant information. The filter used for the average pooling layer is of size 2 × 2, and the stride is 2. The output of the second pooling layer is flattened to be the input of the fully connected layer. The first fully connected layer has 4M nodes and the second one has 2M nodes. Similarly to the DFNN, the ReLU function is used as the activation function, and batch normalization is performed. For the output classification layer, we employ the softmax function. The CNN is trained to minimize the crossentropy loss between the output and the transmitted symbols.<br>

Now, let's implement the CNN using Pytorch based on the paper:<br>
<script src="https://gist.github.com/gyulab/c3c6ab94c45eb4634646abbc398b4e07.js"></script>

Training:
<script src="https://gist.github.com/gyulab/24cf41d9380c59ca622b1e80fa5905f2.js"></script>
<br><br>

<b><a href="https://cse.msu.edu/~caozc/papers/sensys21-li.pdf">III. Chenning Li et al, NELoRa: Towards Ultra-low SNR LoRa Communication with Neural-enhanced Demodulation</a></b><br>
&nbsp;&nbsp;&nbsp;&nbsp;LoRa enables low signal-to-noise ratio (SNR) communication. However, the standard demodulation method does not fully exploit the properties of chirp signals, thus yields a sub-optimal SNR threshold under which the decoding fails. Consequently, the communication range and energy consumption have to be compromised for robust transmission. This paper presents NELoRa, a neural-enhanced LoRa demodulation method, exploiting the feature abstraction ability of deep learning to support ultra-low SNR LoRa communication.<br>

&nbsp;&nbsp;&nbsp;&nbsp;Taking the spectrogram of both amplitude and phase as input, they first design a mask-enabled Deep Neural Network (DNN) filter that extracts multi-dimension features to capture clean chirp symbols. Second, they develop a spectrogram-based DNN decoder to decode these chirp symbols accurately. Finally, they propose a generic packet demodulation system by incorporating a method that generates high-quality chirp symbols from received signals. <br>

![alt text]({{ site.baseurl }}/assets/images/general_research/52.PNG "image"){:.profile}<br>

&nbsp;&nbsp;&nbsp;&nbsp;The paper introduces a neural-enhanced demodulation approach for LoRa (Low Range) signals. The proposed approach uses a dual-channel spectrogram of the chirp symbol as input to a deep neural network (DNN) model for decoding the encoded data bits. The dual-DNN model consists of two modules: a noise filter and a spectrogram-based decoder. The noise filter aims to preserve the primary features of the chirp symbol by masking the raw spectrogram, and it contains multiple blocks of convolutional neural networks (CNN) and one long short-term memory (LSTM) layer. The masked spectrogram is then input to a CNN-based decoder to capture the spatial energy peak distribution and temporal staggered pattern for decoding. The DNN model is trained using two loss functions for back-propagation, one for the noise filter and one for the decoder, with the goal of minimizing the average loss on the training dataset. Data augmentation techniques are also employed to improve the generalization of the DNN model. Experimental results demonstrate that the proposed neural-enhanced demodulation approach outperforms existing methods in terms of demodulation accuracy for LoRa signals, especially under low signal-to-noise ratio (SNR) conditions. <br>
<!--
Here is the demo code to build a network based on this paper:<br>
<script src="https://gist.github.com/gyulab/f07c362fc3b8d7e031ef64579c762030.js"></script>
-->

<br>

<b>[References]</b>
1. Kosta Dakic et al, LoRa Signal Demodulation Using Deep Learning, a Time-Domain Approach
2. Angesom Ataklity Tesfay et al, Deep Learning-based Signal Detection for Uplink in LoRa-like Networks
3. Chenning Li et al, NELoRa: Towards Ultra-low SNR LoRa Communication with Neural-enhanced Demodulation
4. A Primer on Deep Learning Architectures and Applications in Speech Processing
