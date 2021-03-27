
---
title: '一看就会的SCSS'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3663'
author: 掘金
comments: false
date: Fri, 26 Mar 2021 07:41:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=3663'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.前言</h3>
<p><code>Scss</code> 是 <code>Sass3</code> 引入的新的语法，其语法完全兼容<code>css3</code>，并且继承了<code>Sass</code>的强大功能。<code>Sass</code>和<code>Scss</code>其实是同一种东西。</p>
<p><code>Sass</code>是一款强化<code>CSS</code>的辅助工具，它在<code>CSS</code>语法的基础上增加了变量（<code>variables</code>）、嵌套（<code>nested rules</code>)、混合（<code>mixins</code>）、导入（<code>inline imports</code>)等高级功能，这些拓展令<code>CSS</code>更加强大与优雅。使用<code>Sass</code>有助于更好地组织管理样式文件，以及更高效地开发项目。</p>
<h3 data-id="heading-1">2.<code>SCSS</code>基础</h3>
<h4 data-id="heading-2">2.1嵌套选择器</h4>
<p>编译前</p>
<pre><code class="copyable">body &#123;
    background: #FFF;
    p&#123;
        color: #000;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译为css</p>
<pre><code class="copyable">body &#123;
  background: #FFF;
&#125;
body p &#123;
  color: #000;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2.2 <code>&</code>符号</h4>
<p>编译前</p>
<pre><code class="copyable">// &符可以引用父级选择器
li &#123;
    background: #FFF;
    a &#123;
      color:#ff7788;
    &#125;
    &::hover &#123;
        background: #000;
    &#125;
&#125;
.card-item &#123;
  width: 350px;
  height: 200px;
  &-img &#123;
    width: 100%;
    height: 100%;
    object-fit: contain;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译为css</p>
<pre><code class="copyable">li &#123;
  background: #FFF;
&#125;

li a &#123;
  color: #ff7788;
&#125;

li::hover &#123;
  background: #000;
&#125;

.card-item &#123;
  width: 350px;
  height: 200px;
&#125;

.card-item-img &#123;
  width: 100%;
  height: 100%;
  object-fit: contain;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2.3 嵌套属性</h4>
<p>比如字体有<code>font-size</code>,<code>font-weight</code>,<code>font-family</code>等多个属性，但每个属性前面都有个<code>font</code>，那么我们可以用嵌套属性来简写, <strong>此方法使用使用较少</strong></p>
<p>编译前</p>
<pre><code class="copyable">body &#123;
    font: &#123; //注意font后面一定要接 : ,不然会被认为是一个类名
        size:16px;
        weight:700;
        family:'宋体'
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译为css</p>
<pre><code class="copyable">body &#123;
  font-size: 16px;
  font-weight: 700;
  font-family: '宋体';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">2.4 变量</h4>
<p>编译前</p>
<pre><code class="copyable">$width: 5rem;
.main &#123;
   width: $width;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译为css</p>
<pre><code class="copyable">.main &#123;
   width: 5rem;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">2.5 <code>@mixin</code>混合</h4>
<p><code>@mixin</code> 可以将重复的代码提取出来，然后谁要用就 <code>@include</code> 引入</p>
<pre><code class="copyable">@mixin box &#123;
    background: #ffff00;
    border:1px solid #ffff00;
    color:blue;
&#125;
.bigBox &#123;
    @include box;
    height:200px;
    width:200px;
&#125;
.smallBox &#123;
    @include box;
    height:50px;
    width:50px
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译为css</p>
<pre><code class="copyable">.bigBox &#123;
  background: #ffff00;
  border: 1px solid #ffff00;
  color: blue;
  height: 200px;
  width: 200px;
&#125;

.smallBox &#123;
  background: #ffff00;
  border: 1px solid #ffff00;
  color: blue;
  height: 50px;
  width: 50px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2.6 <code>@extend</code></h4>
<p>在写网页时常常遇到这种情况：一个元素使用的样式与另一个元素完全相同，但又添加了额外的样式。通常会在<code>HTML</code>中给元素定义两个<code>class</code>，一个通用样式，一个特殊样式。假设现在要设计一个普通错误样式与一个严重错误样式，一般会这样写：</p>
<pre><code class="copyable"><div class="error seriousError">
  Oh no! You've been hacked!
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样式如下</p>
<pre><code class="copyable">.error &#123;
  border: 1px #f00;
  background-color: #fdd;
&#125;
.seriousError &#123;
  border-width: 3px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>麻烦的是，这样做必须时刻记住使用 <code>.seriousError</code> 时需要参考 <code>.error</code> 的样式，带来了很多不便：比如加重维护负担，导致 <code>bug</code>，或者给 <code>HTML</code> 添加无语意的样式。</p>
<p>使用 <code>@extend</code> 可以避免上述情况，告诉 <code>Sass</code> 将一个选择器下的所有样式继承给另一个选择器。</p>
<pre><code class="copyable">.error &#123;
  border: 1px #f00;
  background-color: #fdd;
&#125;
.seriousError &#123;
  @extend .error;
  border-width: 3px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的意思是将 <code>.error</code> 下的所有样式继承给 <code>.seriousError</code>，<code>border-width: 3px;</code> 是单独给 <code>.seriousError</code> 设定特殊样式，这样，使用 <code>.seriousError</code> 的地方可以不再使用 <code>.error</code>。</p>
<p>编译后</p>
<pre><code class="copyable">.error, .seriousError &#123;
  border: 1px #f00;
  background-color: #fdd; 
&#125;
.seriousError &#123;
  border-width: 3px; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来一个例子：</p>
<p>编译前</p>
<pre><code class="copyable">.error &#123;
  border: 1px #f00;
  background-color: #fdd;
&#125;
.seriousError &#123;
  @extend .error;
  border-width: 3px;
&#125;
.criticalError &#123;
  @extend .seriousError;
  position: fixed;
  top: 10%;
  bottom: 10%;
  left: 10%;
  right: 10%;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后</p>
<pre><code class="copyable">.error, .seriousError, .criticalError &#123;
  border: 1px #f00;
  background-color: #fdd; 
&#125;

.seriousError, .criticalError &#123;
  border-width: 3px;
&#125;

.criticalError &#123;
  position: fixed;
  top: 10%;
  bottom: 10%;
  left: 10%;
  right: 10%;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>继承这个方法会将共同的<code>css</code>写在一起，减少了代码量</strong></p>
<h4 data-id="heading-8">2.7 <code>@function</code></h4>
<p>这个方法提供了在<code>scss</code>中计算属性的功能</p>
<pre><code class="copyable">@function r($size) &#123;
  @return $size / 144 * 1rem;
&#125;
// 使用
p &#123;
  width: r(750);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后 （以<code>html</code>标签<code>font-size: 150px</code> 为例）</p>
<pre><code class="copyable">p &#123;
  width: 5rem;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">2.8 控制指令</h4>
<h5 data-id="heading-10">2.8.1 <code>@if</code></h5>
<pre><code class="copyable">p &#123;
  @if 1 + 1 == 2 &#123; border: 1px solid; &#125;
  @if 5 < 3 &#123; border: 2px dotted; &#125;
  @if null  &#123; border: 3px double; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后</p>
<pre><code class="copyable">p &#123;
  border: 1px solid; 
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@if</code> 声明后面可以跟多个 <code>@else if</code> 声明，或者一个 <code>@else </code>声明。如果<code>@if</code>声明失败，<code>Sass</code> 将逐条执行 <code>@else if</code> 声明，如果全部失败，最后执行 <code>@else</code> 声明，例如：</p>
<pre><code class="copyable">$type: monster;
p &#123;
  @if $type == ocean &#123;
    color: blue;
  &#125; @else if $type == matador &#123;
    color: red;
  &#125; @else if $type == monster &#123;
    color: green;
  &#125; @else &#123;
    color: black;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译为</p>
<pre><code class="copyable">p &#123;
  color: green; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">2.8.2 <code>@for</code></h5>
<p><code>@for</code> 指令可以在限制的范围内重复输出格式，每次按要求（变量的值）对输出结果做出变动。这个指令包含两种格式：<code>@for $var from <start> through <end></code>，或者 <code>@for $var from <start> to <end></code>，区别在于 <code>through </code>与 <code>to</code> 的含义：当使用 <code>through</code> 时，条件范围包含 <code><start> </code>与 <code><end> </code>的值，而使用<code> to</code> 时条件范围只包含 <code><start></code> 的值不包含 <code><end></code> 的值。另外，<code>$var</code> 可以是任何变量，比如 <code>$i</code>；<code><start> </code>和 <code><end></code> 必须是整数值。</p>
<pre><code class="copyable">@for $i from 1 through 3 &#123;
  .item-#&#123;$i&#125; &#123; width: 2rem * $i; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译为</p>
<pre><code class="copyable">.item-1 &#123;
  width: 2rem;
&#125;
.item-2 &#123;
  width: 4rem;
&#125;
.item-3 &#123;
  width: 6rem; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">2.8.3 <code>@each</code></h5>
<p><code>@each</code> 指令的格式是 <code>$var in <list></code>, <code>$var</code> 可以是任何变量名，比如 <code>$length</code> 或者 <code>$name</code>，而<code> <list> </code>是一连串的值，也就是值列表。</p>
<p><code>@each </code>将变量<code> $var</code> 作用于值列表中的每一个项目，然后输出结果，例如：</p>
<pre><code class="copyable">@each $animal in puma, sea-slug, egret, salamander &#123;
  .#&#123;$animal&#125;-icon &#123;
    background-image: url('/images/#&#123;$animal&#125;.png');
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译为</p>
<pre><code class="copyable">.puma-icon &#123;
  background-image: url('/images/puma.png'); 
&#125;
.sea-slug-icon &#123;
  background-image: url('/images/sea-slug.png');
&#125;
.egret-icon &#123;
  background-image: url('/images/egret.png');
&#125;
.salamander-icon &#123;
  background-image: url('/images/salamander.png');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">2.8.4 <code>@while</code></h5>
<p><code>@while</code> 指令重复输出格式直到表达式返回结果为 <code>false</code>。这样可以实现比 <code>@for</code> 更复杂的循环，只是很少会用到。例如：</p>
<pre><code class="copyable">$i: 6;
@while $i > 0 &#123;
  .item-#&#123;$i&#125; &#123; width: 2rem * $i; &#125;
  $i: $i - 2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后</p>
<pre><code class="copyable">.item-6 &#123;
  width: 12rem; 
&#125;

.item-4 &#123;
  width: 8rem;
&#125;

.item-2 &#123;
  width: 4rem;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">2.9 文件导入<code>@import</code></h4>
<p><code>css</code>有一个特别不常用的特性，即<code>@import</code>规则，它允许在一个<code>css</code>文件中导入其他<code>css</code>文件。然而，后果是只有执行到<code>@import</code>时，浏览器才会去下载其他<code>css</code>文件，这导致页面加载起来特别慢。</p>
<p><code>sass</code>也有一个<code>@import</code>规则，但不同的是，<code>sass</code>的<code>@import</code>规则在生成<code>css</code>文件时就把相关文件导入进来。这意味着所有相关的样式被归纳到了同一个<code>css</code>文件中，而无需发起额外的下载请求。另外，所有在被导入文件中定义的变量和混合器（参见2.5节）均可在导入文件中使用。</p>
<pre><code class="copyable">@import './style/default.scss';

p &#123;
  font-size: 16px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">3.小结</h3>
<p>变量是<code>sass</code>提供的最基本的工具。通过变量可以让独立的<code>css</code>值变得可重用，无论是在一条单独的规则范围内还是在整个样式表中。同样基础的是<code>sass</code>的嵌套机制。嵌套允许<code>css</code>规则内嵌套<code>css</code>规则，减少重复编写常用的选择器，同时让样式表的结构一眼望去更加清晰。<code>sass</code>同时提供了特殊的父选择器标识符<code>&</code>，通过它可以构造出更高效的嵌套。</p>
<p>你也已经学到了<code>sass</code>的另一个重要特性，样式导入。通过样式导入可以把分散在多个<code>sass</code>文件中的内容合并生成到一个<code>css</code>文件，避免了项目中有大量的<code>css</code>文件通过原生的<code>css @import</code>带来的性能问题。通过嵌套导入和默认变量值，导入可以构建更强有力的、可定制的样式。混合器允许用户编写语义化样式的同时避免视觉层面上样式的重复。你不仅学到了如何使用混合器减少重复，同时学习到了如何使用混合器让你的<code>css</code>变得更加可维护和语义化。继承允许你声明类之间语义化的关系，通过这些关系可以保持你的<code>css</code>的整洁和可维护性。</p>
<p>参考文档：<a href="https://www.sass.hk/docs/" target="_blank" rel="nofollow noopener noreferrer"> Sass 中文网</a>、<a href="https://www.sasscss.com/documentation/syntax" target="_blank" rel="nofollow noopener noreferrer"> Scss语法</a>、<a href="https://www.sass.hk/guide/" target="_blank" rel="nofollow noopener noreferrer"> Sass快速入门 </a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            