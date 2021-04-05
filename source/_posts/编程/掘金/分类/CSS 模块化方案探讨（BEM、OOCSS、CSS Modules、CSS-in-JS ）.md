
---
title: 'CSS 模块化方案探讨（BEM、OOCSS、CSS Modules、CSS-in-JS ...）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3ad49b0044c4f759a023ac787804142~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 08:08:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3ad49b0044c4f759a023ac787804142~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>全文共 4000 余字，预计花费 30 分钟。</p>
</blockquote>
<p>众所周知，CSS 根据选择器名称去全局匹配元素，它没有作用域可言，比如你在页面的两个不同的地方使用了一个相同的类名，先定义的样式就会被覆盖掉。CSS 一直缺乏模块化的概念，命名冲突的问题会持续困扰着你。每次定义选择器名称时，总会顾及其他文件中是否也使用了相同的命名，这种影响在组件开发中尤为明显。💣💣💣</p>
<p>理想的状态下，我们开发一个组件的过程中，应该可以随意的为其中元素进行命名，只需要保证其语义性即可，而不必担心它是否与组件之外的样式发生冲突。</p>
<p>与 JavaScript 社区中的 AMD、CMD、CommonJS、ES Modules 等类似，CSS 社区也诞生了相应的模块化解决方案：BEM、OOCSS、SMACSS、ITCSS，以及 CSS Modules 和 CSS-in-JS 等。</p>
<p>根据这些 CSS 模块化方案的特点，我简单的将它们分为了三大类：</p>
<ol>
<li><strong>CSS 命名方法论</strong>：通过人工的方式来约定命名规则。</li>
<li><strong>CSS Modules</strong>：一个 CSS 文件就是一个独立的模块。</li>
<li><strong>CSS-in-JS</strong>：在 JS 中写 CSS。</li>
</ol>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3ad49b0044c4f759a023ac787804142~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">CSS 命名方法论</h2>
<p>为了避免 CSS 选择器命名冲突的问题，以及更好的实现 CSS 模块化，CSS 社区在早期诞生了一些 CSS 命名方法论，如 BEM、OOCSS、SMACSS、ITCSS、SUITCSS、Atomic CSS 等。</p>
<p>它们几乎都有一个共同的特点——为选择器增加冗长的前缀或后缀，并试图通过人工的方式来生成全局唯一的命名。这无疑会增加了类命名的复杂度和维护成本，也让 HTML 标签显得臃肿。</p>
<h3 data-id="heading-1">BEM</h3>
<p><a href="https://www.bemcss.com/" target="_blank" rel="nofollow noopener noreferrer">BEM</a>（Block Element Modifier）是一种典型的 CSS 命名方法论，由 <a href="https://baike.baidu.com/item/Yandex/10230168" target="_blank" rel="nofollow noopener noreferrer">Yandex</a> 团队（相当于中国的百度）在 2009 年前提出，它的核心思想是 <strong>通过组件名的唯一性来保证选择器的唯一性，从而保证样式不会污染到组件外</strong>。</p>
<p>BEM 命名规约是 <code>.block-name__element-name--modifier-name</code>，即 <code>.模块名__元素名--修饰器名</code> 三个部分，用双下划线 <code>__</code> 来明确区分模块名和元素名，用双横线  <code>--</code> 来明确区分元素名和修饰器名。你也可以在保留 BEM 核心思想的前提下，自定义命名风格，如驼峰法、使用单下划线、使用单横线等。</p>
<p>在 BEM 中不建议使用子代选择器，因为每一个类名已经都是全局唯一的了，除非是 block 相互嵌套的场景。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 示例模块 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card__head"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card__menu"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card__menu-item"</span>></span>menu item 1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card__menu-item"</span>></span>menu item 2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card__menu-item card__menu-item--active"</span>></span>menu item 3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card__menu-item card__menu-item--disable"</span>></span>menu item 4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card__body"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card__foot"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.card</span> &#123;&#125;
<span class="hljs-selector-class">.card__head</span> &#123;&#125;
<span class="hljs-selector-class">.card__menu</span> &#123;&#125;
<span class="hljs-selector-class">.card__menu-item</span> &#123;&#125;
<span class="hljs-selector-class">.card__menu-item--active</span> &#123;&#125;
<span class="hljs-selector-class">.card__menu-item--disable</span> &#123;&#125;
<span class="hljs-selector-class">.card__body</span> &#123;&#125;
<span class="hljs-selector-class">.card__foot</span> &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 Sass/Less/Stylus 的父元素选择器 <code>&</code> 可以更高效的编写 BEM：</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.card</span> &#123;
  &__head &#123;&#125;
  &__menu &#123;
    &-item &#123;
      &--active &#123;&#125;
      &--disable &#123;&#125;
    &#125;
  &#125;
  &__body &#123;&#125;
  &__foot &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">OOCSS</h3>
<p><a href="http://oocss.org/" target="_blank" rel="nofollow noopener noreferrer">OOCSS</a>（Object-Oriented CSS）即面向对象的 CSS，它借鉴了 OOP（面向对象编程）的抽象思维，主张将元素的样式抽象成多个独立的小型样式类，来提高样式的灵活性和可重用性。</p>
<p>OOCSS 有两个基本原则：</p>
<ol>
<li><strong>独立的结构和样式</strong>。即不要将定位、尺寸等布局样式与字体、颜色等表现样式写在一个选择器中。</li>
<li><strong>独立的容器和内容</strong>。即让对象的行为可预测，避免对位置的依赖，子元素即使离开了容器也应该能正确显示。</li>
</ol>
<p>比如：我们有一个容器是页面的 1/4 宽，有一个蓝色的背景，1px 灰色的边框，10px 的左右边距，5px 的上边距，10px 的下边距。以前对于这样一个样式，我们常常给这个容器创建一个类，并把这些样式写在一起。像下面这样。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.box</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">25%</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">5px</span> <span class="hljs-number">10px</span> <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">background</span>: blue;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而使用 OOCSS 的话，我们不能这样做，OOCSS 要求为这个容器创建更多的“原子类”，并且每个样式对应一个类，这样是为了后面可以重复使用这些组件的样式，避免重复写相同的样式，就拿这个实例来说，我们给这个容器增加下面的类：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"size1of4 bgBlue solidGray mt-5 ml-10 mr-10 mb-10"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.size1of4</span> &#123; <span class="hljs-attribute">width</span>: <span class="hljs-number">25%</span>; &#125;
  <span class="hljs-selector-class">.bgBlue</span> &#123; <span class="hljs-attribute">background</span>: blue; &#125;
  <span class="hljs-selector-class">.solidGray</span> &#123; <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>; &#125;
  <span class="hljs-selector-class">.mt-5</span> &#123; <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">5px</span>; &#125;
  <span class="hljs-selector-class">.mr-10</span> &#123; <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">10px</span> &#125;
  <span class="hljs-selector-class">.mb-10</span> &#123; <span class="hljs-attribute">margin-bottom</span>: <span class="hljs-number">10px</span>; &#125;
  <span class="hljs-selector-class">.ml-10</span> &#123; <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>; &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OOCSS 最大的优点是让样式可复用性最大化，也能够显著减少整体的 CSS 代码数量。缺点也很明显，你需要为每个元素搜集一大堆类名，这可是一个不小的体力活 😅。</p>
<p>在 OOCSS 中，类名既要能传递对象的用途，也要有通用性，例如 mod、complex、pop 等。如果将 CSS 类命名的太语义化，例如 navigation-bar，那么就会将其限制在导航栏，无法应用到网页的其它位置。</p>
<h3 data-id="heading-3">SMACSS</h3>
<p><a href="http://smacss.com/" target="_blank" rel="nofollow noopener noreferrer">SMACSS</a>（Scalable and Modular Architecture for CSS）即可伸缩及模块化的 CSS 结构，由 Jonathan Snook 在 2011 年雅虎时提出。</p>
<p>SAMCSS 按照部件的功能特性，将其划分为五大类：</p>
<ol>
<li>基础（Base）是为HTML元素定义默认样式，可以包含属性、伪类等选择器。</li>
<li>布局（Layout）会将页面分为几部分，可作为高级容器包含一个或多个模块，例如左右分栏、栅格系统等。</li>
<li>模块（Module）又名对象或块，是可重用的模块化部分，例如导航栏、产品列表等。</li>
<li>状态（State）描述的是任一模块或布局在特定状态下的外观，例如隐藏、激活等。</li>
<li>主题（Theme）也就是换肤，描述了页面的外观，它可修改前面四个类别的样式，例如链接颜色、布局方式等。</li>
</ol>
<p>SMACSS 推荐使用前缀来区分不同部件：</p>
<ol>
<li>基础规则是直接作用于元素的，因此不需要前缀。</li>
<li>布局的前缀是 <code>l-</code> 或 <code>layout-</code>，例如 <code>.l-table</code>、<code>.layout-grid</code> 等。</li>
<li>模块的前缀是 <code>m-</code> 或模块自身的命名，例如 <code>.m-nav</code>、<code>.card</code>、<code>.field</code> 等。</li>
<li>状态的前缀是 <code>is-</code>，例如 <code>.is-active</code>、<code>.is-current</code> 等。</li>
<li>主题的前缀是 <code>theme-</code>，例如 <code>.theme-light</code>、<code>.theme-dark</code> 等。</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layout-grid"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"field"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"search"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"searchbox"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"msg is-error"</span>></span>There is an error!<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">ITCSS</h3>
<p><a href="https://itcss.io/" target="_blank" rel="nofollow noopener noreferrer">ITCSS</a>（Inverted Triangle CSS，倒三角 CSS）是一套方便扩展和管理的 CSS 体系架构，它兼容 BEM、OOCSS、SMACSS 等 CSS 命名方法论。ITCSS 使用 <strong>分层</strong> 的思想来管理你的样式文件，类似服务端开发中的 MVC 分层设计。</p>
<p>ITCSS 将 CSS 的样式规则划分成以下的几个层次：</p>
<ol>
<li>Settings：项目使用的全局变量，比如颜色，字体大小等等。</li>
<li>Tools：项目使用的 mixins 和 functions。到 Tools 为止，不会生成具体的 CSS 代码。</li>
<li>Generic：最基本的设定，比如 reset.css、normalize.css 等。</li>
<li>Base：最基础的元素（elements），比如 img、p、link、list 等。</li>
<li>Objects：某种设计模式，比如水平居中，</li>
<li>Components：UI 组件，比如 button、switch、slider 等。</li>
<li>Trumps：用于辅助和微调的样式，只有这一层才可以使用 <code>!important</code>。</li>
</ol>
<p>ITCSS 的分层逻辑越往下就越具体，越局限在某个具体的场景。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e4cb70583db4d3bb8b5ed8bb2d604b1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>根据 ITCSS 的思想，你可以这样组织你的 CSS 样式文件：</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">stylesheets/
├── settings/
│   ├── colors.scss
│   ├── z<span class="hljs-literal">-layers</span>.scss
│   └── breakpoints.scss
├── tools/
│   ├── mixins.scss
│   └── functions.scss
├── generic/
│   ├── box<span class="hljs-literal">-sizing</span>.scss
│   └── normalize.scss
├── base/
│   ├── img.scss
│   └── list.scss
├── objects/
│   ├── grid.scss
│   └── media.scss
├── components/
│   ├── buttons.scss
│   └── slider.scss
├── trumps/
│   ├── widths.scss
│   └── gaps.scss
└── index.scss
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是几个基于 ITCSS 的模版项目，可供参考：</p>
<ul>
<li><a href="https://github.com/itcss/itcss-netmag" target="_blank" rel="nofollow noopener noreferrer">github.com/itcss/itcss…</a></li>
<li><a href="https://github.com/gpmd/itcss-boilerplate" target="_blank" rel="nofollow noopener noreferrer">github.com/gpmd/itcss-…</a></li>
<li><a href="https://github.com/cameronroe/bootstrap-itscss" target="_blank" rel="nofollow noopener noreferrer">github.com/cameronroe/…</a></li>
</ul>
<h2 data-id="heading-5">CSS Modules</h2>
<blockquote>
<p>📚 上面提到的这些 CSS 命名方法论，虽然已经不适用于当今的自动化工作流和大前端环境，但是他们有其诞生的时代背景，也确实推动了 CSS 模块化的发展，其背后的设计思想同样值得我们学习，甚至有时候我们仍然能在某些场合下看到他们的影子。</p>
</blockquote>
<p>手写命名前缀后缀的方式让开发者苦不堪言，于是 <a href="https://github.com/css-modules/css-modules" target="_blank" rel="nofollow noopener noreferrer">CSS Modules</a> 这种真正的模块化工具就诞生了。</p>
<p>CSS Modules 允许我们像 import 一个 JS Module 一样去 import 一个 CSS Module。每一个 CSS 文件都是一个独立的模块，每一个类名都是该模块所导出对象的一个属性。通过这种方式，便可在使用时明确指定所引用的 CSS 样式。并且，CSS Modules 在打包时会自动将 id 和 class 混淆成全局唯一的 hash 值，从而避免发生命名冲突问题。</p>
<blockquote>
<p>这里仅罗列一些 CSS Modules 的核心特性，更具体的用法可以参考 <a href="https://github.com/css-modules/css-modules" target="_blank" rel="nofollow noopener noreferrer">官网</a> 或 <a href="http://www.ruanyifeng.com/blog/2016/06/css_modules.html" target="_blank" rel="nofollow noopener noreferrer">阮老师的《CSS Modules 用法教程》</a>。</p>
</blockquote>
<p>CSS Modules 特性：</p>
<ul>
<li><strong>作用域</strong>：模块中的名称默认都属于本地作用域，定义在 <code>:local</code> 中的名称也属于本地作用域，定义在 <code>:global</code> 中的名称属于全局作用域，全局名称不会被编译成哈希字符串。</li>
<li><strong>命名</strong>：对于本地类名称，CSS Modules 建议使用 camelCase 方式来命名，这样会使 JS 文件更干净，即 <code>styles.className</code>。
但是你仍然可以固执己见地使用 <code>styles['class-name']</code>，允许但不提倡。🤪</li>
<li><strong>组合</strong>：使用 <code>composes</code> 属性来继承另一个选择器的样式，这与 Sass 的 <code>@extend</code> 规则类似。</li>
<li><strong>变量</strong>：使用 <code>@value</code> 来定义变量，不过需要安装 PostCSS 和 <a href="https://github.com/css-modules/postcss-modules-values" target="_blank" rel="nofollow noopener noreferrer">postcss-modules-values</a> 插件。</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* style.css */</span>
:<span class="hljs-built_in">global</span>(.card) &#123;
  padding: <span class="hljs-number">20px</span>;
&#125;
<span class="hljs-selector-class">.article</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
&#125;
<span class="hljs-selector-class">.title</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">18px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// App.js</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> styles <span class="hljs-keyword">from</span> <span class="hljs-string">'./style.css'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">article</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.article&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.title&#125;</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"card"</span>></span>Lorem ipsum dolor sit amet.<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">article</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译结果：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.card</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
  &#125;
  <span class="hljs-selector-class">.style__article--ht21N</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
  &#125;
  <span class="hljs-selector-class">.style__title--3JCJR</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">18px</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">article</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"style__article--ht21N"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"style__title--3JCJR"</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card"</span>></span>Lorem ipsum dolor sit amet.<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">article</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">CSS Modules 集成</h3>
<p>在 webpack 中使用 CSS Modules（开启 <a href="https://github.com/webpack-contrib/css-loader" target="_blank" rel="nofollow noopener noreferrer">css-loader</a> 的 modules 特性）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js -> module.rules</span>
&#123;
  <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(c|sa|sc)ss$/i</span>,
  exclude: <span class="hljs-regexp">/node_modules/</span>,
  use: [
    <span class="hljs-string">'style-loader'</span>,
    &#123;
      <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>,
      <span class="hljs-attr">options</span>: &#123;
        <span class="hljs-attr">importLoaders</span>: <span class="hljs-number">2</span>,
        <span class="hljs-comment">// 开启 CSS Modules</span>
        <span class="hljs-attr">modules</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 借助 CSS Modules，可以很方便地自动生成 BEM 风格的命名</span>
        <span class="hljs-attr">localIdentName</span>: <span class="hljs-string">'[path][name]__[local]--[hash:base64:5]'</span>,
      &#125;,
    &#125;,
    <span class="hljs-string">'postcss-loader'</span>,
    <span class="hljs-string">'sass-loader'</span>,
  ],
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 PostCSS 中使用 CSS Modules（使用 <a href="https://github.com/madyankin/postcss-modules" target="_blank" rel="nofollow noopener noreferrer">postcss-modules</a> 插件）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// postcss.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: &#123;
    <span class="hljs-string">'postcss-modules'</span>: &#123;
      <span class="hljs-attr">generateScopedName</span>: <span class="hljs-string">'[path][name]__[local]--[hash:base64:5]'</span>,
    &#125;,
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">配合 CSS 预处理器使用</h3>
<p>使用 CSS Modules 时，推荐配合 CSS 预处理器（Sass/Less/Stylus）一起使用。</p>
<p>CSS 预处理器提供了许多有用的功能，如嵌套、变量、mixins、functions 等，同时也让定义本地名称或全局名称变得容易。</p>
<pre><code class="hljs language-less copyable" lang="less">:<span class="hljs-selector-tag">global</span>(.title) &#123;
  <span class="hljs-attribute">color</span>: yellow;
&#125;

:<span class="hljs-selector-tag">global</span> &#123;
  <span class="hljs-selector-class">.global-class-name</span> &#123;
    <span class="hljs-attribute">color</span>: green;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">VSCode 扩展支持</h3>
<p>在 VSCode 中写 CSS Modules 代码，默认是没有自动提示和跳转至定义处的功能，不够智能。</p>
<p>可以安装 <a href="https://marketplace.visualstudio.com/items?itemName=clinyong.vscode-css-modules" target="_blank" rel="nofollow noopener noreferrer">CSS Modules</a> 扩展。</p>
<p><img alt="l0EwY2Mk4IBgIholi.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/025c45925b974ed5aea51228543accb9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">CSS-in-JS</h2>
<p>React 的出现，打破了以前“关注点分离”的网页开发原则，因其采用组件结构，而组件又强制要求将 HTML、CSS 和 JS 代码写在一起。表面上看是技术的倒退，实际上并不是。</p>
<p>React 是在  JS 中实现了对 HTML 和 CSS 的封装，赋予了 HTML 和 CSS 全新的“编程能力”。对于 HTML，衍生了 JSX 这种 JS 的语法扩展，你可以将其理解为 HTML-in-JS；对于 CSS，衍生出一系列的第三方库，用来加强在 JS 中操作 CSS 的能力，它们被称为 CSS-in-JS。</p>
<p>随着 React 的流行以及组件化开发模式的深入人心，这种"关注点混合"的新写法逐渐成为主流。</p>
<blockquote>
<p>Any application that can be written in JavaScript, will eventually be written in JavaScript. —— Jeff Atwood</p>
</blockquote>
<p>CSS-in-JS 库目前已有几十种实现，你可以在 <a href="https://www.cssinjsplayground.com/" target="_blank" rel="nofollow noopener noreferrer">CSS in JS Playground</a> 上快速尝试不同的实现。下面列举一些流行的 CSS-in-JS 库：</p>
<ul>
<li>styled-components：<a href="https://github.com/styled-components/styled-components" target="_blank" rel="nofollow noopener noreferrer">github.com/styled-comp…</a> 33k（<strong>推荐</strong>）</li>
<li>emotion：<a href="https://github.com/emotion-js/emotion" target="_blank" rel="nofollow noopener noreferrer">github.com/emotion-js/…</a> 13k</li>
<li>Radium：<a href="https://github.com/FormidableLabs/radium" target="_blank" rel="nofollow noopener noreferrer">github.com/FormidableL…</a> 7k（已不再维护）</li>
<li>Styled System：<a href="https://github.com/styled-system/styled-system" target="_blank" rel="nofollow noopener noreferrer">github.com/styled-syst…</a> 7k</li>
<li>styled-jsx：<a href="https://github.com/vercel/styled-jsx" target="_blank" rel="nofollow noopener noreferrer">github.com/vercel/styl…</a> 6k</li>
<li>JSS：<a href="https://github.com/cssinjs/jss" target="_blank" rel="nofollow noopener noreferrer">github.com/cssinjs/jss</a> 6k</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c62c99ec289143bd9c0b5344c29d9048~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">styled-components 💅</h3>
<p>styled-components 是目前最流行的 CSS-in-JS 库，在 React 中被广泛使用。</p>
<p>它使用 ES6 提供的模版字符串功能来构造“样式组件”。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// styles.js</span>
<span class="hljs-keyword">import</span> styled, &#123; css &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>

<span class="hljs-comment">// 创建一个名为 Wrapper 的样式组件 (一个 section 标签, 并带有一些样式)</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Wrapper = styled.section<span class="hljs-string">`
  padding: 10px;
  background: deepskyblue;
`</span>

<span class="hljs-comment">// 创建一个名为 Title 的样式组件 (一个 h1 标签, 并带有一些样式)</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Title = styled.h1<span class="hljs-string">`
  font-size: 20px;
  text-align: center;
`</span>

<span class="hljs-comment">// 创建一个名为 Button 的样式组件 (一个 button 标签, 并带有一些样式, 还接收一个 primary 参数)</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Button = styled.button<span class="hljs-string">`
  padding: 10px 20px;
  color: #333;
  background: transparent;
  border-radius: 4px;

  <span class="hljs-subst">$&#123;(props) => props.primary && css`<span class="css">
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">background</span>: blue;
  `</span>&#125;</span>
`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// App.js</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; Wrapper, Title, Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./styles'</span>

<span class="hljs-comment">// 然后，像使用其他 React 组件一样使用这些样式组件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Wrapper</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Title</span>></span>Hello World, this is my first styled component!<span class="hljs-tag"></<span class="hljs-name">Title</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Button</span>></span>Normal Button<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">primary</span>></span>Primary Button<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Wrapper</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多使用技巧（更具体的内容请参考 <a href="https://styled-components.com/" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>）：</p>
<ul>
<li>可以通过插值的方式给样式组件传递参数（<code>props</code>），这在需要动态生成样式规则时特别有用。</li>
<li>可以通过构造函数 <code>styled()</code> 来继承另一个组件的样式。</li>
<li>使用 <code>createGlobalStyle</code> 来创建全局 CSS 规则。</li>
<li>styled-components 会为自动添加浏览器兼容性前缀。</li>
<li>styled-components 基于 <a href="https://github.com/thysultan/stylis.js#readme" target="_blank" rel="nofollow noopener noreferrer">stylis</a>（一个轻量级的 CSS 预处理器），你可以在样式组件中直接使用嵌套语法，就像在 Sass/Less/Stylus 中的那样。</li>
<li>强烈推荐使用 styled-components 的 Babel 插件 <a href="https://github.com/styled-components/babel-plugin-styled-components" target="_blank" rel="nofollow noopener noreferrer">babel-plugin-styled-components</a>（当然这不是必须的）。它提供了更好的调试体验的支持，比如更清晰的类名、SSR 支持、压缩代码等等。</li>
<li>你也可以在 Vue 中使用 styled-components，<a href="https://github.com/styled-components/vue-styled-components" target="_blank" rel="nofollow noopener noreferrer">vue-styled-components</a>，不过好像没人会这么做~</li>
<li>默认情况下，模版字符串中的 CSS 代码在 VSCode 中是没有智能提示和语法高亮效果的，需要安装 <a href="https://marketplace.visualstudio.com/items?itemName=jpoissonnier.vscode-styled-components" target="_blank" rel="nofollow noopener noreferrer">扩展</a>。</li>
</ul>
<h2 data-id="heading-11">在 Vue 中编写 CSS 的正确姿势</h2>
<p><strong>方式一：使用 Scoped CSS（推荐）</strong></p>
<p>为 <code><style></code> 区块添加 <code>scoped</code> 属性即可开启“组件样式作用域（Scoped CSS）”。</p>
<p>在背后，Vue 会为该组件内所有的元素都加上一个全局唯一的属性选择器，形如 <code>[data-v-5298c6bf]</code>，这样在组件内的 CSS 就只会作用于当前组件中的元素。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">header</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header"</span>></span>header<span class="hljs-tag"></<span class="hljs-name">header</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.header</span> &#123;
  <span class="hljs-attribute">background-color</span>: green;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译结果：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">header</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header"</span> <span class="hljs-attr">data-v-5298c6bf</span>></span>header<span class="hljs-tag"></<span class="hljs-name">header</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-class">.header</span><span class="hljs-selector-attr">[data-v-5298c6bf]</span> &#123;
  <span class="hljs-attribute">background-color</span>: green;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方式二：使用 CSS Modules</strong></p>
<p>为 <code><style></code> 区块添加 <code>module</code> 属性即可开启 CSS Modules。</p>
<p>在背后，Vue 会为组件注入一个名为 <code>$style</code> 的计算属性，并混淆类名，然后你就可以在模板中通过一个动态类绑定来使用它了。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">header</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"$style.header"</span>></span>header<span class="hljs-tag"></<span class="hljs-name">header</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">module</span>></span><span class="css">
<span class="hljs-selector-class">.header</span> &#123;
  <span class="hljs-attribute">background-color</span>: green;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译结果：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">header</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"App__header--382G7"</span>></span>header<span class="hljs-tag"></<span class="hljs-name">header</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-class">.App__header--382G7</span> &#123;
  <span class="hljs-attribute">background-color</span>: green;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">在 React 中编写 CSS 的正确姿势</h2>
<p>React 并没有给我们提供与 Vue 的 <code>scoped</code> 类似的特性，我们需要通过其他方式来实现 CSS 模块化。</p>
<ol>
<li><strong>使用 styled-components</strong>：styled-components 是最流行也是最好用的 CSS-in-JS 库，它将 CSS、JS 以及 React 开发中最流行的一些语法整合起来，易上手，且功能强大。</li>
<li><strong>使用 CSS Modules</strong>：在外部管理 CSS，然后将类名映射到组件内部，他会为每个 class 都分配一个全局唯一 hash。另外，这两个插件会帮你更好地在 React 中使用 CSS Modules：<a href="https://github.com/gajus/react-css-modules" target="_blank" rel="nofollow noopener noreferrer">react-css-modules</a>、<a href="https://github.com/gajus/babel-plugin-react-css-modules" target="_blank" rel="nofollow noopener noreferrer">babel-plugin-react-css-modules</a>。</li>
</ol>
<p>CSS Modules 与 styled-components 是两种截然不同的 CSS 模块化方案，它们最本质的区别是：前者是在外部管理 CSS，后者是在组件中管理 CSS。两者没有孰好孰坏，如果你能接受 CSS-in-JS 这种编程模式，更推荐使用 styled-components。如果一时无法接受，觉得其过于激进了，那就用 CSS Modules。It doesn't matter，选择了哪一个，就用哪一个的体系去管理项目就好了。</p>
<h2 data-id="heading-13">参考资料</h2>
<ol>
<li><a href="https://www.smashingmagazine.com/2012/04/a-new-front-end-methodology-bem/" target="_blank" rel="nofollow noopener noreferrer">BEM: A New Front-End Methodology — Smashing Magazine</a></li>
<li><a href="https://www.smashingmagazine.com/2016/06/battling-bem-extended-edition-common-problems-and-how-to-avoid-them/" target="_blank" rel="nofollow noopener noreferrer">Battling BEM CSS: 10 Common Problems And How To Avoid Them — Smashing Magazine</a></li>
<li><a href="https://www.smashingmagazine.com/2011/12/an-introduction-to-object-oriented-css-oocss/" target="_blank" rel="nofollow noopener noreferrer">An Introduction To Object Oriented CSS (OOCSS) — Smashing Magazine</a></li>
<li><a href="https://github.com/MicheleBertoli/css-in-js" target="_blank" rel="nofollow noopener noreferrer">MicheleBertoli/css-in-js: React: CSS in JS techniques comparison</a></li>
<li><a href="https://github.com/css-modules/css-modules" target="_blank" rel="nofollow noopener noreferrer">CSS Modules 用法教程 - 阮一峰的网络日志</a></li>
<li><a href="http://www.ruanyifeng.com/blog/2017/04/css_in_js.html" target="_blank" rel="nofollow noopener noreferrer">CSS in JS 简介 - 阮一峰的网络日志</a></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            