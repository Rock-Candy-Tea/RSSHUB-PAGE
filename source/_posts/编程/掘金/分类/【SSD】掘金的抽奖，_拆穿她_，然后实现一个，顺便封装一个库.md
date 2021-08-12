
---
title: '【SSD】掘金的抽奖，_拆穿她_，然后实现一个，顺便封装一个库'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7278151b6c614cafbb8c921849130b70~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 16:29:44 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7278151b6c614cafbb8c921849130b70~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>关于关于<a href="https://juejin.cn/column/6991252706941730852" target="_blank" title="https://juejin.cn/column/6991252706941730852">【SSD系列】</a>：<br>
<strong>前端一些有意思的内容，旨在3-10分钟里， 500-1500字，有所获，又不为所累。</strong></p>
<p>掘金抽奖，不中大奖，自己复原UI, 中一个大奖满足自己，顺便封装一个库。</p>
<p>如果点赞破<strong>100</strong>，再写一篇转盘抽奖的相关文章，并顺便封装一个库。</p>
<h2 data-id="heading-1">效果演示</h2>
<h3 data-id="heading-2">PC端</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7278151b6c614cafbb8c921849130b70~tplv-k3u1fbpfcp-watermark.image" alt="luckDraw_d.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">模拟移动端</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02a8ced0a9f24412a6a4e55565cfb686~tplv-k3u1fbpfcp-watermark.image" alt="luckDraw_m.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">源码</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxiangwenhu%2FjuejinBlogsCodes%2Ftree%2Fmaster%2FluckDraw" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xiangwenhu/juejinBlogsCodes/tree/master/luckDraw" ref="nofollow noopener noreferrer">luckDraw 源码</a></p>
<ol>
<li>包含封装库</li>
<li>包含UI</li>
</ol>
<h2 data-id="heading-5">抽奖简析</h2>
<p>抽奖嘛，简单说就是障眼法。 前前后后的动画都是增强一些体验，寻求一点刺激罢了，幻想自己能成为那个大奖获得者。</p>
<h3 data-id="heading-6">常见表现形式</h3>
<p>常见的抽奖表现有两种，<strong>九宫格</strong>和<strong>转盘</strong>，转盘又有<strong>转动指针</strong>和<strong>转动转盘</strong>两种。
从实现难度上来说， 转盘大于九宫格。</p>
<h3 data-id="heading-7">一般的实现方式</h3>
<ol>
<li><strong>九宫格</strong><br>
间隔的设置背景色或者蒙层，越往后间隔越大。</li>
<li><strong>转盘</strong>
<ol>
<li><strong>纯脚本控制</strong>：每个一段时间，转动转盘或者指针，越往后，转动越少。</li>
<li><strong>css动画</strong>： 提前计算旋转角度好，配合css3, 利用好贝塞尔函数，梭哈。</li>
</ol>
</li>
</ol>
<h3 data-id="heading-8">一般逻辑处理</h3>
<ol>
<li><strong>动画先行</strong><br>
就是先执行动画，期间去获取结果，然后决定定格在何处。</li>
<li><strong>结果先行</strong><br>
先获取结果，然后启动动画。</li>
</ol>
<h2 data-id="heading-9">掘金站点技术浅析</h2>
<p>这里就客串分析下掘金的技术栈，推荐一款 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fdapjbgnjinbpoindlpdmhochffioedbn" target="_blank" rel="nofollow noopener noreferrer" title="https://chrome.google.com/webstore/detail/dapjbgnjinbpoindlpdmhochffioedbn" ref="nofollow noopener noreferrer">BuiltWith Technology Profiler</a>的chrome创建，其能分析出网站的采用哪些技术构建。 我们一看看看掘金的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22330a5f771f4c679d29c595652bdb10~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看看DOm节点熟悉的<code>__nuxt</code>和 <code>data-v</code>， 还真是那么回事。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca469dbcc9f0431dbf2dd053d09d7ddb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">掘金抽奖简析</h2>
<p>掘金的抽奖属于典型的九宫格，中间是抽奖的按钮。</p>
<h3 data-id="heading-11">布局</h3>
<p>典型的flex布局，九个格子，九个<code>turntable-item</code>div，抽奖按钮采用单独的<code>lottery</code>样式标记。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc3f578f7f3845d5a85f013d3bae404b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">动画先行还是结果先行？</h3>
<p>抽奖接口是<code>https://api.juejin.cn/growth_api/v1/lottery/draw</code>，我们打开控制面板， Network板块，输入<code>draw</code>过滤请请求。</p>
<p>执行一次，然后block抽奖请求。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33c2ab1839544b2eaf5951fd32a6dbbd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再次执行，可以明显的看到先执行了动画，所以我推断是<strong>动画先行</strong>，至于真相，他重要吗？不重要，反正我也抽不中！！！！！！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f28aa8031ce4bcd9ea64597c18c7eac~tplv-k3u1fbpfcp-watermark.image" alt="luckDraw_block.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">实现思路</h2>
<p>我们采用动画先行方案，先启动动画，中途请求结果，得到结果后，执行命中动画。</p>
<h3 data-id="heading-14">基本思路</h3>
<p><strong>1. 编号</strong><br>
<code>0-n</code>个坑位，九宫格的话，就是<code>0-7</code>个坑位,坑位的东西可以重复。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b753c7cc58c84b82ac5009d6fbc13e1f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2.启动动画</strong><br>
匀速的切换格子，同时请求服务接口。</p>
<p><strong>3. 中奖动画</strong><br>
收到结果后，计算出命中奖品的编号，并执行减速逻辑。</p>
<h3 data-id="heading-15">分离逻辑</h3>
<p>基本思路就是这样子的，为了通用性，我们需要多思考一些，抽奖重要的是逻辑，表面的形式重要吗？
其实并不太重要，所以我们这里把抽奖逻辑封装，提供可变性，并对外提供事件通知。</p>
<p><strong>可变性</strong><br>
可变性一般是通过参数和对外暴露方法来实现的，我们也不例外。</p>
<ol>
<li>格子数，不仅仅是九宫格，10宫格，12宫格都支持</li>
<li>起始位置，不一定是从0开始</li>
<li>起始的时间间隔，之后会越来越慢</li>
<li>至少转动的次数， 如果接口太快，可能感觉没开始就结束了。</li>
<li>得到结果后，我们的减速动画逻辑，应该是内置，同时可以被覆写。</li>
</ol>
<p><strong>事件通知</strong></p>
<p>整个过程可能存在的事件：</p>
<ol>
<li>onStart: // 当开始</li>
<li>onUpdate: // 旋转一次</li>
<li>onEnded:   // 结束</li>
<li>onError:  // 异常</li>
</ol>
<p>我们把这些整个起来, 大概就是这个样子了，都很简单。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">var</span> defaultOption = &#123;
        <span class="hljs-attr">startIndex</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 初始位置</span>
        <span class="hljs-attr">pits</span>: <span class="hljs-number">8</span>,  <span class="hljs-comment">// 格子数</span>
        <span class="hljs-attr">interval</span>: <span class="hljs-number">100</span>, <span class="hljs-comment">// 初始间隔</span>
        <span class="hljs-attr">rate</span>: <span class="hljs-number">2.5</span>,  <span class="hljs-comment">// 系数</span>
        <span class="hljs-attr">cycle</span>: <span class="hljs-number">5</span>,  <span class="hljs-comment">//转动基本次数：即至少需要转动多少次再进入抽奖环节</span>
        <span class="hljs-attr">getInterval</span>: <span class="hljs-literal">null</span> <span class="hljs-comment">// 自定义旋转间隔函数</span>
        <span class="hljs-comment">//onStart: null, // 当开始</span>
        <span class="hljs-comment">//onUpdate: null, // 旋转一次</span>
        <span class="hljs-comment">//onEnded: null,  // 结束</span>
        <span class="hljs-comment">//onError: null  // 异常, 比如转动次数已经达到设定值, 但是没有设置奖项</span>
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">使用代码</h2>
<h3 data-id="heading-17">工具方法</h3>
<p>先封装两个添加方法，一个添加选中的class，一个删除选中的class。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeChosenClass</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> el = lotteryEl.querySelector(<span class="hljs-string">'.turntable-item.chosen'</span>);
    <span class="hljs-keyword">if</span> (el) &#123;
        el.classList.remove(<span class="hljs-string">'chosen'</span>);
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addChosenClass</span>(<span class="hljs-params">index</span>)</span>&#123;
    lotteryEl.querySelector(<span class="hljs-string">'.turntable-item.turntable-item-'</span> + index).classList.add(<span class="hljs-string">'chosen'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">实例化</h3>
<p>Lottery是我们封装的逻辑类。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> options = &#123;
&#125;;
<span class="hljs-keyword">var</span> lottery = <span class="hljs-keyword">new</span> Lottery(options);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">注册启动事件和模拟中奖</h3>
<p>4号坑位是大奖</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> btnStart = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".turntable-box .turntable-item.lottery"</span>);
btnStart.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    lottery.start();
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        setPrize();
    &#125;, <span class="hljs-number">800</span>)
&#125;)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setPrize</span>(<span class="hljs-params"></span>) </span>&#123;
    lottery.setPrize([<span class="hljs-number">4</span>]) <span class="hljs-comment">// 4号坑位是大奖</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">监听抽奖事件</h3>
<pre><code class="hljs language-js copyable" lang="js">lottery.onUpdate = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ins, index, times</span>) </span>&#123;
    removeChosenClass();
    addChosenClass(index);
&#125;

lottery.onEnded = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ins, index, prizeIndexes</span>) </span>&#123;
    removeChosenClass();
    addChosenClass(index);

    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        dialogEl.classList.remove(<span class="hljs-string">"hide"</span>);
    &#125;, <span class="hljs-number">500</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此为止，使用代码完毕，与框架无关。</p>
<h2 data-id="heading-21">逻辑库封装</h2>
<p>逻辑库的完整代码位于 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxiangwenhu%2FjuejinBlogsCodes%2Fblob%2Fmaster%2FluckDraw%2Flottery.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xiangwenhu/juejinBlogsCodes/blob/master/luckDraw/lottery.js" ref="nofollow noopener noreferrer">抽奖逻辑Lottery.js</a></strong> , 我就不全贴出来，不然违背我500-1500字的原则了，就贴一张简单的属性图吧。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ecb9a52f6224d04843fdc9d26ecdeef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-22">小结</h2>
<p>是不是很简单，一切都看起来没那么难。</p>
<h2 data-id="heading-23">写在最后</h2>
<p>不忘初衷，【SSD系列】，3-5分钟，500-1000字，有所得，而不为所累，如果你觉得不错，你的一赞一评就是我前行的最大动力。</p>
<p>技术交流群请到 <a href="https://juejin.cn/pin/6994350401550024741" title="https://juejin.cn/pin/6994350401550024741" target="_blank">这里来</a>。
或者添加我的微信 cloud-dirge，一起学习。</p></div>  
</div>
            