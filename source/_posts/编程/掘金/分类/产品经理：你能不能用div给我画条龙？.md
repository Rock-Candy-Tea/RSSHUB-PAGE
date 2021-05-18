
---
title: '产品经理：你能不能用div给我画条龙？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d686084e16d4dc88b5b17a1d7cd0e1a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 20:06:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d686084e16d4dc88b5b17a1d7cd0e1a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>事情是这样的，前天上午产品经理说想要做一个心愿墙，问我能不能行</p>
<p>我心想，这太容易了，但为了多摸一天鱼，我说还是<strong>有点挑战</strong>的</p>
<p>结果下午，产品经理和设计师就给我发来了设计参考</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d686084e16d4dc88b5b17a1d7cd0e1a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>他们说，心愿墙的设计大致是这样的，每个用户的心愿都是一个气泡，而客户的品牌是”龙“，我们希望在前端页面里用气泡呈现一个龙形的设计，每个气泡都会浮动，鼠标移上去变大，点击后展示心愿详情。</p>
<p>当时我的内心是这样的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/447ed6e19cc04dc1aa00499729d12eeb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我摸鱼的一天要泡汤了吗？</p>
<p><strong>谁都不能阻止我摸鱼</strong></p>
<p>但首先要解决最核心的问题</p>
<h1 data-id="heading-0">龙从哪里来？</h1>
<p>设计师说了，他可以给我一条由气泡组成的龙的设计稿，我说那等你设计稿给我，我再研究把。结果他说，已经有了，你就用这个吧</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862c493c8bd34b2e8dd3713f9be40d5f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>我的刀呢？</strong></p>
<h1 data-id="heading-1">互动问题</h1>
<blockquote>
<p>请在评论区留下你遇到过的最奇葩的需求</p>
</blockquote>
<h1 data-id="heading-2">拆解需求</h1>
<p>遇到不靠谱的产品经理和设计师，前端工程师真是惨。我们顶着最后交付成品的<code>巨锅</code>，所有<code>deadline</code>感觉都只是用来压榨前端工程师的。</p>
<p>我们只能靠自己，因为</p>
<p><strong>谁都不能阻止我摸鱼</strong></p>
<ul>
<li>需求1：有鼠标交互效果（太简单）</li>
<li>需求2：气泡要浮动（css动画，easy）</li>
<li>需求3：气泡组成一条龙</li>
</ul>
<p>此时我脑海里响起这首烂大街的歌</p>
<blockquote>
<p>左边跟我一起画个龙，在你右边画一道彩虹~</p>
</blockquote>
<p><code>诶，画个龙</code></p>
<p><code>用什么画，canvas</code></p>
<p><code>canvas能获得指定区域的像素点阵</code></p>
<p>卧槽，有招儿了</p>
<h1 data-id="heading-3">代码时间</h1>
<p>先用图片搜索找一张龙的剪影</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10b4df2d7b9b424fb431753167337851~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8098e5ef8d6b46288cfd2292dccc2b65~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">将图片绘制到canvas中</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas"</span>);
<span class="hljs-keyword">var</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);

<span class="hljs-keyword">var</span> image = <span class="hljs-keyword">new</span> Image();
image.src = <span class="hljs-string">"dragon.jpg"</span>;
image.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        canvas.width = image.width;
        canvas.height = image.height;

        ctx.drawImage(image,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">获取并裁剪画布的点阵信息</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> imageData = ctx.getImageData(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,image.width,image.height).data;
ctx.fillStyle = <span class="hljs-string">"#ffffff"</span>;
ctx.fillRect(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,image.width,image.height);

<span class="hljs-keyword">var</span> gap = <span class="hljs-number">6</span>;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> h = <span class="hljs-number">0</span>; h < image.height; h+=gap) &#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> w = <span class="hljs-number">0</span>; w < image.width; w+=gap)&#123;
            <span class="hljs-keyword">var</span> position = (image.width * h + w) * <span class="hljs-number">4</span>;
            <span class="hljs-keyword">var</span> r = imageData[position], g = imageData[position + <span class="hljs-number">1</span>], b = imageData[position + <span class="hljs-number">2</span>];

            <span class="hljs-keyword">if</span>(r+g+b==<span class="hljs-number">0</span>)&#123;
                    ctx.fillStyle = <span class="hljs-string">"#000"</span>;
                    ctx.fillRect(w,h,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>);
                &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们获得了这样一条龙的点阵信息</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab8c4d11d4e54e0980f0eb02b5426131~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">通过点阵信息生成气泡dom</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> dragonContainer = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"container"</span>);
<span class="hljs-keyword">var</span> dragonScale = <span class="hljs-number">2</span>;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> h = <span class="hljs-number">0</span>; h < image.height; h+=gap) &#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> w = <span class="hljs-number">0</span>; w < image.width; w+=gap)&#123;
            <span class="hljs-keyword">var</span> position = (image.width * h + w) * <span class="hljs-number">4</span>;
            <span class="hljs-keyword">var</span> r = imageData[position], g = imageData[position + <span class="hljs-number">1</span>], b = imageData[position + <span class="hljs-number">2</span>];

            <span class="hljs-keyword">if</span>(r+g+b==<span class="hljs-number">0</span>)&#123;
                    <span class="hljs-keyword">var</span> bubble = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"img"</span>);
                    bubble.src = <span class="hljs-string">"bubble.png"</span>;
                    bubble.setAttribute(<span class="hljs-string">"class"</span>,<span class="hljs-string">"bubble"</span>);

                    <span class="hljs-keyword">var</span> bubbleSize = <span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">10</span>+<span class="hljs-number">20</span>;
                    bubble.style.left = (w*dragonScale-bubbleSize/<span class="hljs-number">2</span>) + <span class="hljs-string">"px"</span>;
                    bubble.style.top = (h*dragonScale-bubbleSize/<span class="hljs-number">2</span>) + <span class="hljs-string">"px"</span>;
                    bubble.style.width = bubble.style.height = bubbleSize+<span class="hljs-string">"px"</span>;
                    bubble.style.animationDuration = <span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">6</span>+<span class="hljs-number">4</span> + <span class="hljs-string">"s"</span>;

                    dragonContainer.appendChild(bubble);
                &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74fea9a084a14630b925b091adfb6f6c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">开心摸鱼吧</h1>
<p>本例里使用div绘制大量的dom，仅为阐述思路，没考虑性能。利用一些js游戏引擎，比如pixi等，可以很方便的全部交由canvas去绘制并添加交互。</p>
<hr>
<p>本故事纯属虚构，参考案例来自本人2011年底为客户开发的春节活动网站。</p>
<h1 data-id="heading-8">源码</h1>
<p>微信搜索并关注“<code>大帅老猿</code>”，回复<code>泡泡龙</code>获得源码</p></div>  
</div>
            