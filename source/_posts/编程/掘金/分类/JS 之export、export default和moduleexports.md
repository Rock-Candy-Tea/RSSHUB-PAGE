
---
title: 'JS 之export、export default和module.exports'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3036'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 21:58:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=3036'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>export</strong>和<strong>export</strong> <strong>default</strong>是ES6中导出模块中变量的语法</p>
<p><strong>exports</strong>和<strong>module</strong>.<strong>exports</strong>是Nodejs中导出模块中变量的语法（基于CommonJs语法规范）</p>
<p><strong>【export】</strong>-- 命名导出</p>
<p>在创建JavaScript模块时，<strong>export</strong> 语句用于从模块中导出实时绑定的函数、对象或原始值，以便其他程序可以通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fimport" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/import" ref="nofollow noopener noreferrer"><code>import</code></a> 语句使用它们。被导出的绑定值依然可以在本地进行修改。在使用import进行导入时，这些绑定值只能被导入模块所读取，但在export导出模块中对这些绑定值进行修改，所修改的值也会实时地更新。</p>
<p>【语法】</p>
<ol>
<li>
<p>命名导出（每个模块包含任意数量）</p>
</li>
<li>
<p>默认导出（每个模块包含一个）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导出单个特性</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> name1, name2, …, nameN; <span class="hljs-comment">// also var, const</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> name1 = …, name2 = …, …, nameN; <span class="hljs-comment">// also var, const</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FunctionName</span>(<span class="hljs-params"></span>)</span>&#123;...&#125;
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClassName</span> </span>&#123;...&#125;

<span class="hljs-comment">// 导出列表</span>
<span class="hljs-keyword">export</span> &#123; name1, name2, …, nameN &#125;;

<span class="hljs-comment">// 重命名导出</span>
<span class="hljs-keyword">export</span> &#123; variable1 <span class="hljs-keyword">as</span> name1, variable2 <span class="hljs-keyword">as</span> name2, …, nameN &#125;;

<span class="hljs-comment">// 解构导出并重命名</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> &#123; name1, <span class="hljs-attr">name2</span>: bar &#125; = o;

<span class="hljs-comment">// 默认导出</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> expression;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">…</span>) </span>&#123; … &#125; <span class="hljs-comment">// also class, function*</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">name1</span>(<span class="hljs-params">…</span>) </span>&#123; … &#125; <span class="hljs-comment">// also class, function*</span>
<span class="hljs-keyword">export</span> &#123; name1 <span class="hljs-keyword">as</span> <span class="hljs-keyword">default</span>, … &#125;;

<span class="hljs-comment">// 导出模块合集</span>
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> …; <span class="hljs-comment">// does not set the default export</span>
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">as</span> name1 <span class="hljs-keyword">from</span> …; <span class="hljs-comment">// Draft ECMAScript® 2O21</span>
<span class="hljs-keyword">export</span> &#123; name1, name2, …, nameN &#125; <span class="hljs-keyword">from</span> …;
<span class="hljs-keyword">export</span> &#123; import1 <span class="hljs-keyword">as</span> name1, import2 <span class="hljs-keyword">as</span> name2, …, nameN &#125; <span class="hljs-keyword">from</span> …;
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> &#125; <span class="hljs-keyword">from</span> …;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p><strong>【export</strong> <strong>default】</strong> -- 默认导出</p>
<p>两种不同的导出方式，命名导出（export）和默认导出（export default）。能够在每一个模块中定义多个命名导出，但是只允许有一个默认导出。每种方式对应于上述的一种语法：</p>
<p>命名导出：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导出事先定义的特性</span>
<span class="hljs-keyword">export</span> &#123; myFunction，myVariable &#125;;

<span class="hljs-comment">// 导出单个特性（可以导出var，let，</span>
<span class="hljs-comment">//const,function,class）</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> myVariable = <span class="hljs-built_in">Math</span>.sqrt(<span class="hljs-number">2</span>);
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFunction</span>(<span class="hljs-params"></span>) </span>&#123; ... &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认导出：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导出事先定义的特性作为默认值</span>
<span class="hljs-keyword">export</span> &#123; myFunction <span class="hljs-keyword">as</span> <span class="hljs-keyword">default</span> &#125;;

<span class="hljs-comment">// 导出单个特性作为默认值</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; ... &#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123; .. &#125;

<span class="hljs-comment">// 每个导出都覆盖前一个导出</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在导出多个值时，命名导出非常有用。在导入期间，必须使用相应对象的相同名称。</p>
<p>但是，可以使用任何名称导入默认导出，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 文件 test.js</span>
<span class="hljs-keyword">let</span> k; 
<span class="hljs-comment">// 导出</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> k = <span class="hljs-number">12</span>; 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 另一个文件</span>
<span class="hljs-keyword">import</span> m <span class="hljs-keyword">from</span> <span class="hljs-string">'./test'</span>; <span class="hljs-comment">// 由于 k 是默认导出，所以可以自由使用 import m 替代 import k</span>
<span class="hljs-built_in">console</span>.log(m);        <span class="hljs-comment">// 输出为 12 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以重命名命名导出以避免命名冲突：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> &#123; 
myFunction <span class="hljs-keyword">as</span> function1,
    myVariable <span class="hljs-keyword">as</span> variable 
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>【示列】</strong></p>
<p>1.命名导出 -- 列1</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//lib.js</span>
<span class="hljs-comment">//导出常量</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> sqrt = <span class="hljs-built_in">Math</span>.sqrt;
<span class="hljs-comment">//导出函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">square</span>(<span class="hljs-params">x</span>) </span>&#123;
    <span class="hljs-keyword">return</span> x * x;
&#125;
<span class="hljs-comment">//导出函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">diag</span>(<span class="hljs-params">x, y</span>) </span>&#123;
    <span class="hljs-keyword">return</span> sqrt(square(x) + square(y));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//main.js</span>
<span class="hljs-keyword">import</span> &#123; square, diag &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./lib'</span>;
<span class="hljs-built_in">console</span>.log(square(<span class="hljs-number">11</span>)); <span class="hljs-comment">// 121</span>
<span class="hljs-built_in">console</span>.log(diag(<span class="hljs-number">4</span>, <span class="hljs-number">3</span>)); <span class="hljs-comment">// 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.命名导出 -- 列2</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// module "my-module.js"</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cube</span>(<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x * x * x;
&#125;

<span class="hljs-keyword">const</span> foo = <span class="hljs-built_in">Math</span>.PI + <span class="hljs-built_in">Math</span>.SQRT2;

<span class="hljs-keyword">var</span> graph = &#123;
    <span class="hljs-attr">options</span>: &#123;
        <span class="hljs-attr">color</span>:<span class="hljs-string">'white'</span>,
        <span class="hljs-attr">thickness</span>:<span class="hljs-string">'2px'</span>
    &#125;,
    <span class="hljs-attr">draw</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'From graph draw function'</span>);
    &#125;
&#125;

<span class="hljs-keyword">export</span> &#123; cube, foo, graph &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; cube, foo, graph &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'my-module.js'</span>;

graph.options = &#123;
    <span class="hljs-attr">color</span>:<span class="hljs-string">'blue'</span>,
    <span class="hljs-attr">thickness</span>:<span class="hljs-string">'3px'</span>
&#125;;

graph.draw();
<span class="hljs-built_in">console</span>.log(cube(<span class="hljs-number">3</span>)); <span class="hljs-comment">// 27</span>
<span class="hljs-built_in">console</span>.log(foo);    <span class="hljs-comment">// 4.555806215962888</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.默认导出 -- 列3</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// module "my-module.js"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cube</span>(<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x * x * x;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> cube <span class="hljs-keyword">from</span> <span class="hljs-string">'./my-module.js'</span>;
<span class="hljs-built_in">console</span>.log(cube(<span class="hljs-number">3</span>)); <span class="hljs-comment">// 27</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.默认导出 -- 列4</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// module "my-module.js"</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handlerHexDisplay</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-keyword">return</span> data;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sendCommand</span>(<span class="hljs-params">address,command</span>) </span>&#123;
    <span class="hljs-keyword">return</span> address+command;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;sendCommand , openCom&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> cube <span class="hljs-keyword">from</span> <span class="hljs-string">'./my-module.js'</span>;
cosole.log(cube.sendCommand(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>))
cosole.log(cube.openCom(<span class="hljs-number">10</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>【module.exports】</strong></p>
<p>Node应用由模块组成，采用CommonJS模块规范。根据这个规范，每个文件就是一个模块，有自己的作用域。在一个文件里面定义的变量、函数、类，都是私有的，对其他文件不可见。CommonJS规范规定，每个模块内部，<code>module变量代表当前模块。这个变量是一个对象</code>，它的exports属性（即module.exports）是对外的接口。加载某个模块，其实是加载该模块的module.exports属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clear</span>(<span class="hljs-params"></span>) </span>&#123;
  uni.clearStorageSync();
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-attr">clear</span>:clear,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码通过module.exports输出函数 clear</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> example = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./example.js'</span>); <span class="hljs-comment">// 导入方法一</span>
<span class="hljs-keyword">import</span> example <span class="hljs-keyword">from</span> <span class="hljs-string">'./example.js'</span><span class="hljs-comment">// 导入方法二</span>
<span class="hljs-built_in">console</span>.log(example.x);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>【示列】</strong></p>
<ol>
<li>列1</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// common.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">functA</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">functB</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'2'</span>)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">functC</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'3'</span>)
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-attr">functA</span>:functA,
      <span class="hljs-attr">functB</span>:functB,
      <span class="hljs-attr">functC</span>:functC
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/common.js'</span>;
<span class="hljs-built_in">console</span>.log(common.functA);
<span class="hljs-built_in">console</span>.log(common.functB);
<span class="hljs-built_in">console</span>.log(common.functC);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>列2   -  返回一个JSON Object</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> app = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'app'</span>,
    <span class="hljs-attr">version</span>: <span class="hljs-string">'1.0.0'</span>,
    <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = app;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方法可以返回全局共享的变量或者方法。
调用方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> app = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./app.js'</span>);
app.sayName(<span class="hljs-string">'hello'</span>);<span class="hljs-comment">//hello</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>列3   -  返回一个构造函数</li>
</ol>
<p>CLASS.js:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> CLASS = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">args</span>)</span>&#123;
     <span class="hljs-built_in">this</span>.args = args;
&#125;
<span class="hljs-built_in">module</span>.exports = CLASS;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> CLASS = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./CLASS.js'</span>);
varc = <span class="hljs-keyword">new</span> CLASS(<span class="hljs-string">'arguments'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>列3   -  返回一个实例对象</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//CLASS.js</span>
<span class="hljs-keyword">var</span> CLASS = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">"class"</span>;
&#125;
CLASS .prototype.func = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    alert(<span class="hljs-built_in">this</span>.name);
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CLASS();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> c = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./CLASS.js'</span>);
c.func();<span class="hljs-comment">//"class"</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            