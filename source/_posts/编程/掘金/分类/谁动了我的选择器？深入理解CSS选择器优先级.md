
---
title: '谁动了我的选择器？深入理解CSS选择器优先级'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/460c266955c64fad9e2b3f9f7d4f37a6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 15:49:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/460c266955c64fad9e2b3f9f7d4f37a6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">😏序言</h1>
<p>在前端的面试中，有一道很普遍的题目，就是<strong>CSS选择器的优先级</strong>。原来周一觉得这个东西好像蛮简单的，就是认知里面的类选择器、id选择器和标签，然后就没了。但是殊不知很多时候我们都输给了“我以为”，事实证明一切内容并没有想象中的那么简单。</p>
<p>当我看完书的时候，才发现优先级需要通过计算来确定，然后呢，还有通配选择器、选择符和逻辑组合伪类等等各种类型的计算。</p>
<p>在没有看书之前，我对这些内容的想法可能是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/460c266955c64fad9e2b3f9f7d4f37a6~tplv-k3u1fbpfcp-watermark.image" alt="懵" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因此，写下这篇文章，总结关于 <code>CSS</code> 选择器中的优先级。一起来学习⑧~💡</p>
<h1 data-id="heading-1">🧐文章内容抢先看</h1>
<p>在开始讲解本文之前，我们先用一张思维导图来了解本文的结构内容。<strong>详情见下图👇</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/111648a5e52c4b78bf44f952887142bf~tplv-k3u1fbpfcp-watermark.image" alt="思维导图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来开始进入本文的讲解~</p>
<h1 data-id="heading-2">🤐一、基础知识</h1>
<h2 data-id="heading-3">1、为什么CSS选择器很强</h2>
<ul>
<li>传统编程语言讲求逻辑清晰，层次分明，并且主要为功能服务。</li>
<li>但 <code>CSS</code> 却是为样式服务的，它<strong>重表现</strong>，<strong>轻逻辑</strong>，如同人的思想一样，相互碰撞才能产生火花。</li>
<li>对于 <code>CSS</code> 选择器来说，它作为 <code>CSS</code> 世界的支柱，其作用好比<strong>人类的脊柱</strong>，与 <code>HTML</code> 结构、浏览器行为、用户行为以及整个 <code>CSS</code> 世界相互依存、相互作用，这必然会产生很多碰撞，使得 <code>CSS</code> 选择器变得非常强悍。</li>
</ul>
<h2 data-id="heading-4">2、CSS选择器的一些基本概念</h2>
<h3 data-id="heading-5">（1）4种基本概念</h3>
<p>CSS选择器可以分为<strong>4类</strong>，即<strong>选择器</strong>、<strong>选择符</strong>、<strong>伪类</strong>和<strong>伪元素</strong>。下面介绍这四种类型的区别。</p>
<h4 data-id="heading-6">Ⅰ. 选择器</h4>
<p>选择器，指的是我们平常使用的 <code>css</code> 声明块前面的标签、类名等等。<strong>比如：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#333</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码中的 <code>body</code> 就是一种选择器，是<strong>类型选择器</strong>，也可以称为<strong>标签选择器</strong>。</p>
<hr>
<p><strong>再比如：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.container</span>&#123;
<span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码中的 <code>.container</code> 也是选择器，属于<strong>属性选择器</strong>中的一种，我们也经常称它为<strong>类选择器</strong>。</p>
<h4 data-id="heading-7">Ⅱ. 选择符</h4>
<p><code>CSS</code> 中有<strong>5种</strong>选择符，<strong>分别为：</strong></p>





























<table><thead><tr><th align="center">选择符</th><th align="center">定义</th></tr></thead><tbody><tr><td align="center">空格（ ）</td><td align="center">表示后代关系</td></tr><tr><td align="center">尖括号（>）</td><td align="center">表示父子关系</td></tr><tr><td align="center">加号（+）</td><td align="center">表示相邻兄弟关系</td></tr><tr><td align="center">波浪号（~）</td><td align="center">表示兄弟关系</td></tr><tr><td align="center">双管道（||）</td><td align="center">表示列关系</td></tr></tbody></table>
<p>我们来举些例子，更好的理解这几种选择符。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 后代关系 */</span>
<span class="hljs-selector-class">.container</span> <span class="hljs-selector-tag">img</span> &#123;
    <span class="hljs-attribute">object-fit</span>: contain;
&#125;

<span class="hljs-comment">/* 父子关系 */</span>
<span class="hljs-selector-tag">ol</span> > <span class="hljs-selector-tag">li</span> &#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
&#125;

<span class="hljs-comment">/* 相邻兄弟关系 */</span>
<span class="hljs-selector-tag">button</span> + <span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">10px</span>;
&#125;

<span class="hljs-comment">/* 兄弟关系 */</span>
<span class="hljs-selector-tag">button</span> ~ <span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
&#125;

<span class="hljs-comment">/* 列 */</span>
<span class="hljs-selector-class">.col</span> || <span class="hljs-selector-tag">td</span> &#123;
    <span class="hljs-attribute">background-color</span>: gray;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意的是，相邻兄弟关系和兄弟关系的区别，这两个看起来很相似，很容易混淆。</p>
<p>对于 <code>+</code> 的相邻关系，指的是当前的 <code>button</code> 以及在它<strong>同一层级上的下一个元素</strong> <code>p</code> 的样式；而对于 <code>~</code> 来说，就是当前 <code>button</code> 以及在它<strong>同一层级上的所有 <code>p</code> 元素</strong>的样式。</p>
<p>可以说 <code>+</code> 号是<strong>一对一关系</strong>，而 <code>~</code> 则是<strong>一对多关系</strong>。</p>
<h4 data-id="heading-8">Ⅲ. 伪类</h4>
<p>伪类的特征是其前面会有一个<strong>冒号</strong> <code>:</code> 。对于伪类来说，它通常与<strong>浏览器行为</strong>和<strong>用户行为</strong>相关联，可以把它看成是 <code>css</code> 世界中的 <code>javascript</code> 。<strong>比如：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:hover</span>&#123;
<span class="hljs-attribute">color</span>: gray;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">Ⅳ. 伪元素</h4>
<p>伪元素的特征是其前面会有两个冒号 <code>::</code> ，常见的有 <code>::before</code> 、 <code>::after</code> 、 <code>::first-letter</code> 和 <code>::first-line</code> 等。</p>
<h3 data-id="heading-10">（2）CSS选择器的命名空间</h3>
<p><code>CSS</code> 选择器中还有一个<strong>命名空间</strong>的概念。所谓命名空间，就是我们平常所看到的 <code>@namespace</code> ，主要作用是用来<strong>避免冲突</strong>。</p>
<p>比如说，我们在 <code>html</code> 和 <code>svg</code> 中都会用到 <code><a></code> 链接，这个时候就很可能会发生冲突。那问题来了，冲突制造了，又该怎么解决呢？这个时候就可以用刚刚提到的命名空间 <code>@namespace</code> 来解决。</p>
<p>我们来看一段代码，更直观的了解命名空间。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><<span class="hljs-selector-tag">p</span>>
这是文字:
<a>点击刷新</a>
</p>
<p>
这是SVG:
<svg>
<a xlink:href>
<path d=<span class="hljs-string">"M433.109 23.694c...2.706z"</span>/>
</a>
</svg>
</p>
@namespace <span class="hljs-built_in">url</span>(<span class="hljs-string">http://w3.org/1999/xhtml</span>);
<span class="hljs-keyword">@namespace</span> svg url(<span class="hljs-attribute">http</span>://www.w3.org/<span class="hljs-number">2000</span>/svg);
<span class="hljs-comment">/* 管道符 */</span>
svg|<span class="hljs-selector-tag">a</span> &#123;
    <span class="hljs-attribute">color</span>: black;
    fill: currentColor;
&#125;
<span class="hljs-comment">/* 标签选择器 */</span>
<span class="hljs-selector-tag">a</span> &#123;
    <span class="hljs-attribute">color</span>: gray;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家可以看到， <code>svg|a</code> 中有一个管道符 <code>|</code> ，那么管道符前面的字符表示的就是<strong>命名空间</strong>的代称，而管道符后面的内容则是<strong>选择器</strong>。这段代码最终的显示效果是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28878b10776e4910b94fa285d5c70f62~tplv-k3u1fbpfcp-watermark.image" alt="命名空间" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果按照我们预定的，可能有的小伙伴觉得样式不是越靠后优先级越高吗，而为什么 <code>svg</code> 中的 <code>a</code> 还是显示了<strong>黑色</strong>，而不是<strong>灰色</strong>呢？</p>
<p>其实，大家可以看到上面的命名空间，上述代码中就表示了，在 <code>http://www.w3.org/2000/svg</code> 这个命名空间下所有 <code><a></code> 的颜色都是<strong>黑色 <code>black</code></strong> ，且由于 <code>xhtml</code> 的命名空间（大家定位到第一个命名空间）也被指定了。因此呢， <code>svg</code> 中的 <code><a></code> 标签也就不会受到 <code>标签选择器a</code> 的影响，即便 <code>纯标签选择器a</code> 的优先级再高，那也是无效的。</p>
<hr>
<p>讲到这个，我们来对 <code>css选择器命名空间</code> 做个小结：</p>
<p>其实， <code>css选择器命名空间</code> 的兼容性很好，至少相似10年前浏览器就支持了。但是呢，确很少有人在项目中去使用它。这是为什么呢？</p>
<p>原因主要有<strong>以下两点：</strong></p>
<ul>
<li>
<p>在 <code>html</code> 中直接内联 <code>svg</code> 的应用场景相对来说还是比较少的，你可以试想一下，我们平常在引用阿里图标的时候，会直接把svg那一大串资源，给自己引入到自己的页面中吗？应该没有人这么干吧。所以，它更多的是作为独立资源来使用。</p>
</li>
<li>
<p>还有一个原因就是，有它更好的替代方案。<strong>比如：</strong></p>
<pre><code class="hljs language-css copyable" lang="css">svg <span class="hljs-selector-tag">a</span>&#123;
<span class="hljs-attribute">color</span>: black;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样做的唯一缺点就是，增加了 <code>svg</code> 中 <code>a</code> 元素的优先级。但是再大多数的情况下，对我们的开发基本上没什么影响。</p>
</li>
</ul>
<p>所以呢，对于 <code>css</code> 选择器的<strong>命名空间</strong>，大家可以选择了解即可，至少在遇到<strong>大规模冲突</strong>场景下，给自己多一个解决方法~</p>
<h1 data-id="heading-11">😲二、CSS选择器的优先级</h1>
<p>几乎所有的 <code>css</code> 样式冲突、样式覆盖等等问题，都跟 <code>css</code> 声明的优先级错位脱不开关系。接下来，我们将从 <code>css</code> 优先级规则以及优先级的计算为切入点，来了解关于 <code>css</code> 选择器的优先级。</p>
<h2 data-id="heading-12">1、优先级规则概览</h2>
<h3 data-id="heading-13">（1）选择器权重</h3>
<p><code>css</code> 优先级有着明显的不可逾越的等级制度，因此，我们可以将其划分为 <strong>0~5</strong> 这 <strong>6 个等级</strong>。其中，前4个等级由 <code>css选择器</code> 决定，后2个等级由 <code>书写形式</code> 和 <code>特定语法</code> 决定。 下面来了解这6种等级制度各自的区别，<strong>具体如下表：</strong></p>








































<table><thead><tr><th align="center">等级</th><th align="center">定义</th><th align="center">计算值</th></tr></thead><tbody><tr><td align="center"><strong>0级</strong></td><td align="center">通配选择器、选择符和逻辑组合伪类</td><td align="center">0</td></tr><tr><td align="center"><strong>1级</strong></td><td align="center">标签选择器</td><td align="center">1</td></tr><tr><td align="center"><strong>2级</strong></td><td align="center">类选择器、属性选择器和伪类</td><td align="center">10</td></tr><tr><td align="center"><strong>3级</strong></td><td align="center">ID选择器</td><td align="center">100</td></tr><tr><td align="center"><strong>4级</strong></td><td align="center">style属性内联</td><td align="center">1000</td></tr><tr><td align="center"><strong>5级</strong></td><td align="center">!important</td><td align="center">10000</td></tr></tbody></table>
<h3 data-id="heading-14">（2）选择器说明</h3>
<p>继续，我们对这6个级别对应的选择器样式来做个简单的了解。<strong>具体如下：</strong></p>
<p><strong>0级：通配选择器、选择符和逻辑组合伪类</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 通配选择器指星号（*） */</span>
* &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
&#125;

<span class="hljs-comment">/* ------------------分割线------------------- */</span>

<span class="hljs-comment">/* 选择符指+、>、~、空格和|| 
   具体上面有做详细说明，不再细述 */</span>
<span class="hljs-selector-class">.container</span> <span class="hljs-selector-tag">img</span> &#123;
    <span class="hljs-comment">/* 后代关系 */</span>
&#125;

<span class="hljs-selector-tag">ol</span> > <span class="hljs-selector-tag">li</span> &#123;
    <span class="hljs-comment">/* 父子关系 */</span>
&#125;

<span class="hljs-selector-tag">button</span> + <span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-comment">/* 相邻兄弟关系 */</span>
&#125;

<span class="hljs-selector-tag">button</span> ~ <span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-comment">/* 兄弟关系 */</span>
&#125;

<span class="hljs-selector-class">.col</span> || <span class="hljs-selector-tag">td</span> &#123;
    <span class="hljs-comment">/* 列 */</span>
&#125;

<span class="hljs-comment">/* ------------------分割线------------------- */</span>

<span class="hljs-comment">/* 逻辑组合伪类有:not()、:is()和:where()
   需要注意的是，只有逻辑组合伪类的优先级是0，其他伪类的优先级并不是这样的 */</span>
<span class="hljs-selector-pseudo">:not</span>() &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1级：标签选择器</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 标签选择器类似于body,p,span,div等等这些标签元素 */</span>
<span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2级：类选择器、属性选择器和伪类</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 类选择器指class */</span>
<span class="hljs-selector-class">.container</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#666</span>;
&#125;

<span class="hljs-comment">/* ------------------分割线------------------- */</span>

<span class="hljs-comment">/* 属性选择器指指针对某个标签里面的属性进行特定标识
   比如以下，表示只对有 href 属性的锚（a 元素）应用样式 */</span>
<span class="hljs-selector-tag">a</span><span class="hljs-selector-attr">[href]</span> &#123;
    <span class="hljs-attribute">color</span>:<span class="hljs-number">#666</span>;
&#125;

<span class="hljs-comment">/* ------------------分割线------------------- */</span>

<span class="hljs-comment">/* 伪类指:hover等 */</span>
<span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:hover</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#666</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3级：ID选择器</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#container</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#999</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4级：style属性内联</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: #ccc;"</span>></span>
优先级
<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>5级：! important</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* !important是顶级优先级，
可以重置 js 设置的样式，
唯一推荐使用的场景就是使 js 设置无效（切勿滥用）*/</span>
<span class="hljs-selector-id">#container</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#999</span> <span class="hljs-meta">!important</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">2、优先级计算</h2>
<p>上面我们了解到了关于 <code>css</code> 选择器的各种玩法，那下面我们就来看一下它是怎么玩的。</p>
<h3 data-id="heading-16">（1）选择器优先级计算</h3>
<p>我们用一个表格来罗列处常见的一些计算。当然，大家也可以拿起小本本边看边进行计算。<strong>具体如下表：</strong></p>

































































<table><thead><tr><th align="center">选择器</th><th align="center">计算值</th><th align="center">计算细则</th></tr></thead><tbody><tr><td align="center">*&#123; &#125;</td><td align="center">0</td><td align="center">1个0级通配选择器，优先级数值计算结果为0</td></tr><tr><td align="center">p &#123; &#125;</td><td align="center">1</td><td align="center">1个1级通配选择器，计算结果为1</td></tr><tr><td align="center">ul > li &#123; &#125;</td><td align="center">2</td><td align="center">2个1级标签选择器，1个0级选择符，计算结果为1+0+1</td></tr><tr><td align="center">li > ol + ol &#123; &#125;</td><td align="center">3</td><td align="center">3个1级标签选择器，2个0级选择符，计算结果为1+0+1+0+1</td></tr><tr><td align="center">.foo &#123; &#125;</td><td align="center">10</td><td align="center">1个2级类名选择器，计算结果为10</td></tr><tr><td align="center">a:not([rel=nofollow]) &#123; &#125;</td><td align="center">11</td><td align="center">1个标签选择器，1个0级否定伪类，1个2级属性选择器，计算结果为1+0+10</td></tr><tr><td align="center">a:hover &#123; &#125;</td><td align="center">11</td><td align="center">1个1级标签选择器，1个2级伪类，计算结果为1+10</td></tr><tr><td align="center">ol li.foo &#123; &#125;</td><td align="center">12</td><td align="center">2个1级标签选择器，1个2级类名选择器，1个0级空格选择符，计算结果为1+0+1+10</td></tr><tr><td align="center">li.foo.bar &#123; &#125;</td><td align="center">21</td><td align="center">1个1级标签选择器，2个2级类名选择器，计算结果为1+10+10</td></tr><tr><td align="center">#foo &#123; &#125;</td><td align="center">100</td><td align="center">1个3级id选择器，计算结果为100</td></tr><tr><td align="center">#foo .bar p &#123; &#125;</td><td align="center">111</td><td align="center">1个3级id选择器，1个2级类名选择器，1个1级标签选择器，2个0级空格选择器，计算结果为100+10+1+0+0</td></tr></tbody></table>
<h3 data-id="heading-17">（2）“后来居上”原则</h3>
<p>还有一种可能会出现的情况就是，遇到计算结果相同的，我们该如何取值呢？<strong>比如：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">“zh-CN”</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"foo"</span>></span>颜色是<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">body</span><span class="hljs-selector-class">.foo</span><span class="hljs-selector-pseudo">:not</span>(<span class="hljs-selector-attr">[dir]</span>) &#123;
        <span class="hljs-attribute">color</span>: red;
    &#125;
    
    <span class="hljs-selector-tag">html</span><span class="hljs-selector-attr">[lang]</span> > <span class="hljs-selector-class">.foo</span> &#123;
        <span class="hljs-attribute">color</span>: blue;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来分析下以上这段代码。首先，第一段 <code>css</code> 代码中，出现1个标签选择器 <code>body</code> ，1个类名选择器 <code>.foo</code> 和1个否定伪类 <code>:not</code> ，以及1个属性选择器 <code>[dir]</code> 。因此计算结果为 <code>1+10+0+10</code> ，也就是 <code>21</code> 。</p>
<p>我们再来分析第二段代码， <code>html[lang] > .foo</code> 中出现1个标签选择器 <code>html</code> ，1个属性选择器 <code>[lang]</code> ，1个类名选择器 <code>.foo</code> ，这里 <code>0级选择器</code> 忽略不计。因此，最终计算结果为 <code>1+10+10=21</code> 。</p>
<p>所以，大家可以看到，两个最终的计算结果都是 <code>21</code> 。那我们到底用哪个样式呢？</p>
<p>印证标题所说的，遵循**“后来居上”原则**， 最终这段代码显示为蓝色。</p>
<h3 data-id="heading-18">（3）提升优先级的小技巧</h3>
<p>在实际开发中，我们难免会遇到需要增加 <code>css</code> 选择器优先级的场景。殊不知很多小伙伴可能直接就把内联和 <code>!important</code> 直接怼上去了，这样子造成的后果可能有点恐怖了。</p>
<p>所以，我们需要来了解几种增加选择器权重的做法。<strong>具体如下：</strong></p>
<p>假设现在我要给下面这段代码<strong>增加权重</strong>，<strong>例如：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.foo</span> &#123;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很多时候我们的做法可能是<strong>增加嵌套</strong>或者是<strong>增加一个标签选择器</strong>，<strong>例如：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 增加嵌套 */</span>
<span class="hljs-selector-class">.father</span> <span class="hljs-selector-class">.foo</span> &#123;

&#125;

<span class="hljs-comment">/* 增加标签选择器 */</span>
<span class="hljs-selector-tag">div</span><span class="hljs-selector-class">.foo</span> &#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这种做法往往不是最好的，因为它会增加了代码的耦合度，降低代码的可维护性。试想一下，一旦类名变了，或者标签换了，那你的样式岂不是就要往回去改了，这样会不会就有点不太友好了。</p>
<hr>
<p>所以，我们引出一下两种方式，来解决这个问题。<strong>具体如下：</strong></p>
<p><strong>第一种：</strong> 重复选择器自身</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.foo</span><span class="hljs-selector-class">.foo</span> &#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>第二种：</strong> 借助已存在的属性选择器</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.foo</span><span class="hljs-selector-attr">[class]</span> &#123;

&#125;

<span class="hljs-selector-id">#foo</span><span class="hljs-selector-attr">[id]</span> &#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样看起来，会不会就友好了许多呢。</p>
<h1 data-id="heading-19">🥳三、结束语</h1>
<p>在上文中，我们讲到关于 <code>css</code> 选择器的一些基础知识，以及 <code>css</code> 选择器的优先级的各种计算方式，还有关于“后来居上”原则和一些提升优先级的小tips。</p>
<p>讲到这里，关于 <code>css</code> 选择器优先级的讲解就结束啦！希望对大家有帮助~</p>
<h1 data-id="heading-20">🐣彩蛋 One More Thing</h1>
<h2 data-id="heading-21">🏷️往期推荐&参考资料</h2>
<p>position和z-index👉<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_44803753%2Farticle%2Fdetails%2F119154210" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_44803753/article/details/119154210" ref="nofollow noopener noreferrer">你可能对position和z-index有一些误解</a></p>
<p>书籍👉张鑫旭老师的《CSS选择器世界》</p>
<h2 data-id="heading-22">🏷️番外篇</h2>
<blockquote>
<ul>
<li>关注公众号<strong>星期一研究室</strong>，第一时间关注优质文章，<strong>更多精选专栏待你解锁</strong>~</li>
<li>如果这篇文章对你有用，记得<strong>留个脚印jio</strong>再走哦~</li>
<li>以上就是本文的全部内容！我们下期见！👋👋👋</li>
</ul>
</blockquote></div>  
</div>
            