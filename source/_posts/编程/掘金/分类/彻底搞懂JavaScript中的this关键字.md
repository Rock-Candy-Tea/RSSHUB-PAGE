
---
title: '彻底搞懂JavaScript中的this关键字'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7009'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 23:02:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=7009'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文对JavaScript中的this关键字进行全方位的解析，看完本篇文章，希望读者们能够完全理解this的绑定问题。</p>
<p>开篇：对于那些没有投入时间去学习this机制的JavaScript开发者来说，this的绑定是一件令人困惑的事。（<strong>包括曾经的自己</strong>）。</p>
<p>误区：学习this的第一步是明白<strong>this既不指向函数本身也不指向函数的词法作用域</strong>，你是否被类似这样的解释所误导？但其实这种说法都是错误的。</p>
<p>概括：<strong>this实际是在函数被调用时发生的绑定，它所指向的位置完全取决于函数被调用的位置。</strong></p>
<h2 data-id="heading-0"><span class="prefix"></span><span class="content">一、调用位置</span><span class="suffix"></span></h2>
<p>在理解this的绑定过程之前，首先要理解调用位置：<strong>调用位置就是函数在代码中被调用的位置（而不是声明的位置）。</strong></p>
<p>所以说，寻找调用位置就是寻找“函数被调用的位置”，这里最重要的点是要分析<strong>调用栈（存放当前正在执行的函数的位置）</strong>。</p>
<p>什么是调用栈和调用位置？</p>
<p>关系：<strong>调用位置就在当前正在执行的函数（调用栈）的前一个位置</strong>。</p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">func1</span></span>() &#123;<br>  // 当前调用栈：func1<br>  // 当前调用位置是全局作用域（调用栈的前一个位置）<br>  console.log(<span class="hljs-string">'func1'</span>)<br>  func2() // 这里是：func2的调用位置<br>&#125;<br><br><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">func2</span></span>() &#123;<br>  // 当前调用栈：func1 -> func2<br>  // 当前调用位置是在func1（调用栈的前一个位置）<br>  console.log(<span class="hljs-string">'func2'</span>)<br>  func3() // 这里是：func3的调用位置<br>&#125;<br><br><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">func3</span></span>() &#123;<br>  // 当前调用栈：func1 -> func2 -> func3<br>  // 当前调用位置是在func2（调用栈的前一个位置）<br>  console.log(<span class="hljs-string">'func3'</span>)<br>&#125;<br><br>func1() // 这里是：func1的调用位置<br><span class="copy-code-btn">复制代码</span></code></pre>
<p>关注点：我们是如何从调用栈中分析出真正的调用位置的，<strong>因为这决定了this的绑定</strong>。</p>
<h2 data-id="heading-1"><span class="prefix"></span><span class="content">二、绑定规则</span><span class="suffix"></span></h2>
<ul>
<li>默认绑定</li></ul>
<p>最常用的函数调用类型：<strong>独立函数调用</strong></p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">getName</span></span>() &#123;<br>  console.log(this.name)<br>&#125;<br><br>var name = <span class="hljs-string">'kyrie'</span><br><br>getName() // <span class="hljs-string">'kyrie'</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p>当调用getName()时，this.name拿到了全局对象的name。因为getName()是直接调用的，不带任何修饰符，使用的是<strong>默认绑定</strong>，因此this指向全局对象（<strong>非严格模式</strong>）。</p>
<p>如果使用<strong>严格模式</strong>（'strict mode'）呢？</p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">getName</span></span>() &#123;<br>  <span class="hljs-string">'use strict'</span>;<br><br>  console.log(this.name)<br>&#125;<br><br>var name = <span class="hljs-string">'kyrie'</span><br><br>getName() // <span class="hljs-string">'TypeError: this is undefined'</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p>那么全局对象无法使用默认绑定，<strong>因此this会绑定到undefined</strong>。</p>
<ul>
<li>隐式绑定</li></ul>
<p>调用位置是否有<strong>上下文对象</strong></p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">getName</span></span>() &#123;<br>  console.log(this.name)<br>&#125;<br><br>var person = &#123;<br>  name: <span class="hljs-string">'kyrie'</span>,<br>  getName: getName<br>&#125;<br><br>person.getName() // <span class="hljs-string">'kyrie'</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p>当getName()被调用时，它的落脚点指向person对象，当函数引用有<strong>上下文对象</strong>时，<strong>隐式绑定</strong>会把函数调用中的this绑定到这个上下文对象，因此调用getName()时this被绑定到person，因此this.name跟person.name是一样的</p>
<p>常见问题：隐式丢失？</p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">getName</span></span>() &#123;<br>  console.log(this.name)<br>&#125;<br><br>var person = &#123;<br>  name: <span class="hljs-string">'kyrie'</span>,<br>  getName: getName<br>&#125;<br><br>var getName2 = person.getName() // 函数别名<br>var name = <span class="hljs-string">'wen'</span> // name是全局对象的属性<br>getName2() // <span class="hljs-string">'wen'</span> 这里拿到的是全局对象的name<br><span class="copy-code-btn">复制代码</span></code></pre>
<p>解释：虽然getName2是person.getName的一个<strong>函数引用</strong>，但它引用的getName函数的本身，因此getName2()调用时不带任何修饰符，使用的是<strong>默认绑定</strong>，因此this绑定了<strong>全局对象</strong>。</p>
<ul>
<li>显式绑定</li></ul>
<p>使用<strong>call()</strong> / <strong>apply()</strong> / <strong>bind()</strong> 指定this的绑定对象</p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">getName</span></span>() &#123;<br>  console.log(this.name)<br>&#125;<br><br>var person = &#123;<br>  name: <span class="hljs-string">'kyrie'</span><br>&#125;<br><br>getName.call(person) // <span class="hljs-string">'kyrie'</span><br><br>getName.apply(person) // <span class="hljs-string">'kyrie'</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p>通过getName.call()/ getName.apply() 调用强制把它的this绑定到person上。</p>
<ul>
<li>new绑定</li></ul>
<p>所有函数都可以用new来调用，这种函数调用称为<strong>构造函数调用</strong>。</p>
<p><strong>重点</strong>：实际上并不存在所谓的“构造函数”，只有对于<strong>函数的“构造调用”</strong>。</p>
<h5 data-id="heading-2"><span class="prefix"></span><span class="content">使用new来调用函数，或者说发生构造函数调用时，会自动执行以下的四步操作：</span><span class="suffix"></span></h5>
<ol>
<li><p>创建（或者构造）一个<strong>新的对象</strong></p>
</li><li><p>这个新对象会被执行[[原型]]连接（暂时忽略，属于原型内容，后面再介绍它）</p>
</li><li><p>这个新对象会<strong>绑定到函数调用的this</strong></p>
</li><li><p>如果函数没有返回其他对象，则new表达式中的函数会<strong>自动返回这个新的对象</strong></p>
</li></ol>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> setName(name) &#123;<br>  this.name = name<br>&#125;<br><br>var person = new setName(<span class="hljs-string">'kyrie'</span>)<br>console.log(person.name) // <span class="hljs-string">'kyrie'</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p>使用new调用setName()时，会创建<strong>一个新对象</strong>并把这个新对象<strong>绑定到setName()调用的this上</strong>，并把这个对象<strong>返回</strong>。</p>
<h2 data-id="heading-3"><span class="prefix"></span><span class="content">三、优先级</span><span class="suffix"></span></h2>
<p>毫无疑问，默认绑定的优先级是四条规则中最低的，所以暂不考虑它。</p>
<ol>
<li>隐式绑定和显式绑定哪个优先级高？</li></ol>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">getName</span></span>() &#123;<br>  console.log(this.name)<br>&#125;<br><br>var p1 = &#123;<br>  name: <span class="hljs-string">'kyrie'</span>,<br>  getName: getName<br>&#125;<br><br>var p2 = &#123;<br>  name: <span class="hljs-string">'wen'</span>,<br>  getName: getName<br>&#125;<br><br>p1.getName() // <span class="hljs-string">'kyrie'</span><br><br>p2.getName() // <span class="hljs-string">'wen'</span><br><br>p1.getName.call(p2) // <span class="hljs-string">'wen'</span><br><br>p2.getName.call(p1) // <span class="hljs-string">'kyrie'</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p>结果，<strong>显式绑定的优先级比隐式绑定高。</strong></p>
<ol start="2">
<li>隐式绑定和new绑定哪个优先级高？</li></ol>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> setName(name) &#123;<br>  this.name = name<br>&#125;<br><br>var p1 = &#123;<br>  setName: setName<br>&#125;<br><br>var p2 = &#123;&#125;<br><br>p1.setName(<span class="hljs-string">'kyrie'</span>)<br>console.log(p1.name) // <span class="hljs-string">'kyrie'</span><br><br>p1.setName.call(p2, <span class="hljs-string">'wen'</span>)<br>console.log(p2.name) // <span class="hljs-string">'wen'</span><br><br>var p3 = new p1.setName(<span class="hljs-string">'zbw'</span>)<br>console.log(p1.name) // <span class="hljs-string">'kyrie'</span><br>console.log(p3.name) // <span class="hljs-string">'zbw'</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p>结果，<strong>new绑定的优先级比隐式绑定高</strong></p>
<ol start="3">
<li>显式绑定和new绑定的哪个优先级高？</li></ol>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> setName(name) &#123;<br>  this.name = name<br>&#125;<br><br>var p1 = &#123;&#125;<br><br>// <span class="hljs-built_in">bind</span>会返回一个新的函数<br>var setP1Name = setName.bind(p1)<br>setP1Name(<span class="hljs-string">'kyrie'</span>)<br>console.log(p1.name) // <span class="hljs-string">'kyrie'</span><br><br>var p2 = new setP1Name(<span class="hljs-string">'wen'</span>)<br>console.log(p1.name) // <span class="hljs-string">'kyrie'</span><br>console.log(p2.name) // <span class="hljs-string">'wen'</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p>结果，<strong>new绑定的优先级比显示绑定高</strong></p>
<p>综上，优先级的正确排序：</p>
<p><strong>从高到低： new > 显示 > 隐式 > 默认</strong></p>
<ul>
<li>判断this的指向</li></ul>
<p>现在我们可以根据优先级来判断函数在某个位置调用this的指向。</p>
<ol>
<li>函数是否通过new来调用（new绑定）？如果是，则this指向新创建的对象</li></ol>
<pre class="custom"><span></span><code class="hljs copyable">var p1 = new Person()<br><span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>函数是否通过call/apply/bind调用（显式绑定）？如果是，则this指向第一个参数</li></ol>
<pre class="custom"><span></span><code class="hljs copyable">var p1 = setName.call(p2)<br><span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>函数是否在某个上下文对象中调用（隐式绑定）？如果是，则this指向该上下文对象</li></ol>
<pre class="custom"><span></span><code class="hljs copyable">var p2 = p1.setName()<br><span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>如果以上三个条件都不满足，则使用默认绑定。如果是在严格模式中，this指向undefined，否则指向全局对象。</li></ol>
<pre class="custom"><span></span><code class="hljs copyable">var p1 = setName()<br><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4"><span class="prefix"></span><span class="content">四、箭头函数的this</span><span class="suffix"></span></h2>
<p>以上上提到判断this指向的四条规则包含所有正常的函数，除了ES6中的<strong>箭头函数</strong>。</p>
<p>概括：箭头函数不像普通函数那样使用function关键字定义，而是用 <strong>“胖箭头” => 定义</strong> 。而且箭头函数并不适用以上的四条规则，它的this绑定完全是根据 <strong>外层作用域（函数或者全局）</strong> 来决定的。</p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">getName</span></span>() &#123;<br>  // 箭头函数的this指向外层作用域<br>  <span class="hljs-built_in">return</span> (name) => &#123;<br>    console.log(this.name)<br>  &#125;<br>&#125;<br><br>var p1 = &#123;<br>  name: <span class="hljs-string">'kyrie'</span><br>&#125;<br><br>var p2 = &#123;<br>  name: <span class="hljs-string">'wen'</span><br>&#125;<br><br>var func = getName.call(p1)<br>func.call(p2) // <span class="hljs-string">'kyrie'</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p>getName()内部创建的箭头函数会<strong>捕获调用时外层作用域（getName）的this</strong>，由于getName的this通过显示绑定到p1上，所以getName里创建的箭头函数也会指向p1，最重要的一点：<strong>箭头函数的this无法被修改</strong>（即使是<strong>优先级最高的new绑定也不行</strong>）</p>
<h2 data-id="heading-5"><span class="prefix"></span><span class="content">总结</span><span class="suffix"></span></h2>
<p>要判断一个运行中的函数的this绑定，需要找到该函数的调用位置（结合调用栈），接着根据优先级得出的四条规则来判断this的绑定对象。</p>
<ol>
<li><p>函数由new调用？绑定到新创建的对象</p>
</li><li><p>由call/apply/bind调用？绑定到指定对象</p>
</li><li><p>由上下文对象调用？绑定到上下文对象</p>
</li><li><p>默认：严格模式下绑定到undefined，否则绑定到全局对象</p>
</li></ol>
<p>ES6的箭头函数不适用以上四条规则，而是<strong>根据当前的词法作用域来决定this绑定</strong>，也就是说，箭头函数会<strong>继承外层函数调用的this绑定</strong>（无论绑定到什么），而且<strong>箭头函数的this绑定无法被修改</strong>。</p>
</div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            