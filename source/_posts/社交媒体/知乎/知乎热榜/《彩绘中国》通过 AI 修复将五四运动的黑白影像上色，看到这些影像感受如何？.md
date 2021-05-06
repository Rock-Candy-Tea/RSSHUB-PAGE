
---
title: '《彩绘中国》通过 AI 修复将五四运动的黑白影像上色，看到这些影像感受如何？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic4.zhimg.com/v2-70ff41ce57600628c93e535257177525_1440w.jpg'
author: 知乎
comments: false
date: Wed, 05 May 2021 07:03:05 GMT
thumbnail: 'https://pic4.zhimg.com/v2-70ff41ce57600628c93e535257177525_1440w.jpg'
---

<div>   
桔了个仔的回答<br><br><h2>感受</h2><p>之前看《你好李焕英》里，有一个表现手法非常让我印象深刻。就是一开始场景是黑白的，然后慢慢变成彩色的，从黑白到彩色的这个过程，让我有种「进入新的现实」的感觉。</p><p>类似的，当我看到当年五四运动这些影像从黑白变成彩色后，仿佛置身五四运动现场，尽管画面分辨率不高，色彩也不那么完美，但就是能给人一种身临其境的感觉，回到一百年前，与青年们一起救亡图存。</p><p>当时的青年尚能挺身而出，忧国忧民，我相信，现代的青年也能奋发图强，肩负起对于这个国家的历史责任，塑造起具有时代光芒的民族精神。</p><p>看了下回答区，大家都对技术原理感兴趣啊，那我来用简单的语言讲讲吧。</p><p><br></p><h2>技术原理</h2><p>AI上色的原理是什么？那我们就需要介绍一种深度学习网络架构了，它就是GAN（这里不是粗话）。GAN不是干饭人的干，而是生成对抗网络（英语：Generative Adversarial Network，简称GAN）。当然，太复杂的技术讲解可能会让读者迷惑，于是我找到一张很直白的原理图。</p><figure data-size="normal"><img src="https://pic4.zhimg.com/v2-70ff41ce57600628c93e535257177525_1440w.jpg" data-caption data-size="normal" data-rawwidth="720" data-rawheight="278" data-default-watermark-src="https://pic1.zhimg.com/v2-96c272454917b9440d6f705f28908df5_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic4.zhimg.com/v2-70ff41ce57600628c93e535257177525_r.jpg" referrerpolicy="no-referrer"></figure><p>GAN网络分两部分，一个是生成器（Generator），一个是鉴别器（Discriminator）。生成器通过对图像上色，然后交给鉴别器。鉴别器判断这一个图片看起来真不真，如果觉得假，鉴别器会返回「修改意见」，让生成器重新试试，直到鉴别器觉得足够真了。如果你觉得还不好懂，我再打个比方，这就好像美术老师指导学生画画的过程，一开始学生画出来的不够好，老师指出，学生尝试改改，老师再检查，再给意见，直到老师满意。</p><p>这就是一张图的上色过程。而视频是一帧帧画面组成的，给视频上色可以理解为通过这个网络架构给视频里的每一帧上色。不过没有这么简单，毕竟视频一秒钟几十帧，一帧帧上色有点慢，而且每一帧之前可能会出现上色效果不一致。所以有的架构会针对细节调整。例如DeOldify采用了NoGAN（一种新型GAN训练模型），用来解决之前DeOldify模型中出现的一些关键问题。例如如视频中闪烁的物体</p><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-45af37fe9489fcea84983de10dcd8c7b_1440w.jpg" data-size="normal" data-rawwidth="500" data-rawheight="375" class="origin_image zh-lightbox-thumb" data-original="https://pic1.zhimg.com/v2-45af37fe9489fcea84983de10dcd8c7b_r.jpg" referrerpolicy="no-referrer"><figcaption>使用NoGAN前，画面闪烁严重</figcaption></figure><figure data-size="normal"><img src="https://pic4.zhimg.com/v2-373651d93f0e4810c7f42fcefe8290e1_1440w.jpg" data-size="normal" data-rawwidth="506" data-rawheight="380" class="origin_image zh-lightbox-thumb" data-original="https://pic4.zhimg.com/v2-373651d93f0e4810c7f42fcefe8290e1_r.jpg" referrerpolicy="no-referrer"><figcaption>使用NoGAN后闪烁减少</figcaption></figure><p>当然，实际还原的色彩其实和原本的色彩是不一样的，仅仅是能让其看起来自然。我做了个实验（AI上色工具稍后介绍到），能看到上色效果和原来的效果并不一样。我下载了这么一张向日葵的照片</p><figure data-size="normal"><img src="https://pic2.zhimg.com/v2-478b3478f3b547e875a42ad4d2692935_1440w.jpg" data-caption data-size="normal" data-rawwidth="600" data-rawheight="400" data-default-watermark-src="https://pic3.zhimg.com/v2-aadb74212b56b330da9fd44dda9f77b3_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic2.zhimg.com/v2-478b3478f3b547e875a42ad4d2692935_r.jpg" referrerpolicy="no-referrer"></figure><p>我手动转成黑白的</p><figure data-size="normal"><img src="https://pic4.zhimg.com/v2-adc76de365d95be9739fd0a0bc93c35b_1440w.jpg" data-caption data-size="normal" data-rawwidth="600" data-rawheight="400" data-default-watermark-src="https://pic2.zhimg.com/v2-8740e18d0f49ef85a72efad5dc10f3ab_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic4.zhimg.com/v2-adc76de365d95be9739fd0a0bc93c35b_r.jpg" referrerpolicy="no-referrer"></figure><p>这时候再让AI上色，咦，向日葵变成雏菊了。不过看起来竟然也有另一番美感。</p><figure data-size="normal"><img src="https://pic3.zhimg.com/v2-2aba1fd268e8c831835495a54105bf84_1440w.jpg" data-caption data-size="normal" data-rawwidth="600" data-rawheight="400" data-default-watermark-src="https://pic3.zhimg.com/v2-c0f85821c4e9a3100683e5adeb0324e6_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic3.zhimg.com/v2-2aba1fd268e8c831835495a54105bf84_r.jpg" referrerpolicy="no-referrer"></figure><p><br></p><p>一般来说，给人上色会更接近实际情况些。因为人的肤色比较有限，判别器里已经学习过人脸的颜色可能是哪些，转换成灰度图像后对应什么颜色值，所以AI不太可能会给黑白的人像涂成绿色脸</p><h2>动手试试</h2><p>如果你是技术小白，你可以直接打开这个网址，你只需要上传一张图片就能自动上色。</p><a href="http://link.zhihu.com/?target=https%3A//deepai.org/machine-learning-model/colorizer" data-draft-node="block" data-draft-type="link-card" data-image="https://pic1.zhimg.com/v2-f180ab0c53af335565724e625a67eaa1_200x0.jpg" data-image-width="259" data-image-height="354" class=" wrap external" target="_blank" rel="nofollow noreferrer">Image Colorization</a><p>例如效果如下：</p><figure data-size="normal"><img src="https://pic3.zhimg.com/v2-a6bb531434a6a1fe14389ad16d86d7a0_1440w.jpg" data-caption data-size="normal" data-rawwidth="1649" data-rawheight="1138" data-default-watermark-src="https://pic3.zhimg.com/v2-b72b782085d652a93d1e5aece095e977_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic3.zhimg.com/v2-a6bb531434a6a1fe14389ad16d86d7a0_r.jpg" referrerpolicy="no-referrer"></figure><p>看起来效果很棒吧。如果你懂点技术但不懂机器学习，可以用DeepAI提供的API。例如python调用方法如下</p><div class="highlight"><pre><code class="language-python3"><span><span class="kn">import</span> <span class="nn">requests</span>
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
</span></code></pre></div><p>如果你想深入研究，建议去fork DeOldify的repo，自己动手玩玩</p><a href="http://link.zhihu.com/?target=https%3A//github.com/jantic/DeOldify" data-draft-node="block" data-draft-type="link-card" class=" external" target="_blank" rel="nofollow noreferrer"><span class="invisible">https://</span><span class="visible">github.com/jantic/DeOld</span><span class="invisible">ify</span><span class="ellipsis"></span></a><p></p>  
</div>
            