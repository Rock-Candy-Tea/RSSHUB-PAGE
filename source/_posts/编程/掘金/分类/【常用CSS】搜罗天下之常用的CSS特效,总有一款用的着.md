
---
title: '【常用CSS】搜罗天下之常用的CSS特效,总有一款用的着'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9767f7e621544f68a7d105b32aef6972~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 01:14:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9767f7e621544f68a7d105b32aef6972~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2 万元奖池等你挑战！</a></p>
<h2 data-id="heading-0">实用 CSS 特效</h2>
<h2 data-id="heading-1">一、svg 实现跳转 github 图标</h2>
<p>在查阅文档时, 经常看到这个分享图标, 鼠标移上去还会动, 以为很是麻烦, 就是一个 <code>svg</code> 图标</p>
<p>搭建个人博客等网站时,也可以把这个按钮添加进来, 有点技术元素了没! 先上效果:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9767f7e621544f68a7d105b32aef6972~tplv-k3u1fbpfcp-zoom-1.image" alt="1" loading="lazy" referrerpolicy="no-referrer"></p>
<p>超简单使用: 代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 右上角 github corner --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"svg-wrap"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://your-url/"</span> <span class="hljs-attr">target</span>=<span class="hljs-string">"_blank"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"github-corner"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"80"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"80"</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 250 250"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"fill:#b45dea; color:#fff; position: absolute; top: 0; border: 0; right: 0;"</span> <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"true"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"</span>></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"currentColor"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"transform-origin: 130px 106px;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"octo-arm"</span>></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"currentColor"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"octo-body"</span> ></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">二、四角边框</h2>
<p>需求: 是不是似曾相识..</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cc0c98aed3145e49aea769a485725a5~tplv-k3u1fbpfcp-zoom-1.image" alt="qr-card" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现效果如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc8e2d044add49b4a57176b7298f7c9a~tplv-k3u1fbpfcp-zoom-1.image" alt="qr-card-example" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Talk is cheap, show the codes</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card-wrapper"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content-box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.card-wrapper</span> &#123;
  <span class="hljs-attribute">display</span>: inline-block;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">13px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#00ffd4</span>, <span class="hljs-number">#00ffd4</span>) left top, <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#00ffd4</span>, <span class="hljs-number">#00ffd4</span>) left top,
    <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#00ffd4</span>, <span class="hljs-number">#00ffd4</span>) right top, <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#00ffd4</span>, <span class="hljs-number">#00ffd4</span>) right top,
    <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#00ffd4</span>, <span class="hljs-number">#00ffd4</span>) left bottom, <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#00ffd4</span>, <span class="hljs-number">#00ffd4</span>) left bottom,
    <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#00ffd4</span>, <span class="hljs-number">#00ffd4</span>) right bottom, <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#00ffd4</span>, <span class="hljs-number">#00ffd4</span>) right bottom;
  <span class="hljs-attribute">background-repeat</span>: no-repeat;
  <span class="hljs-attribute">background-size</span>: <span class="hljs-number">2px</span> <span class="hljs-number">20px</span>, <span class="hljs-number">20px</span> <span class="hljs-number">2px</span>;
&#125;
<span class="hljs-selector-class">.content-box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">213px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">132px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">#b45dea</span> <span class="hljs-number">1px</span> solid;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">213</span>, <span class="hljs-number">213</span>, <span class="hljs-number">213</span>, <span class="hljs-number">0.3</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">三、渐变边框的探索</h2>
<h3 data-id="heading-4">1. 最原始方案: 背景组合 叠加产生渐变边框</h3>
<p>父元素使用背景渐变 <code>linear-gradient</code>, 再通过叠加一个其他颜色的背景盖在上面, 即子(伪)元素使用背景 <code>background</code> 盖住, 从而达到渐变边框的需求. 效果如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a8f4fc1b54547c7961b64b477d08e4a~tplv-k3u1fbpfcp-zoom-1.image" alt="1.背景组合产生渐变边框" loading="lazy" referrerpolicy="no-referrer"></p>
<p>非常简单，简单的示意图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87186e973133492abc88f085f6a17222~tplv-k3u1fbpfcp-zoom-1.image" alt="1.背景组合产生渐变边框" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现代码如下:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box bd-6"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content bd-6"</span>></span>1. 背景组合产生渐变边框<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span>1. 背景组合产生渐变边框<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.bd-6</span> &#123;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">6px</span>;
&#125;
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">270px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">66px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">145deg</span>, <span class="hljs-number">#0061fe</span>, <span class="hljs-number">#ff00f0</span>);
&#125;
<span class="hljs-selector-class">.content</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">265px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">60px</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">18px</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">3px</span>;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">24</span>, <span class="hljs-number">24</span>, <span class="hljs-number">24</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同理也可以使用 伪元素 <code>::before</code> 和 <code>::after</code>, 这样一个标签就可实现了,</p>
<blockquote>
<p>但是如果需求背景是透明的就不行了</p>
</blockquote>
<h3 data-id="heading-5">2. CSS3 border 属性 border-image</h3>
<p>前面的实现方法都是使用了多个标签, 不雅也不推荐,</p>
<p>根据 <code>CSS3</code> 找到最新实现方案: <code>border-image</code> 我们可以给 <code>border</code> 元素添加 <code>image</code>， 类似于 <code>background-image</code>，可以是渐变也可以是图片, 也可背景透明, 但设置圆角会失效。</p>
<blockquote>
<p>具体语法可以参考: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fborder-image" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-image" ref="nofollow noopener noreferrer">border-image</a></p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"border-image"</span>></span>border-image<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.border-image</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-comment">/* 这里边框类型没有效果 但仍需设置 */</span>
  <span class="hljs-attribute">border</span>: <span class="hljs-number">10px</span> solid;
  <span class="hljs-comment">/* 圆角失效 */</span>
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">border-image-source</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">145deg</span>, <span class="hljs-number">#0061fe</span>, <span class="hljs-number">#ff00f0</span>);
  <span class="hljs-attribute">border-image-slice</span>: <span class="hljs-number">1</span>;
  <span class="hljs-attribute">border-image-repeat</span>: stretch;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>border-radius 失效</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f27090b95ea24244a8f513528f8351e8~tplv-k3u1fbpfcp-zoom-1.image" alt="border-image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">3. 使用 background-clip</h3>
<p>只需一个单独的标签即可,</p>
<blockquote>
<p>同样: 如果需求背景是透明的就不行了</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2a85839b1004294a24e8b31a281fb20~tplv-k3u1fbpfcp-zoom-1.image" alt="bg-clip" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.bg-clip</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">border</span>: solid <span class="hljs-number">10px</span> transparent;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#fee</span>, <span class="hljs-number">#fee</span>), <span class="hljs-built_in">linear-gradient</span>(to right, green, gold);
  <span class="hljs-attribute">background-origin</span>: border-box;
  <span class="hljs-attribute">background-clip</span>: content-box, border-box;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4. clip-path</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"border-image-clip-path"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.border-image-clip-path</span> &#123;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">80px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">10px</span> solid;
  <span class="hljs-attribute">border-image</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">45deg</span>, <span class="hljs-number">#0061fe</span>, <span class="hljs-number">#ff00f0</span>) <span class="hljs-number">1</span>;
  <span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">inset</span>(<span class="hljs-number">0</span> round <span class="hljs-number">10px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，还可以用 <code>filter: hue-rotate()</code> 再加个渐变动画：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.border-image-clip-path</span> &#123;
  <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">hue-rotate</span>(<span class="hljs-number">360deg</span>);
&#125;

<span class="hljs-keyword">@keyframes</span> huerotate &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">hue-rotate</span>(<span class="hljs-number">0deg</span>);
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">hue-rorate</span>(<span class="hljs-number">360deg</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>边框背景渐变动画:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb7271e837ce4458a72180744b4627d6~tplv-k3u1fbpfcp-zoom-1.image" alt="1" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">四、渐变字体</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b38e71c72184160a2a77bf8ccbe7f14~tplv-k3u1fbpfcp-zoom-1.image" alt="grident-text" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"gradient-text"</span>></span>
  gradient Text gradient Text gradient Text gradient Text gradient Text gradient Text
<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.gradient-text</span> &#123;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to right, <span class="hljs-number">#0061fe</span>, <span class="hljs-number">#ff00f0</span>);
  -webkit-<span class="hljs-attribute">background-clip</span>: text;
  <span class="hljs-attribute">background-clip</span>: text;
  <span class="hljs-attribute">color</span>: transparent;
  <span class="hljs-attribute">text-transform</span>: uppercase;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">五、在售状态标志</h2>
<p>比较原始的方案: 采用定位方法...后续更新...</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddd95e48b4ba4c9c8dfc710b91e37714~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"badge"</span>></span>ON SALE<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">img</span>
    <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/gh/xn213/img-hosting@master/juejin-posts-imgs/compare_mbp16__fykfvftfaeuu_large.6fi0c3rwsq00.png"</span>
    <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">overflow</span>: hidden;
&#125;
<span class="hljs-selector-class">.badge</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">left</span>: -<span class="hljs-number">30px</span>;
  <span class="hljs-attribute">background</span>: red;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">120px</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">45deg</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/169dcd48057945f390953fe79c100c1a~tplv-k3u1fbpfcp-zoom-1.image" alt="compare_mbp16__fykfvftfaeuu_large_onsale" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">其他</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5cebf71fb1a448b9d74d0a50a356a26~tplv-k3u1fbpfcp-zoom-1.image" alt="color-copy-share" loading="lazy" referrerpolicy="no-referrer"></p>
<p>🎉</p>
<p>🎉</p>
<p>🎉</p></div>  
</div>
            