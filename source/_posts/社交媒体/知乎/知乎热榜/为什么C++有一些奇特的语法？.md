
---
title: '为什么C++有一些奇特的语法？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic2.zhimg.com/v2-66c0140c495ae5741767f6c9b7169ba3_1440w.jpg?source=b1748391'
author: 知乎
comments: false
date: Mon, 04 Jul 2022 03:59:05 GMT
thumbnail: 'https://pic2.zhimg.com/v2-66c0140c495ae5741767f6c9b7169ba3_1440w.jpg?source=b1748391'
---

<div>   
IceBear的回答<br><br><blockquote data-pid="EpbHPa55">当真没有见过哪一门编程语言用上了<<</blockquote><h2>我见过，不但用上了 >>  << 做位移，甚至还用它们来表示输入输出。</h2><p><br></p><h2>猜猜我是谁？</h2><figure data-size="normal"><img src="https://pic2.zhimg.com/v2-66c0140c495ae5741767f6c9b7169ba3_1440w.jpg?source=b1748391" data-caption data-size="normal" data-rawwidth="674" data-rawheight="104" class="origin_image zh-lightbox-thumb" data-original="https://pic2.zhimg.com/v2-66c0140c495ae5741767f6c9b7169ba3_r.jpg?source=b1748391" referrerpolicy="no-referrer"></figure><figure data-size="normal"><img src="https://pic2.zhimg.com/v2-b5eda20133e8c98dfefa3b698677ab96_720w.jpg?source=b1748391" data-caption data-size="normal" data-rawwidth="416" data-rawheight="194" data-default-watermark-src="https://picx.zhimg.com/v2-83d87d4a4a60db94a490dc70476928a6_720w.jpg?source=b1748391" class="content_image" referrerpolicy="no-referrer"></figure><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-a2dd3678ae37199b26852952bc6dd952_720w.jpg?source=b1748391" data-caption data-size="normal" data-rawwidth="382" data-rawheight="221" data-default-watermark-src="https://pic3.zhimg.com/v2-9810b1c4413d34207d926daf3e0f9b42_720w.jpg?source=b1748391" class="content_image" referrerpolicy="no-referrer"></figure><p data-pid="aCWpuOBP">。</p><p data-pid="XmCoueQB">。</p><p data-pid="UoUuhjEb">。</p><p data-pid="zWn9hySn">。</p><p data-pid="Sb4Ktp16">。</p><p data-pid="mm8s9NKC">。</p><p data-pid="ed9nvlHe">。</p><p><br></p><h2>Python</h2><figure data-size="normal"><img src="https://pica.zhimg.com/v2-118bbfc578546d309b5f6c279db20d37_1440w.jpg?source=b1748391" data-caption data-size="normal" data-rawwidth="1919" data-rawheight="1079" data-default-watermark-src="https://pic1.zhimg.com/v2-8f0aeae7a8578d6877410ab8d89d223c_720w.jpg?source=b1748391" class="origin_image zh-lightbox-thumb" data-original="https://pica.zhimg.com/v2-118bbfc578546d309b5f6c279db20d37_r.jpg?source=b1748391" referrerpolicy="no-referrer"></figure><div class="highlight"><pre><code class="language-python"><span><span class="k">class</span> <span class="nc">integer</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>


<span class="k">class</span> <span class="nc">istream</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__rshift__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg</span><span class="p">):</span>
        <span class="n">arg</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="nb">input</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">self</span>

<span class="n">cin</span> <span class="o">=</span> <span class="n">istream</span><span class="p">()</span>


<span class="k">class</span> <span class="nc">ostream</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__lshift__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">arg</span> <span class="o">==</span> <span class="n">endl</span><span class="p">:</span>
            <span class="n">endl</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">""</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span>

<span class="n">cout</span> <span class="o">=</span> <span class="n">ostream</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">endl</span><span class="p">(</span><span class="n">out</span><span class="p">:</span> <span class="n">ostream</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>

<span class="n">x</span> <span class="o">=</span> <span class="n">integer</span><span class="p">()</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">integer</span><span class="p">()</span>

<span class="n">cin</span> <span class="o">>></span> <span class="n">x</span> <span class="o">>></span> <span class="n">y</span><span class="p">;</span>
<span class="n">cout</span> <span class="o"><<</span> <span class="s2">"Hello World "</span> <span class="o"><<</span> <span class="n">x</span> <span class="o"><<</span> <span class="n">y</span> <span class="o"><<</span> <span class="n">endl</span><span class="p">;</span>
</span></code></pre></div><p></p>  
</div>
            