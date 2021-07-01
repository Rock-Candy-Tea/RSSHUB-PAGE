
---
title: 'CSS 里的整洁架构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb7f27fce620411992fa32ba7498fc8d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 07:14:40 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb7f27fce620411992fa32ba7498fc8d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>在历数技术进步的代价时，弗洛伊德遵循的路线使人感到压抑。他同意塔姆斯的评论：<strong>我们的发明只不过是手段的改进，目的却未见改善</strong>。</p>
<p>——尼尔波斯曼《技术垄断》</p>
</blockquote>
<p>虽然开发工具早已经从 preprocessor 进化到了 styled component 甚至是 functional css，但在我看来新的工具并没有让我们的样式代码写的更好，只是更快——也可能会让代码坏的更快。工具的繁荣并没有让那些导致代码难以维护的根本问题烟消云散，而是更易让我们对其视而不见。这篇文章旨在回答一个问题：为什么样式代码难以写对，它的陷阱究竟在哪里？</p>
<p>如果一本正经的聊架构，套路多半是按照某些重要的特征依次展开讲解。但这些所谓的重要特征其实在编程领域中是放之四海而皆准的，例如“扩展性”、“可复用”、“可维护性”等等，按这种思路聊，空谈大于应用。所以我们不如通过解决某个具体的样式问题，来审视样式代码应该如何编写和组织</p>
<p>下图是一个非常简单的 popup 组件，我们会以它的样式开发过程串起整篇的内容。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb7f27fce620411992fa32ba7498fc8d~tplv-k3u1fbpfcp-watermark.image" alt="success.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们首先以一种简单粗暴的方式来实现它，直觉上看，实现这个 popup 只需要三个元素即可：div 是最外面的容器，h1 用于包裹 "Success" 文案，button 用来实现按钮</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"popup"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>Success<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span>></span>OK<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我不会完整的写出它的完整样式，只大概列出其中一些关键属性</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.popup</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: space-around;

  <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;

  <span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
  &#125;

  <span class="hljs-selector-tag">button</span> &#123;
    <span class="hljs-attribute">background</span>: orange;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一版实现即完成了。目前看来并没有什么不妥。</p>
<p>问题不在于实现而是在于维护。接下来我就以一些常见的实际需求变更来看看上面的代码存在怎样的问题。</p>
<h2 data-id="heading-0">对 DOM 元素的依赖</h2>
<p>假设现在需要在“Success”下方新增一个元素用于展示成功的具体信息</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/122e8219362f4bbaa70e869d6bb1903a~tplv-k3u1fbpfcp-watermark.image" alt="success-detail.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>想当然的我们需要新增一个 div 标签。但如果这样的话上面样式中的 .popup div 样式就会同时对这两个 div 产生同样的效果，这并不是我们希望的，很明显这两个元素的样式是不同的。OK，如果你坚持使用标签作为选择器的话，你可以使用伪类选择器 nth-child 来区分样式：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.popup</span> &#123;
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">1</span>) &#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
  &#125;

  <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">5px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但如果某一天你认为"Success"应该使用 h1 而非 div 封装更为恰当的话，那么修改的成本则是：</p>
<ul>
<li>将 div 改为 h1，</li>
<li>将 <code>div:nth-child(1)</code> 样式改为 h1 所属，</li>
<li>将 <code>div:nth-child(2)</code> 还原为 div 样式</li>
</ul>
<p>但如果你一开始就能给 button 和 div 一个确切的 class 名称，那么当你修改 DOM 元素时也仅仅需要修改 DOM 元素，而无需修改样式文件了</p>
<p>上面举得这个例子是水平拓展的情况，也就是说我在某一元素的同一级新增一个元素。纵向拓展也会出现同样的问题，你可以完全想象的出类似于这样的选择器：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.popup</span> <span class="hljs-selector-tag">div</span> > <span class="hljs-selector-tag">div</span> > <span class="hljs-selector-tag">h1</span> > <span class="hljs-selector-tag">span</span> &#123;

&#125;

<span class="hljs-selector-class">.popup</span> &#123;
  <span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-selector-tag">div</span> &#123;
      <span class="hljs-selector-tag">span</span> &#123;&#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>无论是上面代码中的哪一种情况，样式是否生效都极度依赖于 DOM 结构。在一连串的 DOM 标签的层级关系中，哪怕只有一个元素出现了问题（可能是元素标签类型发生了修改，还有可能是在它之上新增了一个元素）都会导致样式大面积失效。同时这样的做法也会让你复用样式难上加难，如果你希望复用 <code>.popup div > div > h1 ></code> 的样式，你不得不将 DOM 结构也拷贝到想要复用的地方。</p>
<p>所以这里我们至少能得出一个结论：CSS 不应该过分的依赖 HTML 结构</p>
<p>而之所以加上“过分”二字，是因为样式完全无法脱离结构独立存在，例如 .popup .title .icon 这样的的依赖关系背后就暗示了 HTML 结构的大致轮廓。</p>
<p>所以我们可以继续将上面的原则稍作更正：CSS 应该拥有对 HTML 的最小知识。理想情况下一个 .button 样式无论应用在任何元素上看上去都应该像同一个立体的可点击按钮。</p>
<h2 data-id="heading-1">父元素依赖</h2>
<p>上一节中我们开发完毕的组件通常会在页面上被多处引用，但总存在个别场景需要你对组件稍作修改才得以适配。假设有一个需求是希望把这个 popup 应用在他们的移动端网站上，但为了适配动设备，某些元素的有关尺寸例如长宽内外边距等都要缩小，你会怎么实现？</p>
<p>我见过的 90% 的解决方案都是以添加父元素的依赖进行实现，也就是判断该组件是否在某个特定的 class 下，如果是的话则修改样式：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">body</span><span class="hljs-selector-class">.mobile</span> &#123;
  <span class="hljs-selector-class">.popup</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但如果此时你需要给平板设备添加一个新的样式，我猜你可能会再添加一个 <code>body.tablet &#123; .popup &#123;&#125; &#125;</code> 代码。又如果移动端网站有两处需要使用 popup ，那么你的代码很最终会变成这样：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">body</span><span class="hljs-selector-class">.mobile</span> &#123;
  <span class="hljs-selector-class">.sidebar</span> &#123;
    <span class="hljs-selector-class">.popup</span>
  &#125;
  
  <span class="hljs-selector-class">.content</span> &#123;
    <span class="hljs-selector-class">.popup</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的代码依然是难以复用的。如果某位开发者看到了移动端网站 popup 打开的样式很喜欢，然后想移植到另一处，那么单纯引入 popup 组件是不够的，他还需要找到真正的生效的代码，将样式和 DOM 层级都复制粘贴过去。</p>
<p>在一个组件自身已经拥有样式的情况下，过分的依赖父组件间接的调整样式，是一种 case by case 的编码行为，本质上这架空了 popup 自带样式。假设 popup 自带 box-shadow 的样式属性，但在有的用例里，box-shadow 可能会被加重，而在有的用例里，box-shadow 又可能会消失，那么它自带的 box-shadow 根部本就没有意义了，因为它永远不会生效。</p>
<p>架空违背了“最小惊讶原则”，给后续的维护者带来了“惊喜”。如果此时 popup 的设计稿发生了修改，阴影需要减少，则修改它自身的样式是不会生效的，或者说无法在每一处生效。而至于还有哪些地方无法生效，为什么它们无法生效，维护者并不知道，他同样需要 case by case 的去查看代码。这么做无疑增加了修改代码的成本</p>
<p>解决这个问题并不像解决 DOM 依赖问题那么简单，需要我们多管齐下。</p>
<h2 data-id="heading-2">样式角色的分离</h2>
<p>想提高代码的可维护性，分离关注点永远是屡试不爽的手段。纵观现有的各类组织样式的方法论，比如 SMASS 或者是 ITCSS，对样式进行适当的角色划分是它们的核心思想之一。</p>
<p>我们以一个完整的 popup 样式为例：</p>
<pre><code class="hljs language-less copyable" lang="less">
<span class="hljs-selector-class">.popup</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>; 

  <span class="hljs-attribute">background</span>: blue;
  <span class="hljs-attribute">color</span>: white;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid gary;

  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这一组样式中，我们看到</p>
<ul>
<li>有与布局相关的 width,     height</li>
<li>与视觉样式相关的 background, color</li>
<li>自身的布局样式 flex</li>
<li>其他样式比如 border</li>
</ul>
<p>根据这些特点和常见的规范，可以考虑从下面几个维度对样式进行分离：</p>
<ul>
<li><strong>布局（Layout）和尺寸（size）</strong>: 一个组件在不同的父组件下拥有不同的尺寸是再正常不过的事情。与其定义一个被架空随时会被覆盖的尺寸，不如将布局的工作交由专职的组件处理。反过来说，该组件自生并不拥有尺寸，例如它可以选择总是以 100% 的宽和高充满包裹它的容器</li>
</ul>
<p>从表面上看，这种行为只是将样式（尺寸）从一个组件转移到另一个组件（容器）上，但却从根本上解决了我们上面提到的父元素依赖的困恼。任何想使用 popup 的其他组件，不用再设法关心 popup 组件的尺寸是如何实现的，它只需要关自己。</p>
<p>进一步从深层次上说，它消灭了<strong>依赖</strong>。你可能没有注意到，flex 布局的样式配置遵循的就是这种模式：当你想让你孩子元素按照某种规则布局的话，你只需要修改父元素和 flex 布局样式属性即可，完全不用再在孩子元素的样式上做出修改。</p>
<p>我个人认为另一个反模式的例子是 <code>text-overflow: ellipsis</code> 属性，单一的该样式属性是不足以自动省略容器内的文字，容器还需要满足 1) 宽度必须是 px 像素为单位 2) 元素必须拥有 <code>overflow:hidden</code> 和 <code>white-space:nowrap</code> 两组样式。也就是说当你想实现 A 功能时，必须依赖 B 和 C 功能的实现。</p>
<p>而至于布局功能元素是与父元素为同一元素，还是独立元素，我倾向于后者，毕竟几个 markup 代码并不会给我们添加多少负担，但清晰的职责划分却能给我们将来的维护带来不少便利</p>
<p>在这个前提下任何给 popup 添加的布局样式实际上都意味这你新增了隐性依赖，因为你实际上是在暗示：它在这个父容器下的这个 margin 值看上去刚好。</p>
<ul>
<li><strong>修饰类（Modifier）</strong>: SOLID 原则中的 open-closed 告诉我们要对修改关闭，对拓展开发，这对样式代码也同样成立。</li>
</ul>
<p>通常我们不会只需要单一样式的按钮，可能还需要带有红底白字的错误样式的按钮，还需要黄底白字的警告样式按钮。这种用例常见的解决方案不是新建 N 个不同的按钮样式，比如 primary-button, error-button（这样务必会出现很多公共的 button 代码），而是在一个 button 样式的基础上，通过提供样式的“修饰”类来达到最终的目的。例如基础款的按钮 class 名称为 button, 如果你想让它变得带有警告样式的话，只需要同时使用 error 的 class 名称即可</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"button error"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从本质上说这也是一种关注点的分离，只不过从这个角度上看它关心的是“变”与“不变”。我们将“变量”统统转移到“修饰”类中。</p>
<p>但这种方案在实现时会遇到不少问题，首先是修饰类的设计，例如当我在定义例如 error, primary, warning 的修饰类时，究竟哪些样式属性是我可以覆盖的哪些是不可以，这必须有事前约定。否则某人在写 error 样式时，可能会无脑的覆盖原 button 上的样式直到看上去满意为止。它依赖于抽象能力，但糟糕的抽象比不抽象还要难以维护。</p>
<ul>
<li><strong>模块化</strong>：借着组件模块化这股东风，样式模块化似乎是水到渠成的事情。但如果眼光放长远一些，模块化并不仅限于将样式赶到某个角落封装起来集中管理。从上面的例子也不难看到，借用样式中父元素依赖的特性可以轻松打破这种封装。</li>
</ul>
<p>组件并非是封装样式的唯一单位，在一个网站中，还可能存在诸如 base、reset 这种全局或者说切面性质的样式属性。我理想的模块化样式应该能够轻松达到以下的目的：</p>
<ul>
<li>控制样式影响的方向性：例如全局样式能够影响组件，但组件不能够影响全局</li>
<li>样式模块间的隔离和污染：虽然 A 组件是 B 组件的子元素，但 B 组件的样式不会影响 A 的样式</li>
</ul>
<p>诠释这两点最好的例子是在进行响应式开发时，业内通用的对字体大小适配的解决方案。例如下面这个组件的 html 结构</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ancestor"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent"</span>></span>
    parent
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
      hello
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>    
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在样式中我们会设定：</p>
<ul>
<li>ancestor 组件字体相对于根元素 html 变化，所以使用 rem 单位</li>
<li>parent 和 child 的字体单位需要相对于该组件（也就是 ancestor）的基准字体进行变化，所以使用 em 单位</li>
</ul>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.ancestor</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1rem</span>;
&#125;
<span class="hljs-selector-class">.parent</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1.5em</span>;
&#125;
<span class="hljs-selector-class">.child</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">2em</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样当我们需要根据设备调整字体大小时，只需要调整根元素 html 字体大小，那么页面上其他元素就会自我调节了。而如果我们只想调整局部样式时，我们只需要调整 .ancestor 的字体大小即可，不会影响到其他元素。</p>
<p>你阅读到这里不难看出来，样式难写对的问题在于它太容易影响别的组件，也太容易受别的组件所影响了。绝大部分人遇到的问题是：</p>
<ul>
<li>我以为我修改的是 A 组件的样式，但无形中却影响到了 B 组件</li>
<li>组件 A 同时受好几组样式的影响，无论单独修改谁都无法达到最终的效果</li>
</ul>
<p>解决这个问题的办法早就有了，那就是样式的隔离。比如在 Angular 中，它是靠给元素添加随机属性并且给样式附带上属性选择器来实现的，例如你同时创建了 page-title 组件和 section-title 组件，它们都拥有 h1 元素的样式，但是在编译之后你看到的 css 分别是：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">h1</span><span class="hljs-selector-attr">[_ngcontent-kkb-c18]</span> &#123;
    <span class="hljs-attribute">background</span>: yellow;
&#125;

<span class="hljs-selector-tag">h1</span><span class="hljs-selector-attr">[_ngcontent-kkb-c19]</span> &#123;
    <span class="hljs-attribute">background</span>: blue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样所有的 h1 元素样式都不会被互相影响</p>
<h2 data-id="heading-3">实现里的问题</h2>
<h3 data-id="heading-4">Pre-Processer</h3>
<p>无论你主观上多么想避免以上的所有问题，给样式一个好的整洁架构。在实现的过程中，我们依然会不小心掉入工具的陷阱中。</p>
<p>再一次回到我们上面提到的 popup 样式：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.popup</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
  
  <span class="hljs-attribute">background</span>: blue;
  <span class="hljs-attribute">color</span>: white;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假如你发现 <code>&#123; background: blue; color: white; &#125;</code> 作为常见样式出现频繁，希望对它进行复用，在使用 Sass 编程的前提下很明显此时你有两个选择：@mixin 或者 @extend。</p>
<p>如果采用 mixin，代码如下</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-variable">@mixin</span> common &#123;  
  <span class="hljs-attribute">background</span>: blue;
  <span class="hljs-attribute">color</span>: white;
&#125;

.popup &#123;  
  <span class="hljs-variable">@include</span> common;  
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而如果采用 extend：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.common</span> &#123;  
  <span class="hljs-attribute">background</span>: blue;
  <span class="hljs-attribute">color</span>: white;
&#125;

<span class="hljs-selector-class">.popup</span> &#123;  
  <span class="hljs-variable">@extend</span> .common;  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个问题是，无论你选择哪种模式，你都很难说开发者是有意在依赖抽象还是在依赖实现。我们可以把 @mixin common 和 .common 解读为对一种抽象的封装，但很有可能后续的消费者只是想复用 background 和 color 而已。一旦如此，common 模块就变得难以修改，因为对任意一个属性的修改都会影响到未知的若干个模块。</p>
<p>在 SASS 中虽然我们可以给类名添加参数，把它当作参数相互传递，但它与我们实际编程中的变量和函数并不相同：JavaScript 中的函数我们往往只关心它的输入与输出，只是定义函数并不会对程序的结果造成影响。而当你在定义样式类的那个时刻就已经可能对页面产生了影响，并且其中的每一条属性都会产生影响。</p>
<p>如果你听说过“组合优于继承”，我相信会对这一点有更深刻的体验。你可以回想继承体系中存在的副作用，例如继承打破了对超类的封装，子类不能减少超类的接口等等，在 SASS 的这类复用关系中都能找到相似的影子。</p>
<p>extend 相比 mixin 更危险的地方在于，它破坏了我们一如既往组织模块的方式。</p>
<p>例如目前已有一个 page 页面，其中拥有一组 page-title 的样式：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.page</span> &#123;
  <span class="hljs-selector-class">.page-title</span> &#123;
      <span class="hljs-selector-class">.icon</span> &#123;
          <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
      &#125;
      
      <span class="hljs-selector-class">.label</span> &#123;
          <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
      &#125;
  &#125;    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在 card-title 想通过 extend 来复用它:</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.card-title</span> &#123;
    <span class="hljs-variable">@extend</span> .page-title;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么编译之后的结果看上去会非常奇怪：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.page</span> <span class="hljs-selector-class">.page-title</span> <span class="hljs-selector-class">.icon</span>, <span class="hljs-selector-class">.page</span> <span class="hljs-selector-class">.card-title</span> <span class="hljs-selector-class">.icon</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.page</span> <span class="hljs-selector-class">.page-title</span> <span class="hljs-selector-class">.label</span>, <span class="hljs-selector-class">.page</span> <span class="hljs-selector-class">.card-title</span> <span class="hljs-selector-class">.label</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>哪怕你没有听说过 BEM，你的编程经验也应该会告诉你 page 和 card 的样式应属于不同的模块。但事实上编译后的结果更像是优先考虑复用，从横切面强行把二者耦合在一起。</p>
<p>而如果你尝试将公共的 title 样式抽象为 mixin，再在 page-title 和 card-title 中进行复用：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-variable">@mixin</span> title &#123;
    <span class="hljs-selector-class">.icon</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
    &#125;
    
    .label &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    &#125;
&#125;

<span class="hljs-selector-class">.page</span> &#123;
    <span class="hljs-selector-class">.page-title</span> &#123;
        <span class="hljs-variable">@include</span> title        
    &#125;
&#125;

<span class="hljs-selector-class">.card-title</span> &#123;
    <span class="hljs-variable">@include</span> title
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译的结果如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.page</span> <span class="hljs-selector-class">.page-title</span> <span class="hljs-selector-class">.icon</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.page</span> <span class="hljs-selector-class">.page-title</span> <span class="hljs-selector-class">.label</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
&#125;

<span class="hljs-selector-class">.card-title</span> <span class="hljs-selector-class">.icon</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.card-title</span> <span class="hljs-selector-class">.label</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显 page 和 card 的样式更泾渭分明</p>
<h3 data-id="heading-5">An Necessary Evil</h3>
<p>如果你问我我是否会遵守上面自己写的每一条原则，我的答案是否定的。在实际开发中我倾向用便捷性换取可维护性。</p>
<p>在编程领域里面唯一不变的就是变化本身，无论在敲键盘之前你面向对象设计的多么准确，对组件拆分的多么恰当，任何业务上的变化都有可能让你所有的设计推倒重来。所以为了保证代码能够精确反馈业务知识的合理性，我们需要时常对代码设计重新设计。</p>
<p>你可以想象整个过程需要重新审视架构，从头阅读理解代码，修改完毕后验证。执行这一系列步骤需要不小的成本，还不包括其中的试错，以及因为重构而浪费的添加新功能的机会。更重要的是成本摆在那里，但收益却并不明显。</p>
<p>如果你的样式代码是基于 design system 之上的，那么你的改动成本会更高。因为你更不可能以个人的视角随心所欲的改动代码了，而是要自上而下的用整个产品的设计语言来衡量修改的合理性。</p>
<p>另一个更实际的问题是，代码从来不是依靠个人来维护。当这一套理论在团队内并没有达成共识，或者是大家只在理论层面了解过而实操时并不在意时，少数人的精心付出终究会化为泡影。代码在理想状态下应该最大成度上摒弃“人”这个因素成为流水线上工业化的产品。所以当我发现某个框架只有要求人们阅读完数十页最佳实践有关的文档才能写出符合官方标准的好代码时，那么现实工作中好代码出现的概率基本为0——在规范输出代码上，一则有效的 eslint 规则比十页文档都要强。而在本篇中叙述的各种原则属于后者。</p>
<p>然而 css 代码被写的乱七八糟又会怎样呢？产品坏了是肯定的，但相比其他 bug 有意思的事情是：</p>
<ul>
<li>相比脚本而言发现样式问题的概率高，所见即所得。</li>
<li>带来的破坏相比脚本功能小，问题下产品依然可用</li>
<li>修复问题成本低，甚至不需要完整阅读源码即可有针对性的快速修复</li>
</ul>
<p>基于上面的三点，同时考虑到当下技术栈繁杂学习成本高，脚本开发工作量大，交付压力重，样式架构的正确性想当然是被牺牲掉的那一个。</p>
<p>最后重申我不鼓励这样的行为，这只是屈服于现实压力下其中的一种可能性而已。如果你所在的项目资源充足，以及大家有决心把事情做对，那也未尝不可。</p>
<h3 data-id="heading-6">Functional CSS</h3>
<p>在我看来还有一类实践是游离于以上体系之外的，比如 tailwind 和 tachyons 。之所以将它们称之为“函数式”样式，是因为在这些框架不提供组件化、语义化的样式，比如 .card， .btn，而提供的是“工具类（utility class）”，比如 .overflow-auto，.box-content，它们 类似于函数式编程中没有副作用的纯函数。当你需要给你元素添加样式时，只需要给这个元素添加对应的 class 名称即可：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"overflow-auto box-content float-left"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之所以说这种实践游离于以上体系之外，是因为它打破了我上面所说的前提：样式和 DOM 结构之间存在依赖关系。在这种编程模式下，因为不再存在“级联”关系，所以每个元素的样式都是独立的，互不影响。</p>
<p>如此看来这种模式简直就是天堂，本文里提及的所有问题都可以避免了：父元素依赖、角色耦合、预处理器里纠结的复用。</p>
<p>但仔细想想，这种方式是不是很 inline style 类似？用 inline style 也能解决我们所说的上述所有问题。我们是不是又回到了起点？</p>
<p>除了上面的问题外，我不再给出进一步推荐或者反对意见的原因在于，一方面这种实践存在<a href="https://dev.to/jaredcwhite/why-tailwind-isn-t-for-me-5c90/comments" target="_blank" rel="nofollow noopener noreferrer">很大</a>的<a href="https://github.com/tachyons-css/tachyons/issues/12" target="_blank" rel="nofollow noopener noreferrer">争议</a>。另一方面我缺乏使用这类框架的经验。这里经验的判断标准不是“是否用过”，而是“是否长期投入到多人协作的大型项目中”——“长期”、“多人”、“大型”这几个关键词很重要。因为我们在做技术选型的时候，更多要考虑和现有项目的契合度、团队的适应成本，以及评估长远来看它能给我们带来巨大的好处是否能抵消替换它的成本。这些经验是我缺乏的。</p>
<p>本文也同步发表在<a href="https://zhuanlan.zhihu.com/front-end" target="_blank" rel="nofollow noopener noreferrer">前端技术漫游指南</a>，欢迎关注</p></div>  
</div>
            