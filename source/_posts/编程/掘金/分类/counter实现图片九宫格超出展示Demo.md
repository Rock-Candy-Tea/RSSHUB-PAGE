
---
title: 'counter实现图片九宫格超出展示Demo'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/310103d07a2640dba7d43a3d82b726de~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 23:05:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/310103d07a2640dba7d43a3d82b726de~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">效果展示</h3>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/310103d07a2640dba7d43a3d82b726de~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-1">绘制大致容器</h3>
<p><code>gird</code>简易布局,11个<code>dd</code>元素模拟图片</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">dl</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"view"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dd</span>></span><span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dl</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">dl</span>,
<span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.view</span> &#123;
    <span class="hljs-attribute">display</span>: grid;
    grid-template-<span class="hljs-attribute">columns</span>: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">3</span>, <span class="hljs-number">1</span>fr);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
&#125;
<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#fff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c02f5d1668294661a21a02fd9260c709~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-2"><code>counter</code>计算属性展示数量</h3>
<p>使用<code>::before伪元素覆盖住图片，将</code>counter<code>计算的数量展示在</code>::before元素中</p>
<p><a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">counter</a></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.view</span> &#123;
    <span class="hljs-attribute">display</span>: grid;
    grid-template-<span class="hljs-attribute">columns</span>: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">3</span>, <span class="hljs-number">1</span>fr);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">counter-reset</span>: images;
&#125;
<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">counter-increment</span>: images;
&#125;
<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span><span class="hljs-selector-pseudo">::before</span>&#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">"+"</span><span class="hljs-built_in">counter</span>(images);
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30e5a21617064572993e93214e14e9f0~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<p><code>counter</code>已经将全部<code>dd</code>元素数量展示出来,可我们只需要超出第九个<code>dd</code>元素的数量,这要怎么做呢？</p>
<p>其实很简单，使用<a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">:nth-child伪类</a>选择<strong>第九个<code>dd</code>元素后的兄弟元素</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.view</span> &#123;
    <span class="hljs-attribute">display</span>: grid;
    grid-template-<span class="hljs-attribute">columns</span>: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">3</span>, <span class="hljs-number">1</span>fr);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">counter-reset</span>: images;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#fff</span>;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">9</span>)~<span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">counter-increment</span>: images;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">9</span>) ~ <span class="hljs-selector-tag">dd</span><span class="hljs-selector-pseudo">::before</span>&#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">"+"</span><span class="hljs-built_in">counter</span>(images);
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>~ dd</code>表示后面所有的<code>dd</code>元素</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/165fa3b02bc947ea8e76a9a73d5a3519~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<p>嘿嘿！只差将最后的元素移个位置了，可以使用定位</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">dl</span>,
<span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.view</span> &#123;
    <span class="hljs-attribute">display</span>: grid;
    grid-template-<span class="hljs-attribute">columns</span>: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">3</span>, <span class="hljs-number">1</span>fr);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">counter-reset</span>: images;
    <span class="hljs-attribute">position</span>: relative;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#fff</span>;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">9</span>)~<span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">counter-increment</span>: images;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">9</span>)~<span class="hljs-selector-tag">dd</span><span class="hljs-selector-pseudo">::before</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">"+"</span><span class="hljs-built_in">counter</span>(images);
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将超出第九个的所有元素定位至容器右下方</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90b41870d7fb4df684fce89779c22c00~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-3">原生js实现点击展示</h3>
<p>超出第九个的所有元素被定位在右下，利用js实现点击定位的元素则将元素去除定位属性</p>
<pre><code class="hljs language-css copyable" lang="css">//去除定位 
<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span><span class="hljs-selector-class">.no-befter</span> &#123;
    <span class="hljs-attribute">position</span>: static <span class="hljs-meta">!important</span>;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span><span class="hljs-selector-class">.no-befter</span><span class="hljs-selector-pseudo">::before</span> &#123;
    <span class="hljs-attribute">display</span>: none <span class="hljs-meta">!important</span>;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> dd = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'dd'</span>),
    len = dd.length;
dd[len - <span class="hljs-number">1</span>].onclick = <span class="hljs-function">() =></span> &#123;
    [].slice.call(dd).forEach(<span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
        val.classList.add(<span class="hljs-string">'no-befter'</span>);
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/448023a8b7fd4fee98d18f9ba9fb13ff~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-4">counter另一种思维实现</h3>
<p><code>counter</code>实现九宫格，上面是使用<code>counter</code>默认从<code>0</code>开始。现在重新设置<code>counter</code>从<code>-9</code>开始计算。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">dl</span>,
<span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.view</span> &#123;
    <span class="hljs-attribute">display</span>: grid;
    grid-template-<span class="hljs-attribute">columns</span>: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">3</span>, <span class="hljs-number">1</span>fr);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">counter-reset</span>: images -<span class="hljs-number">9</span>;
    <span class="hljs-attribute">position</span>: relative;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">counter-increment</span>: images;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span><span class="hljs-selector-pseudo">::before</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-built_in">counter</span>(images);
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">text-align</span>: center;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/433e01dd6e58411f8a8b4528826e0f37~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<p>同理，超出第九个元素才展示数量，然后定位</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">dl</span>,
<span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.view</span> &#123;
    <span class="hljs-attribute">display</span>: grid;
    grid-template-<span class="hljs-attribute">columns</span>: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">3</span>, <span class="hljs-number">1</span>fr);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">counter-reset</span>: images -<span class="hljs-number">9</span>;
    <span class="hljs-attribute">position</span>: relative;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">counter-increment</span>: images;
&#125;

<span class="hljs-selector-class">.view</span> <span class="hljs-selector-tag">dd</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">9</span>)~<span class="hljs-selector-tag">dd</span>:before &#123;
    content: <span class="hljs-built_in">counter</span>(images);
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79bde449359a4449bbf51f73896901a4~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<p>后面的代码就不展示了，基本上是一样的。</p>
<p>所有代码保存在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flihai-boop%2Fsimple-dome%2Fblob%2Fmaster%2Fcounter%25E5%25AE%259E%25E7%258E%25B0%25E4%25B9%259D%25E5%25AE%25AB%25E6%25A0%25BC%25E5%259B%25BE%25E7%2589%2587%25E5%25B1%2595%25E7%25A4%25BA.html" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lihai-boop/simple-dome/blob/master/counter%E5%AE%9E%E7%8E%B0%E4%B9%9D%E5%AE%AB%E6%A0%BC%E5%9B%BE%E7%89%87%E5%B1%95%E7%A4%BA.html" ref="nofollow noopener noreferrer"> github</a>需要的自取。</p>
<h3 data-id="heading-5">最后</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_45472813%2Farticle%2Fdetails%2F118382226" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_45472813/article/details/118382226" ref="nofollow noopener noreferrer">CSS::marker让文字序号不再呆板</a>,<code>counter</code>配合<code>::marker</code>可以做有趣列表展示。</p>
<p>公众号:隔壁姥爷，求个关注❤️‍🔥</p></div>  
</div>
            