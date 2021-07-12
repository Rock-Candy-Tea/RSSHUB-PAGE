
---
title: '有趣的JS存储'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0d9e94946ef4f16afe563d05ec7876b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 02:03:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0d9e94946ef4f16afe563d05ec7876b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前前言</h3>
<p>大家好我是推啊前端团队的<a href="https://juejin.cn/user/4371313963840669" target="_blank" title="https://juejin.cn/user/4371313963840669">展程</a>同学。</p>
<p>今天给大家分享一下关于JS存储的问题。</p>
<p>建议阅读时间：<strong>5-10</strong>分钟。</p>
<hr>
<h3 data-id="heading-1">序章</h3>
<p>首先看一道经典的关于JS存储的题目，来一场紧张又刺激的脑内吃鸡大战吧：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = &#123;<span class="hljs-attr">n</span>:<span class="hljs-number">1</span>&#125;;
a.x = a = &#123;<span class="hljs-attr">n</span>:<span class="hljs-number">2</span>&#125;;
<span class="hljs-built_in">console</span>.log(a.x);
<span class="hljs-built_in">console</span>.log(a);·
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问输出？
想必大家心中都有答案了 ...
结果很显然是有趣的，</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0d9e94946ef4f16afe563d05ec7876b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这里有部分现场观众朋友就问了，这特喵咋undefined？不是赋值了吗？别急先别骂人，往下看：</p>
<hr>
<h3 data-id="heading-2">探索时刻</h3>
<p>我们先将代码这样修改：</p>
<pre><code class="hljs language-js copyable" lang="js">a.x = a = &#123;<span class="hljs-attr">n</span>:<span class="hljs-number">2</span>&#125;;   ---- >  a = a.x = &#123;<span class="hljs-attr">n</span>:<span class="hljs-number">2</span>&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33bb35f5fdcc4f42b0bd08fec810b375~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结果显然是一致的，不论是先给 a 赋值还是先给 a.x 赋值结果都是一致的，
查了一些资料后，得知这等式中 . 的优先级别是最高的，</p>
<p>因此这题的思路：</p>
<p><strong>JS会把变量存到栈中，而对象则会存在堆中。</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97dbac1d692642fca2fab5d441abd671~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>第一行代码：变量 a 的指针指向堆栈；</li>
<li>第二行代码：a.x = a = &#123;n:2&#125;;   堆1中的变量对像X指向堆2 &#123; n:2 &#125;， 接着给a赋值 a=&#123;n:2&#125; ,a的指针被改变指向堆2，然后堆1没有被指针指向，被GC回收，因此输出的 a.x 是underfinde 而 a 的值是 &#123;n:2&#125;；</li>
</ol>
<p>理解上述代码只需要稍微理解一下js变量储存：</p>
<p>大家都知道，JavaScript中的变量类型分为两种，一种是<strong>基本数据类型</strong>，另外一种就是<strong>引用类型</strong>。</p>
<p>两种数据类型的存储方式在JS中也有所不同。</p>
<p>另外，内存分为<strong>栈区（stack）和堆区（heap）</strong>，然后在JS中开发人员并不能直接操作堆区，堆区数据由JS引擎操作完成，那这二者在存储数据上到底有什么区别呢？</p>
<hr>
<h3 data-id="heading-3">揭晓时刻</h3>
<p>一幅图告诉你：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a611ecd722448548e987dec45b9c938~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　JS中变量的定义在内存中包括三个部分：</p>
<ul>
<li><strong>变量标示</strong>　　（比如上图中的Str，变量标示存储在内存的栈区）</li>
<li><strong>变量值</strong>　　  （比如上面中的Str的值souvenir或者是obj1对象的指向堆区地址，这个值也是存储在栈区）</li>
<li><strong>对象</strong>　　    （比如上图中的对象1或者对象2，对象存储在堆区）</li>
</ul>
<p>也就是说，对于基本数据类型来说，只使用了内存的栈区。
我们再做一个有趣的改动：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = &#123;<span class="hljs-attr">n</span>:<span class="hljs-number">1</span>&#125;;
<span class="hljs-keyword">var</span> b=a;
a.x = a = &#123;<span class="hljs-attr">n</span>:<span class="hljs-number">2</span>&#125;;
<span class="hljs-built_in">console</span>.log(a.x);
<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-built_in">console</span>.log(b);
<span class="hljs-built_in">console</span>.log(b.x);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到我们并没有对 b 进行操作但是 b.x 等于&#123;n:2&#125;，这是一个被操作过的值，就如上述可知 b的指针指向堆1，所以堆没有被回收，而被显示出来了 ~</p>
<p>从这么一个简单例子，你是否对JS存储机制有了新的认识呢 ~</p>
<p>欢迎大佬们的指正和各种蹂躏调教 ~~~</p>
<blockquote>
<p>投稿来源：<a href="https://juejin.cn/post/6983975113792159774" target="_blank" title="https://juejin.cn/post/6983975113792159774">juejin.cn/post/698397…</a></p>
</blockquote></div>  
</div>
            