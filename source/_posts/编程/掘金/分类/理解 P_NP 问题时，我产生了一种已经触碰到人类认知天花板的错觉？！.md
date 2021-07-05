
---
title: '理解 P_NP 问题时，我产生了一种已经触碰到人类认知天花板的错觉？！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://s3.jpg.cm/2021/07/04/In298R.th.png'
author: 掘金
comments: false
date: Sat, 03 Jul 2021 20:36:21 GMT
thumbnail: 'https://s3.jpg.cm/2021/07/04/In298R.th.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
</blockquote>
<h2 data-id="heading-0">概念初识</h2>
<p>咱研究算法的时候，一定遇到过动态规划中的 <strong><a href="https://zh.wikipedia.org/wiki/P/NP%E9%97%AE%E9%A2%98" target="_blank" rel="nofollow noopener noreferrer">旅行商问题（TSP）</a></strong>！</p>
<p>TSP 是一个 NP 完全问题，今天咱要聊聊正是七大 <a href="https://zh.wikipedia.org/wiki/%E5%8D%83%E7%A6%A7%E5%B9%B4%E5%A4%A7%E7%8D%8E%E9%9B%A3%E9%A1%8C" target="_blank" rel="nofollow noopener noreferrer">千禧年大奖难题</a> 之首的 <strong>【P/NP 问题】！</strong></p>
<ul>
<li>注：每解破一道千禧年大奖难题可获奖金100万美元</li>
</ul>
<p>其实，本瓜在前不久的一篇文章<a href="https://juejin.cn/post/6973499606961225741" target="_blank">《做题家：不可不会的“算法设计与分析”！》</a>中提过一嘴：</p>
<blockquote>
<p><strong>“了解 P/NP 问题！有一种让我觉得已经触碰到人类【数学天花板】的错觉。😵”</strong></p>
</blockquote>
<p>现在再看这句话，<strong>我小了，格局小了！</strong> 此句应更正为：</p>
<blockquote>
<p><strong>“P/NP 问题应该是现代人类【认知的天花板】！它有着足以颠覆整个世界的力量！💪”</strong></p>
</blockquote>
<p><strong>那究竟什么是 P/NP 问题 ？？？</strong></p>
<p>一言以蔽之：</p>
<blockquote>
<p><strong>如果一个问题的解，可以在多项式时间内被验证（P），那么是否证明可以在多项式时间内找到这个解（NP）？</strong></p>
</blockquote>
<ul>
<li>多项式时间：如 O(n<sup>2</sup>)、O(n<sup>100</sup>)、O(n<sup>200</sup>) 等；</li>
</ul>
<p>如果能证明是可以的（即 <strong>P = NP</strong>），或者证明是不可以的（即 <strong>P ≠ NP</strong>），您就能拿 100 万美金了。</p>
<p><a href="https://imagelol.com/image/In298R" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/04/In298R.th.png" alt="In298R.th.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<blockquote>
<p>最通俗来讲，如果证明了 <strong>P = NP</strong>，就意味着：<strong>【当我们提出一个问题的验证方法后，我们就能获得了这个问题的解！】</strong></p>
</blockquote>
<p>这是非常恐怖的一句话！当代计算机科学和信息技术的基础是 P ≠ NP，如果证明了 P = NP，世界将迎来大变革！</p>
<ul>
<li>2002 年对 P/NP 领域专家的一次调查显示，相信 P = NP 以及 P ≠ NP 的专家的比例是 9:61。</li>
</ul>
<h2 data-id="heading-1">举个栗子</h2>
<p>举个例子🌰：</p>
<p>数独问题，验证很容易，只要遍历行和列去检查就可以了，时间复杂度是 O(n<sup>2</sup>)。</p>
<p>但是，反过来，如果给你一个数独问题，你是否能在多项式时间内求出它的解？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43a8359fcf0b48e797a84755b5e50b95~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>目前的结论是：不确定！</strong></p>
<p>再举一例🌰：</p>
<p>当我告诉 319 是两个质数的乘积时（即告诉了验证方法），请问 319 是哪两个质数的乘积呢？如果是一个非常非常大的质数呢？</p>
<p><a href="https://imagelol.com/image/In3cT8" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/04/In3cT8.md.png" alt="In3cT8.md.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>这个问题，和数独问题一样，能在多项式时间内验证（做乘法运算即可），但不确定是否能在多项式时间内求解。</p>
<p>即它们的特点：<strong>很好验证，但是求解很难！！</strong></p>
<hr>
<p>现实中还有非常多的这类例子🌰：</p>
<p>我们可以在多项式时间内验证它（<strong>P</strong>：polynomial time），但是不确定否可以在多项式时间内找到这个解（<strong>NP</strong>：nondeterministic polynomial time）。</p>
<p>比如：资源调度问题、图着色问题、哈密顿回路问题、旅行商问题......</p>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_of_NP-complete_problems" target="_blank" rel="nofollow noopener noreferrer">wiki：List of NP-complete problems</a></li>
</ul>
<p>这些看似是数学问题、信息技术问题，但是却体现在生活的方方面面！</p>
<h2 data-id="heading-2">比特币卒</h2>
<blockquote>
<p>如果 <strong>P = NP</strong>，现代【非对称加密】的密码体系会彻底崩掉（比如比特币等加密货币，会直接消失）。</p>
</blockquote>
<p>我们知道非对称加密体系：<strong>通过私钥可以算出公钥，而通过公钥无法算出私钥。</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f61411dd880d4cd688a6beeb47a9ea18~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这种非对称性是安全的最强重要保障！</p>
<pre><code class="copyable">私钥（K）* G = 公钥（P）

公钥（P）/ G = 私钥（K）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对私钥（K）做 G 运算，得出 公钥（P），这个很容易！（<strong>验证容易</strong>）</p>
<p>但是由公钥（P）<strong>做 G 运算的逆运算</strong>得到 私钥（K），目前认为是：非常非常非常难的，几乎不可能，这是加密安全的最重要基础！（<strong>求解困难</strong>）。</p>
<p>如果证明了 <strong>P = NP</strong>，那么我们就可以通过计算机在多项式时间内算出这个私钥解啦！那就没有加密可言啦！！所以，加密体系也就崩溃掉了！！</p>
<p>你可能会疑问：这个多项时间如果很大呢，比如 O(n<sup>100</sup>)？</p>
<p>答：只要 P = NP，即使这个多项式时间很大，我们迟早也能把它算出来！因为问题不变，算力是不断提升的。<a href="https://www.zhihu.com/question/26933442" target="_blank" rel="nofollow noopener noreferrer">量子计算</a></p>
<p>这样说，如果现代密码系统崩溃，其中的利益远远大于破解 P/NP 问题的 100 万美元~</p>
<h2 data-id="heading-3">人与机器</h2>
<p>更加细思极恐的是，如果证明了 <strong>P = NP</strong>，【人与机器】的界限开始变得模糊。</p>
<p>MIT 计算机科学和人工智能实验室教授 Scott Aaronson 说：</p>
<blockquote>
<p>“如果 P = NP 的话，这个世界将是完全不同的地方。任何创意都不再会有价值！一个问题被找到后，从认知它到解决它不会再有遥不可及的距离。喜欢交响乐的人，可以成为莫扎特；喜欢逐步论证的人，可以成为高斯。<strong>艺术和智能都由计算的深层架构所模制</strong>。”</p>
</blockquote>
<p>意味着：无论多复杂的问题，只要能在多项式时间内验证，就代表着我们能在多项式时间内解决它。即使是艺术创造！</p>
<p>计算机能精确地模仿某一个特定的人。网络的身份鉴定将变得相当困难，以致于不得不借助物理方式；</p>
<p><a href="https://imagelol.com/image/In3rAt" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/04/In3rAt.md.png" alt="In3rAt.md.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h2 data-id="heading-4">万物归一</h2>
<p>肖邦曾说过：</p>
<blockquote>
<p>“简单是最终的成就。”</p>
</blockquote>
<p>我们将 P/NP 问题的释义再夸张一点：</p>
<p><strong>P/NP 终极之问：世界上一切复杂的问题是不是都能变成简单的问题？</strong></p>
<p>没人知道。</p>
<p>或许人类最终无法找到这最简单的真理，就像游戏里的人物无法理解我们一样。</p>
<p><strong>这个宇宙是混沌的？还是有序的？</strong></p>
<p>呜呼~这次算是顶到天花板了QAQ？一切归于寂寥......</p>
<p><a href="https://imagelol.com/image/In3Nf5" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/04/In3Nf5.md.png" alt="In3Nf5.md.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h2 data-id="heading-5">推荐阅读</h2>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/43806136" target="_blank" rel="nofollow noopener noreferrer">浅谈P vs. NP</a></li>
<li><a href="https://www.youtube.com/watch?v=0_XmvNu0J40" target="_blank" rel="nofollow noopener noreferrer">椭圆曲线加密与哈希函数是什么？非对称加密是什么？比特币中的数学原理</a></li>
<li><a href="https://www.youtube.com/watch?v=RGJ7Q8JHZj8&t=5s" target="_blank" rel="nofollow noopener noreferrer">世界七個數學難題之一：P與NP @Hackerdashery</a></li>
<li><a href="https://www.cnblogs.com/yymn/p/4853747.html" target="_blank" rel="nofollow noopener noreferrer">NP难问题求解综述</a></li>
<li><a href="https://apple4us.com/2010/a-proof-that-p-is-not-equal-to-np" target="_blank" rel="nofollow noopener noreferrer">P 不等于 NP……么？</a></li>
<li><a href="http://www.matrix67.com/blog/archives/2552" target="_blank" rel="nofollow noopener noreferrer">假如P=NP，世界将会怎样？</a></li>
<li><a href="https://zhishifenzi.blog.caixin.com/archives/167252" target="_blank" rel="nofollow noopener noreferrer">最新证明面临质疑：P/NP问题为什么这么难？</a></li>
<li><a href="https://zi.media/@yidianzixun/post/biWXuZ" target="_blank" rel="nofollow noopener noreferrer">科學家發現人類的意識與宇宙的混沌本質有關</a></li>
</ul>
<blockquote>
<p>我是掘金安东尼，输出暴露输入，技术洞见生活，下次再会~</p>
</blockquote></div>  
</div>
            