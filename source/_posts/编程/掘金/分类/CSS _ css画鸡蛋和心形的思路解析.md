
---
title: 'CSS _ css画鸡蛋和心形的思路解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10437cb42b16417ba920a45f9d1df658~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 01:32:59 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10437cb42b16417ba920a45f9d1df658~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与更文挑战的第5天，活动详情查看 <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>在之前的文章【CSS | 4句CSS送你一个小月牙】中，汇总了很多经常用到的css形状，本篇文章主要是分析一下圆形系列和其他系列的实现思路。</p>
</blockquote>
<h2 data-id="heading-0">关于鸡蛋的实现</h2>
<p>主要利用的核心属性<code>border</code></p>
<p>首先：我们先来画一个普通的正方形</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10437cb42b16417ba920a45f9d1df658~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">.div &#123;
    width: 100px;
    height: 100px;
    background-color: #FFCC99;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用<code>border-radius: 50%</code>，我们可以得到一个圆形</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5583478dae194407bd07abcae9e8e8d7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">.div &#123;
    width: 100px;
    height: 100px;
    background-color: #FFCC99;
    border-radius: 50%;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先来把这个圆形变成椭圆；</p>
<p>思路：改变圆的width或height;</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63baeb0fc24a4e22b6bcb0ed37100935~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">.div &#123;
    width: 65px;/*改变宽 左图*/
    height: 100px;
    background-color: #FFCC99;
    border-radius: 50%;
&#125;
.div &#123;
    width: 100px;
    height: 65px;/*改变高 右图*/
    background-color: #FFCC99;
    border-radius: 50%;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们已经实现椭圆效果了，看上去是不是已经有点像是鸡蛋了呢，但是如果认真观察过鸡蛋会发现，其实鸡蛋的两端大小是不同的。</p>
<p>现在我们要怎么实现大头和小头的效果呢？</p>
<p>思路：我们可以利用<code>border-radius</code>属性来实现。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b64c8caaeb9495889168144515e92e4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以使用border-radius的百分比的值进行分离，然后控制百分比不一致。</p>
<p>关键代码:<code>border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d5dbbd395884595a611e73c931f7a15~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#egg &#123;
      display: block;
      width: 126px;
      height: 180px;
      background-color: #FFCC99;
      border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">关于心形的实现</h2>
<h3 data-id="heading-2">方法一</h3>
<p>现在想要用一个div画出一颗心，核心方法就是使用伪元素。</p>
<p>首页，先从画一个容器：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/067d0c30d4654625941cd4a50d473e6a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#heart &#123;/*实际使用只需要保留position属性*/
    position: relative;
    width: 100px;
    height: 90px;
    background: #FF9966
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后利用伪元素<code>:before</code>和<code>:after</code>画两个长方形</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98ee6509ba4d4896adeeb7c4288d52e6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#heart:before &#123;
    position: absolute;
    content: "";
    left: 50px;
    top: 0;
    width: 50px;
    height: 80px;
    background: #66CCFF;
    &#125;
#heart:after &#123;
    position: absolute;
    content: "";
    left: 0;
    top: 0;
    width: 50px;
    height: 80px;
    background: #66FFFF;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>给长方形的上半部分加<code>border-radius: 50px 50px 0 0;</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/305df9e6d94c49868c3853d253913a0f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#heart:before &#123;
   （...同上省略）
    border-radius: 50px 50px 0 0;
    &#125;
  #heart:after &#123;
    （...同上省略）
    border-radius: 50px 50px 0 0;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用<code>transform</code>属性，对两个长方形做一个正负45度的旋转</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8d68e3ad56f4d8cb1628a320ee5058c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#heart:before &#123;
    （...同上省略）
    transform: rotate(-45deg);
    &#125;
 #heart:after &#123;
    （...同上省略）
    transform: rotate(45deg);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后利用<code>transform-origin</code>属性，调整一下旋转元素的基点位置；</p>
<p>最后把颜色都改为红色，心形就画好啦！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10ed15578ad34b39b723c0ff5b3a6eb6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#heart:before &#123;
    （...同上省略）
    transform-origin: 0 100%;
    &#125;
 #heart:after &#123;
    （...同上省略）
    transform-origin :100% 100%;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">方法二</h3>
<p>还有一种更好理解的方法，同样利用伪元素来实现；</p>
<p>先画一个正方形</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ad9d06f51934d179de867fd7e89a4a9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#heart &#123;
    position: relative;
    width: 100px;
    height:100px;
    background: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后利用两个伪元素:before和:after，画两个圆,圆心分别定为在正方形的上面和右边；</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc8e9276932c4458a80c0e42ab858171~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#heart:before &#123;
    position: absolute;
    content: "";
    top: -50px;
    right:0;
    width: 100px;
    height: 100px;
    background: #66CCFF;
    border-radius: 50%
 
&#125;
#heart:after &#123;
    position: absolute;
    content: "";
    right: -50px;
    bottom: 0;
    width: 100px;
    height: 100px;
    background: #66FFFF;
    border-radius: 50%
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把两个圆的颜色变成和正方形的一样，可以看到倒下的心形已经出来了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3db40c3ba554944b95f83a645ccdd04~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们只需要把整个div旋转45度，心形就画好了！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a289c251d96445838a9fd4fbef7f8d19~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#heart &#123;
    position: relative;
    width: 100px;
    height:100px;
    background: #FF9966;
   transform: rotate(-45deg);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>小可爱看完就点个赞再走吧！🤞🤞🤞</p></div>  
</div>
            