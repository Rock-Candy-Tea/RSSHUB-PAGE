
---
title: 'IDE配置代码片段模板'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af446c30c3d346d080745c5746265957~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 21:46:27 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af446c30c3d346d080745c5746265957~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在Vue学习工程中，经常需要创建不同的文件，有js文件，也有组件文件。在文件中，有部分代码是相同或相似，如何能够节省这些重复性劳动？我们可以将这些代码生成代码片段，在新的文件中通过快捷方式快速生成相应的代码，剩下的只是按需少量修改相应的代码段来完善功能即可。</p>
<h2 data-id="heading-1">Webstorm - Live Templates</h2>
<ul>
<li>设置路径：</li>
</ul>
<p>File -> Settings -> Live Templates；</p>
<ul>
<li>
<p>右侧工作区找到 'Vue'，点击最右侧的 '+'；</p>
</li>
<li>
<p>配置缩写'Abbreviation'，如'vue'</p>
</li>
<li>
<p>添加Template Text</p>
</li>
</ul>
<p>如下图所示：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af446c30c3d346d080745c5746265957~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>确定后，在新的文件中，通过输入'vue'可直接引用如上配置的代码片段。</p>
<h2 data-id="heading-2">VSCode - User Snippets</h2>
<ul>
<li>设置路径：</li>
</ul>
<p>File -> Preferences -> User Snippets</p>
<ul>
<li>选择你需要自定义模板的文件，以vue为例</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1c6570fbc65442a8d57cb9f212af272~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>配置对应文件json</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-string">"vue-component-template"</span>: &#123;
    <span class="hljs-string">"prefix"</span>: <span class="hljs-string">"template_comp"</span>,
    <span class="hljs-string">"body"</span>: [
      <span class="hljs-string">"<template>"</span>,
      <span class="hljs-string">"  <div>"</span>,
      <span class="hljs-string">"    <h3>权限管理页面</h3>"</span>,
      <span class="hljs-string">"  </div>"</span>,
      <span class="hljs-string">"</template>"</span>,
      <span class="hljs-string">""</span>,
      <span class="hljs-string">"<script>"</span>,
      <span class="hljs-string">"export default &#123;&#125;"</span>,
      <span class="hljs-string">"</script>"</span>,
      <span class="hljs-string">""</span>,
      <span class="hljs-string">"<style lang=\"less\" scoped></style>"</span>
    ],
    <span class="hljs-string">"description"</span>: <span class="hljs-string">"Vue component"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            