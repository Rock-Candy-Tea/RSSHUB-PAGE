
---
title: 'CSS系列 -- flex布局'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/480fdae0e4b141a1bfd01ed30c43dd63~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 23:43:42 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/480fdae0e4b141a1bfd01ed30c43dd63~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>flex布局被称为<code>弹性布局</code>，是CSS3中新增内容</p>
<h4 data-id="heading-0">创建flex盒子</h4>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">display</span>: flex;
或 dispaly: inline-flex;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">flex-direction属性  决定主轴的方向（即项目的排列方向）</h4>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex-direction</span>: row; <span class="hljs-comment">/*主轴是横向的，自左至右*/</span> 【默认值】
<span class="hljs-attribute">flex-direction</span>: column; <span class="hljs-comment">/*主轴是横向的，自上而下*/</span>
<span class="hljs-attribute">flex-direction</span>: row-reverse; <span class="hljs-comment">/*主轴是横向的，自右至左*/</span> 
<span class="hljs-attribute">flex-direction</span>: column-reverse; <span class="hljs-comment">/*主轴是横向的，自下而上*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">flex-wrap属性 决定是否换行</h4>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex-wrap</span>: nowrap; <span class="hljs-comment">/*不换行*/</span>【默认值】
<span class="hljs-attribute">flex-wrap</span>: wrap; <span class="hljs-comment">/*换行，第一行在上方*/</span> 
<span class="hljs-attribute">flex-wrap</span>: wrap-reverse; <span class="hljs-comment">/*换行，第一行在下方*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">justify-content 属性 定义项目在主轴上的对齐方式</h4>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">justify-content</span>: flex-start; <span class="hljs-comment">/*左对齐*/</span>【默认值】
<span class="hljs-attribute">justify-content</span>: flex-end; <span class="hljs-comment">/*右对齐*/</span> 
<span class="hljs-attribute">justify-content</span>: center; <span class="hljs-comment">/*居中*/</span>
<span class="hljs-attribute">justify-content</span>: space-between; <span class="hljs-comment">/*两端对齐，项目之间的间隔都相等*/</span> 
<span class="hljs-attribute">justify-content</span>: space-around; <span class="hljs-comment">/*每个项目两侧的间隔相等。项目之间的间隔比项目与边框的间隔大一倍*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/480fdae0e4b141a1bfd01ed30c43dd63~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">align-items 属性 定义项目在交叉轴上如何对齐</h4>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">align-items</span>: baseline; <span class="hljs-comment">/*占满整个容器的高度*/</span>【默认值】
<span class="hljs-attribute">align-items</span>: flex-start; <span class="hljs-comment">/*交叉轴的起点对齐*/</span>
<span class="hljs-attribute">align-items</span>: flex-end; <span class="hljs-comment">/*交叉轴的终点对齐*/</span> 
<span class="hljs-attribute">align-items</span>: center; <span class="hljs-comment">/*交叉轴的中点对齐*/</span>
<span class="hljs-attribute">align-items</span>: stretch; <span class="hljs-comment">/*项目的第一行文字的基线对齐*/</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61276454c2904e66810a2c2afcf760d1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">align-content 属性 定义多根轴线的对齐方式</h4>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">align-content</span>: stretch; <span class="hljs-comment">/*轴线占满整个交叉轴*/</span>【默认值】
<span class="hljs-attribute">align-content</span>: flex-start; <span class="hljs-comment">/*交叉轴的起点对齐*/</span>
<span class="hljs-attribute">align-content</span>: flex-end; <span class="hljs-comment">/*交叉轴的终点对齐*/</span> 
<span class="hljs-attribute">align-content</span>: center; <span class="hljs-comment">/*交叉轴的中点对齐*/</span>
<span class="hljs-attribute">align-content</span>: space-between; <span class="hljs-comment">/*两端对齐，项目之间的间隔都相等*/</span> 
<span class="hljs-attribute">align-content</span>: space-around; <span class="hljs-comment">/*每个项目两侧的间隔相等。项目之间的间隔比项目与边框的间隔大一倍*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75ca1720778a4cef98fb47af04f27a67~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            