
---
title: 'H.266_VVC 标准之面向屏幕应用的编解码技术'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e48cde9b0bab4978adc0c0866738cd35~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 18:13:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e48cde9b0bab4978adc0c0866738cd35~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>作者：许继征</strong></p>
<h2 data-id="heading-0"><strong>概述：</strong></h2>
<p>屏幕内容编码是从H.265/HEVC起引入的面向屏幕应用的编解码技术。H.265/HEVC包含了Hash-based Motion Estimation、Intra Block Copy、Transform Skip、Block-based Differential Pulse-Code Modulation、Adaptive Motion Vector Resolution、Palette Mode和Adaptive Colour Transform。除了删除了在序列级别的Adaptive Motion Vector Resolution（在序列级别规定了是否需要开启帧级别的控制，在H.266/VVC里面被应用更广泛的工具取代），其它的工具在H.266/VVC里面有一系列调整。本文将介绍这一系列调整。</p>
<h1 data-id="heading-1">1. 介绍</h1>
<p>针对屏幕内容的应用，最早先在标准里提出了Screen Content Coding的概念 <strong>[1]</strong> 。并在H.265/HEVC、AV1 <strong>[2]</strong> 和H.266/VVC里引入了众多的编解码工具。本文将介绍H.266/VVC中的主要屏幕编解码工具。</p>
<h1 data-id="heading-2">2. Hash-based Motion Estimation</h1>
<p>在涉及屏幕内容时，通常下一帧的一部分会是上一帧的精确拷贝。利用这个特点我们可以将屏幕内容分开处理，来快速判断是否有精确匹配 <strong>[3]</strong>。在参考帧的原始信号上，计算出对每个位置的4x4～64x64的循环校验码即CRC值，再在当前帧分块的位置算出对应块的原始值的CRC值。通过比较这两个CRC值可以得到是否精确匹配。这部分工具是非标准的，但对应用非常重要。</p>
<h1 data-id="heading-3">3. Intra Block Copy</h1>
<p>Intra Block Copy简称为IBC，针对的是本帧的非相邻块的预测。IBC的预测单元是Coding Unit，但只对64x64及以下的Coding Unit用。H.266/VVC里面新增加的是VPDU（Virtual Pipeline Data Units）内存的重利用和Virtual buffer的概念。VPDU是片上内存的基本单元，和CTU的对应关系如下表：</p>
<p>表1. CTU和VPDU的对应关系：</p>





















<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>CTU = 128x128</td><td>VPDU = 64x64</td></tr><tr><td>CTU = 64x64</td><td>VPDU = 64x64</td></tr><tr><td>CTU = 32x32</td><td>VPDU = 32x32</td></tr></tbody></table>
<p><img alt="12.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e48cde9b0bab4978adc0c0866738cd35~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p align="center">图1. CTU=128x128的时候的Virtual buffer view和Picture view</p>
<p>图1所示的是CTU=128x128的时候的Virtual buffer view和Picture view的对应，其中每个方块对应的是64x64的luma块。灰色的块是invalid区域（有任何一个sample落入该区域就算是invalid的）、蓝色是当前VPDU、绿色是可以参考的VPDU[4]。
下图显示的是CTU=64x64的时候的Virtual buffer view和Picture view的对应。</p>
<p><img alt="13.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8d8830b0b8f4e06804111d2b8c100bb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p align="center">图2. CTU=64x64的时候的Virtual buffer view和Picture view</p>
所以VPDU（64x64）的内存只需要维持4个。另外，对于I帧亮度和色度用不同的分块树的情况禁止了色度的IBC的，相对应的色度块就只能选其它的帧内模式。还有，对Local dual tree（P或B帧里对应的防止块过小的限制）也不能用色度的IBC。
<h1 data-id="heading-4">4. Transform Skip</h1>
<p>Transform Skip在Screen Content Coding里面应用很广。在H.266/VVC里，作为一个变换单元的工具，Transform Skip做了额外的设计。在解码端Transform Skip先是从左往右、从上往下扫描每个子块，再在子块内部做对角线扫描 <strong>[5]</strong>。对每个非0系数至多会对应扫描5遍，分别对比了小系数的幅度编码。相应地设置一个跟面积为1.75倍的限额，超过了这个限额就全部转为无上下文的编码。</p>
<h1 data-id="heading-5">5. Block-based Differential Pulse-Code Modulation</h1>
<p>Block-based Differential Pulse-Code Modulation，简写为BDPCM，是应用在帧内预测的模式。应用时，都会推断成Transform Skip，并且有横向的或者是纵向的区别。纵向模式时候，解码过程中残差r(i,j)会减去上一行的重构值</p>
<pre><code class="copyable">r(i,j)=r(i,j)+r'(i-1,j),i>0                                                   （1）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>横向也类似。</p>
<h1 data-id="heading-6">6. Adaptive Colour Transform</h1>
<p>Adaptive Colour Transform应用于4:4:4的GBR格式（其它格式也能用，但好处不大）。在解码端Adaptive Colour Transform是应用于解码残差和重构JCCR、以及反变换之间的步骤。当Coding Unit的相应标志位为1时（此时只可能是三个分量都是一个解码树），解码器在残差域进行如下操作：</p>
<pre><code class="copyable">tmp = Y – (Cg >> 1)
G  = Cg + tmp
B  = tmp – (Co >> 1)
R  = B + Co                                  
（2）             
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中Y、Cg、Co分别代表三个分量的残差值，R、G、B分别代表恢复的三个分量的残差值。为了平衡能量，反量化的时候QP分别加上了-5、1和3。</p>
<h1 data-id="heading-7">7. Palette Mode</h1>
<p>Palette Mode是针对4:4:4 Profile（包括4:4:4 Profile下的4:2:0和4:2:2）设计的，与H.265/HEVC下的Palette mode类似。在Palette Mode里面，可以有1个（只是Luma）、2个（只是Chroma）和3个（Luma和Chroma的联合编码）。对于3个预测平面（定义为一个三元组列表，每一帧的初始为空）的设置，相对应的最大预测长度为63，相对应的最大的每个块的索引值是31；对于1或者2这两个值分别为31和15。跟HEVC一样，不管是几个预测平面，块里面都是分横向或者纵向的蛇形扫描。最后，Palette Mode会对Coding Unit进行不大于16个样本的分割，然后去扫描 <strong>[6]</strong>。</p>
<h1 data-id="heading-8">8. 性能</h1>
<p>针对4:2:0格式，H.266/VVC Main 10档次有如上述2、3、4、5小节中介绍的编码工具可以用，而H.265/HEVC的Version 1相对应的只有4x4的Transform Skip可以用。性能对比如下表。</p>
<p>表2: VTM-9.0 <strong>[7]</strong> 对比HM-16.21 <strong>[8]</strong>, 4:2:0格式 <strong>[9]</strong> ：
<img alt="图1.jpeg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f649ef1fdfe54578a85ced3e55f870a5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>而对于4:4:4格式，H.266/VVC Main 10 4:4:4档次能用上述2、3、4、5、6、7小节中介绍的编码工具。性能对比如下表。</p>
<p>表3: VTM-9.0对比HM-16.21+SCM-8.8 <strong>[8]</strong>, 4:4:4格式 <strong>[9]</strong> ：
<img alt="图2.jpeg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55756d9466474a07a754c739f44f8636~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            