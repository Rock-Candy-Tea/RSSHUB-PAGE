
---
title: 'Game theory as an engine for large-scale data analysis'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=688'
author: DeepMind
comments: false
date: Thu, 06 May 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=688'
---

<div>   
<p><strong>EigenGame maps out a new approach to solve fundamental ML problems.</strong></p>
<p>Modern AI systems approach tasks like <a href="https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html">recognising objects in images</a> and <a href="https://deepmind.com/blog/article/alphafold-a-solution-to-a-50-year-old-grand-challenge-in-biology" rel="noopener" target="_blank">predicting the 3D structure of proteins</a> as a diligent student would prepare for an exam. By training on many example problems, they minimise their mistakes over time until they achieve success. But this is a solitary endeavour and only one of the known forms of learning. Learning also takes place by interacting and playing with others. It’s rare that a single individual can solve extremely complex problems alone. By allowing problem solving to take on these game-like qualities, previous DeepMind efforts have trained AI agents to play <a href="https://deepmind.com/blog/article/capture-the-flag-science">Capture the Flag</a> and achieve <a href="https://deepmind.com/blog/article/alphastar-mastering-real-time-strategy-game-starcraft-ii" rel="noopener" target="_blank">Grandmaster level at Starcraft</a>. This made us wonder if such a perspective modeled on game theory could help solve other fundamental machine learning problems.</p>
<p>Today at <a href="https://iclr.cc/" rel="noopener" target="_blank">ICLR 2021</a> (the International Conference on Learning Representations), we presented “<a href="https://openreview.net/forum?id=NzTU59SYbNq" rel="noopener" target="_blank">EigenGame: PCA as a Nash Equilibrium</a>,” which received an Outstanding Paper Award. Our research explored a new approach to an old problem: we reformulated principal component analysis (PCA), a type of <a href="https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix" rel="noopener" target="_blank">eigenvalue problem</a>, as a competitive multi-agent game we call EigenGame. PCA is typically formulated as an optimisation problem (or single-agent problem); however, we found that the multi-agent perspective allowed us to develop new insights and algorithms which make use of the latest computational resources. This enabled us to scale to massive data sets that previously would have been too computationally demanding, and offers an alternative approach for future exploration.</p>
<h4>PCA as a Nash equilibrium</h4>
<p>First described in the early 1900s, <a href="https://en.wikipedia.org/wiki/Principal_component_analysis" rel="noopener" target="_blank">PCA</a> is a long-standing technique for making sense of the structure of high-dimensional data. This approach is now ubiquitous as a first step in the data-processing pipeline and makes it easy to cluster and visualise data. It can also be a useful tool for learning low-dimensional representations for regression and classification. More than a century later, there are still compelling reasons to study PCA.</p>
<p>Firstly, data was originally recorded by hand in paper notebooks, and now it is stored in data centres the size of warehouses. As a result, this familiar analysis has become a computational bottleneck. Researchers have explored <a href="https://arxiv.org/abs/0909.4061" rel="noopener" target="_blank">randomised algorithms</a> and other directions to improve how PCA scales, but we found that these approaches have difficulty scaling to massive datasets because they are unable to fully harness recent deep-learning-centric advances in computation — namely access to many parallel GPUs or TPUs.</p>
<p>Secondly, PCA shares a common solution with many important ML and engineering problems, namely the <a href="https://en.wikipedia.org/wiki/Singular_value_decomposition" rel="noopener" target="_blank">singular value decomposition</a> (SVD). By approaching the PCA problem in the right way, our insights and algorithms apply more broadly across the branches of the ML tree.</p>  
</div>
            