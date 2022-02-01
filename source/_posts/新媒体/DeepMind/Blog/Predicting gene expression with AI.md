
---
title: 'Predicting gene expression with AI'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=6328'
author: DeepMind
comments: false
date: Mon, 04 Oct 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6328'
---

<div>   
<p><strong>Based on Transformers, our new Enformer architecture advances genetic research by improving the ability to predict how DNA sequence influences gene expression.</strong></p>
<p>When the <a href="https://www.genome.gov/human-genome-project/What" rel="noopener" target="_blank">Human Genome Project</a> succeeded in mapping the DNA sequence of the human genome, the international research community were excited by the opportunity to better understand the genetic instructions that influence human health and development. DNA carries the genetic information that determines everything from eye colour to susceptibility to certain diseases and disorders. The roughly 20,000 sections of DNA in the human body known as genes contain instructions about the amino acid sequence of proteins, which perform numerous essential functions in our cells. Yet these genes make up less than 2% of the genome. The remaining base pairs — which account for 98% of the 3 billion “letters” in the genome — are called “non-coding” and contain less well-understood instructions about when and where genes should be produced or expressed in the human body. At DeepMind, we believe that AI can unlock a deeper understanding of such complex domains, accelerating scientific progress and offering potential benefits to human health.</p>
<p>Today Nature Methods published “<a href="https://www.nature.com/articles/s41592-021-01252-x" rel="noopener" target="_blank">Effective gene expression prediction from sequence by integrating long-range interactions</a>” (first shared as a preprint on <a href="https://www.biorxiv.org/content/10.1101/2021.04.07.438649v1" rel="noopener" target="_blank">bioRxiv</a>), in which we — in collaboration with our Alphabet colleagues at <a href="https://www.calicolabs.com/" rel="noopener" target="_blank">Calico</a> — introduce a neural network architecture called Enformer that led to greatly increased accuracy in predicting gene expression from DNA sequence. To advance further study of gene regulation and causal factors in diseases, we also made our model and its initial predictions of common genetic variants <a href="https://github.com/deepmind/deepmind-research/tree/master/enformer" rel="noopener" target="_blank">openly available here</a>.</p>
<p>Previous work on gene expression has typically used convolutional neural networks as fundamental building blocks, but their limitations in modelling the influence of distal enhancers on gene expression have hindered their accuracy and application. Our initial explorations relied on <a href="https://github.com/calico/basenji" rel="noopener" target="_blank">Basenji2</a>, which could predict regulatory activity from relatively long DNA sequences of 40,000 base pairs. Motivated by this work and the knowledge that regulatory DNA elements can influence expression at greater distances, we saw the need for a fundamental architectural change to capture long sequences.</p>
<p>We developed a new model based on <a href="https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html" rel="noopener" target="_blank">Transformers</a>, common in natural language processing, to make use of self-attention mechanisms that could integrate much greater DNA context. Because Transformers are ideal for looking at long passages of text, we adapted them to “read” vastly extended DNA sequences. By effectively processing sequences to consider interactions at distances that are more than 5 times (i.e., 200,000 base pairs) the length of previous methods, our architecture can model the influence of important regulatory elements called enhancers on gene expression from further away within the DNA sequence.</p>  
</div>
            