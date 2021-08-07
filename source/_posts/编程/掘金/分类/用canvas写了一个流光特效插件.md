
---
title: '用canvas写了一个流光特效插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ecaa6ca47cb4de4a0e6a454919a9039~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 19:17:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ecaa6ca47cb4de4a0e6a454919a9039~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 前言</h2>
<blockquote>
<p>本插件初衷专为 大数据可视化页面打造，提供UI的流光动效</p>
<p>插件提供了直线流光、曲线流光两种动效方式，并且内置有单帧渲染方法、自动动画方法等等</p>
<p>背景素材是用的网上找的资源</p>
</blockquote>
<h2 data-id="heading-1">2. 效果展示</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ecaa6ca47cb4de4a0e6a454919a9039~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e890a2aa718c4c75a9936944b4d5ada8~tplv-k3u1fbpfcp-watermark.image" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0324c2c90c24da9b96e9a8271705536~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">3. API</h2>
<h3 data-id="heading-3">3.1 config</h3>
<blockquote>
<p><code>Object</code></p>
<p>光线的相关配置，每条光线单独配置</p>
</blockquote>
<h4 data-id="heading-4">3.1.1 config.moveType</h4>
<blockquote>
<p><code>String</code></p>
<p>流光移动方式，可以选择<code>line</code>或者<code>curve</code>，默认值为<code>line</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">config: &#123;
    <span class="hljs-attr">moveType</span>: <span class="hljs-string">'curve'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">3.1.2 config.isBridgePattern</h4>
<blockquote>
<p><code>boolean</code></p>
<p>是否开启桥接模式，如果移动轨迹为简单的单方向时，推荐开启，这样动画会更加的顺滑</p>
<p>可以选择<code>true</code>或者<code>false</code>，默认值为<code>false</code></p>
</blockquote>
<h4 data-id="heading-6">3.1.3 config.length</h4>
<blockquote>
<p><code>number</code></p>
<p>流光光线长度（单位px），默认值为40</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">config: &#123;
    <span class="hljs-attr">length</span>: <span class="hljs-number">100</span>,        <span class="hljs-comment">//如果不配置该参数，那么其值默认为40</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">1.4 config.shade</h4>
<blockquote>
<p><code>number</code></p>
<p>流光两头渐变长度，<code>length</code>包含了该长度，默认值是<code>length</code>的1/3</p>
<p>不要将shade设置的过长，否则会出现一些无法预料的问题(一般情况下，不用设置，默认即可)</p>
</blockquote>
<h4 data-id="heading-8">3.1.5 config.speedDistance</h4>
<blockquote>
<p><code>number</code></p>
<p>流光单帧移动的距离（单位px），默认值是2</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">config: &#123;
    <span class="hljs-attr">speedDistance</span>: <span class="hljs-number">2</span>,       <span class="hljs-comment">//如果不配置该参数，那么其值默认为2</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">3.1.6 config.color</h4>
<blockquote>
<p><code>string</code></p>
<p>流光主体颜色（仅支持rgb三元色），默认值为255,255,255，即白色</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">config: &#123;
    <span class="hljs-attr">color</span>: <span class="hljs-string">'0, 181, 253'</span>,       <span class="hljs-comment">//如果不配置该参数，那么其值默认为 255,255,255</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">3.1.7 config.lineWidth</h4>
<blockquote>
<p><code>number</code></p>
<p>流光线条粗细度（单位px），默认值是1</p>
</blockquote>
<h4 data-id="heading-11">3.1.8 config.shadowBlur</h4>
<blockquote>
<p><code>number</code></p>
<p>流光阴影模糊度（单位px），默认值为0</p>
</blockquote>
<h4 data-id="heading-12">3.1.9 config.shadowColor</h4>
<blockquote>
<p><code>string</code></p>
<p>流光阴影颜色（仅支持rgb三颜色），默认值与color同步</p>
</blockquote>
<h4 data-id="heading-13">3.1.10 config.interval</h4>
<blockquote>
<p><code>number</code></p>
<p>流光循环动画间隔时间（单位s），默认值为0</p>
<p>如果希望流光播放完毕后，隔一段时间再继续，那么控制它即可</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">config: &#123;
    <span class="hljs-attr">interval</span>: <span class="hljs-number">1</span>,        <span class="hljs-comment">//如果不配置该参数，那么其值默认为0 也就是立即循环</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">3.1.11 config.delay</h4>
<blockquote>
<p><code>number</code></p>
<p>动画起始的延迟时间（单位s），默认值为0</p>
<p>如果希望流光一开始等待一段时间才开始，那么控制它即可</p>
</blockquote>
<h3 data-id="heading-15">3.2 points</h3>
<blockquote>
<p><code>Array</code></p>
<p>光线移动轨迹的关键坐标点，可配置多个点位，以形成一条轨迹线</p>
</blockquote>

























<table><thead><tr><th>参数</th><th>说明</th><th>类型</th></tr></thead><tbody><tr><td>x</td><td>x轴坐标</td><td>Number</td></tr><tr><td>y</td><td>y轴坐标</td><td>Number</td></tr><tr><td>cp</td><td>二次贝塞尔曲线控制点（曲线专用）</td><td>Number</td></tr></tbody></table>
<pre><code class="hljs language-js copyable" lang="js">points: [
    &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">772</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-number">115</span>,
    &#125;,
    &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">582</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-number">272</span>,
        <span class="hljs-attr">cp</span>: [<span class="hljs-number">569</span>,<span class="hljs-number">172</span>],
    &#125;,
    &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">773</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-number">409</span>,
        <span class="hljs-attr">cp</span>: [<span class="hljs-number">602</span>,<span class="hljs-number">368</span>]
    &#125;,
    &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">1160</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-number">407</span>,
        <span class="hljs-attr">cp</span>: [<span class="hljs-number">960</span>,<span class="hljs-number">455</span>],
    &#125;,
],
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">注意：</h3>
<blockquote>
<p>以上配置，均只针对于一条线，如果希望同时有多条线，那么每条线均需要单独配置，例如以下<code>options</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> options = [
    &#123;
        <span class="hljs-attr">config</span>: &#123;
            <span class="hljs-attr">moveType</span>: <span class="hljs-string">'curve'</span>,       <span class="hljs-comment">//line 直线    curve曲线</span>
            <span class="hljs-attr">shade</span>: <span class="hljs-number">40</span>,          <span class="hljs-comment">//渐变长度</span>
            <span class="hljs-attr">length</span>: <span class="hljs-number">100</span>,         <span class="hljs-comment">//光线长度</span>
            <span class="hljs-attr">speedDistance</span>: <span class="hljs-number">8</span>,       <span class="hljs-comment">//每帧移动距离</span>
            <span class="hljs-attr">color</span>: <span class="hljs-string">'0, 181, 253'</span>,       <span class="hljs-comment">//线条颜色</span>
            <span class="hljs-attr">lineWidth</span>: <span class="hljs-number">2</span>,       <span class="hljs-comment">//线条粗细</span>
            <span class="hljs-attr">shadowBlur</span>: <span class="hljs-number">5</span>,      <span class="hljs-comment">//线条阴影模糊级别</span>
            <span class="hljs-attr">shadowColor</span>: <span class="hljs-string">'#0ccf67'</span>,    <span class="hljs-comment">//阴影颜色</span>
            <span class="hljs-attr">interval</span>: <span class="hljs-number">1</span>,        <span class="hljs-comment">//循环动画间隔时间</span>
        &#125;,
        <span class="hljs-attr">points</span>: [
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">772</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">115</span>,
            &#125;,
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">582</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">272</span>,
                <span class="hljs-attr">cp</span>: [<span class="hljs-number">569</span>,<span class="hljs-number">172</span>],
            &#125;,
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">773</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">409</span>,
                <span class="hljs-attr">cp</span>: [<span class="hljs-number">602</span>,<span class="hljs-number">368</span>]
            &#125;,
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">1160</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">407</span>,
                <span class="hljs-attr">cp</span>: [<span class="hljs-number">960</span>,<span class="hljs-number">455</span>],
            &#125;,
        ],
    &#125;,
    &#123;
        <span class="hljs-attr">config</span>: &#123;
            <span class="hljs-attr">moveType</span>: <span class="hljs-string">'line'</span>,       <span class="hljs-comment">//line 直线    curve曲线</span>
            <span class="hljs-attr">shade</span>: <span class="hljs-number">30</span>,          <span class="hljs-comment">//渐变长度</span>
            <span class="hljs-attr">length</span>: <span class="hljs-number">60</span>,         <span class="hljs-comment">//光线长度</span>
            <span class="hljs-attr">speedDistance</span>: <span class="hljs-number">5</span>,       <span class="hljs-comment">//每帧移动距离</span>
            <span class="hljs-attr">color</span>: <span class="hljs-string">'0, 181, 253'</span>,       <span class="hljs-comment">//线条颜色</span>
            <span class="hljs-attr">lineWidth</span>: <span class="hljs-number">5</span>,       <span class="hljs-comment">//线条粗细</span>
            <span class="hljs-attr">shadowBlur</span>: <span class="hljs-number">5</span>,      <span class="hljs-comment">//线条阴影模糊级别</span>
            <span class="hljs-attr">shadowColor</span>: <span class="hljs-string">'#0ccf67'</span>,    <span class="hljs-comment">//阴影颜色</span>
            <span class="hljs-attr">interval</span>: <span class="hljs-number">2</span>,        <span class="hljs-comment">//循环动画间隔时间</span>
        &#125;,
        <span class="hljs-attr">points</span>: [
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">960</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">242</span>,
            &#125;,
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">960</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">129</span>,
            &#125;,
        ],
    &#125;,
    &#123;
        <span class="hljs-attr">config</span>: &#123;
            <span class="hljs-attr">moveType</span>: <span class="hljs-string">'line'</span>,       <span class="hljs-comment">//line 直线    curve曲线</span>
            <span class="hljs-attr">shade</span>: <span class="hljs-number">30</span>,          <span class="hljs-comment">//渐变长度</span>
            <span class="hljs-attr">length</span>: <span class="hljs-number">60</span>,         <span class="hljs-comment">//光线长度</span>
            <span class="hljs-attr">speedDistance</span>: <span class="hljs-number">7</span>,       <span class="hljs-comment">//每帧移动距离</span>
            <span class="hljs-attr">color</span>: <span class="hljs-string">'0, 181, 253'</span>,       <span class="hljs-comment">//线条颜色</span>
            <span class="hljs-attr">lineWidth</span>: <span class="hljs-number">5</span>,       <span class="hljs-comment">//线条粗细</span>
            <span class="hljs-attr">shadowBlur</span>: <span class="hljs-number">5</span>,      <span class="hljs-comment">//线条阴影模糊级别</span>
            <span class="hljs-attr">shadowColor</span>: <span class="hljs-string">'#0ccf67'</span>,    <span class="hljs-comment">//阴影颜色</span>
            <span class="hljs-attr">interval</span>: <span class="hljs-number">2</span>,        <span class="hljs-comment">//循环动画间隔时间</span>
        &#125;,
        <span class="hljs-attr">points</span>: [
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">960</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">242</span>,
            &#125;,
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">1112</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">369</span>,
            &#125;,
        ],
    &#125;,
    &#123;
        <span class="hljs-attr">config</span>: &#123;
            <span class="hljs-attr">moveType</span>: <span class="hljs-string">'line'</span>,       <span class="hljs-comment">//line 直线    curve曲线</span>
            <span class="hljs-attr">length</span>: <span class="hljs-number">120</span>,         <span class="hljs-comment">//光线长度</span>
            <span class="hljs-attr">speedDistance</span>: <span class="hljs-number">7</span>,       <span class="hljs-comment">//每帧移动距离</span>
            <span class="hljs-attr">color</span>: <span class="hljs-string">'0, 181, 253'</span>,       <span class="hljs-comment">//线条颜色</span>
            <span class="hljs-attr">lineWidth</span>: <span class="hljs-number">2</span>,       <span class="hljs-comment">//线条粗细</span>
            <span class="hljs-attr">shadowBlur</span>: <span class="hljs-number">5</span>,      <span class="hljs-comment">//线条阴影模糊级别</span>
            <span class="hljs-attr">shadowColor</span>: <span class="hljs-string">'#0ccf67'</span>,    <span class="hljs-comment">//阴影颜色</span>
        &#125;,
        <span class="hljs-attr">points</span>: [
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">100</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">100</span>,
            &#125;,
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">100</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">300</span>,
            &#125;,
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">300</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">300</span>,
            &#125;,
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">300</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">100</span>,
            &#125;,
            &#123;
                <span class="hljs-attr">x</span>: <span class="hljs-number">100</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">100</span>,
            &#125;,
        ],
    &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">4. 使用方式</h2>
<h3 data-id="heading-18">4.1 使用内嵌动画</h3>
<blockquote>
<p>本插件内嵌有开启动画的接口，我们通过配置初始化以后，直接调用，即可播放流光动画</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">... <span class="hljs-comment">//options配置省略</span>
​
<span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">new</span> FlowingLight(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'light'</span>),options).animate();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>上述案例，我们通过<code>new FlowingLight</code>，创建一个流光动画实例对象，同时我们需要传递两个参数，第一个参数是指定的<code>canvas</code>DOM对象，第二个参数是<code>options</code>配置参数，之后我们通过调用内嵌的<code>animate</code>接口，开始播放流光动画</p>
</blockquote>
<h3 data-id="heading-19">4.2 单帧动画渲染</h3>
<blockquote>
<p>有时候，我们页面并不只是流光动画，还有其它的需要渲染，此时我们就可以使用单帧动画的方式，来进行兼容处理</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> lightObj;
... <span class="hljs-comment">//options配置省略</span>
​
<span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    lightObj = <span class="hljs-keyword">new</span> FlowingLight(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'light'</span>),options);
    heart();
&#125;;
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">heart</span>(<span class="hljs-params"></span>) </span>&#123;
    requestAnimationFrame(heart);       <span class="hljs-comment">//心跳循环</span>
    lightObj.drawLight();   <span class="hljs-comment">//执行流光动画实例，单帧渲染逻辑</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            