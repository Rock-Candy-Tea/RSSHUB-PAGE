
---
title: 'es6的export和export default指令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9988'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 07:56:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=9988'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">前言</h3>
<p>上一篇<a href="https://juejin.cn/post/6995942854325436424" target="_blank" title="https://juejin.cn/post/6995942854325436424">文章</a>说了<code>CommonJS</code>规范的exports与module.exports的异同， 今天来讲讲es6新增的export和export default指令。</p>
<p>在一个模块内，内部声明的变量，函数，类等是无法在另外一个模块内访问到，如果需要访问，需要先通过<code>es6</code>提供的指令<code>export</code>,<code>export default</code>先导出， 然后再使用<code>import</code>导入使用。</p>
<blockquote>
<p>以下代码属于es6语法，如果需要node识别该文件是es6模块，需要你把文件命名为xxx.mjs</p>
</blockquote>
<p>如果你的node版本是低于<code>v13.2.0</code>，运行命令需要加上<code>--experimental-modules</code>， 否则会报错<code>Error [ERR_REQUIRE_ESM]: Must use import to load ES Module</code></p>
<pre><code class="hljs language-js copyable" lang="js">node --experimental-modules  xxx.mjs
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">export</h3>
<p>export，导出给外部的接口,可以是变量，函数，类等等。</p>
<p>使用如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a.mjs</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> name = <span class="hljs-string">'答案cp3'</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
&#125;

<span class="hljs-comment">// 导入的时候</span>
<span class="hljs-keyword">import</span> &#123;name, fn, A&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.mjs'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是导出的时候不能单单就是把一个值导出，这样会报错</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span>  name = <span class="hljs-string">'答案cp3'</span>
<span class="hljs-keyword">export</span> name <span class="hljs-comment">// 报错</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;
<span class="hljs-keyword">export</span> fn <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以换种写法，通过<code>&#123;&#125;</code>把导出给外部的接口和内部的变量关联起来。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> name = <span class="hljs-string">'答案cp3'</span>
<span class="hljs-keyword">export</span> &#123; name &#125; 

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;
<span class="hljs-keyword">export</span> &#123;fn&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>export 还可以使用<code>as</code>重命名</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a.mjs</span>
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'答案cp3'</span>
<span class="hljs-keyword">export</span> &#123; name <span class="hljs-keyword">as</span> newName &#125; <span class="hljs-comment">// 重命名为newName</span>

<span class="hljs-comment">// 导入的时候</span>
<span class="hljs-keyword">import</span> &#123; newName &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.mjs'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">export default</h3>
<p>export default指令，默认导出，在导入模块的时候无需写<code>&#123;&#125;</code>, 可以取任何名字，这个名字代表的是<strong>默认导出</strong>。</p>
<p>使用如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a.mjs</span>
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'答案cp3'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> name

<span class="hljs-comment">// 导入的时候 anyName可以是任何名字</span>
<span class="hljs-keyword">import</span> anyName <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.mjs'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个例子，你可以会好奇，为啥 <code>export default</code>可以导出一个变量值？</p>
<p>这是因为<code>export default</code>本质上是导出一个属性为<code>default</code>的变量，你可以给这个属性赋值，变量值，函数名都可以。</p>
<p>但是跟export那种不一样,它可以把一个值导出</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">var</span> name = <span class="hljs-string">'答案cp3'</span> <span class="hljs-comment">// 报错</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> fn <span class="hljs-comment">// 正确</span>

<span class="hljs-keyword">var</span> name = <span class="hljs-string">'答案cp3'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> name
<span class="hljs-comment">// 等同于</span>
<span class="hljs-keyword">export</span> &#123;name <span class="hljs-keyword">as</span> <span class="hljs-keyword">default</span>&#125;

<span class="hljs-comment">// 导入的时候 </span>
<span class="hljs-keyword">import</span> name <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.mjs'</span>

<span class="hljs-comment">// 等同于</span>
<span class="hljs-keyword">import</span> &#123;<span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> name&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.mjs'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外， <code>export default</code>一个模块只能使用一次，相当于<code>default</code>是一个常量，不能重复赋值。</p>
<h3 data-id="heading-3">import</h3>
<p>上面提过，模块是<code>export</code>,<code>export default</code>先导出， 然后再使用<code>import</code>导入使用</p>
<p>它一般是配合<code>export</code>，<code>export default</code>一起使用。 如果是使用<code>export</code>，<code>import</code> 需要使用<code>&#123;&#125;</code>, 如果是<code>export default</code>, 则无需写<code>&#123;&#125;</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a.mjs</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> name = <span class="hljs-string">'答案cp3'</span>
<span class="hljs-keyword">var</span> age = <span class="hljs-number">18</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> age

<span class="hljs-comment">// 导入</span>
<span class="hljs-keyword">import</span> age, &#123;name&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.mjs'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后 import也可以使用<code>as</code>重命名，以上面代码为例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> age, &#123; name <span class="hljs-keyword">as</span> name1 &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.mjs'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>age那个就不能重命名了，因为你想取别的名都可以取</p>
<p>name重命名之后name就不能用了</p>
<p>import导入都变量都是常量，一般都不能改（也不建议改）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> age, &#123; name <span class="hljs-keyword">as</span> name1 &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.mjs'</span>

age = <span class="hljs-number">17</span> <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还可以使用<code>*</code>来代表整个导出对象, 它一般是配合<code>as</code>重命名一起使用</p>
<p>以上面例子继续：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> info <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.mjs'</span>
<span class="hljs-built_in">console</span>.log(info) <span class="hljs-comment">// &#123; default: 18, name: '答案cp3' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">总结</h3>
<p>以上就是我总结的关于es6的export和export default指令，以上代码希望大家有时间都能敲一下，加深印象。</p>
<p>感谢你们的阅读。</p></div>  
</div>
            