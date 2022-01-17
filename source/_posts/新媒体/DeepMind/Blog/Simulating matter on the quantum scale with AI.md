
---
title: 'Simulating matter on the quantum scale with AI'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=8055'
author: DeepMind
comments: false
date: Thu, 09 Dec 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8055'
---

<div>   
<p><strong>Solving some of the major challenges of the 21st Century, such as producing clean electricity or developing high temperature superconductors, will require us to design new materials with specific properties. To do this on a computer requires the simulation of electrons, the subatomic particles that govern how atoms bond to form molecules and are also responsible for the flow of electricity in solids. Despite decades of effort and several significant advances, accurately modelling the quantum mechanical behaviour of electrons remains an open challenge. Now, in a <a href="https://www.science.org/stoken/author-tokens/ST-218/full" rel="noopener" target="_blank">paper</a></strong><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;"> </strong><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">(<a href="https://storage.googleapis.com/deepmind-media/papers/Data_Driven_Density_Functional_Design/data_driven_density_functional_design_unformatted.pdf" rel="noopener" target="_blank">Open Access PDF</a>) </strong><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">published in Science, we propose DM21, a neural network achieving state of the art accuracy on large parts of chemistry. To accelerate scientific progress, we’re also open sourcing our <a href="https://github.com/deepmind/deepmind-research/tree/master/density_functional_approximation_dm21" rel="noopener" target="_blank">code</a> for anyone to use.</strong></p>
<p></p>
<p>Nearly a century ago, Erwin Schrödinger proposed <a href="https://www.nobelprize.org/prizes/physics/1933/schrodinger/facts/" rel="noopener" target="_blank">his famous equation</a> governing the behaviour of quantum mechanical particles. Applying this equation to electrons in molecules is challenging because all electrons repel each other. This would seem to require tracking the probability of each electron’s position — a remarkably complex task for even a small number of electrons. One major breakthrough came in the 1960s, when Pierre Hohenberg and Walter Kohn realised that it is not necessary to track each electron individually. Instead, knowing the probability for <em>any</em> electron to be at each position (i.e., the electron density) is sufficient to exactly compute all interactions. Kohn received a <a href="https://www.nobelprize.org/prizes/chemistry/1998/kohn/facts/" rel="noopener" target="_blank">Nobel Prize in Chemistry</a> after proving this, thus founding Density Functional Theory (DFT).</p>
<p></p>
<p>Although DFT proves a mapping exists, for more than 50 years the exact nature of this mapping between electron density and interaction energy — the so-called density functional — has remained unknown and has to be approximated. Despite the fact that DFT intrinsically involves a level of approximation, it is the only practical method to study how and why matter behaves in a certain way at the microscopic level and has therefore become one of the most widely used techniques in all of science. Over the years, researchers have proposed many approximations to the exact functional with varying levels of accuracy. Despite their popularity, all of these approximations suffer from systematic errors because they fail to capture certain crucial mathematical properties of the exact functional.</p>
<p></p>
<p>By expressing the functional as a neural network and incorporating these exact properties into the training data, we learn functionals free from important systematic errors — resulting in a better description of a broad class of chemical reactions.</p>  
</div>
            