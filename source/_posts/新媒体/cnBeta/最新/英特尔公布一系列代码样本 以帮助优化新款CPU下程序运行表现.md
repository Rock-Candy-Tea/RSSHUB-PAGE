
---
title: '英特尔公布一系列代码样本 以帮助优化新款CPU下程序运行表现'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0610/baf49341092aabf.png'
author: cnBeta
comments: false
date: Thu, 10 Jun 2021 05:59:32 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0610/baf49341092aabf.png'
---

<div>   
<strong>英特尔一直更新着一份冗长的"优化参考手册"，向开发者展示如何为其最新的CPU微架构优化代码，</strong>但伴随着他们最新手册的更新，现在有了很多实际的代码样本，以缓解学习英特尔优化技术的过程，从而充分利用其最新的处理器。<br>
 <p>在开源/Linux支持和其他直接与新硬件相关的关键领域之外，英特尔的工程师已经以性能的名义为开源项目做了很多工作，比如经常直接贡献优化和其他功能，以利用其最新处理器在流行开源项目中的功能，我们已经多次报道过英特尔的这种贡献。</p><p>从这些直接来自英特尔的开源代码贡献，以及由他们在项目中维护的开源代码，如在oneAPI中，独立开发者已经可以收集到很多关于优化技术和最佳利用其最新的处理器的信息。还有《英特尔64/IA-32架构优化参考手册》，但作为一个很好的助手，现在该手册还附有工作（可构建）的代码样本，作为学习英特尔代码优化曲线的一个更容易的初始步骤。</p><p>英特尔最新的《优化参考手册》可以在<a href="https://software.intel.com/content/www/us/en/develop/download/intel-64-and-ia-32-architectures-optimization-reference-manual.html">software.intel.com</a>上找到，而令人兴奋的新元素是GitHub上的<a href="https://github.com/intel/optimization-manual">intel/optimization-manual</a>。</p><p><a href="https://static.cnbetacdn.com/article/2021/0610/baf49341092aabf.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0610/baf49341092aabf.png" title alt="_]FHR(&#125;$XDT_H9QE%GZD5%F.png" referrerpolicy="no-referrer"></a></p><p>这个新的GitHub资源库提供了与优化手册相配套的工作代码样本。所有这些代码样本都可以通过Linux上的CMake构建系统和使用任何半新的代码编译器在大约任何英特尔Haswell CPU或更新的处理器上轻松地完整构建。</p><p><img src="https://static.cnbetacdn.com/article/2021/0610/262075fddf6b61c.png" title alt="&#125;&#125;_91N@0B3FU_~T52~NHK1V.png" referrerpolicy="no-referrer"></p><p>这些新的代码样本主要涉及AVX/AVX2/FMA优化，INT8深度学习推理，以及AVX-512的使用，以便在针对最新的英特尔CPU（如Xeon Scalable Ice Lake、Tiger Lake和Rocket Lake）时获得实践。很高兴看到英特尔工程师在所有其他开源代码贡献和其他活动之外，继续向开发者社区做出的这些开放性贡献。</p>   
</div>
            