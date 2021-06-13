
---
title: '浅析CSS样式权重和优先级'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf4552696d840deb93dc87a0b9481b0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 23:42:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf4552696d840deb93dc87a0b9481b0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第<strong>13</strong>天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">一、什么是优先级：</h2>
<p>即通过优先级来判断如何在页面上显示这些样式。优先级是基于不同种类的选择器组成的匹配规则。
关于CSS的选择器可以看这篇<a href="https://juejin.cn/post/6970500385479852040" target="_blank">《一次性搞懂CSS选择器》</a>，这里就不重复讲啦。</p>
<h2 data-id="heading-1">二、优先级是怎么样计算的？</h2>
<p><strong>注意: 文档树中元素的接近度对优先级没有影响</strong></p>
<p>比如我们在这样一段代码当中，对同一个div进行样式的设定。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">通配符 VS 标签选择器</h3>
<p>当我们对其声明<strong>通配符和标签选择器</strong>两种的时候，由于<strong>标签选择器的优先级大于通配符</strong>，所以在盒子里面呈现绿色。</p>
<pre><code class="hljs language-css copyable" lang="css"><style>
    <span class="hljs-selector-class">.container</span> &#123;
        <span class="hljs-attribute">text-align</span>: center;
        <span class="hljs-attribute">color</span>: white;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    &#125;
    * &#123;  
        <span class="hljs-attribute">background-color</span>: firebrick;    <span class="hljs-comment">/* 通配符 */</span>
    &#125;
    <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">background-color</span>: green;   <span class="hljs-comment">/* 标签选择器 */</span>
    &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf4552696d840deb93dc87a0b9481b0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">属性选择器VS标签选择器</h3>
<p>同样的例子，我们修改一下选择器的类型。</p>
<pre><code class="hljs language-css copyable" lang="css">    <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">background-color</span>: green;   <span class="hljs-comment">/* 标签选择器 */</span>
    &#125;
    <span class="hljs-selector-class">.container</span> &#123;
        <span class="hljs-attribute">background-color</span>: crimson;   <span class="hljs-comment">/* 属性选择器 */</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4180a7664e84fc4be8ed1c422627280~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，<strong>属性选择器的优先级是大于标签选择器的</strong>，所以呈现红色。</p>
<h3 data-id="heading-4">id选择器 VS 属性选择器</h3>
<pre><code class="hljs language-css copyable" lang="css">    <span class="hljs-selector-class">.container</span> &#123;
        <span class="hljs-attribute">background-color</span>: crimson;   <span class="hljs-comment">/* 属性选择器 */</span>
    &#125;
    <span class="hljs-selector-id">#box</span> &#123;
        <span class="hljs-attribute">background-color</span>: gold;   <span class="hljs-comment">/* id选择器 */</span>
    &#125;    
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88fc8996e805469bb284377193506e1b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
由此可见，<strong>id选择器的优先级大于属性选择器</strong>，所以呈现金色。</p>
<h3 data-id="heading-5">行内样式 VS id选择器</h3>
<p>我们在开发中其实也是会写到行内样式的，接下来我们就来看看哪个的优先级更高。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: hotpink;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#box</span> &#123;
  <span class="hljs-attribute">background-color</span>: gold;   <span class="hljs-comment">/* id选择器 */</span>
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示的效果👇</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e0bdd9a3f1f4fe2b238b899cf6b5612~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>所以行内样式其实是比普通的选择器的优先级高的。</strong></p>
<h3 data-id="heading-6">!important</h3>
<p>另外，<code>!important</code>是例外的规则，当一个样式当中使用了<code>!important</code>规则时，会覆盖其他的任何。</p>
<p>比如我们在刚刚优先级最低的通配符当中设置背景颜色，其他选择器样式都不变。</p>
<pre><code class="hljs language-css copyable" lang="css"> * &#123;
   <span class="hljs-attribute">background-color</span>: indigo <span class="hljs-meta">!important</span>;
&#125;
<span class="hljs-comment">/* 标签选择器 */</span>
<span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">background-color</span>: green;
&#125;
<span class="hljs-comment">/* 属性选择器 */</span>
<span class="hljs-selector-class">.container</span> &#123;
   <span class="hljs-attribute">background-color</span>: crimson;
&#125;
<span class="hljs-comment">/* id选择器 */</span> 
<span class="hljs-selector-id">#box</span> &#123;
   <span class="hljs-attribute">background-color</span>: gold;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6f6788f7f18449e9a17bb491aaf5969~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，<strong>使用<code>!important</code>的优先级是最高的</strong>，所以覆盖了前面的样式。</p>
<p>但是盲目使用<code>!important</code>是一种<strong>坏习惯</strong>，因为它破坏了样式表当中的规则，当我们在调试的时候，就会变得非常的困难。</p>
<p><strong>最后总结一下选择器上的优先级：</strong></p>
<p><strong>!important>行内样式>id选择器>class选择器/属性选择器>标签选择器>通配符</strong>*</p></div>  
</div>
            