
---
title: '无规矩不成方圆，整理一些CSS开发规范 _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75bf07772aea48b58bc788fb84adf0a7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 20:54:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75bf07772aea48b58bc788fb84adf0a7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">书写顺序</h2>
<h4 data-id="heading-1">相关属性一组</h4>
<p>相关的属性声明应当归为一组，并按照下面的顺序排列：</p>
<p><strong>Positioning</strong></p>
<p><strong>Box model</strong></p>
<p><strong>Typographic</strong></p>
<p><strong>Visual</strong></p>
<h4 data-id="heading-2">说明</h4>
<p>（1）由于<strong>定位</strong>（positioning）可以从正常的文档流中移除元素，并且还能覆盖盒模型（box model）相关的样式，因此排在首位。</p>
<p>（2）<strong>盒模型</strong>排在第二位，因为它决定了组件的尺寸和位置。</p>
<p>（3）<strong>其他属性</strong>只是影响组件的内部（inside）或者是不影响前两组属性，因此排在后面。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75bf07772aea48b58bc788fb84adf0a7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">缩写属性</h2>
<p>　　CSS有些属性是可以缩写的，比如padding,margin,font等等，这样精简代码同时又能提高用户的阅读体验。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/412e774bf1834c0d8f422f8c5e4c7d7d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">去掉小数点前的“0”</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b1e73cede954e99bab1721b1962d4a1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">简写命名</h2>
<p>　　很多用户都喜欢简写类名，但前提是要让人看懂你的命名才能简写哦!</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/892ac55d4b2e487091be59033608316d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">16进制颜色代码缩写</h2>
<p>　　有些颜色代码是可以缩写的，我们就尽量缩写吧，提高用户体验为主。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aad846b5905e41ca992fcb450b47f7ca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">连字符CSS选择器命名规范</h2>
<p>　　1.长名称或词组可以使用中横线来为选择器命名。</p>
<p>　　2.不建议使用“_”下划线来命名CSS选择器，为什么呢?</p>
<p>　　输入的时候少按一个shift键;</p>
<p>　　浏览器兼容问题 (比如使用_tips的选择器命名，在IE6是无效的)</p>
<p>　　能良好区分JavaScript变量命名(JS变量命名是用“_”)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/258d4681cd6e401baae2fff13cc85811~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">不要随意使用Id</h2>
<p>　　id在JS是唯一的，不能多次使用，而使用class类选择器却可以重复使用，另外id的优先级优先与class，所以id应该按需使用，而不能滥用。　</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53c99b6362694fb69728171b73150694~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">为选择器添加状态前缀</h2>
<p>　　有时候可以给选择器添加一个表示状态的前缀，让语义更明了，比如下图是添加了“.is-”前缀。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74efda7f79d144b6bb63d3f1a04dca8b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">不要使用 @import</h2>
<p>与  标签相比，@import 指令要慢很多，不光<strong>增加了额外的请求次数</strong>，还会导致不可预料的问题。</p>
<h4 data-id="heading-11">替代方法</h4>
<p>（1）使用多个  元素</p>
<p>（2）通过 Sass 或 Less 类似的 CSS 预处理器将多个 CSS 文件编译为一个文件</p>
<p>（3）通过 Rails、Jekyll 或其他系统中提供过 CSS 文件合并功能</p>
<h2 data-id="heading-12">CSS的命名规范(BEM,OOCSS)：</h2>
<p>什么是BEM：BEM的意思就是块（block）、元素（element）、修饰符（modifier）,是由Yandex团队提出的一种前端命名方法论。这种巧妙的命名方法让你的CSS类对其他开发者来说更加透明而且更有意义。</p>
<p>命名约定如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.block</span>&#123;&#125; // 块即是通常所说的 Web 应用开发中的组件或模块。每个块在逻辑上和功能上都是相互独立的。

<span class="hljs-selector-class">.block__element</span>&#123;&#125; // 元素是块中的组成部分。元素不能离开块来使用。BEM 不推荐在元素中嵌套其他元素。

<span class="hljs-selector-class">.block--modifier</span>&#123;&#125; // 修饰符用来定义块或元素的外观和行为。同样的块在应用不同的修饰符之后，会有不同的外观。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：</p>
<p>BEM 的优点在于所产生的 CSS 类名都只使用一个类别选择器，可以避免传统做法中由于多个类别选择器嵌套带来的复杂的属性级联问题。在 BEM 命名规则中，所有的 CSS 样式规则都只用一个类别选择器。因此所有样式规则的特异性（specificity）都是相同的，也就不存在复杂的优先级问题。这可以简化属性值的层叠规则。代码清单中的命名规则的好处在于每个 CSS 类名都很简单明了，而且类名的层次关系可以与 DOM 节点的树型结构相对应。</p>
<p>缺点：</p>
<p>这样类名过于长，且复杂。</p>
<p>什么是OOCSS（面向对象CSS）：</p>
<p>OOCSS 表示的是面向对象 CSS（Object Oriented CSS），是一种把面向对象方法学应用到 CSS 代码组织和管理中的实践。 OOCSS最关键的一点就是：提高他的灵活性和可重用性。这个也是OOCSS最重要的一点。OOCSS主张是通过在基础组件中添加更多的类，从而扩展基础组件的CSS规则，从而使CSS有更好的扩展性。</p>
<p>以下是一个基础库创建的样式：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.metadata</span>&#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1.2em</span>;
  <span class="hljs-attribute">text-align</span>: left;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若在给其添加更多的样式：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.metadata</span>&#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1.2em</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span> <span class="hljs-number">0</span>;
    <span class="hljs-comment">/*在基础组件上新加的样式*/</span>
    <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#efefef</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就使前面创建的基础组件<code>metadata</code>变成了一个特定的组件了，使其在其他场景下较难复用。</p>
<p>优点：</p>
<ul>
<li>减少CSS代码。</li>
<li>具有清洁的HTML标记，有语义的类名，逻辑性强的层次关系。</li>
<li>语义标记，有助于SEO。</li>
<li>更好的页面优化，更快的加载时间（因为有很多组件重用）。</li>
<li>可扩展的标记和CSS样式，有更多的组件可以放到库中，而不影响其他的组件。</li>
<li>能轻松构造新的页面布局，或制作新的页面风格。</li>
</ul>
<p>缺点：</p>
<p>OOCSS适合真正的大型网站开发，因为大型网站用到的可重用性组件特别的多，如果运用在小型项目中可能见不到什么成效。所以用不用OOCSS应该根据你的项目来决定。如果没用巧妙的使用，创建组件可能对于你来说是一堆没用的东西，成为一烂摊子，给你的维护带来意想不到的杯具，说不定还是个维护的噩梦。</p></div>  
</div>
            