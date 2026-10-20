---
layout: post
title: IBM Analog Hardware Accelerator Kit Research Archive
date: "2024-07-27T14:25:52-05:00"
description: "Running transformer models (GPT-2, BERT) on analog in-memory computing hardware with IBM AIHWKit: a GPT-2 example now included in the official AIHWKit release, and a layer-wise noise sensitivity analysis of BERT on SQuAD."
thumbnail: /assets/img/research/aihwkit/bert-distribution.jpg
tags: [1_Georgia_Tech]
---

#### Presentation Video
<iframe src="https://drive.google.com/file/d/1J8sBSpqyenYCgdGmYVPzVXodfiKUonrs/preview" style="width:100%; height:400px;" frameborder="0"></iframe>
<br>

**Official Example (IBM AIHWKit)**: <a href="https://github.com/IBM/aihwkit/blob/master/examples/36_gpt2_on_wikitext.py" target="_blank">examples/36_gpt2_on_wikitext.py</a><br>
**My Fork**: <a href="https://github.com/gyulab/aihwkit" target="_blank">github.com/gyulab/aihwkit</a> (<a href="https://github.com/gyulab/aihwkit/blob/master/examples/31_gpt2_on_wikitext.py" target="_blank">GPT-2</a>, <a href="https://github.com/gyulab/aihwkit/blob/master/examples/31_gpt2_decoder_model.ipynb" target="_blank">GPT-2 notebook</a>, <a href="https://github.com/gyulab/aihwkit/blob/master/examples/32_bert_on_squad_noise_analysis.py" target="_blank">BERT noise analysis</a>)<br><br>

Update) The GPT-2 example I started in summer 2024 is now part of the official IBM AIHWKit examples as **Example 36** ("This example was initiated by Gyujun Jeong"), released with **AIHWKit 1.1.0** and later versions.



# Motivation: Transformers on Analog In-Memory Computing

&nbsp;&nbsp;&nbsp;&nbsp;Analog in-memory computing (AIMC) performs matrix-vector multiplications directly inside non-volatile memory crossbars, avoiding the data movement that dominates the energy of large neural networks. However, analog weights are **noisy**: programming noise, read noise, conductance drift, and limited ADC/DAC precision all perturb the computation.

&nbsp;&nbsp;&nbsp;&nbsp;**IBM Analog Hardware Acceleration Kit (AIHWKit)** is an open-source PyTorch toolkit that simulates these non-idealities, so we can ask: *how do modern transformer models behave on analog hardware, and which layers are most sensitive to noise?* In this project, I explored two transformer families:
1. **GPT-2 (decoder):** an end-to-end example for analog conversion, hardware-aware (HWA) fine-tuning, and text generation.
2. **BERT (encoder):** a layer-by-layer noise sensitivity analysis on question answering.

<br><br>

# Part 1. GPT-2 on AIHWKit

#### Model & Dataset
* **Model:** <a href="https://huggingface.co/distilbert/distilgpt2" target="_blank">DistilGPT2</a> (88.2M parameters), the smallest GPT-2 variant, for demonstration.
* **Dataset:** wikitext-2-raw-v1 (~18 MB on disk).
* **Workflow:** load the pre-trained model from Hugging Face → convert it to analog with `convert_to_analog()` → HWA fine-tuning → evaluate perplexity at different weight noise levels and inference times (drift), logged to TensorBoard.

#### Analog Layers
&nbsp;&nbsp;&nbsp;&nbsp;After `convert_to_analog()`, the **LM head** (768 → 50257) becomes an `AnalogLinear` layer mapped onto two simulated crossbar tiles. In this demonstration, the GPT-2 blocks use Hugging Face `Conv1D` modules (attention `c_attn`/`c_proj`, MLP `c_fc`/`c_proj`), which were not replaced by the converter, so they stay digital along with the embeddings and LayerNorms.

![GPT-2 Layers](/assets/img/research/aihwkit/gpt2-layers.jpg "image"){:.profile}<br>

#### Results
![GPT-2 Train Loss](/assets/img/research/aihwkit/gpt2-train-loss.jpg "image"){:.profile}<br>
![GPT-2 Validation](/assets/img/research/aihwkit/gpt2-validation.jpg "image"){:.profile}<br>

| Model | Validation Loss | Perplexity (PPL) |
| :--- | :--- | :--- |
| Digital (reference, <a href="https://huggingface.co/Intel/distilgpt2-wikitext2" target="_blank">Intel/distilgpt2-wikitext2</a>) | 3.326 | 27.8 |
| Analog, HWA fine-tuned (AIHWKit) | 4.059 | 57.9 |

<br>

&nbsp;&nbsp;&nbsp;&nbsp;The analog model still generates coherent text from a prompt, showing that the full pipeline (conversion → HWA training → generation) works end-to-end:
* **Input:** "Once upon a time"
* **Output:** "Once upon a time of war, the German army was able to defeat the German army in the Battle of the Rhine"

![GPT-2 Inference](/assets/img/research/aihwkit/gpt2-inference.jpg "image"){:.profile}<br>

&nbsp;&nbsp;&nbsp;&nbsp;I opened a pull request to IBM/AIHWKit (<a href="https://github.com/IBM/aihwkit/pull/664" target="_blank">#664</a>). The example was later integrated by the maintainers into the official repository as <a href="https://github.com/IBM/aihwkit/blob/master/examples/36_gpt2_on_wikitext.py" target="_blank">Example 36</a>.

<br><br>

# Part 2. BERT Noise Analysis on SQuAD

#### Setup
* **Task:** SQuAD v1.1 (100k+ question-answer pairs). BERT takes `[CLS] question [SEP] passage [SEP]` and predicts start/end logits of the answer span.
* **Metrics:** F1 score (token overlap between predicted and ground-truth spans) and Exact Match (EM).
* **Analog configuration:** PCM-like noise model, 512×512 tiles, 256-level DAC/ADC resolution, output noise, and global drift compensation.
* **Method:** For each layer, one at a time, inject **Gaussian weight noise (mean = 0, std = 0.1)** and re-evaluate F1/EM. This isolates how much each layer contributes to the accuracy loss.

![BERT Code](/assets/img/research/aihwkit/bert-code.jpg "image"){:.profile}<br>
![BERT Layers](/assets/img/research/aihwkit/bert-layers.jpg "image"){:.profile}<br>

#### Baseline
&nbsp;&nbsp;&nbsp;&nbsp;Without additional noise, the analog BERT achieves **F1 ≈ 88** and **EM ≈ 81**, stable over drift times up to 10<sup>6</sup> s. This is the reference for the layer-wise analysis.

![BERT Baseline](/assets/img/research/aihwkit/bert-baseline.jpg "image"){:.profile}<br>

#### Layer-wise Sensitivity

| Layer Group | F1 / EM under noise | Observation |
| :--- | :--- | :--- |
| **Embeddings** (word, position, token type) | F1 0.59–4.19, EM < 1 | **Most vulnerable**: noise corrupts the input representation itself |
| Attention (query/key/value) | F1 86.75–87.47, EM 78.67–79.67 | Robust: attention tolerates noise to a certain extent |
| Intermediate / output dense | Mostly ~87, worst F1 77.13, EM 63.69 | Complex output dense layers can be highly sensitive |
| LayerNorm | F1 ~87, EM ~79 | Strong resistance; normalization stabilizes small perturbations |
| QA outputs | F1 ~87, EM ~79 | Robust: directly reads the contextualized embeddings |

<br>

![BERT Embedding](/assets/img/research/aihwkit/bert-embedding.jpg "image"){:.profile}<br>
![BERT Dense](/assets/img/research/aihwkit/bert-dense.jpg "image"){:.profile}<br>

&nbsp;&nbsp;&nbsp;&nbsp;**Noise propagation:** Noise injected in earlier layers propagates and can be amplified downstream. For example, the same output dense tile gives F1 87.23 in encoder layer 0 but drops to **F1 77.13** in layer 3.

![BERT Noise Propagation](/assets/img/research/aihwkit/bert-propagation.jpg "image"){:.profile}<br>

#### Why Are Some Layers Vulnerable?
**Hypothesis 1, Weight magnitude:** "Heavier weights dominate, so they are more noise-sensitive." I correlated the mean and std of each tile's weights with its F1 score. The correlation coefficients were only **−0.005 (mean)** and **0.090 (std)**, so weight magnitude is *not* the explanation.

![BERT Weight Magnitude](/assets/img/research/aihwkit/bert-weight-magnitude.jpg "image"){:.profile}<br>

**Hypothesis 2, Distribution spread:** Comparing the vulnerable layer (`output.dense ... array.3.0`, F1 77.13) with an average layer (F1 88.24), the vulnerable layer shows a **wider weight distribution and less consistent neuron activations**. This higher variability makes it less able to generalize under perturbation, which likely explains its lower F1.

![BERT Distribution](/assets/img/research/aihwkit/bert-distribution.jpg "image"){:.profile}<br>

<br><br>

# Summary

* **GPT-2 on AIHWKit:** Built an end-to-end analog GPT-2 example (conversion, HWA fine-tuning, drift-aware evaluation, text generation), now included in the official IBM AIHWKit as Example 36.
* **Layer importance:** In BERT, the first layers (embeddings) and complex final transformations (output dense) are the most critical, since they handle the initial encoding of raw input and the final prediction.
* **Layer functionality:** Layers with complex transformations and **wider weight/activation distributions** are more susceptible to analog noise, while attention, LayerNorm, and QA outputs are comparatively robust.
* **Takeaway for hardware design:** Not all layers need the same analog precision. Keeping sensitive layers (e.g., embeddings) digital or giving them more robust mapping is a practical path for transformer inference on AIMC.

<br>

### Slides: BERT Noise Analysis using AIHWKit (July 18, 2024)
<iframe src="https://drive.google.com/file/d/1Q_J0C1Z9MtZeBEsPk3PK8MJ6ZTHk2Lw_/preview" style="width:100%; height:600px;" frameborder="0"></iframe>

### Slides: GPT-2 Example Implementation (June 25, 2024)
<iframe src="https://drive.google.com/file/d/1rbIu6mdYRK0MGFGlL7RWprEDQ55h7E3x/preview" style="width:100%; height:600px;" frameborder="0"></iframe>
