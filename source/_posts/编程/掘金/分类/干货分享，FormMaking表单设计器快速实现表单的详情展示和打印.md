
---
title: '干货分享，FormMaking表单设计器快速实现表单的详情展示和打印'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8520ada392384e629738430a3a60038f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 23:57:27 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8520ada392384e629738430a3a60038f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>我们在实际的表单应用中，常常会遇到表单编辑好后，如何快速的展示详情页面又或者直接能够打印呢。接下来我们会在本文中详细道来。</p>
<h2 data-id="heading-1">设计表单</h2>
<p>通过 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fform.making.link%2Fsample%2F%23%2Fzh-CN%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://form.making.link/sample/#/zh-CN/" ref="nofollow noopener noreferrer">FormMaking</a> 设计出表单。这里我们使用表格布局，设计出如下样式的表单：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8520ada392384e629738430a3a60038f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>关于如何设计出这样的表单，可以前往<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fln7ccx%2Fntgo8q%2Fsdxou2" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/ln7ccx/ntgo8q/sdxou2" ref="nofollow noopener noreferrer">复杂报表设计</a>查看。</p>
</blockquote>
<h2 data-id="heading-2">展示表单详情</h2>
<p>我们需要展示表单详情的时候，只需要配置表单组件的参数，启用表单打印阅读即可，表单就会将文本框转化为文本类型。设置如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">fm-generate-form</span> 
    <span class="hljs-attr">:data</span>=<span class="hljs-string">"jsonData"</span> 
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"generateForm"</span> 
    <span class="hljs-attr">:print-read</span>=<span class="hljs-string">"true"</span> ></span>
<span class="hljs-tag"></<span class="hljs-name">fm-generate-form</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5156190a2e394dc4b6ae05d5b8ad65b0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>将 <code>print-read</code> 属性设置成 <code>true</code> 即可，是不是很简单呢。</p>
</blockquote>
<h2 data-id="heading-3">表单打印</h2>
<p>实现表单打印也是非常简单的，我们上面已经将表单设置成打印阅读模式，让文本框消失，直接展示文本了，我们就可以直接调用 <code>window.print()</code>来实现页面的打印。</p>
<p>但是，有时我们的页面上还有其它的元素，比如打印按钮等，我们不想将其打印出来，这个时候我们就需要使用 CSS 媒体查询 <code>@media print</code> 来修改样式，实现在打印设备上的展示效果。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">fm-generate-form</span> 
      <span class="hljs-attr">:data</span>=<span class="hljs-string">"jsonData"</span>
      <span class="hljs-attr">ref</span>=<span class="hljs-string">"generateForm"</span>
      <span class="hljs-attr">:print-read</span>=<span class="hljs-string">"true"</span>
    ></span>
    <span class="hljs-tag"></<span class="hljs-name">fm-generate-form</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"print-btn"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handlePrint"</span>></span>打印<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-keyword">@media</span> print&#123; <span class="hljs-selector-class">.print-btn</span>&#123; <span class="hljs-attribute">display</span>: none; &#125; &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来看看最后的效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee287e065d6d424882d7546e2377b8aa~tplv-k3u1fbpfcp-watermark.image" alt="Kapture 2021-08-24 at 10.41.15.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            