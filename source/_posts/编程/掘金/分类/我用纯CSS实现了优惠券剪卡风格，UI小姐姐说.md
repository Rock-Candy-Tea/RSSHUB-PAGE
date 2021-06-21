
---
title: '我用纯CSS实现了优惠券剪卡风格，UI小姐姐说....'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ed7bf66fd64ae38cb10fb02c21f738~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 06:29:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ed7bf66fd64ae38cb10fb02c21f738~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的20天，活动详情查看 <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>在做商城类项目的时候，我们可能都会经历过“优惠券”这类需求，笔者在过往工作中，都是直接要求UI切图来实现，直到有一天产品告诉我一个奇思妙想：这个优惠券的宽度会随内容变化的！一下子让我陷入了人生的大思考，这样图片方式可不好整呐，因此萌生一个想法：能不能用纯css实现这些效果呢？</p>
<h2 data-id="heading-0">0. 内倒角</h2>
<p>首先我们来看下css如何实现内倒角</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.card</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">background-image</span>: 
        <span class="hljs-built_in">radial-gradient</span>(circle at left <span class="hljs-number">50px</span>, <span class="hljs-number">#fff</span>, <span class="hljs-number">#fff</span> <span class="hljs-number">10px</span>, transparent <span class="hljs-number">10px</span>),
        <span class="hljs-built_in">radial-gradient</span>(circle at right <span class="hljs-number">50px</span>, <span class="hljs-number">#fff</span>, <span class="hljs-number">#fff</span> <span class="hljs-number">10px</span>, transparent <span class="hljs-number">11px</span>),
        <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">100px</span> top, <span class="hljs-number">#fff</span>, <span class="hljs-number">#fff</span> <span class="hljs-number">10px</span>, transparent <span class="hljs-number">11px</span>),
        <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">100px</span> bottom, <span class="hljs-number">#fff</span>, <span class="hljs-number">#fff</span> <span class="hljs-number">10px</span>, transparent <span class="hljs-number">11px</span>);
    <span class="hljs-attribute">background-color</span>: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ed7bf66fd64ae38cb10fb02c21f738~tplv-k3u1fbpfcp-zoom-1.image" alt="内倒角效果图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实最先想到的是画圆形，在这个例子当中，主要是利用了设置背景图的属性与radial-gradient渐变来实现，实际效果差不多，在形状上呢还是保持整体方形，相信大家也看出来副作用，首先这个添加的渐变需要和背景颜色同步，比如设置的倒角是白色，背景是灰色的，那就露馅啦。</p>













<table><thead><tr><th>使用圆形的可能情况</th><th>为倒角设置颜色的效果</th></tr></thead><tbody><tr><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7f7270c7efb4ad69119560475d11be5~tplv-k3u1fbpfcp-zoom-1.image" alt="testerror" loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/721e510a72a84a16bb7f53870b052acf~tplv-k3u1fbpfcp-zoom-1.image" alt="test2" loading="lazy" referrerpolicy="no-referrer"></td></tr></tbody></table>
<h2 data-id="heading-1">1. 实现虚线</h2>
<p>上面实现了内倒角，接下来就要考虑虚线了，既然要纯css，能不能把虚线也给优雅地实现了呢，其实线性渐变就可以做到，一起来看看：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.line</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">1px</span>;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to right, <span class="hljs-number">#ccc</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#ccc</span> <span class="hljs-number">50%</span>, transparent <span class="hljs-number">50%</span>);
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">12px</span> <span class="hljs-number">1px</span>;
    <span class="hljs-attribute">background-repeat</span>: repeat-x;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码效果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/076e1f5e11c947dc8596d6db15180ee7~tplv-k3u1fbpfcp-zoom-1.image" alt="虚线" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 稍微调整下size属性就能改变虚线宽度 */</span>
<span class="hljs-attribute">background-size</span>: <span class="hljs-number">20px</span> <span class="hljs-number">1px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0a34e08b7814bbb957c2d0c917d0fd2~tplv-k3u1fbpfcp-zoom-1.image" alt="虚线2" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">2. 实现波浪框</h2>
<p>同样是利用径向渐变，我们尝试下波浪框效果：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.card</span> &#123;
    <span class="hljs-attribute">background</span>: red;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">position</span>: relative;
&#125;
<span class="hljs-selector-class">.card</span>:after &#123;
    content: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">left</span>: -<span class="hljs-number">5px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle, <span class="hljs-number">#ffffff</span>, <span class="hljs-number">#ffffff</span> <span class="hljs-number">4px</span>, transparent <span class="hljs-number">5px</span>);
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">10px</span> <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fce812f54ca45c3b3c7c5e1d4a37060~tplv-k3u1fbpfcp-zoom-1.image" alt="bolang" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">3. 组合</h2>
<p>通过以上例子，优惠券剪卡风格的效果已经呼之欲出了，我们只需要把这些效果组合起来，对颜色位置宽度等细节进行调整~</p>
<p>竖型优惠券例子效果：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.card1</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">120px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">background-image</span>: 
        <span class="hljs-built_in">radial-gradient</span>(circle at left <span class="hljs-number">90px</span>, <span class="hljs-number">#fff</span>, <span class="hljs-number">#fff</span> <span class="hljs-number">10px</span>, transparent <span class="hljs-number">10px</span>),
        <span class="hljs-built_in">radial-gradient</span>(circle at right <span class="hljs-number">90px</span>, <span class="hljs-number">#fff</span>, <span class="hljs-number">#fff</span> <span class="hljs-number">10px</span>, transparent <span class="hljs-number">11px</span>);
    <span class="hljs-attribute">background-color</span>: red;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
&#125;

<span class="hljs-selector-class">.card1</span> > <span class="hljs-selector-class">.line</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">60px</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">96px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">1px</span>;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to right, <span class="hljs-number">#ffffff</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#ffffff</span> <span class="hljs-number">50%</span>, transparent <span class="hljs-number">50%</span>);
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">12px</span> <span class="hljs-number">1px</span>;
    <span class="hljs-attribute">background-repeat</span>: repeat-x;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8954cd83b3841a59fe3dd830a74c246~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>究极组合，横型优惠券剪卡风格效果：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.card2</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">background-image</span>: 
        <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">130px</span> top, <span class="hljs-number">#fff</span>, <span class="hljs-number">#fff</span> <span class="hljs-number">10px</span>, transparent <span class="hljs-number">11px</span>),
        <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">130px</span> bottom, <span class="hljs-number">#fff</span>, <span class="hljs-number">#fff</span> <span class="hljs-number">10px</span>, transparent <span class="hljs-number">11px</span>);
    <span class="hljs-attribute">background-color</span>: red;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
&#125;

<span class="hljs-selector-class">.card2</span> > <span class="hljs-selector-class">.line</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">right</span>: <span class="hljs-number">31px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">78px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">1px</span>;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to right, <span class="hljs-number">#ffffff</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#ffffff</span> <span class="hljs-number">50%</span>, transparent <span class="hljs-number">50%</span>);
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">12px</span> <span class="hljs-number">1px</span>;
    <span class="hljs-attribute">background-repeat</span>: repeat-x;
    <span class="hljs-attribute">transform</span>:<span class="hljs-built_in">rotate</span>(<span class="hljs-number">90deg</span>);
&#125;

<span class="hljs-selector-class">.card2</span>:after &#123;
    content: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">right</span>: -<span class="hljs-number">5px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle, <span class="hljs-number">#ffffff</span>, <span class="hljs-number">#ffffff</span> <span class="hljs-number">4px</span>, transparent <span class="hljs-number">5px</span>);
<span class="hljs-comment">/* 这里可以优化一下，变为半圆，right也可以设置为0了 */</span>
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle at right, <span class="hljs-number">#ffffff</span>, <span class="hljs-number">#ffffff</span> <span class="hljs-number">4px</span>, transparent <span class="hljs-number">5px</span>);
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">10px</span> <span class="hljs-number">14px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d9beef0fd894aafb66be04e0143fc9b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是不是有那么点味道了呢，仅用径向渐变和线性渐变就能做出来效果，一想到UI小姐姐都不用切图给我，可以早早下班回去陪她男朋友了，我赶紧向她展示了成果，没想到小姐姐跟我说，你这没阴影不好看呀，这下子让我又一次陷入了人生的大思考。</p>
<p>回到工位上，我放弃了思考，颤抖的手胡乱地加了一个shadow，果然，露馅了啊！
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e9d263031fa410a95596f6fd2c43f8d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是我们要冷静，之前的思路是先画一个方形，然后放置圆形或半圆叠盖，所以最终还是会原形毕露，结果还是必须掏空那段半圆缺口啊，可css明显是做不到的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bb996df446143d8983126eb4ef910d4~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
等等，这时候就需要逆转想法，不是先画一个方形再剔除半圆，而是一开始就不画半圆这个缺口，将整个不规则形状填充出来，也就不需要剔除半圆了，先来看看下面这段css以及它的效果：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background</span>: 
  <span class="hljs-built_in">radial-gradient</span>(circle at right bottom, blue <span class="hljs-number">10px</span>, red <span class="hljs-number">0</span>) top right /<span class="hljs-number">50%</span> <span class="hljs-number">50px</span> no-repeat,
  <span class="hljs-built_in">radial-gradient</span>(circle at right top, blue <span class="hljs-number">10px</span>, orange <span class="hljs-number">0</span>) bottom right / <span class="hljs-number">50%</span> <span class="hljs-number">50px</span> no-repeat,
  <span class="hljs-built_in">radial-gradient</span>(circle at left top, blue <span class="hljs-number">10px</span>, yellow <span class="hljs-number">0</span>) bottom left / <span class="hljs-number">50%</span> <span class="hljs-number">50px</span> no-repeat,
  <span class="hljs-built_in">radial-gradient</span>(circle at left bottom, blue <span class="hljs-number">10px</span>, green <span class="hljs-number">0</span>) top left / <span class="hljs-number">50%</span> <span class="hljs-number">50px</span> no-repeat;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a480c49316d0416e96e87b1ee2f8e382~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按这个思路将上面的例子转为画上下两瓣方形，给透明径向渐变绘制的circle以外的区域填上颜色，而阴影部分就用filter来处理</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.card2</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">background</span>: 
        <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">130px</span> top, transparent <span class="hljs-number">10px</span>, red <span class="hljs-number">0</span>) top / <span class="hljs-number">100%</span> <span class="hljs-number">51px</span> no-repeat,
        <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">130px</span> bottom, transparent <span class="hljs-number">10px</span>, red <span class="hljs-number">0</span>) bottom / <span class="hljs-number">100%</span> <span class="hljs-number">51px</span> no-repeat;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">drop-shadow</span>(<span class="hljs-number">2px</span> <span class="hljs-number">2px</span> <span class="hljs-number">2px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">2</span>));
    <span class="hljs-comment">/* box-shadow: 12px 12px 2px 1px rgba(0, 0, 255, .2); */</span>
&#125;
<span class="hljs-selector-class">.card2</span> > <span class="hljs-selector-class">.line</span> &#123;
    <span class="hljs-comment">/* 没变化 */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终效果如下，为了看清阴影故意加深了：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d87864080d5842518ef70d5b5d3eebdd~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没办法，波浪框还是覆盖上去的半圆，所以设置不上贴合的阴影效果，但是基本的券卡形式总算是完美实现了。</p>
<p>第二天UI小姐姐跟我说，她改了设计图，叫我看看，我说停停，要不你还是切图给我吧。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a1823cf1ea84467b6365b1ac1bc9894~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            