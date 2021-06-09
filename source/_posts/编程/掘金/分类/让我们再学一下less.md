
---
title: '让我们再学一下less'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7702'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 00:47:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=7702'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第8天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h3 data-id="heading-0">写在前面</h3>
<p>less之前看过很多文章，也写过，但是只是记住一些常用用法，很多时候又得去网上翻找资料才记得，所以今天我打算把less重温一遍，把安装，使用，语法这些都记录下来，记录成文章，方便后续查阅。</p>
<h3 data-id="heading-1">定义</h3>
<blockquote>
<p>less 是一门 CSS 预处理语言，可以通过预处理器把less文件编译成css，less增加了变量、混合（mixin）、函数等功能，弥补了css的不足，让编写css更加方便</p>
</blockquote>
<h3 data-id="heading-2">使用</h3>
<h4 data-id="heading-3">第一种方式：引入less.js</h4>
<ol>
<li>
<p>在html引入less.js</p>
<p>可以通过cdn方式，也可以把less下载下来，然后通过script标签引入</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"http://cdnjs.cloudflare.com/ajax/libs/less.js/3.11.1/less.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
// 或者
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"less.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>引入编写好的less文件</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet/less"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"index.less"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"less.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：<code>link</code>标签要在<code>script</code>标签之前引入，<code>rel</code>属性也要设置成<code>stylesheet/less</code></p>
</blockquote>
</li>
<li>
<p>执行html</p>
<blockquote>
<p>注意html要起个本地服务器跑，不要直接在浏览器中运行，否则会有跨域问题；</p>
</blockquote>
</li>
</ol>
<h4 data-id="heading-4">第二种方式：安装依赖</h4>
<ol>
<li>node全局安装less
<pre><code class="hljs language-js copyable" lang="js">npm install -g less  <span class="hljs-comment">// 也可以通过  yarn global add less</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>在命令行执行
<pre><code class="hljs language-js copyable" lang="js">lessc index.less index.css
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>在html引入编译好的<code>index.css</code></li>
</ol>
<h3 data-id="heading-5">语法</h3>
<h4 data-id="heading-6">变量（Variables）</h4>
<p>css 如果一个颜色多个地方使用，就得定义多次，如果需要修改，也得改多次，这样很不方便；<br>
less支持变量的写法，把那些用的比较多的相同的值通过变量来定义，只需修改一次。</p>
<p>以 <code>@</code> 开头声明变量</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-variable">@width:</span> <span class="hljs-number">50px</span>;
<span class="hljs-variable">@color:</span> red;
<span class="hljs-variable">@bgColor:</span> blue;

<span class="hljs-selector-class">.div1</span> &#123;
 <span class="hljs-attribute">width</span>: <span class="hljs-variable">@width</span>;
 <span class="hljs-attribute">color</span>: <span class="hljs-variable">@color</span>;
 <span class="hljs-attribute">background</span>: <span class="hljs-variable">@bgColor</span>;
&#125;
<span class="hljs-selector-class">.div2</span> &#123;
 <span class="hljs-attribute">width</span>: <span class="hljs-variable">@width</span>;  <span class="hljs-comment">// 如果要修改width 只需改上面定义的width就行</span>
 <span class="hljs-attribute">color</span>: <span class="hljs-variable">@color</span>;
 <span class="hljs-attribute">background</span>: <span class="hljs-variable">@bgColor</span>;
&#125;

<span class="hljs-comment">// less编译后</span>
<span class="hljs-selector-class">.div1</span> &#123;
 <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
 <span class="hljs-attribute">color</span>: red;
 <span class="hljs-attribute">background</span>: blue;
&#125;
<span class="hljs-selector-class">.div2</span> &#123;
 <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
 <span class="hljs-attribute">color</span>: red;
 <span class="hljs-attribute">background</span>: blue;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">混合（Mixins)</h4>
<p>将一类样式的封装好，可以在别的元素里面直接调用，复用</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-comment">// 需要复用的样式</span>
<span class="hljs-selector-class">.center</span>(<span class="hljs-variable">@width</span>: <span class="hljs-number">100px</span>) &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-variable">@width</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">line-height</span>: normal;
&#125;
<span class="hljs-selector-id">#div1</span> &#123;
   <span class="hljs-comment">// 调用</span>
  <span class="hljs-selector-class">.center</span>();
&#125;
<span class="hljs-selector-id">#div2</span> &#123;
   <span class="hljs-comment">// 调用,可以传参</span>
  <span class="hljs-selector-class">.center</span>(<span class="hljs-number">200px</span>);
&#125;
<span class="hljs-comment">// 编译后</span>
<span class="hljs-selector-id">#div1</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">line-height</span>: normal;
&#125;
<span class="hljs-selector-id">#div2</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">line-height</span>: normal;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">嵌套（Nesting）</h4>
<p>css的元素之间的样式是不能嵌套的，less扩展了这个，可以跟 HTML 的组织结构一样嵌套写样式，方便寻找和修改<br>
嵌套用的比较多有个符号<code>&</code>，代表的是父级元素的引用</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-variable">@color:</span> red;
<span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-selector-class">.header</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-variable">@color</span>;
  &#125;
  <span class="hljs-selector-class">.content</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-variable">@color</span>;
    <span class="hljs-selector-class">.item</span> &#123;
      <span class="hljs-attribute">color</span>: <span class="hljs-variable">@color</span>;
      <span class="hljs-selector-tag">&</span><span class="hljs-selector-class">.item-1</span> &#123;
        <span class="hljs-attribute">color</span>: <span class="hljs-variable">@color</span>;
      &#125;
      <span class="hljs-selector-tag">&</span><span class="hljs-selector-tag">-2</span> &#123; <span class="hljs-comment">// 要注意这种情况，这里只是使用父级名称</span>
        <span class="hljs-attribute">color</span>: <span class="hljs-variable">@color</span>;
      &#125;
    &#125;
  &#125;
  <span class="hljs-selector-class">.footer</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-variable">@color</span>;
  &#125;
&#125;

<span class="hljs-comment">// 编译后</span>
<span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.header</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.content</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.content</span> <span class="hljs-selector-class">.item</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.content</span> <span class="hljs-selector-class">.item</span><span class="hljs-selector-class">.item-1</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.content</span> <span class="hljs-selector-class">.item-2</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.footer</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">运算（Operations）</h4>
<p>支持<code>+</code>，<code>-</code>，<code>*</code>，<code>/</code> 符号运算</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-variable">@width-200:</span> <span class="hljs-number">100px</span> + <span class="hljs-number">100px</span>;
<span class="hljs-variable">@width-50:</span> <span class="hljs-number">150px</span> - <span class="hljs-number">100px</span>;
<span class="hljs-variable">@width-10:</span> <span class="hljs-number">5px</span> * <span class="hljs-number">2px</span>;

<span class="hljs-selector-class">.div1</span> &#123;
 <span class="hljs-attribute">width</span>: <span class="hljs-variable">@width-200</span>;
&#125;
<span class="hljs-selector-class">.div2</span> &#123;
 <span class="hljs-attribute">width</span>: <span class="hljs-variable">@width-50</span>;
&#125;
<span class="hljs-selector-class">.div3</span> &#123;
 <span class="hljs-attribute">width</span>: <span class="hljs-variable">@width-10</span>;
&#125;

<span class="hljs-comment">// 编译后</span>
<span class="hljs-selector-class">.div1</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
&#125;
<span class="hljs-selector-class">.div2</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
&#125;
<span class="hljs-selector-class">.div3</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">内置函数（Functions）</h4>
<p>Less 内置了很多函数，可以处理百分比，小数，颜色等等</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-variable">@width:</span> <span class="hljs-number">0.5</span>;
<span class="hljs-variable">@color:</span> <span class="hljs-number">#fa0141</span>;
<span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-attribute">width</span>: percentage(<span class="hljs-variable">@width</span>); <span class="hljs-comment">// returns `50%`</span>
    <span class="hljs-attribute">color</span>: saturate(<span class="hljs-variable">@color</span>, <span class="hljs-number">5%</span>) <span class="hljs-comment">// 增加5%的颜色饱和度</span>
&#125;

<span class="hljs-comment">// 编译后</span>
<span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fb0041</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">导入（Importing）</h4>
<p>可以导入别的less文件,也可以是css文件，导入后可以使用该文件的变量之类等等</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">import</span> '<span class="hljs-selector-tag">other</span><span class="hljs-selector-class">.less</span>'
<span class="hljs-selector-tag">import</span> '<span class="hljs-selector-tag">other</span><span class="hljs-selector-class">.css</span>'
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">注释（Comments）</h4>
<p>多行注释可以使用 <code>/**/</code>，单行注释可以使用<code>//</code></p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-comment">/*
多行注释
*/</span>

<span class="hljs-comment">// 单行注释</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">循环 (Loop)</h4>
<p>less没有现成的for循环，一般是用<code>when + 递归</code>实现；</p>
<pre><code class="hljs language-less copyable" lang="less">示例代码：
<span class="hljs-selector-class">.loop</span>(<span class="hljs-variable">@counter</span>) <span class="hljs-keyword">when</span> (<span class="hljs-variable">@counter</span> > <span class="hljs-number">0</span>) &#123;
  <span class="hljs-selector-class">.loop</span>((<span class="hljs-variable">@counter</span> - <span class="hljs-number">1</span>));    <span class="hljs-comment">// 下一次调用，直到@counter等于0</span>
  <span class="hljs-attribute">width</span>: (<span class="hljs-number">10px</span> * <span class="hljs-variable">@counter</span>); 
&#125;

<span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-selector-class">.loop</span>(<span class="hljs-number">5</span>); <span class="hljs-comment">// 调用，传参5</span>
&#125;

<span class="hljs-comment">// 编译后</span>
<span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">30px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">条件判断 (Condition)</h4>
<p>less 没有现成的<code>if else</code>，你可以使用 <code>when</code>,  如果需要可以结合<code>and</code> 或者 <code>not</code> 或者 <code>,</code>逗号运算符</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.width1</span>(<span class="hljs-variable">@width</span>) <span class="hljs-keyword">when</span> (<span class="hljs-variable">@width</span> > <span class="hljs-number">200px</span>) &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-variable">@width</span>;
    <span class="hljs-attribute">background</span>: yellow;
&#125;
<span class="hljs-comment">// and 都要满足</span>
<span class="hljs-selector-class">.width2</span>(<span class="hljs-variable">@width</span>) <span class="hljs-keyword">when</span> (<span class="hljs-variable">@width</span> > <span class="hljs-number">200px</span>)  <span class="hljs-keyword">and</span> (<span class="hljs-variable">@width</span> < <span class="hljs-number">400px</span>) &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-variable">@width</span>;
    <span class="hljs-attribute">background</span>: red;
&#125;
<span class="hljs-comment">// not 非运算，不用满足</span>
<span class="hljs-selector-class">.width3</span>(<span class="hljs-variable">@width</span>) <span class="hljs-keyword">when</span>  <span class="hljs-keyword">not</span> (<span class="hljs-variable">@width</span> > <span class="hljs-number">200px</span>)&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-variable">@width</span>;
    <span class="hljs-attribute">background</span>: blue;
&#125;
<span class="hljs-comment">// 逗号运算符 或运算，其中一个满足就行</span>
<span class="hljs-selector-class">.width4</span>(<span class="hljs-variable">@width</span>) <span class="hljs-keyword">when</span>  (<span class="hljs-variable">@width</span> > <span class="hljs-number">100px</span>), (<span class="hljs-variable">@width</span> > <span class="hljs-number">200px</span>)&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-variable">@width</span>;
    <span class="hljs-attribute">background</span>: green;
&#125;
<span class="hljs-selector-class">.div1</span> &#123;
  <span class="hljs-selector-class">.width1</span>(<span class="hljs-number">400px</span>);
&#125;
<span class="hljs-selector-class">.div2</span> &#123;
  <span class="hljs-selector-class">.width2</span>(<span class="hljs-number">300px</span>);
&#125;
<span class="hljs-selector-class">.div3</span> &#123;
 <span class="hljs-selector-class">.width3</span>(<span class="hljs-number">100px</span>);
&#125;
<span class="hljs-selector-class">.div4</span> &#123;
 <span class="hljs-selector-class">.width4</span>(<span class="hljs-number">150px</span>);
&#125;

<span class="hljs-comment">// 编译后</span>
<span class="hljs-selector-class">.div1</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
  <span class="hljs-attribute">background</span>: yellow;
&#125;
<span class="hljs-selector-class">.div2</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">background</span>: red;
&#125;
<span class="hljs-selector-class">.div3</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background</span>: blue;
&#125;
<span class="hljs-selector-class">.div4</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">150px</span>;
  <span class="hljs-attribute">background</span>: green;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">继承(extend)</h4>
<p><code>:extend</code>是一个伪类，可继承它所引用的选择器的样式，参数是<code>所要引用的选择器</code>；</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.a</span> &#123;
  <span class="hljs-attribute">color</span>: red;
  <span class="hljs-selector-class">.b</span> &#123;
    <span class="hljs-attribute">color</span>: green;
  &#125;
&#125;
<span class="hljs-selector-class">.c</span> &#123;
  <span class="hljs-selector-tag">&</span>:<span class="hljs-selector-tag">extend</span>(.a);
&#125;

<span class="hljs-comment">// 编译后</span>
<span class="hljs-comment">// a和c样式写在一起</span>
<span class="hljs-selector-class">.a</span>,
<span class="hljs-selector-class">.c</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-class">.a</span> <span class="hljs-selector-class">.b</span> &#123;
  <span class="hljs-attribute">color</span>: green;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">总结</h3>
<p>以上就是总结的常用的less语法，希望你们看了之后有所收获。</p></div>  
</div>
            