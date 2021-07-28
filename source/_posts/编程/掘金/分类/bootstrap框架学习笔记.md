
---
title: 'bootstrap框架学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8129'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 01:36:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=8129'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">bootstrap框架相关知识点</h2>
<ol>
<li><code> bootstrap</code>框架首先下载它的<code>css</code>和<code>js</code>，还有<code>jQuery.js</code>并引用。以移动设备优先。</li>
<li>流体容器：<code>container-fluid</code>，就是一个弹性布局，容器的<code>width</code>为<code>auto</code>，只是两边加了15px的<code>padding</code>。</li>
<li>固定容器：<code>container</code>，有阈值，容器的<code>width</code>会随设备分辨率的不同而生产变化。

























<table><thead><tr><th>阈值</th><th>width</th></tr></thead><tbody><tr><td>大于等于1200(lg 大屏pc)</td><td>1170（1140+槽宽）</td></tr><tr><td>大于等于992(md 中屏pc)小于1200</td><td>970（940+槽宽）</td></tr><tr><td>大于等于768(sm 平板)小于992</td><td>750（720+槽宽）</td></tr><tr><td>小于768(xs 移动手机)</td><td>auto</td></tr></tbody></table>
</li>
</ol>
<h2 data-id="heading-1">栅格源码分析</h2>
<ol>
<li>
<p>流体容器&固定容器 公共样式</p>
</li>
</ol>
<pre><code class="copyable">    margin-right: auto;

    margin-left: auto;

    padding-left: 15px;

    padding-right: 15px;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>固定容器 特定样式（顺序不可变）
变化就出错,因为是从小到大排序的,相反会导致小的读不到.</li>
</ol>
<pre><code class="copyable">@media (min-width: @screen-sm-min) &#123;

width: @container-sm;

&#125;

@media (min-width: @screen-md-min) &#123;

width: @container-md;

&#125;

@media (min-width: @screen-lg-min) &#123;

width: @container-lg;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>行</li>
</ol>
<pre><code class="copyable">margin-left: -15px;

margin-right: -15px;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>列（递归）</li>
</ol>
<pre><code class="copyable">.make-grid-columns()--->

.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1,

.col-xs-2, .col-sm-2, .col-md-2, .col-lg-2,

...

.col-xs-12, .col-sm-12, .col-md-12, .col-lg-12&#123;

    position: relative;

    min-height: 1px;

    padding-left: 15px;

    padding-right: 15px;

&#125;

.make-grid(xs)--->

float-grid-columns(@class);

 .col-xs-1,.col-xs-2,.col-xs-3,.col-xs-4,...col-xs-12&#123;

 float: left;

&#125;

.loop-grid-columns(@grid-columns, @class, width);

.col-xs-12&#123;

 width:12/12;

 &#125;

 .col-xs-11&#123;

 width:11/12;

 &#125;

 ...

 .col-xs-1&#123;

 width:1/12;

 &#125;

.loop-grid-columns(@grid-columns, @class, pull);

.loop-grid-columns(@grid-columns, @class, push);

push pull:

 .col-xs-push-12&#123; .col-xs-pull-12&#123;

 left:12/12; right:12/12;

 &#125; &#125;

 .col-xs-push-11&#123;

 left:11/12;

 &#125;

 ... ...
 .col-xs-push-1&#123;
 left:1/12;
 &#125;

.col-xs-push-0&#123; .col-xs-pull-0&#123;

 left:auto; right:auto;

 &#125; &#125;

.loop-grid-columns(@grid-columns, @class, offset);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">栅格系统</h2>
<p><code>col-lg-x</code></p>
<p><code>col-md-x</code></p>
<p><code>col-sm-x</code></p>
<p><code>col-xs-x</code></p>
<pre><code class="copyable">x默认拥有12个等级
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">列偏移</h2>
<p>调整的是<code>margin-left</code>，分13个等级（0到12）</p>
<p>0时为0%</p>
<h2 data-id="heading-4">列排序</h2>
<p>（注意阈值上样式的设置不能跳跃）</p>
<p><code>push</code>的时候调整的是left（从左往右），分13个等级（0到12）</p>
<p>0时为<code>auto</code></p>
<p><code>pull</code>的时候调整的是right（从右往左），分13个等级（0到12）</p>
<p>0时为<code>auto</code></p>
<h2 data-id="heading-5">响应式工具</h2>
<p><code>visible-</code> 到一定阈值时显示</p>
<p><code>hidden- </code>到一定阈值时隐藏</p>
<h2 data-id="heading-6">栅格盒模型设计的精妙之处</h2>
<p>容器两边具有15px的<code>padding</code></p>
<p>行 两边具有-15px的<code>margin</code></p>
<p>列 两边具有15px的<code>padding</code></p>
<ol>
<li>
<p>为了维护槽宽的规则，列两边必须得要15px的<code>padding</code></p>
</li>
<li>
<p>为了能使列嵌套行，行两边必须要有-15px的<code>margin</code></p>
</li>
<li>
<p>为了让容器可以包裹住行，容器两边必须要有15px的<code>padding</code></p>
</li>
</ol></div>  
</div>
            