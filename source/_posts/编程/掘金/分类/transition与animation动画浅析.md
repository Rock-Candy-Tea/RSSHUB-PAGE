
---
title: 'transition与animation动画浅析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5267'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:19:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=5267'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">浏览器渲染原理</h3>
<ol>
<li>处理 HTML 并构建 DOM 树</li>
<li>处理 CSS构建 CSSOM 树</li>
<li>将 DOM 与 CSSOM 合并成一个渲染树</li>
<li>根据渲染树来布局，计算每个节点的位置</li>
<li>调用 GPU 绘制，合成图层，显示在屏幕上</li>
</ol>
<hr>
<h3 data-id="heading-1">transition</h3>
<p>语法：</p>
<ul>
<li>transition:属性名 时长 过渡方式 延迟:transition:left 200ms linear</li>
<li>可以用逗号分隔两个不同属性：transition:left 200ms,top 400ms</li>
<li>可以用all代表所有属性：transition:all 200ms</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.demo</span>&#123;
    <span class="hljs-attribute">height</span>:<span class="hljs-number">100px</span>;
    <span class="hljs-attribute">width</span>:<span class="hljs-number">100px</span>;
    <span class="hljs-attribute">transition</span>: <span class="hljs-number">1s</span> <span class="hljs-number">1s</span> height ease;   <span class="hljs-comment">/*合在一起*/</span>
&#125;
或者：
<span class="hljs-selector-class">.demo</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">border</span>:<span class="hljs-number">1px</span> solid red;
  <span class="hljs-attribute">transition-property</span>: all;      <span class="hljs-comment">/*指定要过渡的css属性，本例中，还可以指定width或height其中的一种，all为全部*/</span>     
  <span class="hljs-attribute">transition-duration</span>: <span class="hljs-number">1s</span>;      <span class="hljs-comment">/*整个过渡的时长*/</span>          
  <span class="hljs-attribute">transition-delay</span>: <span class="hljs-number">1s</span>;          <span class="hljs-comment">/*延迟时间*/</span>        
  <span class="hljs-attribute">transition-timing-function</span>: ease;    <span class="hljs-comment">/*过渡效果*/</span>
&#125;
<span class="hljs-selector-class">.demo</span><span class="hljs-selector-pseudo">:hover</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">450px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">450px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>属性详解</strong></p>
<ul>
<li>transition-property：</li>
</ul>
<p>不是所有属性都能过渡，只有属性具有一个中间点值才具备过渡效果。</p>
<ul>
<li>transition-duration：</li>
</ul>
<p>指定从一个属性到另一个属性过渡所要花费的时间。默认值为0。</p>
<ul>
<li>transiton-timing-function：</li>
</ul>
<p>有如下几种：
liner ：匀速
ease：默认
ease-in：减速
ease-out：加速
ease-in-out：先加速再减速
cubic-bezier：三次贝塞尔曲线</p>
<ul>
<li>触发过渡的方式：</li>
</ul>
<p>单纯的代码不会触发任何过渡操作，需要通过用户的行为（如点击，悬浮等）触发，可触发的方式一般有：:hover :focus :checked 媒体查询触发 JavaScript触发</p>
<ul>
<li>局限性：
<ul>
<li>transition需要事件触发，所以没法在网页加载时自动发生。</li>
<li>transition是一次性的，不能重复发生，除非一再触发。</li>
<li>transition只能定义开始状态和结束状态，不能定义中间状态，也就是说只有两个状态。</li>
<li>一条transition规则，只能定义一个属性的变化，不能涉及多个属性。</li>
</ul>
</li>
</ul>
<hr>
<h3 data-id="heading-2">animation</h3>
<ul>
<li>animation可以通过控制关键帧来控制动画的每一步，实现更为复杂的动画效果。</li>
<li>缩写语法：animation:时长|过渡方式|延迟|次数|方向|填充模式|是否暂停|动画名;</li>
<li>时长：1s 或者 1000ms</li>
<li>过渡方式：跟transition 取值一样，如linear</li>
<li>次数：3说着2.4 说着 infinite（无限循环）</li>
<li>方向：reverse | alternate（效果：开始>结束>开始） | alternate-reverse</li>
<li>填充模式：none | forwards | backwards | both</li>
<li>是否暂停：paused | running</li>
</ul>
<p><strong>以上属性均有对应的单独属性</strong></p>
<p>示例：跳动的心</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"heart"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bottom"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css">*&#123;<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;<span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;<span class="hljs-attribute">box-sizing</span>:border-box;&#125;

<span class="hljs-selector-id">#heart</span>&#123;
  <span class="hljs-attribute">margin</span>:<span class="hljs-number">100px</span>;
  <span class="hljs-attribute">position</span>:relative;
  <span class="hljs-attribute">display</span>: inline-block;
  <span class="hljs-attribute">animation</span>:heart <span class="hljs-number">800ms</span> infinite alternate;
&#125;

<span class="hljs-keyword">@keyframes</span> heart&#123;
  <span class="hljs-number">0%</span>&#123;
    <span class="hljs-attribute">transform</span>:<span class="hljs-built_in">scale</span>(<span class="hljs-number">1.0</span>);
  &#125;
  <span class="hljs-number">100%</span>&#123;
    <span class="hljs-attribute">transform</span>:<span class="hljs-built_in">scale</span>(<span class="hljs-number">1.2</span>);
  &#125;
&#125;

<span class="hljs-selector-id">#heart</span>><span class="hljs-selector-class">.bottom</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">background</span>: red;
  <span class="hljs-attribute">transform</span>:<span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>);
&#125;

<span class="hljs-selector-id">#heart</span>><span class="hljs-selector-class">.left</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">background</span>: red;
  <span class="hljs-attribute">border-radius</span>:<span class="hljs-number">50%</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">position</span>:absolute;
  <span class="hljs-attribute">bottom</span>:<span class="hljs-number">100%</span>;
  <span class="hljs-attribute">right</span>:<span class="hljs-number">100%</span>;
  <span class="hljs-attribute">transform</span>:<span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>) <span class="hljs-built_in">translateX</span>(<span class="hljs-number">40px</span>);
&#125;

<span class="hljs-selector-id">#heart</span>><span class="hljs-selector-class">.right</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">background</span>: red;
  <span class="hljs-attribute">border-radius</span>:<span class="hljs-number">50%</span> <span class="hljs-number">50%</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
  <span class="hljs-attribute">position</span>:absolute;
  <span class="hljs-attribute">bottom</span>:<span class="hljs-number">100%</span>;
  <span class="hljs-attribute">left</span>:<span class="hljs-number">100%</span>;
  <span class="hljs-attribute">transform</span>:<span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>) <span class="hljs-built_in">translateY</span>(<span class="hljs-number">40px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            