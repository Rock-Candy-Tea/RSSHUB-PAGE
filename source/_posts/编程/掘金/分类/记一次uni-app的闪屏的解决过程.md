
---
title: '记一次uni-app的闪屏的解决过程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9683'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 19:48:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=9683'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在做一个深色背景的APP时发现切换页面时，页面会闪白一下</p>
<ol>
<li>在APP.vue中的全局样式会先加载</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">page&#123;
<span class="hljs-attr">height</span>: <span class="hljs-number">100</span>%;
background-color: #<span class="hljs-number">151721</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也有文章介绍在page.json里面写背景颜色，但是试了一下没有page的高度100%，也会闪白一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"app-plus"</span>:&#123;
            <span class="hljs-string">"background"</span>: <span class="hljs-string">"#151721"</span>
            &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>非tabbar页面都不闪白了，但是有两个需要从后端的获取数据在渲染的tabbar页面还会闪白。猜想可能是数据渲染造成的问题，所以设置页面</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">opacity: <span class="hljs-number">0</span>;
transition: all .5s;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加载完成之后再opacity: 1;以为这个问题解决了，结果只解决了一个其中tabbar页面闪白的问题</p>
<ol start="3">
<li>还有一个tabbar页面是首页，打开APP先是广告页在跳转到首页，这个过程就会闪白一下，用上述同样的方法并不能解决。反正各种方法都试了很久，最后突然想到是不是我的跳转方法的问题，我用的是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhhyang.cn%2Fv2%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://hhyang.cn/v2/" ref="nofollow noopener noreferrer">uni-simple-router</a>来实现跳转，从广告页跳转到首页用this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>R</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mi mathvariant="normal">.</mi><mi>p</mi><mi>u</mi><mi>s</mi><mi>h</mi><mi>T</mi><mi>a</mi><mi>b</mi><mo stretchy="false">(</mo><mo stretchy="false">)</mo><mo separator="true">,</mo><mtext>然后换成</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">Router.pushTab(),然后换成this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.00773em;">R</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord">.</span><span class="mord mathnormal">p</span><span class="mord mathnormal">u</span><span class="mord mathnormal">s</span><span class="mord mathnormal">h</span><span class="mord mathnormal" style="margin-right:0.13889em;">T</span><span class="mord mathnormal">a</span><span class="mord mathnormal">b</span><span class="mopen">(</span><span class="mclose">)</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord cjk_fallback">然</span><span class="mord cjk_fallback">后</span><span class="mord cjk_fallback">换</span><span class="mord cjk_fallback">成</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>Router.replaceAll()方法来跳转，解决闪白问题。</li>
</ol>
<p>（广告是做的一个页面，没有用uni-app的广告，因为这个广告只是介绍这个APP的内容，不知道有没有大佬知道别的做广告的方法？）</p></div>  
</div>
            