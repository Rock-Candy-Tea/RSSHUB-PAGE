
---
title: '费米实验室的最新研究结果表明 W 玻色子的质量严重偏离标准模型的理论预言，如何看待这一结果？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic1.zhimg.com/v2-fd87084bd5373d1875e6391e90309507_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-04-09 08:10:35
thumbnail: 'https://pic1.zhimg.com/v2-fd87084bd5373d1875e6391e90309507_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">


<div class="answer">

<strong>
<img class="avatar" src="https://pic1.zhimg.com/v2-fd87084bd5373d1875e6391e90309507_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">雪峰的自由之路，</span><span class="bio">粒子天体物理 实验数据分析</span>
<a href="https://www.zhihu.com/question/526650510/answer/2429182613" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>实验测到的 W 玻色子质量比标注模型高 7 sigma。我就从数据分析的角度简单讨论一下结果。</p>
<p><strong>摘要</strong></p>
<p>这篇文章是 CDF 实验基于 2002 年 -2011 年间数据对 W 玻色子质量的测量。测量结果和标准模型的预言不相容。「该不相容是统计涨落造成的」的概率小于 7 sigma，或者说地球从诞生至今会发生四次，因此可以排除该假设。如果这不是分析的问题造成的，那么这意味着我们需要扩充标注模型，意味着有新的物理。</p>
<p>我过去的工作主要是实验数据分析，那么我就从实验数据分析的角度讨论一下这个分析。作为重点内容，我将这部分内容提前。在后半部分介绍实验的背景。</p>
<p><strong>对分析的讨论</strong></p>
<p>这个分析要测的是 W 玻色子的质量，它和分布的峰的位置相关。一般来说，对峰的位置的测量的分析要比对流强、事例率、或者散射截面的测量要更干净一些。本底模型做的不好，对结果的影响要更小一些。当然，这个分析的结果的精度太高了，～千分之一，因此本底形状的的影响也不一定小。作者在表 2 中总结了系统误差来源。</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-65b97e726e44cb35c2b116c889aebd80_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>TABLE 2. Uncertainties on the combined MW result.OPEN IN VIEWER</figcaption></figure>
<p>直观的来说，对结果影响最大的就是能标的准确性（即量能器对产物能量的测量的准确性）。在这个分析中，作者用 J/psi 粒子的能量刻度了探测器能标。通过刻度发现探测器的能标偏低，低了 -0.1393±0.0026%，见图 2。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-dd61a252d7afd383819ef29bae81e80f_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>FIG. 2. Calibration of track momentum and electron’s calorimeter energy.(A) Fractional deviation of momentum Δ / Δp/p (per mille) extracted from fits to the / → J/ψ→μμ resonance peak as a function of the mean muon unsigned curvature ⟨1/ T⟩1/pTμ (blue circles). A linear fit to </figcaption></figure>
<p>探测器的能标的精度可能会随能量变化。这就好比一把不均匀的尺子在 10cm 处短了 1%，可能在 20cm 处短 2%。J/psi 粒子的能量约 3 GeV，W 玻色子的能量约 80 GeV。3 GeV 初我们修正了千分之一级别的偏差（bias）之后，剩余的偏差（bias）在十万分之二的量级。</p>
<p>我们不能简单的假设在 80 GeV 处修正后的偏差（bias）还是十万分之一。万一和尺子一样变形是不均匀的怎么办？作者想的办法是用 Z 玻色子来估计系统误差。Z 玻色子的质量约 90 GeV。作者发现修正后 Z 玻色子的质量的测量结果和理论预言值相差约十万分之五。<strong>还是拿尺子打比方。如果尺子的形变程度是均匀的增大的，</strong>那么在 80 GeV 处能表的精度也应该是十万分之四左右的量级，这就和作者估计的系统误差<sup>[1]</sup>一致了。</p>
<p>但是这有一个问题：<strong>这个修正太！大！了！</strong>它的幅度是精度的 100 倍，而且这个修正是可以被避免的。作者完全可以修改重建和模拟算法，从源头上消灭这个偏差（bias）。这种在事后做的修正都是不好的 analysis smell。</p>
<p>既然有不好的 smell，我们就要问，为什么没有从源头上直接修改重建 / 模拟算法消灭掉这个偏差？</p>
<ul>
<li>一种可能性是作者用了另外的办法刻度重建 / 模拟算法。这就意味着两套刻度系统有 tension。那为什么不放弃第一套系统用第二套系统？是不是放弃了第一套系统别的结果就不对了？</li>
<li>另一种可能性是作者没有时间来做这个修正。这不太可能。十年都等了，不急这一时。</li>
<li>还有一种可能是作者不能从头修掉这个千分之一的 bias，它会带来别的问题。举个例子，电磁量能器的 scintillation yield 一调，能标是对了，可能能量分辨率就不对了。事例率这么高，能量分辨率不对会拟合不上，只能后期强行做修正，只 scale 能量不修改能量分辨率。</li>
</ul>
<p>此外，再对比一下 ATLAS 的结果：</p>
<p><a class=" external" href="http://link.zhihu.com/?target=https%3A//link.springer.com/article/10.1140/epjc/s10052-017-5475-4" target="_blank" rel="nofollow noreferrer"><span class="invisible">https://</span><span class="visible">link.springer.com/artic</span><span class="invisible">le/10.1140/epjc/s10052-017-5475-4</span><span class="ellipsis"></span></a></p>
<p>注意到 CDF 这次结果的统计误差是 6.4 MeV，而 ATLAS 这篇文章的统计误差是 7 MeV，因此 ATLAS 这篇文章的统计量和 CDF 的是类似的。而 ATLAS 的系统误差要大得多，主要多了“模型误差”，或者不同的产生子导致的 PDF 形状的差别引起的结果的差别。</p>
<p>由于 ATLAS 的结果受限于系统误差，取更多的数不能缩小最终的误差，因此要想检验 CDF 的结果，取更多的数是不行了，需要想别的办法。</p>
<p>最后，（感谢评论里朋友的提醒）这结果能被发表在 Science 上，那么它肯定是被审稿人认可的。所以大家也不用太担心结果的正确性。分析本身也不是一件简单的工作，将来还是要等 LHC 来检验这个结果。</p>
<p>下面是背景介绍部分。</p>
<p><strong>作者做了什么？</strong></p>
<p>CDF 是一个位于兆电子伏特加速器（Tevatron）上的谱仪、或者复合粒子探测器<sup>[2]</sup>。我们对撞了正反质子，收集了对撞产物的能量、动量的分布。利用分布的峰值计算了 W 玻色子的质量。</p>
<p><strong>费米国家实验室的 Tevatron 对撞机</strong></p>
<p>Tevatron 是美国费米国家实验室的对撞机<sup>[3]</sup>。费米国家实验室位于伊利诺伊州的巴塔利亚 Batavia, Illinois，如下图所示，在芝加哥湖、芝加哥的西南城郊。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-0601da2425241a7d70885d9beaf34baf_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>费米国家实验室在美国的地理位置。来自 google map。</figcaption></figure>
<p>Tevatron 对撞机从 1968 年 12 月开始动工，于 1970 年 12 月开始对撞。在 2011 年左右，同类型的欧洲大型强子对撞机（LHC）<sup>[4]</sup>的亮度是 Tevatron 对撞机的十倍，且能量也是 Tevatron 的～3.6 倍，费米国家实验室在 2011 年 9 月 30 日关闭了 Tevatron。Tevatron 最着名的成果包括发现了顶夸克。对撞机将正反质子加速，加速后的正反质子分别在圆环形真空轨道内顺时针和逆时针运动，在对撞点处受磁场控制偏向后对撞。实物图和示意图分别如下：</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-5ff0bf471dda4208ba7ed64498c04937_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>By Fermilab, Reidar Hahn - [1] from [2]en.wikipedia.org, upload from Riffsyphon1024, Public Domain, https://commons.wikimedia.org/w/index.php?curid=134075</figcaption></figure>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-8c6700de086494ee95676bb1a5055268_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>费米国家实验室关于 Tevatron 对撞机的介绍。https://www.fnal.gov/pub/tevatron/</figcaption></figure>
<p><strong>CDF 实验</strong></p>
<p>Collider Detector at Fermilab（CDF）是一个位于 Tevatron 上的谱仪<sup>[5]</sup>。谱仪像洋葱一样分成很多层，每层的职责不一样。正负质子在对撞后会变成新的粒子再飞出产生一条条径迹。谱仪内不同的层可以测量不同类型的例子的动量和能量。部分层则被用来鉴别粒子种类。CDF 的实物图和示意图分别如下。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-f49542848eceefda17a81a5d35c6c4a8_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>By Bodhitha at the English-language Wikipedia, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=17063375</figcaption></figure>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-b6a42a628104976521a28409b04c1391_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>The Collider Detector at Fermilab recorded high-energy particle collisions produced by the Tevatron collider from 1985 to 2011. About 400 scientists at 54 institutions in 23 countries are still working on the wealth of data collected by the experiment. Photo: Fermilab</figcaption></figure>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-2f3600d25c1d02c9e8c6b8214ec48a2d_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>Search for Bs0→μμ and B0→μμ decays with the full CDF Run II data set - Scientific Figure on ResearchGate. Available from: https://www.researchgate.net/figure/Cutaway-isometric-view-of-the-CDF-II-detector_fig1_259884756 [accessed 8 Apr, 2022]</figcaption></figure>
<p><strong>通过对撞产物的能动量分布得到 W 玻色子质量</strong></p>
<p>见文章中的图 4。在清洗了数据之后，我们收集了电子道和谬子道的末态产物的能动量分布，共 6 个分布。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-404007c85b22b2bbe69a977b2a9f0dd8_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>Decay of the W boson.(A to C) Distributions for mT (A), ℓTpTℓ (B), and TpTν(C) for the muon channel. (D to F) Same as in (A) to (C) but for the electron channel. The data (points) and the best-fit simulation template (histogram) including backgrounds (shaded regions) are shown</figcaption></figure>
<p>他们都可以被用来测量 W 玻色子的质量。测量结果见下表。其中第一列是分布的名称，第二列是用该行所对应的分布测量的 W 玻色子的质量，第三列是模型和数据的吻合程度，越小越好。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-21387256acb4368bf5057522da544020_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>TABLE 1. Individual fit results and uncertainties for the MW measurements.The fit ranges are 65 to 90 GeV for the mT fit and 32 to 48 GeV for the ℓTpTℓ and TpTν fits. The χ2 of the fit is computed from the expected statistical uncertainties on the data points. The bottom row s</figcaption></figure>
<p><strong>结论是什么？</strong></p>
<p>CDF 测量了 W 玻色子的质量，为 80.4335±0.0094 GeV。这和当前标注模型的预言值 80.357±0.006 GeV 不相容。这种差别完全是随机涨落造成的概率小于 7 sigma，即地球从诞生至今平均会发生四次，因此我们认为这种不相容不是统计涨落造成的，他们真的不同。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-6d38b5e39eea148617eafe740a1516a8_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>Comparison of this CDF II measurement and past MW measurements with the SM expectation.The latter includes the published estimates of the uncertainty (4 MeV) due to missing higher-order quantum corrections, as well as the uncertainty (4 MeV) from other global measurements used as</figcaption></figure>
<p><strong>为什么会不同？</strong></p>
<p>事实上，在这次实验之前理论和实验结果就已经有一定的 tension 了，不过是 2 sigma 级别<sup>[6]</sup>，有可能只是统计涨落造成的。在<sup>[6]</sup>中，作者将标准模型扩充到最小 R 对称的超对称标准模型（Minimal R-symmetric Supersymmetric Standard Model，MRSSM），那么 W 玻色子的质量就应该更大。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-ff4988124ace717ecb78589916a7850e_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>蓝色实心线：MRSSM 对 W 玻色子质量的预言。</figcaption></figure>
<p>考虑 CDF 给出的 W 玻色子的质量为 80.4335±0.0094 GeV，那么在 MRSSM 模型下超对称粒子的质量约为 1 TeV。</p>
<p><strong>标准模型中 W 玻色子的质量是怎么来的？</strong></p>
<p>这里只简要的介绍一下。</p>
<p>众所周知，我们要先写一个 Lagrangian。这个 Lagrangian 应该满足各种各样的对称性，因为物理规律和人类如何研究它、如何选取坐标系、Gauge 无关。</p>
<p>为了满足洛伦兹不变形，Lagrangian 应该写成逆变 - 协变张量。为了满足轻子数守恒等，微分算子应该换成包含媒介子的“超级微分算子”：</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Cpartial_+%5Cmu+%5CRightarrow+D_%5Cmu%28x%29+%3D+%5Cpartial_%5Cmu+%2B+%5Cfrac%7Bi%7D%7B2%7D+g+%5Cunderline%7BA%7D_%5Cmu%28x%29+%5Ccdot+%5Cunderline%5Ctau++%2B+%5Cdfrac%7Bi%7D%7B2%7D+g%27+B_%5Cmu%28x%29%5C%5C" alt referrerpolicy="no-referrer"></p>
<p>然后引入满足对称性的 Higgs 标量场</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5CPhi%28x%29" alt referrerpolicy="no-referrer"></p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Cmathcal%7BL%7D_%7B%5Crm+Higgs%7D+%3D+%28D_%5Cmu%5CPhi%29%5E%5Cdagger%28D%5E%5Cmu%5CPhi%29+-+%5Cmu%5E2+%5CPhi%5E%5Cdagger%5CPhi+-+%5Clambda+%28%5CPhi%5E%5Cdagger%5CPhi%29%5E2%5C%5C+" alt referrerpolicy="no-referrer"></p>
<p>Higgs 粒子会滑到能量最低处</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=V%28%5CPhi%29+%3D+%5Cmu%5E2%5CPhi%5E%5Cdagger%5CPhi+%2B+%5Clambda%28%5CPhi%5E%5Cdagger%5CPhi%29%5E2+%3D+%5Clambda%5Cleft%28%5CPhi%5E%5Cdagger%5CPhi-%5Cfrac%7Bv%5E2%7D%7B2%7D%5Cright%29%5E2+%5C%5C+%5CPhi%28x%29+%3D+%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D0%5C%5Cv%2BH%28x%29%5Cend%7Barray%7D%5Cright%29%5C%5C" alt referrerpolicy="no-referrer"></p>
<p>将这两个式子带入满足对称的 Lagrangian，对称性就自发的被破坏了，产生了质量项</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%7D%5Cmathcal%7BL%7D_%7B%5Crm+Higgs%7D%26+%3D+%5Cfrac%7B1%7D%7B2%7D%28%5Cpartial+H%29%5E2+%2B+%5Cfrac%7Bg%5E2%7D%7B4%7D%28v%2BH%29%5E2W_%5Cmu%5E%5Cdagger+W%5E%5Cmu+%2B+...%5C%5C+%26%3D+...+%2B+%5Cfrac%7Bg%5E2v%5E2%7D%7B4%7DW_%5Cmu%5E%5Cdagger+W%5E%5Cmu%2B...+%5Cend%7Balign%7D%5C%5C" alt referrerpolicy="no-referrer"></p>
<p>这样 W 玻色子就有质量了。</p>
<p>经提醒提醒这里也不一定需要新模型，参考 <a class="member_mention" href="http://www.zhihu.com/people/61ae1075562184cc6aa91a2f09394ee3">@二甲氨基苯甲醛</a> 的答案</p>
<p><a class="internal" href="https://www.zhihu.com/question/526650510/answer/2429597393">费米实验室的最新研究结果表明 W 玻色子的质量严重偏离标准模型的理论预言，如何看待这一结果？</a></p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/526650510">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            