
---
title: 'CSS BEM 命名规范 _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90e814a606504ba0a28392d06735c1c0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 23:55:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90e814a606504ba0a28392d06735c1c0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>BEM 是一种前端项目开发的方法学，由 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fyandex.ru%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://yandex.ru/" ref="nofollow noopener noreferrer">Yandex</a> 公司提出。</p>
<p>BEM 的名称来源于该方法学的三个组成部分的英文首字母，分别是块（Block）、元素（Element）和修饰符（Modifier）。</p>
<p>这里推荐一篇关于使用 BEM 的组件命令规范的示例文章：<a href="https://link.juejin.cn/?target=https%3A%2F%2F9elements.com%2Fbem-cheat-sheet%2F%23form-blocks" target="_blank" rel="nofollow noopener noreferrer" title="https://9elements.com/bem-cheat-sheet/#form-blocks" ref="nofollow noopener noreferrer">bem naming cheat sheet by 9elements</a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90e814a606504ba0a28392d06735c1c0~tplv-k3u1fbpfcp-watermark.image" alt="bem naming cheat sheet by 9elements" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中介绍了包括：面包屑、按钮、卡片、列表、导航、布局、表单控件等一些组件的结构、命令示例。</p>
<h2 data-id="heading-0">什么是 CSS BEM？</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbem.info%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://bem.info/" ref="nofollow noopener noreferrer">BEM</a>（<strong>Block Element Modifier，块元素修饰符</strong>）方法是 CSS 类的命名约定，旨在通过定义命名空间来解决范围问题来使 CSS 更具可维护性。</p>
<p>它原则上建议为独立的 CSS 类命名，并且在需要层级关系时，将关系也体现在命名中，这自然会使选择器高效且易于覆盖。</p>
<ul>
<li><strong>block（块）</strong> 是一个独立的组件，可在项目中重复使用，并充当子组件（元素）的 "命名空间"。</li>
<li>当 <strong>block（块）</strong> 或 <strong>element（元素）</strong> 处于特定状态或结构或样式不同时，将 <strong>modifier（修饰符）</strong> 用作标志。</li>
</ul>
<h2 data-id="heading-1">BEM 命名约定</h2>
<ul>
<li><code>block</code> 代表了更高级别的抽象或组件。</li>
<li><code>block__element</code> 代表 <code>.block</code> 的后代，用于形成一个完整的 <code>.block</code> 的整体。</li>
<li><code>block--modifier</code> 代表 <code>.block</code> 的不同状态或不同版本。</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.block</span> &#123;&#125;
<span class="hljs-selector-class">.block__element</span> &#123;&#125;
<span class="hljs-selector-class">.block--modifier</span> &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">示例</h2>
<ul>
<li>BEM 实体名称全部是小写字母或数字。名称中的不同单词用单个连字符（<code>-</code>）分隔。</li>
<li>BEM 元素名称和块名称之间通过两个下划线（<code>__</code>）分隔。</li>
<li>BEM 修饰符和其所修饰的实体名称之间通过两个连字符（<code>--</code>）来分隔。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"menu"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"menu__item menu__item--selected"</span>></span>Item 1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"menu__item"</span>></span>Item 2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"menu__item"</span>></span>Item 3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS 如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.menu</span> &#123;
  <span class="hljs-attribute">list-style</span>: none;
&#125;
<span class="hljs-selector-class">.menu__item</span> &#123;
  <span class="hljs-attribute">font-weight</span>: bold;
&#125;
<span class="hljs-selector-class">.menu__item--selected</span> &#123;
  <span class="hljs-attribute">color</span>: plum;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>分析</strong></p>
<ul>
<li><code>.menu</code> 封装一个独立的实体，它本身是有意义的。虽然块可以嵌套并相互交互，但在语义上它们是相等的；没有优先级或等级制度。</li>
<li><code>.menu__item</code> 块的一部分，没有独立的意义。任何元素在语义上都与其块相关联。</li>
<li><code>.menu__item--selected</code> 块或元素上的修饰符。使用它们来改变外观、行为或状态。</li>
</ul>
<h2 data-id="heading-3">BEM 命名规范带来的好处</h2>
<p>BEM 的优点在于所产生的 CSS 类名都只使用一个类别选择器，可以避免传统做法中由于多个类别选择器嵌套带来的复杂的属性级联问题。</p>
<p>换句话说，其所有样式规则的<strong>特异性（specificity）</strong> 都是相同的，也就不存在复杂的优先级问题，简化了层叠规则。如果你还不是很了解特异性的话，可以查阅之前写的一篇 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F9c6fd2979705" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/9c6fd2979705" ref="nofollow noopener noreferrer">CSS 继承、级联和特异性</a>。</p>
<p>细分后，可以从<strong>模块化</strong>、<strong>可重用性</strong>、<strong>结构</strong>三部分进行理解：</p>
<ul>
<li><strong>模块化</strong>：块样式从不依赖于页面上的其他元素，因此您将永远不会遇到级联带来的问题。</li>
<li><strong>可重用性</strong>：以不同的方式构成独立的块，并以智能方式对其进行重用，从而减少了必须维护的 CSS 代码量。</li>
<li><strong>结构</strong>：BEM 方法为您的 CSS 代码提供了坚实的结构，使结构保持简单易懂。</li>
</ul>
<h2 data-id="heading-4">其他的一些命名规范</h2>
<p>除了 BEM 以外，还有其他一些常用命名规范如：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fstubbornella%2Foocss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/stubbornella/oocss" ref="nofollow noopener noreferrer">OOCSS</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsmacss.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://smacss.com/" ref="nofollow noopener noreferrer">SMACSS</a> 等。</p>
<h3 data-id="heading-5">OOCSS</h3>
<p>OOCSS 表示的是面向对象 CSS（<strong>Object Oriented CSS</strong>），是一种把面向对象方法学应用到 CSS 代码组织和管理中的实践</p>
<p><strong>OOCSS 有两个重要的原则</strong></p>
<ul>
<li>第一个原则是把结构和外观分开。</li>
<li>第二个原则是把容器和内容分开。</li>
</ul>
<h3 data-id="heading-6">SMACSS</h3>
<p>SMACSS 表示的是可扩展和模块化 CSS（<strong>Scalable and Modular Architecture for CSS</strong>）。</p>
<p>SMACSS 把 CSS 样式规则分成若干个不同的类别：</p>
<ul>
<li><strong>基础</strong>：该类别中包含的是默认的 CSS 样式。作为其他样式的基础。</li>
<li><strong>布局</strong>：该类别中包含与页面布局相关的 CSS 样式，用来进行模块的排列。</li>
<li><strong>模块</strong>：该类别中包含的是可复用的模块的 CSS 样式。</li>
<li><strong>状态</strong>：该类别中的 CSS 样式用来描述布局和模块在不同状态下的外观。比如在不同的屏幕尺寸下，布局会发生变化。标签式模块的每个标签页可以有显示或隐藏的状态。</li>
<li><strong>主题</strong>：该类别和状态类似，只不过是用来改变布局和模块的视觉效果。</li>
</ul>
<h2 data-id="heading-7">进一步阅读</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F21935157%2Fanswer%2F20116700" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/21935157/answer/20116700" ref="nofollow noopener noreferrer">如何看待 CSS 中 BEM 的命名方式？</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcsswizardry.com%2F2015%2F08%2Fbemit-taking-the-bem-naming-convention-a-step-further%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://csswizardry.com/2015/08/bemit-taking-the-bem-naming-convention-a-step-further/" ref="nofollow noopener noreferrer">BEMIT: Taking the BEM Naming Convention a Step Further</a></li>
</ul></div>  
</div>
            