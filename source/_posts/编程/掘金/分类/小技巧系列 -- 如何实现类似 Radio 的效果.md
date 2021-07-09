
---
title: '小技巧系列 -- 如何实现类似 Radio 的效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ded5759c9944478d870d7e8e4c407bd5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 04:18:15 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ded5759c9944478d870d7e8e4c407bd5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">需求</h2>
<blockquote>
<p>有五个图标，初始时只能有一个“亮着”，控制鼠标可以“点亮”，但同时只能一个“亮着”</p>
</blockquote>
<ul>
<li>实现目标：</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ded5759c9944478d870d7e8e4c407bd5~tplv-k3u1fbpfcp-watermark.image" alt="4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">步骤</h2>
<p><strong>1. 画出图标</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in list"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"icon"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.icon</span>&#123;
    <span class="hljs-attribute">color</span>: gray;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">charts: [<span class="hljs-string">'chartA'</span>,<span class="hljs-string">'chartB'</span>,<span class="hljs-string">'chartC'</span>,<span class="hljs-string">'chartD'</span>,<span class="hljs-string">'chartE'</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33d2e8abb08747b0bff7bc50e0281230~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2. 绘制出点亮之后的效果</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.icon-active</span>&#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#3c4fe0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/223cf3703a17426491b003b18ab49510~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3. 绑定点击事件</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in list"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"icon"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"chartTypeChange(item)"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">chartChoosed: <span class="hljs-string">'chartA'</span>, <span class="hljs-comment">// 当前选中项</span>
<span class="hljs-attr">charts</span>: [<span class="hljs-string">'chartA'</span>,<span class="hljs-string">'chartB'</span>,<span class="hljs-string">'chartC'</span>,<span class="hljs-string">'chartD'</span>,<span class="hljs-string">'chartE'</span>]
<span class="hljs-function"><span class="hljs-title">chartTypeChange</span>(<span class="hljs-params">choose</span>)</span>&#123; <span class="hljs-comment">// 点击事件</span>
    <span class="hljs-built_in">console</span>.log(choose)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a31bc1a43414422a8d1367ab5c59d8e2~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>绑定当前活跃项并渲染其样式</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> 
    <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in list"</span>
    <span class="hljs-attr">:class</span>=<span class="hljs-string">"chartChoosed === item ? 'icon-active' : 'icon'"</span>
    @<span class="hljs-attr">click</span>=<span class="hljs-string">"chartTypeChange(item)"</span> 
/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里注意的是：</p>
<ul>
<li>属性名称 = "不变的属性值"</li>
<li><code>:</code> + 属性名称 = "会变化的属性值"（是<code>v-bind:属性名称</code>的缩写）</li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">chartChoosed: <span class="hljs-string">'chartA'</span>, <span class="hljs-comment">// 当前选中项</span>
<span class="hljs-attr">charts</span>: [<span class="hljs-string">'chartA'</span>,<span class="hljs-string">'chartB'</span>,<span class="hljs-string">'chartC'</span>,<span class="hljs-string">'chartD'</span>,<span class="hljs-string">'chartE'</span>]
<span class="hljs-function"><span class="hljs-title">chartTypeChange</span>(<span class="hljs-params">choose</span>)</span>&#123; <span class="hljs-comment">// 点击事件</span>
    <span class="hljs-built_in">this</span>.chartChoosed = choose
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ded5759c9944478d870d7e8e4c407bd5~tplv-k3u1fbpfcp-watermark.image" alt="4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至此已完成</p></div>  
</div>
            