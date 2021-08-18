
---
title: 'CSS 响应式布局总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce4925bc96d74e06b8acfa21b492619f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 19:20:05 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce4925bc96d74e06b8acfa21b492619f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">媒体查询(media query)</h1>
<p>媒体查询就是对设备按照某些条件进行查询，使符合查询条件的设备显示对应的样式，从而达到不同设备显示不同样式的效果。</p>
<p>通过媒体查询，我们可以根据各种设备特征和参数的值或者是否存在来调整我们的网站或应用。</p>
<p>下面是一个媒体查询的例子，不同设备的屏幕宽度不同，显示的颜色也不相同</p>
<pre><code class="hljs language-css copyable" lang="css"><style>
 <span class="hljs-keyword">@media</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">768px</span>)&#123; <span class="hljs-comment">/*0~768*/</span>
    <span class="hljs-selector-tag">body</span>&#123;
        <span class="hljs-attribute">background</span>: red;
    &#125;
 &#125;  
 <span class="hljs-keyword">@media</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">425px</span>)&#123; <span class="hljs-comment">/*0~425*/</span>
    <span class="hljs-selector-tag">body</span>&#123;
        <span class="hljs-attribute">background</span>: yellow;
    &#125;
 &#125;  
 <span class="hljs-keyword">@media</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">375px</span>)&#123; <span class="hljs-comment">/*0~375*/</span>
    <span class="hljs-selector-tag">body</span>&#123;
        <span class="hljs-attribute">background</span>: blue;
    &#125;
 &#125;  
 <span class="hljs-keyword">@media</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">320px</span>)&#123; <span class="hljs-comment">/*0~320*/</span>
    <span class="hljs-selector-tag">body</span>&#123;
        <span class="hljs-attribute">background</span>: pink;
    &#125;
 &#125;  

 <span class="hljs-keyword">@media</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">769px</span>)&#123; <span class="hljs-comment">/*769~+∞*/</span>
    <span class="hljs-selector-tag">body</span>&#123;
        <span class="hljs-attribute">background</span>: green;
    &#125;
 &#125;  
</style> 
<span class="hljs-comment">/*注意顺序，优先级问题*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fjs.jirengu.com%2Fvihaxilabo%2F2%2Fedit%3Fhtml%2Coutput" target="_blank" rel="nofollow noopener noreferrer" title="http://js.jirengu.com/vihaxilabo/2/edit?html,output" ref="nofollow noopener noreferrer">查看效果</a></p>
<p>或者这样写</p>
<pre><code class="hljs language-css copyable" lang="css"><style>
  <span class="hljs-keyword">@media</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">320px</span>)&#123; <span class="hljs-comment">/*0~320*/</span>
      <span class="hljs-selector-tag">body</span>&#123;
          <span class="hljs-attribute">background</span>: pink;
      &#125;
   &#125; 
   <span class="hljs-keyword">@media</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">321px</span>) <span class="hljs-keyword">and</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">375px</span>)&#123; <span class="hljs-comment">/*321~768*/</span>
      <span class="hljs-selector-tag">body</span>&#123;
          <span class="hljs-attribute">background</span>: red;
      &#125;
   &#125;  
   <span class="hljs-keyword">@media</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">376px</span>) <span class="hljs-keyword">and</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">425px</span>)&#123; <span class="hljs-comment">/*376~425*/</span>
      <span class="hljs-selector-tag">body</span>&#123;
          <span class="hljs-attribute">background</span>: yellow;
      &#125;
   &#125;  
   <span class="hljs-keyword">@media</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">426px</span>) <span class="hljs-keyword">and</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">768px</span>)&#123; <span class="hljs-comment">/*426~768*/</span>
      <span class="hljs-selector-tag">body</span>&#123;
          <span class="hljs-attribute">background</span>: blue;
      &#125;
   &#125;  

   <span class="hljs-keyword">@media</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">769px</span>)&#123; <span class="hljs-comment">/*769~+∞*/</span>
      <span class="hljs-selector-tag">body</span>&#123;
          <span class="hljs-attribute">background</span>: green;
      &#125;
   &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fjs.jirengu.com%2Fsanamezije%2F1%2Fedit%3Fhtml%2Coutput" target="_blank" rel="nofollow noopener noreferrer" title="http://js.jirengu.com/sanamezije/1/edit?html,output" ref="nofollow noopener noreferrer">查看效果</a></p>
<p>另外，媒体查询的结果是可以用文件来代替其内容的，可以通过引用外部 CSS 文件来实现媒体查询。例如</p>
<p><code><link rel="stylesheet" href="style.css" media="(max-width: 320px)"></code></p>
<p>上面这段代码的意思是：link标签是否生效是受媒体查询影响的，只有满足设备宽度在 0~320px 之间，这个 link 标签才会生效。</p>
<p>注意：link 标签里的文件内容都是会先下载下来的，然后再根据查询条件判断是否生效。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fjs.jirengu.com%2Fneyuriwuke%2F1%2Fedit%3Fhtml%2Ccss%2Coutput" target="_blank" rel="nofollow noopener noreferrer" title="http://js.jirengu.com/neyuriwuke/1/edit?html,css,output" ref="nofollow noopener noreferrer">一个响应式的导航栏demo</a></p>
<p>从以上的例子中我们不难看出，响应式页面的本质就是写了两个页面的内容（移动端+PC端）在同一个页面中，然后根据查询条件来切换该用哪个页面。</p>
<p>那我们为什么不将移动端页面和PC端页面的内容分别写在两个页面中，然后让后端来切换状态呢？</p>
<p>后端伪代码</p>
<pre><code class="hljs language-raw copyable" lang="raw">&#123;&#123; if userAgent.test(/iPhone/) &#125;&#125;
    &#123;&#123; = render 'iphone_index.html' &#125;&#125; /* 检测为iPhone就渲染移动端页面 */
&#123;&#123; else &#125;&#125;
    &#123;&#123; = render 'pc_index.html' &#125;&#125; /* 否则就渲染PC端页面 */
&#123;&#123; end &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以是可以，但这种方式不是目前流行的方式。因为这样做的话，一个页面就不能确定它的 URL 到底是移动端的还是 PC 端的</p>
<p>那我们来看看淘宝，京东等网站是如何做响应式的呢？</p>
<p>当我们在PC端访问<code>taobao.com</code>时，它的域名为</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce4925bc96d74e06b8acfa21b492619f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后用开发者工具把切换至移动端，发现淘宝的域名变了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a99a7b990c84bbaa5b11f323781b688~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发现不同了吗，淘宝的移动端页面和 PC 端页面各有一个域名，因此实际上淘宝的移动端和 PC 端是两个不同的网站。其实淘宝并没有做响应式，淘宝移动端部门和 PC 部门其实是两个不同的部门，他们分别负责移动端页面和 PC 端页面。京东的网站也是一样。</p>
<p>后端伪代码</p>
<pre><code class="hljs language-raw copyable" lang="raw">&#123;&#123; if userAgent.test(/iPhone/) &#125;&#125;
    &#123;&#123; redirect_to `https://h5.m.taobao.com` &#125;&#125; /* 检测是否为移动端域名，是的话就直接访问移动端页面 */
&#123;&#123; else &#125;&#125;
    &#123;&#123; = render 'pc_index.html' &#125;&#125; /* 否则就渲染PC端页面 */
&#123;&#123; end &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在几乎没有多少网站是响应式的，只有一些简单的新闻站点或博客站点才会做响应式，因为它们的页面比较简单，没有多少交互。</p>
<h1 data-id="heading-1">移动端要加一个 meta viewport</h1>
<p>因为一些历史原因，手机端页面默认把 PC 端页面进行了缩放（大多数 PC 端网页宽度为 980px），比如 iphone6 会用 375px 的宽度去模拟PC端网页 980px 的宽度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cab1b5626a54a358c920467acd5a3b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了解决这个默认缩放的问题，就需要在页面中加一个 meta viewport 标签</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"</span>></span>
 // width=device-width: 让当前viewport（视口）宽度等于设备的宽度
 // user-scalable=no: 禁止用户缩放
 // initial-scale=1.0: 设置页面的初始缩放值为1.0（不缩放）
 // maximum-scale=1.0: 允许用户的最大缩放值为1.0
 // minimum-scale=1.0: 允许用户的最小缩放值为1.0 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就解决了这个“980问题”</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2d193d857234fe0b00f120a06b9af71~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">移动端页面与 PC 端页面有什么不同</h1>
<p>移动端页面的交互方式和 PC 端页面不一样，具体表现在：</p>
<ol>
<li>没有 hover</li>
<li>没有 click 事件，但有 touch 事件（可以通过 touch 事件来模拟用户的滑动事件，只需要记录两次触摸的位置，观察两次触摸位置的区别，就知道用户往哪个方向滑动了）。</li>
<li>不能 resize，viewport（视口）的宽度始终等于设备的宽度（PC 端页面的宽度 !== 设备宽度，可以任意调整页面大小），屏幕始终为固定宽高，因此没有办法调整页面的大小。</li>
<li>没有滚动条。
<ul>
<li>当在移动设备上滑动时，才会出现滚动条，停止滑动便会自动隐藏。</li>
<li>例子：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fjs.jirengu.com%2Fveyic%2F2%2Fedit%3Fhtml%2Coutput" target="_blank" rel="nofollow noopener noreferrer" title="http://js.jirengu.com/veyic/2/edit?html,output" ref="nofollow noopener noreferrer">移动端做一个没有滚动条的横向滚动</a></li>
</ul>
</li>
</ol>
<p>其他区别几乎没有了，而且移动端（几乎）没有 IE，因此可以用许多最新的 CSS3 属性，如 transform、transation、animation 等。</p>
<h1 data-id="heading-3">总结</h1>
<ul>
<li>响应式页面的本质就是写了两个页面的内容（移动端+PC端）在同一个页面中，然后根据查询条件来切换该用哪个页面</li>
<li>如果是同一个页面内之间的状态，用JS来切换状态；如果是不同屏幕之间的状态，用媒体查询来切换状态</li>
<li>适配移动端用<strong>媒体查询 & meta viewport</strong></li>
<li>移动端页面的交互方式和 PC 端页面不同</li>
<li>学会隐藏元素 <code>display: none;</code>，移动端常用属性 <code>display: flex</code>，<code>width: calc(50% - 10px);</code></li>
<li>mobile-first 表示优先设计移动端页面的方案，desktop-first 表示优先设计PC端页面的方案</li>
</ul></div>  
</div>
            