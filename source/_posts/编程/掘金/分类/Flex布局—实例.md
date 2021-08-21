
---
title: 'Flex布局—实例'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996fe53c389f4e32846cb25542199c28~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 04:07:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996fe53c389f4e32846cb25542199c28~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2015%2F07%2Fflex-examples.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2015/07/flex-examples.html" ref="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2015/0…</a></p>
</blockquote>
<h2 data-id="heading-0">一、骰子的布局</h2>
<p>骰子的一面，最多可以放置9个点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996fe53c389f4e32846cb25542199c28~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面，就来看看Flex如何实现，从1个点到9个点的布局。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6703f50303d140bbaf86d96f48d6a57c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果不加说明，本节的HTML模板一律如下。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，div元素（代表骰子的一个面）是Flex容器，span元素（代表一个点）是Flex项目。如果有多个项目，就要添加多个span元素，以此类推。</p>
<h3 data-id="heading-1">1.1 单项目</h3>
<hr>
<p>首先，只有左上角1个点的情况。Flex布局默认就是首行左对齐，所以一行代码就够了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c363453bf3b740fea37d8c02355c4e27~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>:flex
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置项目的对齐方式，就能实现居中对齐和右对齐。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa94aeb2dce74b9c9ffea19238b99a18~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
justify-content: center
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15bc665cf3544e8fa6d7a410b31483be~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
justify-content: flex-end
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置交叉轴对齐方式，可以垂直移动主轴。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2aa6e1e752f4eacba1cde57c6acd688~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">.box &#123;
display: flex
align-items:center /* 定义项目交叉轴上怎么对齐 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e95cf6980d84217836f2bc85ea6bc61~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
justify-content:center
align-items:center /* 定义项目交叉轴上怎么对齐 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e6388df742245a88de79d99dd8f17ab~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
justify-content:center
align-items: flex-end /* 定义项目交叉轴上怎么对齐 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd93fa4114884a2ead57f86e12182e64~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
justify-content:flex-end
align-items: flex-end /* 定义项目交叉轴上怎么对齐 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2 双项目</h3>
<hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c55568b69ec743f8b9e07672746b7123~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
justify-content: space-between
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb731acdb7c44f4c8a68be3f1073656e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
flex-direction: column /* 主轴方向从上向下 */
justify-content: space-between
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e3e8373833849ad8e2642127c986e72~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
flex-direction: column
justify-content: space-between
align-items: center /* 主轴方向从上向下 交叉轴方向从左到右 center居中显示 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/518b844cf8dd4943966df78b98a8b887~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
flex-direction: column
justify-content: space-between
align-items: flex-end /* 主轴方向从上向下 交叉轴方向从左到右 flex-end右侧显示 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53c5fb1fe3fe49c496c52c1c5cddde48~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
<span class="hljs-attribute">align-self</span>: center /* 设置单个项目的对齐方式 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06c4153e76424dfc89ca705c7a29e0ed~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
justify-content:space-between
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
<span class="hljs-attribute">align-self</span>: flex-end /* 设置单个项目的对齐方式 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.3三项目</h3>
<hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d014750303df48d0971e801cc9b27fde~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>)&#123;
<span class="hljs-attribute">align-self</span>: center
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>)&#123;
<span class="hljs-attribute">align-self</span>: flex-end
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.4四项目</h3>
<hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01033f86644c46d8a3862dbc78a60984~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">.box &#123;
display: flex
flex-wrap: wrap
justify-content: flex-end
align-content: space-between
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d11628fbd3694be98c53d1fbe64bea4e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>HTML代码如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">flex-wrap</span>: wrap;
  <span class="hljs-attribute">align-items</span>: space-between;
&#125;
<span class="hljs-selector-class">.column</span> &#123;
  <span class="hljs-attribute">display</span>:flex;
 <span class="hljs-attribute">justify-content</span>: space-between
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.5六项目</h3>
<hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acf1a876b20f4eb8a6b8018dec7ef465~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
flex-wrap: wrap
align-content: space-between
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa666e0ec59741c4babfcc7c0119fb2d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex
flex-direction: column
  flex-wrap: wrap
align-content: space-between
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31eb8991ea844c5782714fe04b9a9f11~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>HTML代码如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>:flex;
  <span class="hljs-attribute">flex-wrap</span>: wrap;
&#125;
<span class="hljs-selector-class">.row</span> &#123;
  <span class="hljs-attribute">flex-basis</span>: <span class="hljs-number">100%</span> /* 每行的宽度都是占整个项目的<span class="hljs-number">100%</span> */ 
  display:flex;
&#125;
<span class="hljs-selector-class">.row</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>)&#123;
  <span class="hljs-attribute">justify-content</span>: center;
&#125;
<span class="hljs-selector-class">.row</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>)&#123;
  <span class="hljs-attribute">justify-content</span>: space-between;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">1.6九项目</h3>
<hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06f14194c6334a66831da5976a3f8cfe~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex;
<span class="hljs-attribute">flex-wrap</span>: wrap;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">二、网格布局</h2>
<h3 data-id="heading-8">2.1基本网格布局</h3>
<hr>
<p>最简单的网格布局，就是平均分布。在容器里面平均分配空间，跟上面的骰子布局很像，但是需要设置项目的自动缩放。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/273008a3e3cd4e1694e1229eb6c751d9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>HTML代码如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: flex;
&#125;
<span class="hljs-selector-class">.item</span> &#123;
<span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span> /* 平均分配 每份占<span class="hljs-number">1</span>/<span class="hljs-number">3</span> */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.2 百分比布局</h3>
<hr>
<p>某个网格的宽度为固定的百分比 其余网格平均分配剩余空间</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55921f824d914ff8a1e620a8505f834c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>1.HTML代码如下</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
    1
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
    2
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
    3
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">1</span>) &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">0</span> <span class="hljs-number">1</span> <span class="hljs-number">50%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.HTML代码如下</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
    1
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
    2
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">0</span> <span class="hljs-number">1</span> <span class="hljs-number">33.33%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.HTML代码如下</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
    1
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
    2
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
    3
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">1</span>) &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">0</span> <span class="hljs-number">1</span> <span class="hljs-number">25%</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">0</span> <span class="hljs-number">1</span> <span class="hljs-number">33.33%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">三、圣杯布局</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHoly_Grail_(web_design)" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Holy_Grail_(web_design)" ref="nofollow noopener noreferrer">圣杯布局</a>（Holy Grail Layout）指的是一种最常见的网站布局。页面从上到下，分成三个部分：头部（header），躯干（body），尾部（footer）。其中躯干又水平分成三栏，从左到右为：导航、主栏、副栏。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/319133a4dcd64775ae8ef1eb91633a33~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>HTML布局如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">header</span>></span>header<span class="hljs-tag"></<span class="hljs-name">header</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"body"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">main</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span>内容<span class="hljs-tag"></<span class="hljs-name">main</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"nav"</span>></span>导航<span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">aside</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"aside"</span>></span>侧边内容<span class="hljs-tag"></<span class="hljs-name">aside</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">footer</span>></span>footer<span class="hljs-tag"></<span class="hljs-name">footer</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">min-height</span>:<span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">flex-direction</span>:column;
&#125;
<span class="hljs-selector-tag">header</span>,
<span class="hljs-selector-tag">footer</span>&#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
&#125;
<span class="hljs-selector-class">.body</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
&#125;
<span class="hljs-selector-class">.content</span> &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>; <span class="hljs-comment">/* 中间内容自适应 */</span>
&#125;
<span class="hljs-selector-class">.nav</span>,
<span class="hljs-selector-class">.aside</span> &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">12em</span>; <span class="hljs-comment">/* 设置左右两端的宽度 */</span>
&#125;
<span class="hljs-selector-class">.nav</span> &#123;
  <span class="hljs-attribute">order</span>: -<span class="hljs-number">1</span>; <span class="hljs-comment">/* 将导航栏放在最左边 */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是小屏幕，躯干的三栏自动变为垂直叠加。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@media</span> (<span class="hljs-attribute">max-width</span>:<span class="hljs-number">768px</span>)&#123;
<span class="hljs-selector-class">.body</span> &#123;
    <span class="hljs-attribute">flex-direction</span>: column;
    <span class="hljs-attribute">flex</span>:<span class="hljs-number">1</span>
&#125;
  <span class="hljs-selector-class">.nav</span>,
  <span class="hljs-selector-class">.content</span>,
  <span class="hljs-selector-class">.aside</span> &#123;
    <span class="hljs-attribute">flex</span>: auto;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">四、输入框的布局</h2>
<p>我们常常需要在输入框的前方添加提示，后方添加按钮。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd3f58e166fd4e188317b59112f5eaf4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>HTML代码如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"InputAddOn"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"InputAddOn-item"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"InputAddOn-field"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"InputAddOn-item"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.InputAddOn</span>&#123;
  <span class="hljs-attribute">display</span>: flex;
&#125;
<span class="hljs-selector-class">.InputAddOn-field</span> &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">五、悬挂式布局</h2>
<p>有时，主栏的左侧或右侧，需要添加一个图片栏。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/377e471d472447dc960b53a695245152~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>HTML代码如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"Media"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">""</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"Media-figure"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"Media-body"</span>></span>123<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.Media</span> &#123;
<span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">align-items</span>: flex-start;
&#125;
<span class="hljs-selector-class">.Media-figure</span> &#123;
  <span class="hljs-attribute">margin-right</span>:<span class="hljs-number">1em</span>;
&#125;
<span class="hljs-selector-class">.Media-body</span> &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">六、固定的底栏</h2>
<p>有时，页面内容太少，无法占满一屏的高度，底栏就会抬高到页面的中间。这时可以采用Flex布局，让底栏总是出现在页面的底部。</p>
<p>HTML代码如下</p>
<blockquote>
<pre><code class="hljs language-markup copyable" lang="markup"><body class="Site">
  <header>...</header>
  <main class="Site-content">...</main>
  <footer>...</footer>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>CSS代码如下</p>
<blockquote>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.Site</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">flex-direction</span>: column;
&#125;

<span class="hljs-selector-class">.Site-content</span> &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h2 data-id="heading-14">七、流式布局</h2>
<p>每行的项目数固定，会自动分行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd0443f73b2642b799293d508983e809~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>CSS代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
  <span class="hljs-attribute">background-color</span>: black;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">flex-flow</span>: row wrap;
  <span class="hljs-attribute">align-content</span>: flex-start;
&#125;

<span class="hljs-selector-class">.child</span> &#123;
  <span class="hljs-attribute">box-sizing</span>: border-box;
  <span class="hljs-attribute">background-color</span>: white;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">25%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            