
---
title: '_element ui_如何定制化自己el ui的样式？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b6f7fea688f4427968ada691501093d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 03:19:12 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b6f7fea688f4427968ada691501093d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>el ui 组件大大的提高了我们的开发效率，将一些逻辑和样式封装起来，我们可以直接使用，十分的good。但是，对于公司的一些定制化的需求，仅仅靠着组件提供的api是不方便解决的，特别是样式上的问题。<br>
如果可以修改对el ui组件的样式直接进行修改，那么我们的工作就简化成了修改，而不是重复的造轮子。<br></p>
<h2 data-id="heading-0">存在的问题</h2>
<p>对于使用vue开发的同学来说（比如说我司），想要在一个页面或者一个component中修改el ui的样式，基本无可避免的会影响整个项目中其他的相同的el ui组件的样式，原因是样式是全局的。如果加上<code>scoped</code>,修改又不会生效。</p>
<h2 data-id="heading-1">解决办法</h2>
<p>经过了一天的思考和实验，走了不少弯路，比如写内联的<code>style</code> 和 在 <code>postcss</code> 中加上 <code>!important</code>等方法，发现指标不治本，而且还是会不经意间影响全局其他的el ui组件，怎么样将修改限制到局部作用页面中？</p>
<p><strong>利用<code>postcss</code>和<code>dom</code>的层级关系，进行针对性的修改。</strong></p>
<h2 data-id="heading-2">例子</h2>
<p>比如有以下代码：</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>
      主要按钮
    <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>
      主要按钮2
    <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.button1</span> &#123;
  <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.5</span>;
&#125;
<span class="hljs-selector-class">.button2</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b6f7fea688f4427968ada691501093d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我有两个需求：</p>
<ul>
<li>按钮1背景改为半透明的；</li>
<li>按钮2外形改为正方形；</li>
</ul>
<p>查看组件的api是无法达到这个需求的，那么我直接开始进行修改！<br></p>
<p>打开控制台，可以看到以下dom结构：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91a453fa3f5f40978bf5cabc49268b96~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果直接进行修改，肯定会影响另外一个按钮，达不到我们想要的效果。所以，可以如下：</p>
<ul>
<li>再添加一个class：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"button1"</span>></span>
      主要按钮
<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"button2"</span>></span>
      主要按钮2
<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6c69c93cd39459096b975246f42e32b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>外面套一层全局唯一的dom：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"button1"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>
        主要按钮
      <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"button2"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>
        主要按钮2
      <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>postcss:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.button1</span> &#123;
  & <span class="hljs-selector-class">.el-button</span> &#123;
    <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.5</span>;
  &#125;
&#125;
<span class="hljs-selector-class">.button2</span> &#123;
  & <span class="hljs-selector-class">.el-button</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f42665ae2c9c4073b63ff7d748722900~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个例子还看不出什么区别，但是有的情况下组件的dom嵌套过深，无法直接添加class，用第二种方法一层一层的去找，也还是可以接受的。<br>
不管怎么说，都不太优雅，但也提高了一些逻辑代码的复用度，减少了项目复杂度和工期，也未尝不可一试。</p></div>  
</div>
            