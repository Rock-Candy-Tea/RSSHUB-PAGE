
---
title: '用html+css实现智能阴影效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80376ba459c3449f972b6725f81d23a8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 16:29:10 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80376ba459c3449f972b6725f81d23a8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<p>最近在复盘css的时候，突然脑海中迸发出一个实现智能阴影效果的想法，试了很多种方法但都无法实现，最后使用过滤（filter)的方法得以实现。</p>
<p>至于什么是智能阴影效果，有什么用；那大家就欣赏一下具体效果：
<span href="https://code.juejin.cn/pen/7144278628585439262" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7144278628585439262" data-src="https://code.juejin.cn/pen/7144278628585439262" style="display: none" loading="lazy"></iframe></span>
大家可以发现随着颜色的变化，旁边的阴影区域也会变化；从而实现智能阴影的效果。由于本人不知如何让图片代码片段在掘金上显示真实效果是这样的</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80376ba459c3449f972b6725f81d23a8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="动画.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">下面是一些必备重点知识</h1>
<h2 data-id="heading-1">filter相关知识</h2>
<h3 data-id="heading-2">filter基础知识点</h3>
<p>filter CSS属性将模糊或颜色偏移等图形效果应用于元素。共有十个效果blur、opacity、grayscale、sepia、saturate、hue-rotate、invert、brightness、contrast、drop-shadow。</p>
<ul>
<li>blur:这是一个模糊效果，单位为px</li>
<li>opacity:这是一个透明度的效果  值在0~1之间 0是完全透明，而1是不透明 无效果，例如filter:opacity(0.5).</li>
<li>grayscale:这是一个是一个是图片变灰的效果，值在0~1，</li>
<li>sepia这是褐色效果，值也在0~1之间， 0无效果，1完全变褐</li>
<li>saturate这是饱和度属性，取值大于等于0</li>
<li>invert这是颜色反转属性，值在0 ~ 1或者0 ~ 100%之间</li>
<li>brightness这是亮度，取值为数字或百分数</li>
<li>ontrast这是对比度，取值为大于或等于0的数字或百分数</li>
<li>drop-shadow这是阴影效果</li>
<li>hue-rotate这是色彩旋转，取值是角度，单位是deg</li>
</ul>
<h3 data-id="heading-3">我们的使用</h3>
<p>我们就定义了两个滤镜值：drop-shadow 和 blur
我们的 drop-shadow 滤镜设置了一个50%的阴影效果。blur 滤镜为为元素设置 20px 的模糊效果。这两个滤镜的结合即可完成第一步</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-attr">filter</span>: drop-<span class="hljs-title function_">shadow</span>(0px 0px 10px <span class="hljs-title function_">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.50</span>)) <span class="hljs-title function_">blur</span>(20px);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">动画效果的知识点</h2>
<ul>
<li>@keyframes                  规定动画是什么内容。</li>
<li>animation                  所有动画属性的简写属性。</li>
<li>animation-name               规定@keyframes动画的名称。</li>
<li>animation-duration规定动画完成一个周期所花费的秒或毫秒</li>
<li>animation-timing-function规定动画的速度曲线，默认是“ease”。</li>
<li>animation-delay                    规定动画何时开始，默认是0。</li>
<li>animation-iteration-count规定动画被播放的次数，默认是1，还有infinite（循环）无数次</li>
<li>animation-direction规定动画是否在下一周期逆向播放</li>
<li>animation-play-state规定动画是否正在运行或暂停。默认是"running",还有"paused"</li>
<li>animation-fill-mode规定动画结束后状态，保持forwards回到起始backwards</li>
</ul>
<p>简写效果：animation：动画名称 持续时间 运动曲线 何时开始 播放次数 是否反方向 动画起始或者结束的状态</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-attr">animation</span>: scale 1s  infinite alternate;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">相关代码解读</h1>
<h2 data-id="heading-6">文章主体</h2>
<pre><code class="hljs language-js copyable" lang="js">*&#123;
        <span class="hljs-attr">padding</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attr">margin</span>: <span class="hljs-number">0</span>;
        box-<span class="hljs-attr">sizing</span>: border-box;
    &#125;
    body&#123;
        background-<span class="hljs-attr">color</span>: black;
    &#125;
    @keyframes img&#123;
        <span class="hljs-number">0</span>%&#123;
            <span class="hljs-attr">background</span>:linear-<span class="hljs-title function_">gradient</span>(45deg,<span class="hljs-title function_">rgba</span>(<span class="hljs-number">213</span>, <span class="hljs-number">224</span>, <span class="hljs-number">92</span>, <span class="hljs-number">0.525</span>),<span class="hljs-title function_">rgba</span>(<span class="hljs-number">88</span>, <span class="hljs-number">170</span>, <span class="hljs-number">55</span>, <span class="hljs-number">0.525</span>));
        &#125;
        <span class="hljs-number">25</span>%&#123;
            <span class="hljs-attr">background</span>:linear-<span class="hljs-title function_">gradient</span>(135deg,<span class="hljs-title function_">rgba</span>(<span class="hljs-number">51</span>, <span class="hljs-number">208</span>, <span class="hljs-number">74</span>, <span class="hljs-number">0.525</span>),<span class="hljs-title function_">rgba</span>(<span class="hljs-number">90</span>, <span class="hljs-number">193</span>, <span class="hljs-number">211</span>, <span class="hljs-number">0.525</span>));
        &#125;
        <span class="hljs-number">50</span>%&#123;
            <span class="hljs-attr">background</span>:linear-<span class="hljs-title function_">gradient</span>(45deg,<span class="hljs-title function_">rgba</span>(<span class="hljs-number">210</span>, <span class="hljs-number">135</span>, <span class="hljs-number">55</span>, <span class="hljs-number">0.525</span>),<span class="hljs-title function_">rgba</span>(<span class="hljs-number">214</span>, <span class="hljs-number">55</span>, <span class="hljs-number">52</span>, <span class="hljs-number">0.525</span>));
        &#125;
        <span class="hljs-number">75</span>%&#123;
            <span class="hljs-attr">background</span>:linear-<span class="hljs-title function_">gradient</span>(135deg,<span class="hljs-title function_">rgba</span>(<span class="hljs-number">122</span>, <span class="hljs-number">55</span>, <span class="hljs-number">154</span>, <span class="hljs-number">0.525</span>),<span class="hljs-title function_">rgba</span>(<span class="hljs-number">183</span>, <span class="hljs-number">178</span>, <span class="hljs-number">31</span>, <span class="hljs-number">0.525</span>));
        &#125;
        <span class="hljs-number">100</span>%&#123;
            <span class="hljs-attr">background</span>:linear-<span class="hljs-title function_">gradient</span>(45deg,<span class="hljs-title function_">rgba</span>(<span class="hljs-number">145</span>, <span class="hljs-number">37</span>, <span class="hljs-number">96</span>, <span class="hljs-number">0.525</span>),<span class="hljs-title function_">rgba</span>(<span class="hljs-number">26</span>, <span class="hljs-number">121</span>, <span class="hljs-number">203</span>, <span class="hljs-number">0.525</span>));
        &#125;
    &#125;
    .<span class="hljs-property">box</span>&#123;
        <span class="hljs-attr">width</span>: 300px;
        <span class="hljs-attr">height</span>: 200px;
       <span class="hljs-attr">margin</span>: 100px auto;
        <span class="hljs-attr">background</span>:linear-<span class="hljs-title function_">gradient</span>(45deg,<span class="hljs-title function_">rgba</span>(<span class="hljs-number">213</span>, <span class="hljs-number">224</span>, <span class="hljs-number">92</span>, <span class="hljs-number">0.525</span>),<span class="hljs-title function_">rgba</span>(<span class="hljs-number">88</span>, <span class="hljs-number">170</span>, <span class="hljs-number">55</span>, <span class="hljs-number">0.525</span>));
        background-<span class="hljs-attr">size</span>: <span class="hljs-number">100</span>% <span class="hljs-number">100</span>%;
        background-<span class="hljs-attr">repeat</span>: no-repeat;
        border-<span class="hljs-attr">radius</span>: <span class="hljs-number">50</span>%;
        <span class="hljs-attr">animation</span>: img 5s infinite;
    &#125;
    .<span class="hljs-property">show</span>&#123;
     <span class="hljs-attr">position</span>: relative;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>background:linear-gradient(45deg,rgba(213, 224, 92, 0.525),rgba(88, 170, 55, 0.525));  这是背景的颜色渐变
方法为background:linear-gradient(方向，颜色，颜色）</li>
<li>position: relative; 注意这个一定不能写在.box中，不然阴影效果将体现不出。</li>
</ul>
<h2 data-id="heading-7">阴影效果的实现</h2>
<pre><code class="hljs language-js copyable" lang="js">.<span class="hljs-property">show</span>::after&#123;
    <span class="hljs-attr">content</span>: <span class="hljs-string">""</span>;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;
    <span class="hljs-attr">height</span>: <span class="hljs-number">100</span>%;
    <span class="hljs-attr">position</span>: absolute;
    <span class="hljs-attr">background</span>: inherit;
    border-<span class="hljs-attr">radius</span>: <span class="hljs-number">50</span>%;
    background-<span class="hljs-attr">position</span>: center center;
    <span class="hljs-attr">filter</span>: drop-<span class="hljs-title function_">shadow</span>(0px 0px 100px <span class="hljs-title function_">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>)) <span class="hljs-title function_">blur</span>(100px);
    z-<span class="hljs-attr">index</span>: -<span class="hljs-number">1</span>;
    <span class="hljs-attr">animation</span>: oscillate 1s  infinite alternate;
&#125;
 
@keyframes oscillate &#123;
  <span class="hljs-keyword">from</span> &#123;
    <span class="hljs-attr">transform</span>: <span class="hljs-title function_">scale</span>(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>);
  &#125;
  to &#123;
    <span class="hljs-attr">transform</span>: <span class="hljs-title function_">scale</span>(<span class="hljs-number">1.3</span>, <span class="hljs-number">1.3</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>background: inherit; 这是伪元素对父元素的背景属性的继承</li>
<li>filter: drop-shadow(0px 0px 100px rgba(0, 0, 0, 1)) blur(100px); 用过滤属性实现阴影</li>
<li>z-index: -1；这是类似于图层排列顺序  值越小 排的越前，</li>
<li>transform: scale(1, 1);这是图片放大效果</li>
</ul>
<h1 data-id="heading-8">完整代码</h1>
<pre><code class="hljs language-js copyable" lang="js"><!<span class="hljs-variable constant_">DOCTYPE</span> html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>智能阴影</title>
</head>
<style>
    *&#123;
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    &#125;
    body&#123;
        background-color: black;
    &#125;
    @keyframes img&#123;
        0%&#123;
            background:linear-gradient(45deg,rgba(213, 224, 92, 0.525),rgba(88, 170, 55, 0.525));
        &#125;
        25%&#123;
            background:linear-gradient(135deg,rgba(51, 208, 74, 0.525),rgba(90, 193, 211, 0.525));
        &#125;
        50%&#123;
            background:linear-gradient(45deg,rgba(210, 135, 55, 0.525),rgba(214, 55, 52, 0.525));
        &#125;
        75%&#123;
            background:linear-gradient(135deg,rgba(122, 55, 154, 0.525),rgba(183, 178, 31, 0.525));
        &#125;
        100%&#123;
            background:linear-gradient(45deg,rgba(145, 37, 96, 0.525),rgba(26, 121, 203, 0.525));
        &#125;
    &#125;
    .box&#123;
        width: 300px;
        height: 200px;
       margin: 100px auto;
        background:linear-gradient(45deg,rgba(213, 224, 92, 0.525),rgba(88, 170, 55, 0.525));
        background-size: 100% 100%;
        background-repeat: no-repeat;
        border-radius: 50%;
        animation: img 5s infinite;
    &#125;
    .show&#123;
     position: relative;
    &#125;
    .show::after&#123;
    content: "";
    width: 100%;
    height: 100%;
    position: absolute;
    background: inherit;
    border-radius: 50%;
    background-position: center center;
    filter: drop-shadow(0px 0px 100px rgba(0, 0, 0, 1)) blur(100px);
    z-index: -1;
    animation: oscillate 1s  infinite alternate;
&#125;
 
@keyframes oscillate &#123;
  from &#123;
    transform: scale(1, 1);
  &#125;
  to &#123;
    transform: scale(1.3, 1.3);
  &#125;
&#125;
</style>
<body>
    <div class="box show">
    </div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">结语</h1>
<p>初次在掘金写文章  有诸多不足之处</p></div>  
</div>
            