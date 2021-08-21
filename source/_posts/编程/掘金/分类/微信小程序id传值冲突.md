
---
title: '微信小程序id传值冲突'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a720bf095b4f4db3a7b69474e1bac3f9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 23:43:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a720bf095b4f4db3a7b69474e1bac3f9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">问题</h5>
<p>在微信小程序中，如果传递给组件的参数字段名是“id”，组件内获取this.data.id并非真正传递值。</p>
<h5 data-id="heading-1">触发条件</h5>
<p>微信开发者工具版本：1.05.2108202</p>
<p>基础库版本：2.19.2</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">testComponent</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"&#123;&#123;4&#125;&#125;"</span> <span class="hljs-attr">info</span>=<span class="hljs-string">"&#123;&#123;4&#125;&#125;"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">testComponent</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"&#123;&#123;5&#125;&#125;"</span> <span class="hljs-attr">info</span>=<span class="hljs-string">"&#123;&#123;5&#125;&#125;"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">testComponent</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"&#123;&#123;6&#125;&#125;"</span> <span class="hljs-attr">info</span>=<span class="hljs-string">"&#123;&#123;6&#125;&#125;"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// testComponent.js</span>
Component(&#123;
    <span class="hljs-attr">properties</span>: &#123;
        <span class="hljs-attr">id</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
            <span class="hljs-attr">value</span>: <span class="hljs-number">0</span>,
        &#125;,
        <span class="hljs-attr">info</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
            <span class="hljs-attr">value</span>: <span class="hljs-number">0</span>,
        &#125;,
    &#125;,
    <span class="hljs-attr">lifetimes</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">attached</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.id, <span class="hljs-built_in">this</span>.data.id, <span class="hljs-built_in">this</span>.data.info, <span class="hljs-built_in">this</span>);
        &#125;,
    &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a720bf095b4f4db3a7b69474e1bac3f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>this.id打印出来是顺序的，从1开始算，字符串类型。猜测是类似key的关键字作为索引。</p>
<p><strong>this.data.id打印出来的都是默认值0（不解，按理说properties里面的参数会跟this.data合并）。</strong></p>
<p>this.data.info仅仅是换了字段名（不叫id），能正常打印出传值。</p>
<h5 data-id="heading-2">总结</h5>
<p>组件里面，字段名尽量不要取"id"，以免出现冲突。</p></div>  
</div>
            