
---
title: '【学习笔记】常见 CSS 布局'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b02301fdf604356b878087ab98e9830~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 14 May 2021 22:12:15 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b02301fdf604356b878087ab98e9830~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">水平垂直居中</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b02301fdf604356b878087ab98e9830~tplv-k3u1fbpfcp-watermark.image" alt="垂直水平居中.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 公共代码 */</span>
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"wp"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box size"</span>></span>123123<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">居中元素定宽高</h2>
<p><code>absolute + 负 margin</code></p>
<pre><code class="hljs language-js copyable" lang="js">.wp &#123;
  <span class="hljs-attr">border</span>: 1px solid red;
  width: 300px;
  height: 300px;
  position: relative;
&#125;
.box &#123;
  <span class="hljs-attr">background</span>: green;    
  width: 100px;
  height: 100px;
  position: absolute;
  top: <span class="hljs-number">50</span>%;
  left: <span class="hljs-number">50</span>%;
  margin-left: -50px;
  margin-top: -50px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>absolute + margin auto</code></p>
<pre><code class="hljs language-js copyable" lang="js">.wp &#123;
  <span class="hljs-attr">border</span>: 1px solid red;
  width: 300px;
  height: 300px;
  position: relative;
&#125;
.box &#123;
  <span class="hljs-attr">background</span>: green;    
  width: 100px;
  height: 100px;
  position: absolute;
  top: <span class="hljs-number">0</span>;
  left: <span class="hljs-number">0</span>;
  bottom: <span class="hljs-number">0</span>;
  right: <span class="hljs-number">0</span>;
  margin: auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>absolute + calc</code></p>
<pre><code class="hljs language-js copyable" lang="js">.wp &#123;
  <span class="hljs-attr">border</span>: 1px solid red;
  width: 300px;
  height: 300px;
  position: relative;
&#125;
.box &#123;
  <span class="hljs-attr">background</span>: green;    
  width: 100px;
  height: 100px;
  position: absolute;
  top: calc(<span class="hljs-number">50</span>% - 50px);
  left: calc(<span class="hljs-number">50</span>% - 50px);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">居中元素不定宽高</h2>
<p><code>absolute + transform</code></p>
<pre><code class="hljs language-js copyable" lang="js">.wp &#123;
  <span class="hljs-attr">border</span>: 1px solid red;
  width: 300px;
  height: 300px;
  position: relative;
&#125;
.box &#123;
  <span class="hljs-attr">background</span>: green; 
  position: absolute;
  top: <span class="hljs-number">50</span>%;
  left: <span class="hljs-number">50</span>%;
  transform: translate(-<span class="hljs-number">50</span>%, -<span class="hljs-number">50</span>%);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>line-height + height</code></p>
<pre><code class="hljs language-js copyable" lang="js">.wp &#123;
  <span class="hljs-attr">border</span>: 1px solid red;
  width: 300px;
  height: 300px;
  line-height: 300px;  <span class="hljs-comment">/*行高的值与height相等*/</span>
  text-align: center;
  font-size: <span class="hljs-number">0</span>;   <span class="hljs-comment">/*消除幽灵空白节点、近似居中的bug*/</span>
&#125;
.box &#123;
  <span class="hljs-attr">background</span>: green; 
  display: inline-block;  <span class="hljs-comment">/*如果是块级元素需改为行内或行内块级才生效*/</span>
  vertical-align: middle;
  font-size: 16px;
  line-height: initial; <span class="hljs-comment">/*默认值*/</span>
  text-align: left; <span class="hljs-comment">/*修正文字*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>inline-block</code></p>
<pre><code class="hljs language-js copyable" lang="js">.wp &#123;
  <span class="hljs-attr">border</span>: 1px solid red;
  width: 300px;
  height: 300px;
  position: relative;
  display: inline-block;
  white-space: nowrap;
  text-align: center;
&#125;
.wp::after &#123;
<span class="hljs-attr">content</span>:<span class="hljs-string">''</span>;
display: inline-block;
vertical-align: middle;
height: <span class="hljs-number">100</span>%;
&#125;
.box &#123;
  <span class="hljs-attr">background</span>: green; 
  display: inline-block;  <span class="hljs-comment">/*如果是块级元素需改为行内或行内块级才生效*/</span>
  vertical-align: middle;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>table</code><br>
tabel 单元格中的内容天然就是垂直居中的，需添加一个水平居中属性即可，该方法代码太冗余</p>
<pre><code class="hljs language-js copyable" lang="js"><table>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">tbody</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wp"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>123123<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">td</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">tbody</span>></span></span>
</table>
<span class="hljs-comment">// css</span>
.wp &#123;
    text-align: center;
&#125;
.box &#123;
    <span class="hljs-attr">display</span>: inline-block;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>table-cell</code>：CSS 新增的 table 属性，可把普通元素变为 table 元素的现实效果，该方法和table一样原理，但没有那么多冗余代码，兼容性也还不错</p>
<pre><code class="hljs language-js copyable" lang="js">.wp &#123;
    <span class="hljs-attr">display</span>: table-cell;
    vertical-align: middle;
    text-align: center;
    border: 1px solid red;
    width: 300px;
    height: 300px;
&#125;
.box &#123;
    <span class="hljs-attr">background</span>: green; 
    display: inline-block;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex</code>：注意兼容性</p>
<pre><code class="hljs language-js copyable" lang="js">.wp &#123;
    <span class="hljs-attr">display</span>: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid red;
    width: 300px;
    height: 300px;
&#125;
.box &#123;
    <span class="hljs-attr">background</span>: green; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>grid</code>：网格布局，代码量也很少，但兼容性不如 flex</p>
<pre><code class="hljs language-js copyable" lang="js">.wp &#123;
    <span class="hljs-attr">display</span>: grid;
    border: 1px solid red;
    width: 300px;
    height: 300px;
&#125;
.box &#123;
    <span class="hljs-attr">background</span>: green; 
    align-self: center;
    justify-self: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>writing-mode</code>：可以改变文字的显示方向，如可通过 writing-mode 让文字的显示变为垂直方向，结合 text-align 可实现</p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"wp"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wp-inner"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>123123<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

wp &#123;
    writing-mode: vertical-lr;
    text-align: center;
    border: 1px solid red;
    width: 300px;
    height: 300px;
&#125;
.wp-inner &#123;
    writing-mode: horizontal-tb;
    display: inline-block;
    width: <span class="hljs-number">100</span>%;
&#125;
.box &#123;
    <span class="hljs-attr">background</span>: green; 
    display: inline-block;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>PC端无兼容性要求，推荐 flex；移动端推荐使用 flex；关于 flex 的兼容性决方案，请看这里《<a href="https://yanhaijing.com/css/2016/08/21/flex-practice-on-mobile/" target="_blank" rel="nofollow noopener noreferrer">移动端flex布局实战</a>》</p>
</blockquote>
<h1 data-id="heading-3">两列布局</h1>
<h2 data-id="heading-4">左列定宽，右列自适应</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f56270e06e3436189b5ceb90ab5a486~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>float + margin</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"left"</span>>左列定宽</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

.left &#123;
    background-color: red;
    float: left;
    width: 100px;
    height: 500px;
&#125;
.right &#123;
    background-color: yellow;
    height: 500px;
    margin-left: 100px; <span class="hljs-comment">/*大于等于 left 的宽度*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>float + margin(fix)</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"left"</span>>左列定宽</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right-fix"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

.left &#123;
    background-color: red;
    float: left;
    width: 100px;
    height: 500px;
&#125;
.right-fix &#123;
    <span class="hljs-attr">float</span>: right;
    width: <span class="hljs-number">100</span>%;
    margin-left: -100px; <span class="hljs-comment">/*正值大于或等于 left 的宽度，才能显示在同一行*/</span>
&#125;
.right &#123;
    background-color: yellow;
    height: 500px;
    margin-left: 100px; <span class="hljs-comment">/*大于等于 left 的宽度*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>float + overflow</code></p>
<ul>
<li>优点：代码简单，容易理解，无需关注定宽的宽度，利用 bfc 达到自适应效果</li>
<li>缺点：浮动脱离文档流，需要手动清除浮动，否则容易产生高度塌陷；不支持ie6</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"left"</span>>左列定宽</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

.left &#123;
    background-color: red;
    float: left;
    width: 100px;
    height: 500px;
&#125;
.right &#123;
    background-color: yellow;
    height: 500px;
    overflow: hidden; <span class="hljs-comment">/*触发 BFC 达到自适应*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>绝对定位</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">position</span>: relative;  <span class="hljs-comment">/*子绝父相*/</span>
&#125;
.left &#123;
    background-color: red;
    position: absolute;
    top: <span class="hljs-number">0</span>;
    left: <span class="hljs-number">0</span>;
    width: 100px;
    height: 500px;
&#125;
.right &#123;
    background-color: yellow;
    height: 500px;
    position: absolute;
    top: <span class="hljs-number">0</span>;
    left: 100px;  <span class="hljs-comment">/*值大于等于 left 的宽度*/</span>
    right: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;
    height: 500px;
    display: flex;
&#125;
.left &#123;
    <span class="hljs-attr">width</span>: 100px;
    background-color: red;
&#125;
.right &#123;
    background-color: yellow;
    flex: <span class="hljs-number">1</span>; <span class="hljs-comment">/*均分了父元素剩余空间*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>table</code></p>
<ul>
<li>优点：代码简单，容易理解，无需关注定宽的宽度，利用单元格自动分配达到自适应效果</li>
<li>缺点：margin失效；设置间隔比较麻烦；不支持ie8-</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;
    height: 500px;
    display: table;
&#125;
.left, .right &#123;
    <span class="hljs-attr">display</span>: table-cell;  <span class="hljs-comment">/*利用单元格自动分配宽度*/</span>
&#125;
.left &#123;
    <span class="hljs-attr">width</span>: 100px;
    background-color: red;
&#125;
.right &#123;
    background-color: yellow;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Grid</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;
    height: 500px;
    display: grid;
    grid-template-columns: 100px auto;  <span class="hljs-comment">/*设定 2 列就 ok 了，auto 换成 1fr 也行*/</span>
&#125;
.left &#123;
    background-color: red;
&#125;
.right &#123;
    background-color: yellow;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">左列自适应，右列定宽</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b2ed8d28e54346abcccdc2a3835031~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>float + margin</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    padding-left: 100px;  <span class="hljs-comment">/*抵消 left 的 margin-left 以达到 parent 水平居中*/</span>
&#125;
.left &#123;
      <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;
      height: 500px;
      float: left;
      margin-left: -100px; <span class="hljs-comment">/*正值等于 right 的宽度*/</span>
      background-color: #f00;
&#125;
.right &#123;
      <span class="hljs-attr">height</span>: 500px;
      width: 100px;
      float: right;
      background-color: #0f0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>float + overflow</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>  <!--顺序要换一下-->
</div>

.left &#123;
    background-color: #f00;
    overflow: hidden;  <span class="hljs-comment">/*触发bfc*/</span>
    height: 500px;
&#125;
.right &#123;
    <span class="hljs-attr">height</span>: 500px;
    width: 100px;
    float: right;
    background-color: #0f0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其他的方法如绝对定位、flex、table、grid 与【左列定宽右列自适应】相反</p>
</blockquote>
<h2 data-id="heading-6">一列不定宽，一列自适应（盒子宽度随着内容增加或减少发生变化,另一个盒子自适应）</h2>
<p>改变前
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d543e26aae3741b1acf836bb5a87a30f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>改变后
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28dcaf54c6064d08b989bf42ab64349e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>float + overflow</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列不定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.left &#123;
    margin-right: 10px;
    float: left;  <span class="hljs-comment">/*只设置浮动,不设宽度*/</span>
    height: 500px;
    background-color: #f00;
&#125;
.right &#123;
    <span class="hljs-attr">overflow</span>: hidden;  <span class="hljs-comment">/*触发 bfc */</span>
    height: 500px;
    background-color: #0f0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列不定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent&#123;
      <span class="hljs-attr">display</span>: flex;
&#125;
.left &#123; <span class="hljs-comment">/*不设宽度*/</span>
      margin-right: 10px;
      height: 500px;
      background-color: #f00;
&#125;
.right &#123;
      <span class="hljs-attr">height</span>: 500px;
      background-color: #0f0;
      flex: <span class="hljs-number">1</span>;  <span class="hljs-comment">/*均分 parent 剩余的部分*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Grid</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列不定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent&#123;
      <span class="hljs-attr">display</span>: grid;
      grid-template-columns: auto 1fr;  <span class="hljs-comment">/* auto 和 1fr 换一下顺序就是左列自适应，右列不定宽了*/</span>
&#125;
.left &#123;
      margin-right: 10px;
      height: 500px;
      background-color: red;
&#125;
.right &#123;
      <span class="hljs-attr">height</span>: 500px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">三列布局</h1>
<h2 data-id="heading-8">两列定宽，一列自适应</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbd4aa91a72943db9fee9a5f5edb49d9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>float + margin</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
      min-width: 310px; <span class="hljs-comment">/* 100+10+200，防止宽度不够，子元素换行*/</span>
&#125;
.left &#123;
      margin-right: 10px;  <span class="hljs-comment">/* left 和 center 间隔*/</span>
      float: left;
      width: 100px;
      height: 500px;
      background-color: red;
&#125;
.center &#123;
      <span class="hljs-attr">float</span>: left;
      width: 200px;
      height: 500px;
      background-color: green;
&#125;
.right &#123;
    margin-left: 320px;  <span class="hljs-comment">/*等于 left 和 center 的宽度之和加上间隔，多出来的就是 right 和 center 的间隔*/</span>
    height: 500px;
    background-color: #0f0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>float + overflow</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent&#123;
      min-width: 320px; <span class="hljs-comment">/* 100+10+200+10，防止宽度不够，子元素换行*/</span>
&#125;
.left &#123;
      margin-right: 10px;  <span class="hljs-comment">/* left 和 center 间隔*/</span>
      float: left;
      width: 100px;
      height: 500px;
      background-color: red;
&#125;
.center &#123;
      <span class="hljs-attr">float</span>: left;
      width: 200px;
      height: 500px;
      background-color: green;
      margin-right: 10px; <span class="hljs-comment">/*在此定义和 right 的间隔*/</span>
&#125;
.right &#123;
    <span class="hljs-attr">overflow</span>: hidden;  <span class="hljs-comment">/*触发 bfc*/</span>
    height: 500px;
    background-color: yellow;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent&#123;
    <span class="hljs-attr">height</span>: 500px;
    display: flex;
&#125;
.left &#123;
      margin-right: 10px;  <span class="hljs-comment">/* left 和 center 间隔*/</span>
      width: 100px;
      background-color: red;
&#125;
.center &#123;
      <span class="hljs-attr">width</span>: 200px;
      background-color: green;
      margin-right: 10px; <span class="hljs-comment">/*在此定义和 right 的间隔*/</span>
&#125;
.right &#123; 
    <span class="hljs-attr">flex</span>: <span class="hljs-number">1</span>;  <span class="hljs-comment">/*均分 parent 剩余的部分达到自适应*/</span>
    background-color: yellow;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>table</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent&#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%; 
    display: table;
    height: 520px; <span class="hljs-comment">/*抵消上下间距 10*2 的高度影响*/</span>
    margin: -10px <span class="hljs-number">0</span>;  <span class="hljs-comment">/*抵消上下间距 10 的位置影响*/</span>
    <span class="hljs-comment">/*左右两边间距大了一点，子元素改用 padding 设置盒子间距就没有这个问题*/</span>
    border-spacing: 10px;  <span class="hljs-comment">/*以下子元素 margin 设置间距失效，关键!!!设置间距*/</span>
&#125;
.left &#123;
      <span class="hljs-attr">display</span>: table-cell;
      width: 100px;
      background-color: red;
&#125;
.center &#123;
      <span class="hljs-attr">width</span>: 200px;
      background-color: green;
      display: table-cell;
&#125;
.right &#123; 
    <span class="hljs-attr">display</span>: table-cell;
    background-color: yellow;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Grid</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent&#123;
    <span class="hljs-attr">height</span>: 500px;
    display: grid;
    grid-template-columns: 100px 200px auto; <span class="hljs-comment">/*设置 3 列，固定第一第二列的宽度，第三列 auto 或者 1fr*/</span>
&#125;
.left &#123;
    margin-right: 10px;  <span class="hljs-comment">/*间距*/</span>
    background-color: red;
&#125;
.center &#123;
    margin-right: 10px;  <span class="hljs-comment">/*间距*/</span>
    background-color: green;
&#125;
.right &#123; 
    background-color: yellow;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">两侧定宽，中间自适应</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6150312a7b84055b6023a1eac2061fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>圣杯布局</code></p>
<ul>
<li>利用浮动和相对定位实现</li>
<li>缺点：圣杯布局会有个问题，当将浏览器宽度缩短到一定程度时会使得中间子元素的宽度比左右子元素宽度小，这时布局就会出现问题，所以在使用圣杯布局时一定要设置整个容器的最小宽度</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17d3485401534e7a90a29c2999d5b67e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"header"</span>>header</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent"</span>></span>
  <span class="hljs-comment"><!--#center需要放在前面--></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间自适应
    <span class="hljs-tag"><<span class="hljs-name">hr</span>></span>  <span class="hljs-comment"><!--方便观察原理--></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span>></span>footer<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

.header, .footer &#123;
    height: 60px;
    background-color: #ccc;
&#125;

.parent &#123;
    height: 300px;
    padding: 0 215px 0 115px; /*为了使 center 摆正，左右 padding 分别等于左右盒子的宽，可以结合左右盒子相对定位的 left 调整间距*/
&#125;

.parent div &#123;
    height: 300px
&#125;

.left, .center, .right &#123;
    position: relative;
    float: left;
&#125;

.left &#123;
    margin-left: -100%;  /*使 left 上去一行*/
    left: -115px;  /*相对定位调整 left 的位置，正值大于或等于自身宽度*/
    background-color: red;
    width: 100px;
&#125;

.center &#123;
    width: 100%;  /*由于 parent 的 padding，达到自适应的目的*/
    box-sizing: border-box;
    border: 1px solid #000;
    background-color: yellow;
&#125;

.right &#123;
    left: 215px; /*相对定位调整 right 的位置，大于或等于自身宽度*/
    width: 200px;
    margin-left: -200px;  /*使 right 上去一行*/
    background-color: green;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><code>双飞翼布局</code></p>
<ul>
<li>为了解决圣杯布局的弊端，实现中间部分自适应时多嵌套了一个 div 且不再使用相对定位</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"header"</span>>header</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent"</span>></span>
  <span class="hljs-comment"><!--#center需要放在前面--></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center_inner"</span>></span>中间自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">hr</span>></span>  <span class="hljs-comment"><!--方便观察原理--></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span>></span>footer<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

.header, .footer &#123;
    height: 60px;
    background-color: #ccc;
&#125;

.parent, .parent div &#123;
    height: 300px
&#125;

.left, .center, .right &#123;
    float: left;
&#125;

.left &#123;
    margin-left: -100%;  /*使 left 上去一行*/
    background-color: red;
    width: 100px;
&#125;

.center &#123;
    width: 100%;
    border: 1px solid #000;
    background-color: yellow;
&#125;

.center_inner &#123;
    height: 280px;
    border: 1px solid #000;
    margin: 0 220px 0 120px;  /*关键!!!左右边界等于左右盒子的宽度，多出来的为盒子间隔*/
&#125;

.right &#123;
    width: 200px;
    margin-left: -200px;  /*使 right 上去一行*/
    background-color: green;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex</code></p>
<ul>
<li><strong>flex: flex-grow | flex-shrink | flex-basis;</strong> 分别为：空间充足放大比,空间不足缩小比以及计算剩余空间之前的宽度值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">display</span>: flex;
&#125;

.parent div &#123;
    <span class="hljs-attr">height</span>: 300px;
&#125;

.left, .right &#123;
    <span class="hljs-attr">width</span>: 200px;  <span class="hljs-comment">/* flex: 0 0 200px; */</span>
&#125;

.left &#123;
    background-color: red;
&#125;

.center &#123;
    <span class="hljs-attr">flex</span>: <span class="hljs-number">1</span>;
    background-color: yellow;
&#125;

.right &#123;
    background-color: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>position</code></p>
<ul>
<li>优点：容易理解，兼容性比较好</li>
<li>缺点：需手动计算宽度确定边距；脱离文档流；代码繁多</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">position</span>: relative; <span class="hljs-comment">/*子绝父相*/</span>
&#125;

.parent div &#123;
    <span class="hljs-attr">height</span>: 300px;
&#125;

.left, .right &#123;
    <span class="hljs-attr">width</span>: 200px;  <span class="hljs-comment">/* flex: 0 0 200px; */</span>
&#125;

.left &#123;
    <span class="hljs-attr">position</span>: absolute;
    top: <span class="hljs-number">0</span>;
    left: <span class="hljs-number">0</span>;
    background-color: red;
&#125;

.center &#123;
    margin-left: 200px; <span class="hljs-comment">/*大于等于 left 的宽度或者给 parent 添加同样大小的 padding-left*/</span>
    margin-right: 200px;  <span class="hljs-comment">/*大于等于 right 的宽度或者给 parent 添加同样大小的 padding-right*/</span>
    background-color: yellow;
&#125;

.right &#123;
    <span class="hljs-attr">position</span>: absolute;
    top: <span class="hljs-number">0</span>;
    right: <span class="hljs-number">0</span>;
    background-color: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>table</code></p>
<ul>
<li>优点：代码简洁，容易理解；</li>
<li>缺点：margin失效，采用border-spacing表格两边的间隔无法消除；不支持ie8-</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;
    height: 500px;
    display: table;
&#125;

.left, .right &#123;
    <span class="hljs-attr">width</span>: 200px;  <span class="hljs-comment">/* flex: 0 0 200px; */</span>
&#125;

.left &#123;
    <span class="hljs-attr">display</span>: table-cell;
    background-color: red;
&#125;

.center &#123;
    <span class="hljs-attr">display</span>: table-cell;
    background-color: yellow;
&#125;

.right &#123;
    <span class="hljs-attr">display</span>: table-cell;
    background-color: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Grid</code></p>
<ul>
<li>Grid 是微软提出的网页布局解决方案，最新的 Safari、Chrome、Firefox 都已经进行了支持。个人感觉 Grid 布局比 flex 布局更强大一些，宽高两个方向上都可以得到控制且 Grid 也更容易理解（但 Grid 在移动端的支持应该没有 flex 强）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">display</span>: grid;
    grid-template-columns: 200px auto 200px;
    grid-template-rows: 100px
&#125;

.left &#123;
    background-color: red;
&#125;

.center &#123;
    background-color: yellow;
&#125;

.right &#123;
    background-color: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>
      中间自适应
      <span class="hljs-tag"><<span class="hljs-name">hr</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">height</span>: 500px;
    display: grid;
    grid-template-columns: 100px auto 200px; <span class="hljs-comment">/*设定3列*/</span>
    grid-template-rows: 60px auto 60px; <span class="hljs-comment">/*设定3行*/</span>
    <span class="hljs-comment">/*设置网格区域分布*/</span>
    grid-template-areas:
      <span class="hljs-string">"header header header"</span>
      <span class="hljs-string">"leftside main rightside"</span>
      <span class="hljs-string">"footer footer footer"</span>;
&#125;

.header,.footer &#123;
    background-color: #ccc;
&#125;

.header &#123;
    grid-area: header; <span class="hljs-comment">/*指定在哪个网格区域*/</span>
&#125;

.left &#123;
    grid-area: leftside;
    background-color: red;
&#125;

.center &#123;
    grid-area: main; <span class="hljs-comment">/*指定在哪个网格区域*/</span>
    margin: <span class="hljs-number">0</span> 15px; <span class="hljs-comment">/*设置间隔*/</span>
    border: 1px solid #<span class="hljs-number">000</span>;
    background-color: yellow;
&#125;

.right &#123;
    grid-area: rightside; <span class="hljs-comment">/*指定在哪个网格区域*/</span>
    background-color: green;
&#125;

.footer &#123;
    grid-area: footer; <span class="hljs-comment">/*指定在哪个网格区域*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>CSS3 的 calc </code></p>
<ul>
<li>CSS3 提供的 calc 功能能够实现给宽高等设置动态的值，支持 + - * / 四则运算，注意运算符两边要个留一个空格否则设置无效</li>
<li>同样需要设置浮动将三个元素并排显示</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>左列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>中间自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>右列定宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent div &#123;
    <span class="hljs-attr">float</span>: left;
    height: 300px;
&#125;

.left, .right &#123;
    <span class="hljs-attr">width</span>: 200px;
    background-color: red;
&#125;

.center &#123;
    <span class="hljs-attr">width</span>: calc(<span class="hljs-number">100</span>% - 400px);
    background-color: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">多列布局</h1>
<h2 data-id="heading-11">多列等宽布局</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4551403606e4cb9aeccda28e2778251~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>float</code></p>
<ul>
<li>优点：代码简单，容易理解；兼容性较好</li>
<li>缺点：需要手动清除浮动，否则会容易产生高度塌陷</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.column &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">25</span>%;
    float: left;
    box-sizing: border-box;
    border: 1px solid #<span class="hljs-number">000</span>;
    background-clip: content-box; <span class="hljs-comment">/*背景色从内容开始绘制，方便观察*/</span>
    height: 500px;
&#125;

.column:nth-<span class="hljs-function"><span class="hljs-title">child</span>(<span class="hljs-params">odd</span>)</span> &#123;
      background-color: red;
&#125;

.column:nth-<span class="hljs-function"><span class="hljs-title">child</span>(<span class="hljs-params">even</span>)</span> &#123;
      background-color: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    margin-left: -15px;  <span class="hljs-comment">/*使内容看起来居中*/</span>
    height: 500px;
    display: flex;
&#125;

.column &#123;
    <span class="hljs-attr">flex</span>: <span class="hljs-number">1</span>; <span class="hljs-comment">/*一起平分 parent*/</span>
    margin-left: 15px; <span class="hljs-comment">/*设置间距*/</span>
&#125;

.column:nth-<span class="hljs-function"><span class="hljs-title">child</span>(<span class="hljs-params">odd</span>)</span> &#123;
      background-color: red;
&#125; 

.column:nth-<span class="hljs-function"><span class="hljs-title">child</span>(<span class="hljs-params">even</span>)</span> &#123;
      background-color: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>table</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">height</span>: 500px; 
    display: table; 
    margin: -20px <span class="hljs-number">0</span>;  <span class="hljs-comment">/*抵消上下边 20*2 间距的位置影响*/</span>
    <span class="hljs-comment">/*两边离页面间距较大，改用子元素设置 padding 来当成间隔就不会有这样的问题*/</span>
    border-spacing: 20px;  <span class="hljs-comment">/*设置间距*/</span>
&#125;

.column &#123;
    <span class="hljs-attr">display</span>: table-cell;
&#125;

.column:nth-<span class="hljs-function"><span class="hljs-title">child</span>(<span class="hljs-params">odd</span>)</span> &#123;
      background-color: red;
&#125;

.column:nth-<span class="hljs-function"><span class="hljs-title">child</span>(<span class="hljs-params">even</span>)</span> &#123;
      background-color: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Grid</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"column"</span>></span>等宽等宽等宽等宽等宽等宽等宽等宽等宽等宽<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">height</span>: 500px;
    display: grid;
    grid-template-columns: repeat(<span class="hljs-number">4</span>, 1fr);  <span class="hljs-comment">/*4 就是列数*/</span>
&#125;

.column:nth-<span class="hljs-function"><span class="hljs-title">child</span>(<span class="hljs-params">odd</span>)</span> &#123;
      background-color: red;
&#125;

.column:nth-<span class="hljs-function"><span class="hljs-title">child</span>(<span class="hljs-params">even</span>)</span> &#123;
      background-color: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">九宫格布局</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb9227a2bfa947a2b0a9c24f7aeecbef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>table</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>5<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>6<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>7<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>8<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>9<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">width</span>: 1200px;
    height: 500px;
    margin: <span class="hljs-number">0</span> auto;
    display: table;
&#125;

.row &#123;
    <span class="hljs-attr">display</span>: table-row;
&#125;

.item &#123;
    <span class="hljs-attr">border</span>: 1px solid #<span class="hljs-number">000</span>;
    display: table-cell;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>5<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>6<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>7<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>8<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>9<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">width</span>: 1200px;
    height: 500px;
    margin: <span class="hljs-number">0</span> auto;
    display: flex;
    flex-direction: column;
&#125;

.row &#123;
    <span class="hljs-attr">display</span>: flex;
    flex: <span class="hljs-number">1</span>;
&#125;

.item &#123;
    <span class="hljs-attr">flex</span>: <span class="hljs-number">1</span>;
    border: 1px solid #<span class="hljs-number">000</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Grid</code></p>
<ul>
<li>CSS Grid 非常强大，可以实现各种各样的三维布局</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>5<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>6<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>7<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>8<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>9<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>

.parent &#123;
    <span class="hljs-attr">width</span>: 1200px;
    height: 500px;
    margin: <span class="hljs-number">0</span> auto;
    display: grid;
    grid-template-columns: repeat(<span class="hljs-number">3</span>, 1fr); <span class="hljs-comment">/*等同于1fr 1fr 1fr，此为重复的合并写法*/</span>
    grid-template-rows: repeat(<span class="hljs-number">3</span>, 1fr);  <span class="hljs-comment">/*等同于1fr 1fr 1fr，此为重复的合并写法*/</span>
&#125;

.item &#123;
    <span class="hljs-attr">border</span>: 1px solid #<span class="hljs-number">000</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">栅格系统</h2>
<ul>
<li>优点：代码简洁，容易理解；提高页面内容的流动性，能适应多种设备</li>
</ul>
<p><code>Less</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*生成栅格系统*/</span>
@media screen and (max-width: 768px)&#123;
  .generate-columns(<span class="hljs-number">12</span>);     <span class="hljs-comment">/*此处设置生成列数*/</span>
  .generate-columns(@n, @i: <span class="hljs-number">1</span>) when (@i <= @n) &#123;
    .column-xs-@&#123;i&#125; &#123;
      <span class="hljs-attr">width</span>: (@i * <span class="hljs-number">100</span>% / @n);
    &#125;
    .generate-columns(@n, (@i+<span class="hljs-number">1</span>));
  &#125;
&#125;
@media screen and (min-width: 768px)&#123;
  .generate-columns(<span class="hljs-number">12</span>);    <span class="hljs-comment">/*此处设置生成列数*/</span>
  .generate-columns(@n, @i: <span class="hljs-number">1</span>) when (@i <= @n) &#123;
    .column-sm-@&#123;i&#125; &#123;
      <span class="hljs-attr">width</span>: (@i * <span class="hljs-number">100</span>% / @n);
    &#125;
    .generate-columns(@n, (@i+<span class="hljs-number">1</span>));
  &#125;
&#125;
div[<span class="hljs-class"><span class="hljs-keyword">class</span>^</span>=<span class="hljs-string">"column-xs-"</span>]&#123;
  <span class="hljs-attr">float</span>: left;
&#125;
div[<span class="hljs-class"><span class="hljs-keyword">class</span>^</span>=<span class="hljs-string">"column-sm-"</span>]&#123;
  <span class="hljs-attr">float</span>: left;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后的 CSS 代码</p>
<pre><code class="hljs language-js copyable" lang="js">@media screen and (max-width: 768px) &#123;
  .column-xs-<span class="hljs-number">1</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">8.33333333</span>%;  &#125;
  .column-xs-<span class="hljs-number">2</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">16.66666667</span>%;  &#125;
  .column-xs-<span class="hljs-number">3</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">25</span>%;  &#125;
  .column-xs-<span class="hljs-number">4</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">33.33333333</span>%;  &#125;
  .column-xs-<span class="hljs-number">5</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">41.66666667</span>%;  &#125;
  .column-xs-<span class="hljs-number">6</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">50</span>%;  &#125;
  .column-xs-<span class="hljs-number">7</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">58.33333333</span>%;  &#125;
  .column-xs-<span class="hljs-number">8</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">66.66666667</span>%;  &#125;
  .column-xs-<span class="hljs-number">9</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">75</span>%;  &#125;
  .column-xs-<span class="hljs-number">10</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">83.33333333</span>%;  &#125;
  .column-xs-<span class="hljs-number">11</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">91.66666667</span>%;  &#125;
  .column-xs-<span class="hljs-number">12</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;  &#125;
&#125;
@media screen and (min-width: 768px) &#123;
  .column-sm-<span class="hljs-number">1</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">8.33333333</span>%;  &#125;
  .column-sm-<span class="hljs-number">2</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">16.66666667</span>%;  &#125;
  .column-sm-<span class="hljs-number">3</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">25</span>%;  &#125;
  .column-sm-<span class="hljs-number">4</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">33.33333333</span>%;  &#125;
  .column-sm-<span class="hljs-number">5</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">41.66666667</span>%;  &#125;
  .column-sm-<span class="hljs-number">6</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">50</span>%;  &#125;
  .column-sm-<span class="hljs-number">7</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">58.33333333</span>%;  &#125;
  .column-sm-<span class="hljs-number">8</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">66.66666667</span>%;  &#125;
  .column-sm-<span class="hljs-number">9</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">75</span>%;  &#125;
  .column-sm-<span class="hljs-number">10</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">83.33333333</span>%;  &#125;
  .column-sm-<span class="hljs-number">11</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">91.66666667</span>%;  &#125;  
  .column-sm-<span class="hljs-number">12</span> &#123;  <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;  &#125;
&#125;
div[<span class="hljs-class"><span class="hljs-keyword">class</span>^</span>=<span class="hljs-string">"column-xs-"</span>]&#123;
  <span class="hljs-attr">float</span>: left;
&#125;
div[<span class="hljs-class"><span class="hljs-keyword">class</span>^</span>=<span class="hljs-string">"column-sm-"</span>]&#123;
  <span class="hljs-attr">float</span>: left;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">大小不固定，图片的水平垂直居中</h1>
<blockquote>
<p>参考<a href="https://www.zhangxinxu.com/study/200908/img-text-vertical-align.html#zhangxinxu" target="_blank" rel="nofollow noopener noreferrer">《大小不固定的图片和多行文字的垂直水平居中》</a></p>
</blockquote></div>  
</div>
            