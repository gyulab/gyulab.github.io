---
layout: post
title:  "Deep Learning-based Signal Demodulation: Paper review and Implementation"
date:   2023-03-26T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---

![alt text]({{ site.baseurl }}/assets/images/general_research/38.PNG "image"){:.profile}<br>
&nbsp;&nbsp;&nbsp;&nbsp;Deep learning algorithms have shown significant success in various signal processing and demodulation tasks. Some commonly used deep learning algorithms for signal processing and demodulation are as follows:

- Convolutional Neural Networks (CNNs): CNNs are widely used in image processing applications but can also be applied to 1D signals such as audio and time-series data. In signal processing, CNNs can be used for tasks such as noise reduction, denoising, and filtering.

- Recurrent Neural Networks (RNNs): RNNs are commonly used in speech recognition, natural language processing, and time-series analysis. In signal processing, RNNs can be used for tasks such as speech recognition, signal prediction, and modulation classification.

- Autoencoders: Autoencoders are neural networks that can be used for unsupervised feature learning and dimensionality reduction. In signal processing, autoencoders can be used for tasks such as signal compression, denoising, and feature extraction.

- Generative Adversarial Networks (GANs): GANs are used for generating new data samples that are similar to the training data. In signal processing, GANs can be used for tasks such as signal generation, anomaly detection, and signal restoration.

- Deep Reinforcement Learning (DRL): DRL algorithms can be used for tasks such as adaptive filtering, dynamic spectrum access, and cognitive radio. In DRL, agents learn to optimize actions based on the environment's feedback to achieve a specific goal.

&nbsp;&nbsp;&nbsp;&nbsp;In general, deep learning algorithms can be used for various signal processing and demodulation tasks such as signal classification, denoising, feature extraction, and modulation recognition. The choice of algorithm depends on the specific problem's nature and the available data.

&nbsp;&nbsp;&nbsp;&nbsp;In this section, we will explore two different approaches to detecting and demodulating LoRa signals as presented in various research papers.<br>
<br>

<b>1. Kosta Dakic et al, LoRa Signal Demodulation Using Deep Learning, a Time-Domain Approach</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;The paper "LoRa Signal Demodulation Using Deep Learning, a Time-Domain Approach" by Kosta Dakic et al. proposes a new approach for demodulating LoRa signals using deep learning techniques. The authors observe that the existing demodulation methods for LoRa signals are computationally expensive and require a high sampling rate, which is not practical for many real-world applications. The proposed approach uses a convolutional neural network (CNN) to directly demodulate the LoRa signal in the time-domain. The CNN is trained on a large dataset of LoRa signals with different modulation indices and spreading factors, and is able to accurately estimate the symbol rate, spreading factor, and modulation index of the received signal.<br>

Here are a diagram and datasets illustrating the utilized CNN to demodulate I/Q signal of LoRa symbols:
![alt text]({{ site.baseurl }}/assets/images/general_research/39.PNG "image"){:.profile}<br>
![alt text]({{ site.baseurl }}/assets/images/general_research/40.PNG "image"){:.profile}<br>

Before implementing the NN, we should undergo some steps as follows:
- Data collection and pre-processing: Collect a dataset of LoRa signals with different modulation indices and spreading factors. Pre-process the data by applying filtering, resampling, and normalization techniques.
- Data preparation: Split the dataset into training, validation, and test sets. Prepare the data in the time-domain by dividing the signal into smaller segments and applying a sliding window technique.-
- Model architecture: Define a CNN architecture for demodulating the LoRa signals. The CNN should have multiple convolutional layers followed by max-pooling layers, and then fully connected layers for classification. 
- Training: Train the CNN using the prepared dataset. Use a suitable loss function, optimizer, and learning rate for training. You can also use techniques like data augmentation and early stopping to improve the performance of the model.
- Testing: Evaluate the performance of the trained model on the test dataset. Measure metrics like accuracy, 
precision, and recall to evaluate the performance

&nbsp;&nbsp;&nbsp;&nbsp;Now, let's implement the CNN using Tensorflow based on the paper:<br>
<script src="https://gist.github.com/gyulab/df42521a46d4f1e6f059ce057e351b4f.js"></script>

&nbsp;&nbsp;&nbsp;&nbsp;The authors evaluate the performance of the proposed approach on both simulated and real-world datasets, and compare it with the existing demodulation methods. The results show that the proposed approach is computationally efficient and can achieve high accuracy even in low signal-to-noise ratio (SNR) conditions.Overall, the paper presents a novel approach for demodulating LoRa signals using deep learning techniques that can improve the efficiency and accuracy of LoRa communication systems.<br>
<br>
<br>
<b>Angesom Ataklity Tesfay et al, Deep Learning-based Signal Detection for Uplink in LoRa-like Networks</b><br>




<br><br>

<b>[References]</b>
1. Kosta Dakic et al, LoRa Signal Demodulation Using Deep Learning, a Time-Domain Approach
2. Angesom Ataklity Tesfay et al, Deep Learning-based Signal Detection for Uplink in LoRa-like Networks
3. A Primer on Deep Learning Architectures and Applications in Speech Processing
