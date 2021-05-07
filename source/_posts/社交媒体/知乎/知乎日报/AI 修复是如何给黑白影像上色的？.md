
---
title: 'AI 修复是如何给黑白影像上色的？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic2.zhimg.com/v2-9f4e5c9c9e3fda1b26496f2fbb2a0578_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2021-05-07 04:06:08
thumbnail: 'https://pic2.zhimg.com/v2-9f4e5c9c9e3fda1b26496f2fbb2a0578_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">
《彩绘中国》通过 AI 修复将五四运动的黑白影像上色，看到这些影像感受如何？

<div class="answer">

<strong>
<img class="avatar" src="https://pic2.zhimg.com/v2-9f4e5c9c9e3fda1b26496f2fbb2a0578_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">桔了个仔，</span><span class="bio">人工智能 | 数据科学 |AI风控与反洗钱 | 码农</span>
<a href="https://www.zhihu.com/question/457739121/answer/1868733796" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p><strong>感受</strong></p>
<p>之前看《你好李焕英》里，有一个表现手法非常让我印象深刻。就是一开始场景是黑白的，然后慢慢变成彩色的，从黑白到彩色的这个过程，让我有种「进入新的现实」的感觉。</p>
<p>类似的，当我看到当年五四运动这些影像从黑白变成彩色后，仿佛置身五四运动现场，尽管画面分辨率不高，色彩也不那么完美，但就是能给人一种身临其境的感觉，回到一百年前，与青年们一起救亡图存。</p>
<p>当时的青年尚能挺身而出，忧国忧民，我相信，现代的青年也能奋发图强，肩负起对于这个国家的历史责任，塑造起具有时代光芒的民族精神。</p>
<p>看了下回答区，大家都对技术原理感兴趣啊，那我来用简单的语言讲讲吧。</p>
<p><strong>技术原理</strong></p>
<p>AI 上色的原理是什么？那我们就需要介绍一种深度学习网络架构了，它就是 GAN（这里不是粗话）。GAN 不是干饭人的干，而是生成对抗网络（英语：Generative Adversarial Network，简称 GAN）。当然，太复杂的技术讲解可能会让读者迷惑，于是我找到一张很直白的原理图。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-70ff41ce57600628c93e535257177525_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure><p>GAN 网络分两部分，一个是生成器（Generator），一个是鉴别器（Discriminator）。生成器通过对图像上色，然后交给鉴别器。鉴别器判断这一个图片看起来真不真，如果觉得假，鉴别器会返回「修改意见」，让生成器重新试试，直到鉴别器觉得足够真了。如果你觉得还不好懂，我再打个比方，这就好像美术老师指导学生画画的过程，一开始学生画出来的不够好，老师指出，学生尝试改改，老师再检查，再给意见，直到老师满意。</p>
<p>这就是一张图的上色过程。而视频是一帧帧画面组成的，给视频上色可以理解为通过这个网络架构给视频里的每一帧上色。不过没有这么简单，毕竟视频一秒钟几十帧，一帧帧上色有点慢，而且每一帧之前可能会出现上色效果不一致。所以有的架构会针对细节调整。例如 DeOldify 采用了 NoGAN（一种新型 GAN 训练模型），用来解决之前 DeOldify 模型中出现的一些关键问题。例如如视频中闪烁的物体</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-45af37fe9489fcea84983de10dcd8c7b_720w.gif?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>使用 NoGAN 前，画面闪烁严重</figcaption></figure><figure><img class="content-image" src="https://pic1.zhimg.com/v2-373651d93f0e4810c7f42fcefe8290e1_720w.gif?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>使用 NoGAN 后闪烁减少</figcaption></figure><p>当然，实际还原的色彩其实和原本的色彩是不一样的，仅仅是能让其看起来自然。我做了个实验（AI 上色工具稍后介绍到），能看到上色效果和原来的效果并不一样。我下载了这么一张向日葵的照片</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-478b3478f3b547e875a42ad4d2692935_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure><p>我手动转成黑白的</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-adc76de365d95be9739fd0a0bc93c35b_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure><p>这时候再让 AI 上色，咦，向日葵变成雏菊了。不过看起来竟然也有另一番美感。</p>
<figure><img class="content-image" src="https://pic4.zhimg.com/v2-2aba1fd268e8c831835495a54105bf84_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure><p>一般来说，给人上色会更接近实际情况些。因为人的肤色比较有限，判别器里已经学习过人脸的颜色可能是哪些，转换成灰度图像后对应什么颜色值，所以 AI 不太可能会给黑白的人像涂成绿色脸</p>
<p><strong>动手试试</strong></p>
<p>如果你是技术小白，你可以直接打开这个网址，你只需要上传一张图片就能自动上色。</p>
<p><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//deepai.org/machine-learning-model/colorizer" target="_blank" rel="nofollow noreferrer">Image Colorization</a></p>
<p>例如效果如下：</p>
<figure><img class="content-image" src="https://pic4.zhimg.com/v2-a6bb531434a6a1fe14389ad16d86d7a0_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure><p>看起来效果很棒吧。如果你懂点技术但不懂机器学习，可以用 DeepAI 提供的 API。例如 python 调用方法如下</p>
<div class="highlight">
<pre><code class="language-python3"><span class="kn">import</span> <span class="nn">requests</span>
<span class="n">r</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
    <span class="s2">"https://api.deepai.org/api/colorizer"</span><span class="p">,</span>
    <span class="n">data</span><span class="o">=</span><span class="p">&#123;</span>
        <span class="s1">'image'</span><span class="p">:</span> <span class="s1">'YOUR_IMAGE_URL'</span><span class="p">,</span>
    <span class="p">&#125;,</span>
    <span class="n">headers</span><span class="o">=</span><span class="p">&#123;</span><span class="s1">'api-key'</span><span class="p">:</span> <span class="s1">'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'</span><span class="p">&#125;</span>
<span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">r</span><span class="o">.</span><span class="n">json</span><span class="p">())</span>


<span class="c1"># Example posting a local image file:</span>

<span class="kn">import</span> <span class="nn">requests</span>
<span class="n">r</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
    <span class="s2">"https://api.deepai.org/api/colorizer"</span><span class="p">,</span>
    <span class="n">files</span><span class="o">=</span><span class="p">&#123;</span>
        <span class="s1">'image'</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="s1">'/path/to/your/file.jpg'</span><span class="p">,</span> <span class="s1">'rb'</span><span class="p">),</span>
    <span class="p">&#125;,</span>
    <span class="n">headers</span><span class="o">=</span><span class="p">&#123;</span><span class="s1">'api-key'</span><span class="p">:</span> <span class="s1">'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'</span><span class="p">&#125;</span>
<span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">r</span><span class="o">.</span><span class="n">json</span><span class="p">())</span>
</code></pre>
</div>
<p>如果你想深入研究，建议去 fork DeOldify 的 repo，自己动手玩玩</p>
<p><a class=" external" href="http://link.zhihu.com/?target=https%3A//github.com/jantic/DeOldify" target="_blank" rel="nofollow noreferrer"><span class="invisible">https://</span><span class="visible">github.com/jantic/DeOld</span><span class="invisible">ify</span><span class="ellipsis"></span></a></p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/457739121">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            