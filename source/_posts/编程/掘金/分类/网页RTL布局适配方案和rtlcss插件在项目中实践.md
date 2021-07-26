
---
title: '网页RTL布局适配方案和rtlcss插件在项目中实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 18:25:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文首发于：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbigo-frontend%2Fblog%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/bigo-frontend/blog/" ref="nofollow noopener noreferrer">github.com/bigo-fronte…</a> 欢迎关注、转载。</p>
<h2 data-id="heading-0">前言</h2>
<p>bigo作为全球化的互联网企业，产品体验要求国际化，本地化，所面向的用户来自世界各地，他们在产品使用习惯各有不同。尤其对于使用诸如阿拉伯语、乌尔都语、希伯来语等用户，拥有着庞大的数量群体，他们的阅读习惯与中、英文大为不同，是从右到左的顺序进行阅读，从产品使用上需要兼顾这部分用户需求。为了更好地符合用户习惯，作为一名前端开发，我们更应该在页面针对不同语言进行布局适配，努力地提高用户使用体验。</p>
<h2 data-id="heading-1">何为RTL布局</h2>
<p>RTL布局通常称为LTR的镜像布局，整体上是与我们日常看到的页面布局对称，从右往左显示内容。例如显示的文字右侧排列，从右向左阅读，导航顺序相反布局，带有方向性的图标镜像显示等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a082ed9db7d34f8687626cfafa2b019c~tplv-k3u1fbpfcp-zoom-1.image" alt="compare" loading="lazy" referrerpolicy="no-referrer"></p>
<p>LTR和RTL布局的主要区别</p>

























<table><thead><tr><th>元素</th><th>LTR</th><th>RTL</th></tr></thead><tbody><tr><td>文本</td><td>句子从左向右阅读。</td><td>句子从右向左阅读。</td></tr><tr><td>时间线</td><td>事件序列从左向右进行。</td><td>事件序列从右向左进行。</td></tr><tr><td>图像</td><td>从左向右的箭头表示向前运动：→</td><td>从右向左的箭头表示向前运动：←</td></tr></tbody></table>
<p>虽然RTL大体上是镜像布局，但并不是所有地方都需要这样处理，其中有些细节需要注意：</p>
<ul>
<li>页面交互操作方向同样需要改变方向，例如跑马灯、tab组件，向左滑动代表后退，向右滑动代表前进</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1315b6abc1a45d9854f097b8ae7a456~tplv-k3u1fbpfcp-watermark.image" alt="115487974-53cd0b80-a28c-11eb-812a-d61e91b99d90.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1491cc52198d4c9fb78701b9e635ccc2~tplv-k3u1fbpfcp-zoom-1.image" alt="tab" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>某些图标依然按照原来的方向显示，对于不传递方向性的图标、环形流逝方向、代表右手持有的物体和带有斜杠的图标按原有图案展示即可，无需处理。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/beb4525555d74da28f6bd55155cd6bdc~tplv-k3u1fbpfcp-zoom-1.image" alt="icon" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>媒体播放按钮和进度指示器反映的是播放方向，依然按LTR方向展示</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f27ed9b0a0d41ce90040eb1a1c9cb93~tplv-k3u1fbpfcp-zoom-1.image" alt="mediaplay" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总而言之，页面用户体验和界面设计在RTL布局下需要以RTL阅读思维为核心进行设计，了解了RTL布局的特点后接下来总结下现在比较流行常用的页面适配方案</p>
<h2 data-id="heading-2">RTL适配方案</h2>
<h3 data-id="heading-3">direction</h3>
<p>最常用的适配方法是在标签中添加<code>dir</code>属性或使用css的属性<code>direction</code>，指定值为<code>rtl</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">dir</span>=<span class="hljs-string">"rtl"</span>></span>
content
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">html</span> &#123;
  <span class="hljs-attribute">direction</span>: rtl;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置后，你能够看到页面的文字从右往左的顺序显示。但某些地方会看上去觉得奇怪，这个css属性对于带有左右方向调整的样式例如<code>left</code>，<code>magin-left</code>等属性无效，需要额外的处理，在RTL里将<code>left</code>修改成<code>right</code>，<code>margin-left</code>修改成<code>margin-rigtht</code>。例如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你需要额外添加样式，并进行样式覆盖：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
&#125;

<span class="hljs-selector-attr">[dir=<span class="hljs-string">"rtl"</span>]</span> <span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">right</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下这些css属性在RTL布局需要重新正确地设置：</p>
<pre><code class="copyable">background-position
background-position-x
border-bottom-left-radius
border-bottom-right-radius
border-color
border-left
border-left-color
border-left-style
border-left-width
border-radius
border-right
border-right-color
border-right-style
border-right-width
border-style
border-top-left-radius
border-top-right-radius
border-width
box-shadow
clear
direction
float
left
margin
margin-left
margin-right
padding
padding-left
padding-right
right
text-align
transition
transition-property
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，direction改变flex和inline-block元素的方向，flex布局适配RTL，在遇到RTL布局的场景下，请尽可能地使用flexbox布局。</p>
<h3 data-id="heading-4">transform</h3>
<p>另一个简单粗暴的方法是使页面水平翻转，实现水平镜像对称，用到了<code>transform: scaleX(-1)</code>属性。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">html</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scaleX</span>(-<span class="hljs-number">1</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1015846093a4405da3635fd1f1684bb9~tplv-k3u1fbpfcp-zoom-1.image" alt="scale" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图可以看出，使用<code>scaleX(-1)</code>，页面整体上实现了镜像对称，我们无需在css层面上做过多的细节处理，但相应地文字和图像也翻转了，文字显示上会变得非常奇怪，对于文字要再进行翻转处理一次，涉及文字和非对称的图片也要重新设计。</p>
<h3 data-id="heading-5">css逻辑属性</h3>
<p>CSS逻辑属性定义：是CSS的一个模块，其引入的属性与值能做从逻辑角度控制布局，而不是从物理、方向或维度来控制。<br>
简单地说，CSS逻辑属性没有左右物理方向性的概念，基于参照物来描述起点和终点，如LTR布局下<code>start</code>代表<code>left</code>方向，<code>end</code>代表<code>right</code>方向，RTL布局下<code>start</code>代表<code>right</code>方向，<code>end</code>代表<code>left</code>方向，从而提供原生能力去适配LTR和RTL布局，前端样式开发无需考虑布局适配问题</p>
<p>如使用<code>margin-inline-start</code>来代替<code>margin-left</code>，在RTL布局里相当于设置了<code>margin-right</code>的效果，我们无需额外兼容，类似的属性还有：</p>













































<table><thead><tr><th>使用</th><th>不要使用</th></tr></thead><tbody><tr><td>margin-inline-start: 5px;</td><td>margin-left: 5px;</td></tr><tr><td>padding-inline-end: 5px;</td><td>padding-right: 5px;</td></tr><tr><td>float: inline-start;</td><td>float: left;</td></tr><tr><td>inset-inline-start: 5px;</td><td>left: 5px;</td></tr><tr><td>border-inline-end: 1px;</td><td>border-right: 1px;</td></tr><tr><td>border-&#123;start/end&#125;-&#123;start/end&#125;-radius: 2px;</td><td>border-&#123;top/bottom&#125;-&#123;left/right&#125;-radius: 2px;</td></tr><tr><td>padding: 1px 2px;</td><td>padding: 1px 2px 1px 2px;</td></tr><tr><td>margin-block: 1px 3px; && margin-inline: 4px 2px;</td><td>margin: 1px 2px 3px 4px;</td></tr><tr><td>text-align: start; or text-align: match-parent;</td><td>text-align: left;</td></tr></tbody></table>
<p>在某些css属性没有对应的逻辑属性的时候，我们还是要单独对RTL布局定义</p>
<p>在LTR布局中显示</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.search-box</span> &#123;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">chrome://path/to/searchicon.svg</span>);
  <span class="hljs-attribute">background-position</span>: <span class="hljs-number">7px</span> center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在RTL布局时，添加如下样式进行覆盖</p>
<pre><code class="hljs language-css copyable" lang="css">// 需自行在<span class="hljs-selector-tag">html</span>标签设置dir属性以作区分
<span class="hljs-selector-attr">[dir=<span class="hljs-string">"rtl"</span>]</span> <span class="hljs-selector-class">.search-box</span> &#123;
  <span class="hljs-attribute">background-position</span>-x: right <span class="hljs-number">7px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而这些css逻辑属性具有兼容性的问题，大部分的浏览器版本部分属性不支持、IE浏览器完全不支持
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/121cc1e8190c4dc2a4cadfe278f61f48~tplv-k3u1fbpfcp-zoom-1.image" alt="logical_properties" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2Fcss-logical-props" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/css-logical-props" ref="nofollow noopener noreferrer">查看网站</a></p>
<h3 data-id="heading-6">css in js</h3>
<p>该方案是基于css in js的思想，即是使用js来编写css样式，将css和js代码合并在js文件里，常用于jsx组件语法里面。在React组件里，通过定义样式对象来赋予元素样式，实现组件样式，目前比较流行的css in js库有<code>styled-components</code>。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>;

<span class="hljs-keyword">const</span> Title = styled.h1<span class="hljs-string">`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`</span>;

<span class="hljs-keyword">const</span> Wrapper = styled.section<span class="hljs-string">`
  padding: 4em;
  background: papayawhip;
`</span>;

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Wrapper</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">Title</span>></span>Hello World, this is my first styled component!<span class="hljs-tag"></<span class="hljs-name">Title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Wrapper</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用js操作样式的好处是能够在运行时判断是否在rtl语言环境，并相应地修改css样式代码。可以用到<code>styled-components</code>的一个插件<code>stylis-plugin-rtl</code>来处理RTL布局，其背后原理是使用<code>cssjanus</code>库通过js进行rtl样式转换。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> styled, &#123; StyleSheetManager &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"styled-components"</span>;
<span class="hljs-keyword">import</span> rtlPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">"stylis-plugin-rtl"</span>;

<span class="hljs-keyword">const</span> Box = styled.div<span class="hljs-string">`
  padding-left: 10px;
`</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MakeItRTL</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">StyleSheetManager</span> <span class="hljs-attr">stylisPlugins</span>=<span class="hljs-string">&#123;[rtlPlugin]&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Box</span>></span>My padding will be on the right!<span class="hljs-tag"></<span class="hljs-name">Box</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">StyleSheetManager</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">less/sass预处理语言</h3>
<p>利用css预处理语言的mixin混合指令功能，预先写好混合指令，额外生成RTL布局代码。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-keyword">@mixin</span> margin-left(<span class="hljs-variable">$val</span>: <span class="hljs-number">0</span>) &#123;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-variable">$val</span>;
  <span class="hljs-selector-attr">[dir=<span class="hljs-string">'rtl'</span>]</span> & &#123;
    <span class="hljs-attribute">margin-left</span>: initial;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-variable">$val</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入公共mixin指令scss文件，在需要的时候使用<code>@inlcude</code>方法</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-keyword">@import</span> <span class="hljs-string">'@assets/rtl.scss'</span>;

<span class="hljs-selector-class">.el</span> &#123;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#000</span>;

  <span class="hljs-keyword">@include</span> margin-left(<span class="hljs-number">10px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成后的代码分别适配LTR和RTL布局：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.el</span> &#123;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#000</span>;
&#125;

<span class="hljs-selector-attr">[dir=<span class="hljs-string">'rtl'</span>]</span> <span class="hljs-selector-class">.el</span> &#123;
  <span class="hljs-attribute">margin-left</span>: initial;
  <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">使用rtlcss、css-flip转换工具</h3>
<p>可以通过css转换工具如rtlcss/css-flip，无需提前写好混合指令，即可输出RTL样式布局代码。它能够根据所写的css代码自动转编译成带有rtl布局的css代码，无需额外大量添加rtl布局的css代码，编译过程中自动帮我们处理，省时省力，提高我们项目开发效率。</p>
<p>原来的样式</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.example</span> &#123;
  <span class="hljs-attribute">display</span>:inline-block;
  <span class="hljs-attribute">padding</span>:<span class="hljs-number">5px</span> <span class="hljs-number">10px</span> <span class="hljs-number">15px</span> <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">margin</span>:<span class="hljs-number">5px</span> <span class="hljs-number">10px</span> <span class="hljs-number">15px</span> <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">border-style</span>:dotted dashed double solid;
  <span class="hljs-attribute">border-width</span>:<span class="hljs-number">1px</span> <span class="hljs-number">2px</span> <span class="hljs-number">3px</span> <span class="hljs-number">4px</span>;
  <span class="hljs-attribute">border-color</span>:red green blue black;
  <span class="hljs-attribute">box-shadow</span>: -<span class="hljs-number">1em</span> <span class="hljs-number">0</span> <span class="hljs-number">0.4em</span> gray, <span class="hljs-number">3px</span> <span class="hljs-number">3px</span> <span class="hljs-number">30px</span> black;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">npm install -g rtlcss
rtlcss input.ltr.css output.rtl.css
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后会转换成</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.example</span> &#123;
  <span class="hljs-attribute">display</span>:inline-block;
  <span class="hljs-attribute">padding</span>:<span class="hljs-number">5px</span> <span class="hljs-number">20px</span> <span class="hljs-number">15px</span> <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">margin</span>:<span class="hljs-number">5px</span> <span class="hljs-number">20px</span> <span class="hljs-number">15px</span> <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">border-style</span>:dotted solid double dashed;
  <span class="hljs-attribute">border-width</span>:<span class="hljs-number">1px</span> <span class="hljs-number">4px</span> <span class="hljs-number">3px</span> <span class="hljs-number">2px</span>;
  <span class="hljs-attribute">border-color</span>:red black blue green;
  <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">1em</span> <span class="hljs-number">0</span> <span class="hljs-number">0.4em</span> gray, -<span class="hljs-number">3px</span> <span class="hljs-number">3px</span> <span class="hljs-number">30px</span> black;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rtlcss提供丰富的特性来满足适配需求：</p>
<p>1、 Control Directives(控制指令)<br>
控制指令放置在css声明或css语句之间，它能作用于单个或多个节点</p>
<ul>
<li>忽略属性</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.code</span> &#123;
  <span class="hljs-comment">/*rtl:ignore*/</span>
  <span class="hljs-attribute">direction</span>:ltr;
  <span class="hljs-comment">/*rtl:ignore*/</span>
  <span class="hljs-attribute">text-align</span><span class="hljs-selector-pseudo">:left</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>添加额外的样式</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css">  <span class="hljs-comment">/*rtl:raw:
  #example &#123;
      border-radius: 25px 0 0 25px;
  &#125;
  */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>去除属性</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-comment">/*rtl:remove*/</span>
  <span class="hljs-attribute">direction</span>: rtl;
  <span class="hljs-comment">/*rtl:remove*/</span>
  <span class="hljs-attribute">text-align</span>: right;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>重命名选择器</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*rtl:rename*/</span>
<span class="hljs-selector-class">.float-right</span> &#123;
    <span class="hljs-attribute">float</span>: right;
&#125;

//转换后
<span class="hljs-selector-class">.float-left</span> &#123;
    <span class="hljs-attribute">float</span>: left;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、Value Directives(值指令)<br>
值指令放置在css声明的值里，它能作用于所包含的声明节点</p>
<ul>
<li>添加/插入/替换/忽略 属性值</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.sample</span> &#123;
  <span class="hljs-attribute">font-family</span>:<span class="hljs-string">"Droid Sans"</span>, <span class="hljs-string">"Helvetica Neue"</span>, Arial /*rtl:prepend:<span class="hljs-string">"Droid Arabic Kufi"</span>,*/;
  <span class="hljs-attribute">direction</span>:ltr /*rtl:ignore*/;
  <span class="hljs-attribute">font-size</span>:<span class="hljs-number">16px</span> /*rtl:<span class="hljs-number">14px</span>*/;
  <span class="hljs-attribute">transform</span>:<span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>) /*rtl:append:<span class="hljs-built_in">scaleX</span>(-<span class="hljs-number">1</span>)*/;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#00FF00</span> <span class="hljs-built_in">url</span>(<span class="hljs-string">bgimage.gif</span>) no-repeat /*rtl:insert:fixed*/ top;
&#125;

// 转换后
<span class="hljs-selector-class">.sample</span> &#123;
  <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"Droid Arabic Kufi"</span>, <span class="hljs-string">"Droid Sans"</span>, <span class="hljs-string">"Helvetica Neue"</span>, Arial;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
  <span class="hljs-attribute">transform</span>:<span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>) <span class="hljs-built_in">scaleX</span>(-<span class="hljs-number">1</span>);
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#00FF00</span> <span class="hljs-built_in">url</span>(<span class="hljs-string">bgimage.gif</span>) no-repeat fixed top;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更详尽的使用方法可查看官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Frtlcss.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rtlcss.com/" ref="nofollow noopener noreferrer">rtlcss.com/</a></p>
<p>这里编译后的文件会将LTR相关的属性转换成RTL样式，只保留RTL布局的代码，假如想在一份css文件都存在LTR和RTL布局的样式呢，我们需要用到postcss的插件<code>postcss-rtlcss</code>，结合webpack构建工具，实现自动化添加RTL布局样式</p>
<h3 data-id="heading-9">方案比较</h3>

































<table><thead><tr><th>方案</th><th>结论</th></tr></thead><tbody><tr><td>direction="rtl"</td><td>影响了文字排列和布局，需要手动适配的范围大，要尽可能地使用flex和内联块元素进行布局</td></tr><tr><td>transform: scaleX(-1)</td><td>处理简单，布局镜像，但文本和图片显示会有翻转问题</td></tr><tr><td>css逻辑属性</td><td>原生适配，但浏览器兼容性差，部分属性仍需要另外处理，如<code>background-position</code></td></tr><tr><td>css in js</td><td>适合jsx语法开发，需要基于css in js模式编写，js动态生成css，运行耗时，有性能代价，可读性差</td></tr><tr><td>less/scss 预处理语言混合指令特性</td><td>增加额外rtl样式代码大小，虽然减少了一部分代码编写工作量，但还是要手工引入混合指令处理</td></tr><tr><td>rtlcss、css-flip 转换工具</td><td>增加额外rtl样式代码大小，在构建时自动化生成rtl代码，基本不增加适配开发工作量</td></tr></tbody></table>
<h2 data-id="heading-10">rtlcss插件在项目开发中实践</h2>
<p>rtlcss方案虽然会增加样式代码，但是不用另外额外增加工作量，构建工具帮我们完成了脏活，也不失为较优方案，下面是使用<code>postcss-rtlcss</code>插件在项目开发中的实践，基于此工具的应用，比平时正常开发项目至少节省了0.5天工作量来处理多语言适配。</p>
<p>首先安装需要的插件</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i postcss-rtlcss --save-dev

// 将postcss升级到8.0.0版本
npm i postcss@8.0.0 --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在<code>.postcssrc.js</code>文件中添加配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-string">'plugins'</span>: &#123;
    <span class="hljs-string">'postcss-rtlcss'</span>: &#123;&#125; <span class="hljs-comment">// postcss-rtl插件配置，可以添加插件配置选项</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于用户所使用的语言，在html标签设置属性<code>dir</code>为<code>ltr</code>或<code>rtl</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> rtlLangs = [<span class="hljs-string">'ar'</span>, <span class="hljs-string">'ur'</span>, <span class="hljs-string">'fa'</span>, <span class="hljs-string">'pr'</span>];

<span class="hljs-keyword">if</span> (rtlLangs.includes(navigator.language)) &#123;
  <span class="hljs-built_in">document</span>.documentElement.setAttribute(<span class="hljs-string">'dir'</span>, <span class="hljs-string">'rtl'</span>);
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-built_in">document</span>.documentElement.setAttribute(<span class="hljs-string">'dir'</span>, <span class="hljs-string">'ltr'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在webpack打包时就会使用<code>postcss-rtlcss</code>插件进行处理，项目样式无需过多改动</p>
<p>在bigo内部前端旧项目里直接使用<code>postcss-rtlcss</code>插件，可能会遇到以下问题，有可能是<code>postcss-loader</code>版本不兼容造成的：</p>
<p>1、报<code>Error: true is not a PostCSS plugin</code>错误<br>
解决方法：尝试升级<code>postcss-loader</code>到4.2.0版本</p>
<p>2、报<code>this.getOptions is not a function</code>错误<br>
解决方法：尝试降级<code>postcss-loader</code>到4.2.0版本或降级<code>sass-loader</code>版本<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F66082397%2Ftypeerror-this-getoptions-is-not-a-function" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/66082397/typeerror-this-getoptions-is-not-a-function" ref="nofollow noopener noreferrer">stackoverflow.com/questions/6…</a></p>
<p>使用该插件其中遇到另一个问题是，假如在项目中使用sass或less语言，直接使用rtlcss的指令注释写法是不生效的
<a href="https://link.juejin.cn/?target=https%3A%2F%2Frtlcss.com%2Flearn%2Fusage-guide%2Fvalue-directives%2F%23Tip" target="_blank" rel="nofollow noopener noreferrer" title="https://rtlcss.com/learn/usage-guide/value-directives/#Tip" ref="nofollow noopener noreferrer">rtlcss.com/learn/usage…</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsass-lang.com%2Fdocumentation%2Fsyntax%2Fcomments%23in-scss" target="_blank" rel="nofollow noopener noreferrer" title="https://sass-lang.com/documentation/syntax/comments#in-scss" ref="nofollow noopener noreferrer">sass-lang.com/documentati…</a></p>
<p>对于<code>Control Directives</code>语法，需要<code>/*！</code>开头</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-comment">// 自闭合</span>
<span class="hljs-selector-class">.code</span> &#123;
  <span class="hljs-comment">/*!rtl:ignore*/</span>
  <span class="hljs-attribute">text-align</span><span class="hljs-selector-pseudo">:left</span>;
&#125;

<span class="hljs-comment">// 区块</span>
<span class="hljs-selector-class">.code</span> &#123;
  <span class="hljs-comment">/*!rtl:begin:ignore*/</span>
  <span class="hljs-attribute">direction</span>:ltr;
  <span class="hljs-comment">/*!rtl:end:ignore*/</span>
  <span class="hljs-attribute">text-align</span><span class="hljs-selector-pseudo">:left</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于<code>Value Directives</code>语法，需要使用插值语法<br>
SASS/SCSS会忽略放置在声明里的注释，为了确保Value Directives有效需要使用SASS的插值语法</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.example</span> &#123;
  <span class="hljs-attribute">text-align</span>: left #&#123;<span class="hljs-string">"/*!rtl:ignore*/"</span>&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该postcss插件是基于<code>rtlcss</code>插件的基础上封装的，具体的使用方法可以阅读官方文档
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felchininet%2Fpostcss-rtlcss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/elchininet/postcss-rtlcss" ref="nofollow noopener noreferrer">github.com/elchininet/…</a></p>
<h2 data-id="heading-11">总结</h2>
<p>RTL的适配方案众多，开发者需要结合项目的需求特点来选取和组合方案，以达到最优选型，因地制宜，目的是最大程度上在提高开发效率，节省开发周期的基础上提高可维护性</p>
<h2 data-id="heading-12">相关资料：</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FMozilla%2FDeveloper_guide%2FRTL_Guidelines" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/RTL_Guidelines" ref="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2FCSS_Logical_Properties" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Logical_Properties" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.mdui.org%2Fdesign%2Fusability%2Fbidirectionality.html%23bidirectionality-ui-mirroring-overview" target="_blank" rel="nofollow noopener noreferrer" title="https://www.mdui.org/design/usability/bidirectionality.html#bidirectionality-ui-mirroring-overview" ref="nofollow noopener noreferrer">www.mdui.org/design/usab…</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhacks.mozilla.org%2F2015%2F09%2Fbuilding-rtl-aware-web-apps-and-websites-part-1%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://hacks.mozilla.org/2015/09/building-rtl-aware-web-apps-and-websites-part-1/" ref="nofollow noopener noreferrer">hacks.mozilla.org/2015/09/bui…</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhacks.mozilla.org%2F2015%2F10%2Fbuilding-rtl-aware-web-apps-websites-part-2%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://hacks.mozilla.org/2015/10/building-rtl-aware-web-apps-websites-part-2/" ref="nofollow noopener noreferrer">hacks.mozilla.org/2015/10/bui…</a></p>
<p>欢迎大家留言讨论，祝工作顺利、生活愉快！</p>
<p>我是bigo前端，下期见。</p></div>  
</div>
            