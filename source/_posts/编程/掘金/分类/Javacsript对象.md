
---
title: 'Javacsript对象'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7c8cca868f6406bba2e86ca4c3a4199~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 22:45:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7c8cca868f6406bba2e86ca4c3a4199~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a name="user-content-Cx5s5" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-0">概述</h3>
<p>对象中包含一系列属性，这些属性是无序的。每个属性都有一个字符串key和对应的value。属性名可以是包含空字符串在内的任意字符串，对象中不能存在两个同名的属性。值可以是任意javascript值，或者可以是一个getter或setter函数。除了名字和值之外，每个属性还有一些与之相关的值，称为“属性特性”；除了包含属性之外，每个对象还拥有3个相关的对象特性，如下图所示：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7c8cca868f6406bba2e86ca4c3a4199~tplv-k3u1fbpfcp-zoom-1.image" alt="屏幕快照 2021-06-13 下午3.01.52.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-YCLly" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-1">创建对象</h3>
<p>可以通过对象直接量、关键字new和Object.create()函数来创建对象。
<a name="user-content-lxrkr" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-2">对象直接量</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj1 = &#123;<span class="hljs-attr">x</span>:<span class="hljs-number">1</span>, <span class="hljs-attr">y</span>:<span class="hljs-number">2</span>&#125;; 
<span class="hljs-keyword">let</span> obj2 = &#123; 
  <span class="hljs-attr">x</span>:<span class="hljs-number">1</span>,
  <span class="hljs-attr">y</span>:<span class="hljs-number">2</span>,
  <span class="hljs-attr">z</span>: &#123; 
    <span class="hljs-attr">m</span>:<span class="hljs-string">'a'</span>,
    <span class="hljs-attr">n</span>:<span class="hljs-string">'b'</span>
  &#125;
&#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-S7Icp" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-3">关键字new创建对象（原型链）</h4>
<p>new运算符创建并初始化一个新对象。关键字new后面跟随一个函数调用。这里的函数称做构造函数，构造函数用以初始化一个新创建的对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
foo.prototype.z = <span class="hljs-number">3</span>;

<span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> foo();
obj.y = <span class="hljs-number">2</span>;
obj.x = <span class="hljs-number">1</span>;

obj.x; <span class="hljs-comment">// 1</span>
obj.y; <span class="hljs-comment">// 2</span>
obj.z; <span class="hljs-comment">// 3</span>
<span class="hljs-keyword">typeof</span> obj.toString; <span class="hljs-comment">// ‘function'</span>
<span class="hljs-string">'z'</span> <span class="hljs-keyword">in</span> obj; <span class="hljs-comment">// true</span>
obj.hasOwnProperty(<span class="hljs-string">'z'</span>); <span class="hljs-comment">// false</span>

obj.z = <span class="hljs-number">5</span>;

obj.hasOwnProperty(<span class="hljs-string">'z'</span>); <span class="hljs-comment">// true</span>
foo.prototype.z; <span class="hljs-comment">// still 3</span>
obj.z; <span class="hljs-comment">// 5</span>

obj.z = <span class="hljs-literal">undefined</span>;
obj.z; <span class="hljs-comment">// undefined</span>

<span class="hljs-keyword">delete</span> obj.z; <span class="hljs-comment">// true</span>
obj.z; <span class="hljs-comment">// 3</span>

<span class="hljs-keyword">delete</span> obj.z; <span class="hljs-comment">// true</span>
obj.z; <span class="hljs-comment">// still 3!!!</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/750342fdfb7042179a61ae284880f5fb~tplv-k3u1fbpfcp-zoom-1.image" alt="屏幕快照 2021-06-13 下午3.02.39.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-cPjFN" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-4">Object.create()</h4>
<p>Object.create()创建一个新对象，其中第一个参数是这个对象的原型，第二个参数可选，用以对对象的属性进行进一步描述。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj = <span class="hljs-built_in">Object</span>.create(&#123;<span class="hljs-attr">x</span>:<span class="hljs-number">1</span>, <span class="hljs-attr">y</span>:<span class="hljs-number">2</span>&#125;); <span class="hljs-comment">// obj继承了属性x和y</span>

obj.x <span class="hljs-comment">// 1</span>
<span class="hljs-keyword">typeof</span> obj.toString <span class="hljs-comment">// "function"</span>
obj.hasOwnProperty(<span class="hljs-string">'x'</span>) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ce92cca0072490db5c9a16e91b7a943~tplv-k3u1fbpfcp-zoom-1.image" alt="屏幕快照 2021-06-12 下午9.40.00.png" loading="lazy" referrerpolicy="no-referrer"><br>可以通过传入参数null来创建一个没有原型的新对象，但是通过这种方式创建的对象不会集成任何东西，甚至不包括基础方法，比如toString()，也就是说，它将不能和'+'运算符一起正常工作。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>); 

obj.toString <span class="hljs-comment">// undefined </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f849d62c0394234bcf606b781e83759~tplv-k3u1fbpfcp-zoom-1.image" alt="屏幕快照 2021-06-12 下午9.43.44.png" loading="lazy" referrerpolicy="no-referrer"><br>如果想创建一个普通的空对象（比如通过&#123;&#125;或new Object()创建的对象）,需要传入Object.prototype:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj = <span class="hljs-built_in">Object</span>.create(<span class="hljs-built_in">Object</span>.prototype); <span class="hljs-comment">// obj和&#123;&#125;和new Object()一样 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-CEXV8" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-5">属性操作</h3>
<p><a name="user-content-kSUhY" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-6">属性的查询与设置（读写属性）</h4>
<ul>
<li>可以通过（.）或方括号（[]）运算符来获取属性的值或者给属性赋值。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj = &#123;<span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span>&#125;;

obj.x; <span class="hljs-comment">// 1</span>
obj[<span class="hljs-string">"y"</span>]; <span class="hljs-comment">// 2</span>

obj[<span class="hljs-string">"x"</span>] = <span class="hljs-number">3</span>;
obj.y = <span class="hljs-number">4</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>javascript对象具有“自有属性”，也有一些属性是从原型对象继承而来。假设要查询对象o的属性x，如果o中不存在x，那么将会继续在o的原型对象中查询属性x。如果原型对象中也没有x，但这个原型对象也有原型，那么继续在这个原型对象的原型上执行查询，直到找到x或者找到一个原型是null的对象为止。可以看到，对象的原型构成了一个“链”，通过这个“链”可以实现属性的继承。</li>
<li>现在假设给对象o的属性x赋值，如果o中已经有属性x(这个属性不是继承而来的），那么这个赋值操作只改变这个已有属性的值。如果o中不存在属性x，那么赋值操作给o添加一个新属性x。如果之前o继承自属性x，那么这个继承的属性就被新创建的同名属性覆盖。</li>
<li>属性赋值操作首先检查原型链，以此判定是否允许赋值操作。例如，如果o继承自一个只读属性x，那么赋值操作是不允许的。如果允许属性赋值操作，它也总是在原始对象上创建属性或对已有的属性赋值，而不会去修改原型链。</li>
<li>在javascript中，只有查询属性才会体会到继承的存在，而设置属性则和继承无关。</li>
<li>如果o继承自属性x，而这个属性是一个具有setter方法的accessor属性，那么这时将调用setter方法而不是给o创建一个属性x。需要注意的是，setter方法是由对象o调用的，而不是定义这个属性的原型对象调用的。因为如果setter方法定义任意属性，这个操作只针对o本身，并不会修改原型链。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-built_in">Object</span>.defineProperty(foo.prototype, <span class="hljs-string">'z'</span>, &#123;
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
       <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
    &#125;
&#125;);

<span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> foo();

obj.z; <span class="hljs-comment">// 1</span>
obj.z = <span class="hljs-number">10</span>; <span class="hljs-comment">// obj继承自属性z，而这个属性如果存在get/set方法，给当前对象赋值会失败。</span>
obj.z; <span class="hljs-comment">// still 1</span>

<span class="hljs-built_in">Object</span>.defineProperty(obj, <span class="hljs-string">'z'</span>, &#123;<span class="hljs-attr">value</span> : <span class="hljs-number">100</span>, <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>&#125;); 
<span class="hljs-comment">// 此时如果想给当前对象添加新属性z，只能通过defineProperty方式</span>
obj.z; <span class="hljs-comment">// 100;</span>
<span class="hljs-keyword">delete</span> obj.z;
obj.z; <span class="hljs-comment">// back to 1</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36bdb14ba535460eae2f909c4f6c92c1~tplv-k3u1fbpfcp-zoom-1.image" alt="屏幕快照 2021-06-13 下午3.03.19.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> o = &#123;&#125;;
<span class="hljs-built_in">Object</span>.defineProperty(o, <span class="hljs-string">'x'</span>, &#123;<span class="hljs-attr">value</span> : <span class="hljs-number">1</span>&#125;); <span class="hljs-comment">// writable=false, configurable=false</span>
<span class="hljs-keyword">var</span> obj = <span class="hljs-built_in">Object</span>.create(o);
obj.x; <span class="hljs-comment">// 1</span>
obj.x = <span class="hljs-number">200</span>; <span class="hljs-comment">// writable为false不可写，赋值失败</span>
obj.x; <span class="hljs-comment">// still 1, can't change it</span>

<span class="hljs-built_in">Object</span>.defineProperty(obj, <span class="hljs-string">'x'</span>, &#123;<span class="hljs-attr">writable</span>:<span class="hljs-literal">true</span>, <span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>, <span class="hljs-attr">value</span> : <span class="hljs-number">100</span>&#125;);
obj.x; <span class="hljs-comment">// 100</span>
obj.x = <span class="hljs-number">500</span>;
obj.x; <span class="hljs-comment">// 500</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-C4GxP" href="https://juejin.cn/post/undefined"></a>
<a name="user-content-fzikb" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-7">删除属性</h4>
<ul>
<li>delete运算只能删除自有属性，不能删除继承属性（要删除继承属性必须从定义这个属性的原型对象上删除它，而且这会影响到所有继承自这个原型的对象）。</li>
<li>当delete表达式删除成功或没有任何副作用（比如删除不存在的属性）时，它返回true。如果delete后不是一个属性访问表达式，delete同样返回true。</li>
<li>delete不能删除那些可配置性为false的属性。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> person = &#123;<span class="hljs-attr">age</span> : <span class="hljs-number">28</span>, <span class="hljs-attr">title</span> : <span class="hljs-string">'fe'</span>&#125;;
<span class="hljs-keyword">delete</span> person.age; <span class="hljs-comment">// 删除属性age，返回true</span>
<span class="hljs-keyword">delete</span> person[<span class="hljs-string">'title'</span>]; <span class="hljs-comment">// 删除属性title，返回true</span>
person.age; <span class="hljs-comment">// undefined</span>
<span class="hljs-keyword">delete</span> person.age; <span class="hljs-comment">// 什么都没做（age属性已经不存在了），返回true</span>
<span class="hljs-keyword">delete</span> person.gender; <span class="hljs-comment">// 什么都没做（gender属性不存在），返回true</span>
<span class="hljs-keyword">delete</span> person.toString; <span class="hljs-comment">// 什么都没做（toString是继承而来的），返回true</span>
<span class="hljs-keyword">delete</span> <span class="hljs-number">1</span>; <span class="hljs-comment">// 无意义，返回true</span>

<span class="hljs-keyword">delete</span> <span class="hljs-built_in">Object</span>.prototype; <span class="hljs-comment">// false, 属性是不可配置</span>

<span class="hljs-keyword">var</span> descriptor = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(<span class="hljs-built_in">Object</span>, <span class="hljs-string">'prototype'</span>);
descriptor.configurable; <span class="hljs-comment">// false</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-BUNl5" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-8">检测属性</h4>
<p>javascript对象可以看做属性的集合，我们经常会检测集合中成员的所属关系——判断某个属性是否存在于摸个对象中。可以通过in运算符、hasOwnProperty()和propertyIsEnumerable()方法来完成这个工作。</p>
<ul>
<li>in运算符的左侧是属性名，右侧是对象。如果对象自有属性或继承属性中包含这个属性则返回true；</li>
<li>对象的hasOwnProperty()方法用来检测给定的名字是否是对象的自有属性，对于继承属性返回fasle。</li>
<li>propertyIsEnumerable是hasOwnProperty()的增强版，只有检测是自有属性且这个属性的可枚举性为true时它才返回true。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> cat = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>;
cat.legs = <span class="hljs-number">4</span>;
cat.name = <span class="hljs-string">"Kitty"</span>;

<span class="hljs-string">'legs'</span> <span class="hljs-keyword">in</span> cat; <span class="hljs-comment">// true</span>
<span class="hljs-string">'abc'</span> <span class="hljs-keyword">in</span> cat; <span class="hljs-comment">// false</span>
<span class="hljs-string">"toString"</span> <span class="hljs-keyword">in</span> cat; <span class="hljs-comment">// true, inherited property!!!</span>

cat.hasOwnProperty(<span class="hljs-string">'legs'</span>); <span class="hljs-comment">// true</span>
cat.hasOwnProperty(<span class="hljs-string">'toString'</span>); <span class="hljs-comment">// false</span>

cat.propertyIsEnumerable(<span class="hljs-string">'legs'</span>); <span class="hljs-comment">// true</span>
cat.propertyIsEnumerable(<span class="hljs-string">'toString'</span>); <span class="hljs-comment">// false</span>

<span class="hljs-built_in">Object</span>.defineProperty(cat, <span class="hljs-string">'price'</span>, &#123;<span class="hljs-attr">enumerable</span> : <span class="hljs-literal">false</span>, <span class="hljs-attr">value</span> : <span class="hljs-number">1000</span>&#125;);
cat.propertyIsEnumerable(<span class="hljs-string">'price'</span>); <span class="hljs-comment">// false</span>
cat.hasOwnProperty(<span class="hljs-string">'price'</span>); <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-MRyqJ" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-9">枚举属性</h4>
<p>除了检测对象的属性是否存在，我们还会经常遍历对象的属性。</p>













































<table><thead><tr><th><strong>类型</strong></th><th><strong>特点</strong></th></tr></thead><tbody><tr><td>Object.keys(obj)</td><td>返回对象本身可直接枚举的属性(不含Symbol属性）</td></tr><tr><td>Object.values(obj)</td><td>返回对象本身可直接枚举的属性值(不含Symbol属性）</td></tr><tr><td>Object.entries(obj)</td><td>返回对象本身可枚举属性键值对相对应的数组(不含Symbol属性）</td></tr><tr><td>Object.getOwnPropertyNames(obj)</td><td>返回对象所有自身属性的属性名（不包括Symbol值作为名称的属性）</td></tr><tr><td>Object.getOwnPropertySymbols(obj)</td><td>返回一个给定对象自身的所有 Symbol 属性的数组</td></tr><tr><td>for……in</td><td>所有可枚举的属性（包括原型上的）</td></tr><tr><td>for……of</td><td>必须部署了Iterator接口后才能使用，例如数组、Set和Map结构、类数组对象、Generator对象以及字符串</td></tr><tr><td>forEach</td><td>break不能中断循环</td></tr><tr><td>Reflect.ownKeys(obj)</td><td>对象自身所有属性</td></tr></tbody></table>
<p><a href="https://mp.weixin.qq.com/s/QdwfGIKo206CHceGw_9l0Q" target="_blank" rel="nofollow noopener noreferrer"> </a>上述遍历对象的属性时都遵循同样的属性遍历次序规则：</p>
<ol>
<li>首先遍历所有属性名为数值的属性，按照数字排序</li>
<li>其次遍历所有属性名为字符串的属性，按照生成时间排序</li>
<li>最后遍历所有属性名为Symbol值的属性，按照生成时间排序</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Obj = &#123;
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-number">0</span>)]: <span class="hljs-string">'symbol'</span>,
    <span class="hljs-number">1</span> : <span class="hljs-string">'1'</span>,
    <span class="hljs-string">'c'</span>: <span class="hljs-string">'c'</span>,
    <span class="hljs-string">'1a1'</span>: <span class="hljs-string">'11'</span>,
    <span class="hljs-number">22223333</span>: <span class="hljs-string">'2'</span>,
    <span class="hljs-string">'d'</span>: <span class="hljs-string">'d'</span>
&#125;;

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Reflect</span>.ownKeys(Obj)); <span class="hljs-comment">// [ '1', '22223333', 'c', '1a1', 'd', Symbol(0) ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-cEClA" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-10">getter、setter</h3>
<p>另一种读写属性的方式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> man = &#123;
    <span class="hljs-attr">name</span> : <span class="hljs-string">'Bosn'</span>,
    <span class="hljs-attr">weibo</span> : <span class="hljs-string">'@Bosn'</span>,
    <span class="hljs-keyword">get</span> <span class="hljs-title">age</span>() &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getFullYear() - <span class="hljs-number">1988</span>;
    &#125;,
    <span class="hljs-keyword">set</span> <span class="hljs-title">age</span>(<span class="hljs-params">val</span>) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Age can\'t be set to '</span> + val);
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(man.age); <span class="hljs-comment">// 27</span>
man.age = <span class="hljs-number">100</span>; <span class="hljs-comment">// Age can't be set to 100</span>
<span class="hljs-built_in">console</span>.log(man.age); <span class="hljs-comment">// still 27</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-xrmnb" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-11">属性标签</h3>
<ul>
<li>可写(writable)：表明是否可以设置该属性的值。</li>
<li>可枚举(enumerable)：表明是否可以通过for/in循环返回该属性。</li>
<li>可配置(configurable)：表明是否可以删除或修改该属性。</li>
</ul>
<ol>
<li>数据属性：value、writable、enumerable、configurable</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(&#123;<span class="hljs-attr">pro</span> : <span class="hljs-literal">true</span>&#125;, <span class="hljs-string">'pro'</span>);
<span class="hljs-comment">// Object &#123;value: true, writable: true, enumerable: true, configurable: true&#125;</span>
<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(&#123;<span class="hljs-attr">pro</span> : <span class="hljs-literal">true</span>&#125;, <span class="hljs-string">'a'</span>); <span class="hljs-comment">// undefined</span>

<span class="hljs-keyword">var</span> person = &#123;&#125;;
<span class="hljs-built_in">Object</span>.defineProperty(person, <span class="hljs-string">'name'</span>, &#123;
    <span class="hljs-attr">configurable</span> : <span class="hljs-literal">false</span>,
    <span class="hljs-attr">writable</span> : <span class="hljs-literal">false</span>,
    <span class="hljs-attr">enumerable</span> : <span class="hljs-literal">true</span>,
    <span class="hljs-attr">value</span> : <span class="hljs-string">"Bosn Ma"</span>
&#125;);

person.name; <span class="hljs-comment">// Bosn Ma</span>
person.name = <span class="hljs-number">1</span>; <span class="hljs-comment">// writable为fasle，赋值失败</span>
person.name; <span class="hljs-comment">// still Bosn Ma</span>
<span class="hljs-keyword">delete</span> person.name; <span class="hljs-comment">// false，// configurable为fasle，删除失败</span>

<span class="hljs-built_in">Object</span>.defineProperty(person, <span class="hljs-string">'type'</span>, &#123;
    <span class="hljs-attr">configurable</span> : <span class="hljs-literal">true</span>,
    <span class="hljs-attr">writable</span> : <span class="hljs-literal">true</span>,
    <span class="hljs-attr">enumerable</span> : <span class="hljs-literal">false</span>,
    <span class="hljs-attr">value</span> : <span class="hljs-string">"Object"</span>
&#125;);

<span class="hljs-built_in">Object</span>.keys(person); <span class="hljs-comment">// ["name"]，name的enumerable为true, type的enumerable为false</span>

<span class="hljs-built_in">Object</span>.defineProperties(person, &#123;
    <span class="hljs-attr">title</span> : &#123;<span class="hljs-attr">value</span> : <span class="hljs-string">'fe'</span>, <span class="hljs-attr">enumerable</span> : <span class="hljs-literal">true</span>&#125;,
    <span class="hljs-attr">corp</span> : &#123;<span class="hljs-attr">value</span> : <span class="hljs-string">'BABA'</span>, <span class="hljs-attr">enumerable</span> : <span class="hljs-literal">true</span>&#125;,
    <span class="hljs-attr">salary</span> : &#123;<span class="hljs-attr">value</span> : <span class="hljs-number">50000</span>, <span class="hljs-attr">enumerable</span> : <span class="hljs-literal">true</span>, <span class="hljs-attr">writable</span> : <span class="hljs-literal">true</span>&#125;
&#125;);

<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(person, <span class="hljs-string">'salary'</span>);
<span class="hljs-comment">// Object &#123;value: 50000, writable: true, enumerable: true, configurable: false&#125;</span>
<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(person, <span class="hljs-string">'corp'</span>);
<span class="hljs-comment">// Object &#123;value: "BABA", writable: false, enumerable: true, configurable: false&#125;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>存取器属性：get、set、enumerable、configurable</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Object</span>.defineProperties(person, &#123;
    <span class="hljs-attr">title</span>: &#123;<span class="hljs-attr">value</span> : <span class="hljs-string">'fe'</span>, <span class="hljs-attr">enumerable</span> : <span class="hljs-literal">true</span>&#125;,
    <span class="hljs-attr">corp</span>: &#123;<span class="hljs-attr">value</span> : <span class="hljs-string">'BABA'</span>, <span class="hljs-attr">enumerable</span> : <span class="hljs-literal">true</span>&#125;,
    <span class="hljs-attr">salary</span>: &#123;<span class="hljs-attr">value</span> : <span class="hljs-number">50000</span>, <span class="hljs-attr">enumerable</span> : <span class="hljs-literal">true</span>, <span class="hljs-attr">writable</span> : <span class="hljs-literal">true</span>&#125;,
    <span class="hljs-attr">luck</span>: &#123;
        <span class="hljs-attr">get</span> : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.random() > <span class="hljs-number">0.5</span> ? <span class="hljs-string">'good'</span> : <span class="hljs-string">'bad'</span>;
        &#125;
    &#125;,
    <span class="hljs-attr">promote</span>: &#123;
        <span class="hljs-attr">set</span> : <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">level</span>) </span>&#123;
            <span class="hljs-built_in">this</span>.salary *= <span class="hljs-number">1</span> + level * <span class="hljs-number">0.1</span>;
        &#125;
    &#125;
&#125;);

<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(person, <span class="hljs-string">'salary'</span>);
<span class="hljs-comment">// Object &#123;value: 50000, writable: true, enumerable: true, configurable: false&#125;</span>
<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(person, <span class="hljs-string">'corp'</span>);
<span class="hljs-comment">// Object &#123;value: "BABA", writable: false, enumerable: true, configurable: false&#125;</span>
person.salary; <span class="hljs-comment">// 50000</span>
person.promote = <span class="hljs-number">2</span>;
person.salary; <span class="hljs-comment">// 60000</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可写控制着对值特性的修改。可配置性控制着对其他特性（包括属性是否可以删除）的修改。然而规则远不止这么简单，例如，如果属性是可配置的话，则可以修改不可写属性的值。同样，如果属性是不可配置的，仍然可以将属性修改为不可写属性。以下是完整的规则：</p>
<ul>
<li>如果对象是不可扩展的，则可以编辑已有的自有属性，但不能给它添加新属性。</li>
<li>如果属性是不可配置的，则不能修改他的可配置性和可枚举性。</li>
<li>如果存取器属性是不可配置的，则不能修改其getter和setter方法，也不能将它转换为数据属性。</li>
<li>如果数据属性是不可配置的，则不能将它转换为存取器属性。</li>
<li>如果数据属性是不可配置的，则不能将它的可写性从false修改为true，但可以从true修改为false。</li>
<li>如果数据属性是不可配置且不可写的，则不能修改它的值。然而可配置但不可写属性的值是可以修改的（实际上是先将它标记为可写，然后修改它的值，最后转化为不可写）。</li>
</ul>
<p>总结：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b13de5a53e4cc680b59905e4cc9fb2~tplv-k3u1fbpfcp-zoom-1.image" alt="屏幕快照 2021-06-13 下午2.10.41.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-hGplW" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-12">对象标签</h3>
<ul>
<li><strong>对象的原型（[[<em>proto</em>]]）：指向另外一个对象，本对象的属性继承自它的原型对象。</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1ec224ac17a49139dd5f5a8a0b1ddd3~tplv-k3u1fbpfcp-zoom-1.image" alt="屏幕快照 2021-06-13 下午3.04.45.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>对象的类（[[class]]）：是一个标识对象类型的字符串。</strong></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> toString = <span class="hljs-built_in">Object</span>.prototype.toString;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getType</span>(<span class="hljs-params">o</span>)</span>&#123;
  <span class="hljs-keyword">return</span> toString.call(o).slice(<span class="hljs-number">8</span>,-<span class="hljs-number">1</span>);
&#125;;

toString.call(<span class="hljs-literal">null</span>); <span class="hljs-comment">// "[object Null]"</span>
getType(<span class="hljs-literal">null</span>); <span class="hljs-comment">// "Null"</span>
getType(<span class="hljs-literal">undefined</span>); <span class="hljs-comment">// "Undefined"</span>
getType(<span class="hljs-number">1</span>); <span class="hljs-comment">// "Number"</span>
getType(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">1</span>)); <span class="hljs-comment">// "Number"</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">1</span>); <span class="hljs-comment">// "object"</span>
getType(<span class="hljs-literal">true</span>); <span class="hljs-comment">// "Boolean"</span>
getType(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">true</span>)); <span class="hljs-comment">// "Boolean"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>对象的扩展标记（[[extensible]]）：指明了是否可以向该对象添加新属性。</strong></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj = &#123;<span class="hljs-attr">x</span> : <span class="hljs-number">1</span>, <span class="hljs-attr">y</span> : <span class="hljs-number">2</span>&#125;;
<span class="hljs-built_in">Object</span>.isExtensible(obj); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.preventExtensions(obj);
<span class="hljs-built_in">Object</span>.isExtensible(obj); <span class="hljs-comment">// false</span>
obj.z = <span class="hljs-number">1</span>;
obj.z; <span class="hljs-comment">// undefined, add new property failed</span>
<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(obj, <span class="hljs-string">'x'</span>);
<span class="hljs-comment">// Object &#123;value: 1, writable: true, enumerable: true, configurable: true&#125;</span>

<span class="hljs-built_in">Object</span>.seal(obj);
<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(obj, <span class="hljs-string">'x'</span>);
<span class="hljs-comment">// Object &#123;value: 1, writable: true, enumerable: true, configurable: false&#125;</span>
<span class="hljs-built_in">Object</span>.isSealed(obj); <span class="hljs-comment">// true</span>

<span class="hljs-built_in">Object</span>.freeze(obj);
<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(obj, <span class="hljs-string">'x'</span>);
<span class="hljs-comment">// Object &#123;value: 1, writable: false, enumerable: true, configurable: false&#125;</span>
<span class="hljs-built_in">Object</span>.isFrozen(obj); <span class="hljs-comment">// true</span>

<span class="hljs-comment">// [caution] not affects prototype chain!!!</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-zDAAe" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-13">序列化对象</h3>
<p>对象序列化是指将对象的状态转换为字符串，也可以将字符串还原为对象，可通过JSON.stringify()和JSON.parse()操作。这些方法都使用JSON作为数据交换格式。JSON的语法是javascript语法的子集，它并不能表示javascript里的所有值：</p>
<ul>
<li>支持对象、数组、字符串、无穷大数字、true、false、null，并且他们可以序列化和还原。</li>
<li>NaN、Infinity和-Inifity序列化的结果是null，日期对象序列化的结果是ISO格式的日期字符串。</li>
<li>函数、RegExp、Error对象和undefined值不能序列化和还原。</li>
<li>JSON.stringify()只能序列化对象可枚举的自有属性。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;<span class="hljs-attr">x</span> : <span class="hljs-number">1</span>, <span class="hljs-attr">y</span> : <span class="hljs-literal">true</span>, <span class="hljs-attr">z</span> : [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], <span class="hljs-attr">nullVal</span> : <span class="hljs-literal">null</span>&#125;;
<span class="hljs-built_in">JSON</span>.stringify(obj); <span class="hljs-comment">// "&#123;"x":1,"y":true,"z":[1,2,3],"nullVal":null&#125;"</span>

obj = &#123;<span class="hljs-attr">val</span> : <span class="hljs-literal">undefined</span>, <span class="hljs-attr">a</span> : <span class="hljs-literal">NaN</span>, <span class="hljs-attr">b</span> : <span class="hljs-literal">Infinity</span>, <span class="hljs-attr">c</span> : <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()&#125;;
<span class="hljs-built_in">JSON</span>.stringify(obj); <span class="hljs-comment">// "&#123;"a":null,"b":null,"c":"2015-01-20T14:15:43.910Z"&#125;"</span>

obj = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-string">'&#123;"x" : 1&#125;'</span>);
obj.x; <span class="hljs-comment">// 1</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-BvBBX" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-14">对象方法</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;<span class="hljs-attr">x</span> : <span class="hljs-number">1</span>, <span class="hljs-attr">y</span> : <span class="hljs-number">2</span>&#125;;
obj.toString(); <span class="hljs-comment">// "[object Object]"</span>
obj.toString = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y&#125;;
<span class="hljs-string">"Result "</span> + obj; <span class="hljs-comment">// "Result 3", by toString</span>

+obj; <span class="hljs-comment">// 3, from toString</span>

obj.valueOf = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y + <span class="hljs-number">100</span>;&#125;;
+obj; <span class="hljs-comment">// 103, from valueOf</span>

<span class="hljs-string">"Result "</span> + obj; <span class="hljs-comment">// still "Result 3"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-N8Xbt" href="https://juejin.cn/post/undefined"></a>
<a name="user-content-j7i3n" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-15">参考资料</h3>
<p><a href="http://www.ruanyifeng.com/blog/2011/06/designing_ideas_of_inheritance_mechanism_in_javascript.html" target="_blank" rel="nofollow noopener noreferrer">Javascript继承机制的设计思想</a><br><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object" target="_blank" rel="nofollow noopener noreferrer">对象方法-MDN</a><br><a href="https://mp.weixin.qq.com/s/QdwfGIKo206CHceGw_9l0Q" target="_blank" rel="nofollow noopener noreferrer">遍历对象的9种方法</a>​<br></p></div>  
</div>
            