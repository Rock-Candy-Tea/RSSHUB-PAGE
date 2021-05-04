
---
title: 'JS篇： 闭包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=616'
author: 掘金
comments: false
date: Mon, 03 May 2021 08:04:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=616'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">闭包</h2>
<p>2021/5/3</p>
<h3 data-id="heading-1">一. 什么是闭包？</h3>
<ul>
<li>一个函数和对其周围状态（<strong>lexical environment，词法环境</strong>）的引用捆绑在一起（或者说函数被引用包围），这样的组合就是<strong>闭包</strong>（<strong>closure</strong>）。</li>
<li>闭包让你可以在一个内层函数中访问到其外层函数的作用域。</li>
<li>在 JavaScript 中，每当创建一个函数，闭包就会在函数创建的同时被创建出来。</li>
</ul>
<h3 data-id="heading-2">二. 词法作用域</h3>
<ul>
<li>
<pre><code class="copyable">function init() &#123;
    var name = "Mozilla"; // name 是一个被 init函数 创建的局部变量
    function displayName() &#123; // displayName() 是内部函数，一个闭包
        alert(name); // 使用了父函数中声明的变量
    &#125;
    displayName();
&#125;
init();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>displayName()</code> 是定义在 <code>init()</code> 里的内部函数，并且仅在 <code>init()</code> 函数体内可用。</li>
<li>因为它可以访问到外部函数的变量，所以 <code>displayName()</code> 可以使用父函数 <code>init()</code> 中声明的变量 <code>name</code> 。</li>
</ul>
</li>
<li>
<p>这个<em>词法作用域</em>的例子描述了分析器如何在函数嵌套的情况下解析变量名。</p>
</li>
<li>
<p>词法（lexical）一词指的是，词法作用域根据源代码中声明变量的位置来确定该变量在何处可用。</p>
</li>
<li>
<p><strong>嵌套函数</strong>可访问声明于它们外部作用域的变量。</p>
</li>
</ul>
<h3 data-id="heading-3">三. 闭包</h3>
<ul>
<li>
<pre><code class="copyable">function makeFunc() &#123;
    var name = "Mozilla";
    function displayName() &#123;
        alert(name);
    &#125;
    return displayName;
&#125;

var myFunc = makeFunc();
myFunc();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>内部函数 <code>displayName()</code> <em>在执行前</em>，从外部函数返回。但运行这段代码的效果和之前 <code>init()</code> 函数的示例完全一样。</li>
<li>原因在于，JavaScript中的函数会形成了闭包。</li>
<li><em>闭包</em>是由函数以及声明该函数的词法环境组合而成的。该环境包含了这个闭包创建时作用域内的任何局部变量。</li>
<li>在本例子中，<code>myFunc</code> 是执行 <code>makeFunc</code> 时创建的 <code>displayName</code> 函数实例的引用。</li>
<li><code>displayName</code> 的实例维持了一个对它的词法环境（变量 <code>name</code> 存在于其中）的引用。</li>
<li>因此，当 <code>myFunc</code> 被调用时，变量 <code>name</code> 仍然可用。</li>
</ul>
</li>
<li>
<pre><code class="copyable">function makeAdder(x) &#123;
  return function(y) &#123;
    return x + y;
  &#125;;
&#125;

var add5 = makeAdder(5);
var add10 = makeAdder(10);

console.log(add5(2));  // 7
console.log(add10(2)); // 12
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>makeAdder</code> 是一个函数工厂</li>
<li><code>add5</code> 和 <code>add10</code> 都是闭包。</li>
<li>它们共享相同的函数定义，但是保存了不同的词法环境。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-4">四. 闭包实战</h3>
<h4 data-id="heading-5">1. 切换页面字号</h4>
<ul>
<li>
<pre><code class="copyable">function makeSizer(size) &#123;
  return function() &#123;
    document.body.style.fontSize = size + 'px';
  &#125;;
&#125;
// 调用下面不同的实例，便可切换页面字号
var size12 = makeSizer(12);
var size14 = makeSizer(14);
var size16 = makeSizer(16);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-6">2. 模拟私有方法</h4>
<ul>
<li>
<p>私有方法不仅仅有利于限制对代码的访问：还提供了管理全局命名空间的强大能力，避免非核心的方法弄乱了代码的公共接口部分。</p>
</li>
<li>
<p>JavaScript 没有这种原生支持将方法声明为私有的API</p>
</li>
<li>
<p>但我们可以使用闭包来模拟私有方法。</p>
</li>
<li>
<pre><code class="copyable">var Counter = (function() &#123;
  var privateCounter = 0;
  function changeBy(val) &#123;
    privateCounter += val;
  &#125;
  return &#123;
    increment: function() &#123;
      changeBy(1);
    &#125;,
    decrement: function() &#123;
      changeBy(-1);
    &#125;,
    value: function() &#123;
      return privateCounter;
    &#125;
  &#125;
&#125;)();

console.log(Counter.value()); /* logs 0 */
Counter.increment();
Counter.increment();
console.log(Counter.value()); /* logs 2 */
Counter.decrement();
console.log(Counter.value()); /* logs 1 */
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>本例只创建一个词法环境，为三个函数所共享。</li>
<li>该共享环境包含两个私有项，这两项都无法在这个匿名函数外部直接访问。必须通过匿名函数返回的三个公共函数访问。</li>
<li>这三个公共函数是共享同一个环境的闭包，JavaScript 的词法作用域让它们都可以访问 <code>privateCounter</code> 变量和 <code>changeBy</code> 函数。</li>
</ul>
</li>
</ul>
<h5 data-id="heading-7">改一下</h5>
<ul>
<li>
<p>将匿名的立即执行函数改为一个正常的匿名将函数并赋值给一个变量</p>
</li>
<li>
<pre><code class="copyable">var makeCounter = function() &#123;
  var privateCounter = 0;
  function changeBy(val) &#123;
    privateCounter += val;
  &#125;
  return &#123;
    increment: function() &#123;
      changeBy(1);
    &#125;,
    decrement: function() &#123;
      changeBy(-1);
    &#125;,
    value: function() &#123;
      return privateCounter;
    &#125;
  &#125;
&#125;;

// 创建两个实例引用，生成两个独立的词法环境
// 每个闭包都是引用自己词法作用域内的变量。
// 在一个闭包内对变量的修改，会改变这个闭包的词法环境，但不会影响到另外一个闭包中的变量。
var Counter1 = makeCounter();
var Counter2 = makeCounter();
console.log(Counter1.value()); /* logs 0 */
Counter1.increment();
Counter1.increment();
console.log(Counter1.value()); /* logs 2 */
Counter1.decrement();
console.log(Counter1.value()); /* logs 1 */
console.log(Counter2.value()); /* logs 0 */
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-8">3. 解决for循环var变量提升的问题</h4>
<h5 data-id="heading-9">解释for循环</h5>
<ul>
<li>for循环每循环一次都会创建一个块，并且for循环是很短的时间就循环结束了</li>
<li>而var创建的变量不存在块级作用域，还存在变量提升</li>
<li>所以最后所有块内的var声明的那个变量的值因为变量提升就成了最新的那个值</li>
</ul>
<h5 data-id="heading-10">示例</h5>
<ul>
<li>
<pre><code class="copyable"><p id="help">Helpful notes will appear here</p>

<input type="text" id="email" name="email">
<input type="text" id="name" name="name">
<input type="text" id="age" name="age">

-------------------------------------------------------------------------------------

function showHelp(help) &#123;
  document.getElementById('help').innerHTML = help;
&#125;

function setupHelp() &#123;
  var helpText = [
      &#123;'id': 'email', 'help': 'Your e-mail address'&#125;,
      &#123;'id': 'name', 'help': 'Your full name'&#125;,
      &#123;'id': 'age', 'help': 'Your age (you must be over 16)'&#125;
    ];

  for (var i = 0; i < helpText.length; i++) &#123;
    var item = helpText[i];
    document.getElementById(item.id).onfocus = function() &#123;
      showHelp(item.help);
    &#125;
  &#125;
&#125;

setupHelp();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>赋值给 <code>onfocus</code> 的是闭包。这些闭包是由他们的函数定义和在 <code>setupHelp</code> 作用域中捕获的环境所组成的。</li>
<li>这三个闭包在循环中被创建，但他们共享了同一个词法作用域，在这个作用域中存在一个变量item。</li>
<li>这是因为变量item使用var进行声明，由于变量提升，所以具有函数作用域。</li>
<li>当<code>onfocus</code>的回调执行时，变量对象<code>item</code>（被三个闭包所共享）已经指向了<code>helpText</code>的最后一项。</li>
</ul>
</li>
</ul>
<h5 data-id="heading-11">解决方案</h5>
<h6 data-id="heading-12">1.使用更多的闭包</h6>
<ul>
<li>
<pre><code class="copyable">function showHelp(help) &#123;
  document.getElementById('help').innerHTML = help;
&#125;

function makeHelpCallback(help) &#123;
  return function() &#123;
    showHelp(help);
  &#125;;
&#125;

function setupHelp() &#123;
  var helpText = [
      &#123;'id': 'email', 'help': 'Your e-mail address'&#125;,
      &#123;'id': 'name', 'help': 'Your full name'&#125;,
      &#123;'id': 'age', 'help': 'Your age (you must be over 16)'&#125;
    ];

  for (var i = 0; i < helpText.length; i++) &#123;
    var item = helpText[i];
    document.getElementById(item.id).onfocus = makeHelpCallback(item.help);
  &#125;
&#125;

setupHelp();
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用工厂函数makeHelpCallback为每一个回调创建一个新的词法环境。</p>
</li>
<li>
<p>所有的回调不再共享同一个环境，在这些环境中，<code>help</code> 指向 <code>helpText</code> 数组中对应的字符串。</p>
</li>
</ul>
<h6 data-id="heading-13">2. 使用匿名闭包</h6>
<ul>
<li>
<pre><code class="copyable">function showHelp(help) &#123;
  document.getElementById('help').innerHTML = help;
&#125;

function setupHelp() &#123;
  var helpText = [
      &#123;'id': 'email', 'help': 'Your e-mail address'&#125;,
      &#123;'id': 'name', 'help': 'Your full name'&#125;,
      &#123;'id': 'age', 'help': 'Your age (you must be over 16)'&#125;
    ];

  for (var i = 0; i < helpText.length; i++) &#123;
    (function() &#123;
       var item = helpText[i];
       document.getElementById(item.id).onfocus = function() &#123;
         showHelp(item.help);
       &#125;
    &#125;)(); // 马上把当前循环项的item与事件回调相关联起来
  &#125;
&#125;

setupHelp();
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h6 data-id="heading-14">3. 使用let关键字</h6>
<ul>
<li>
<pre><code class="copyable"> for (var i = 0; i < helpText.length; i++) &#123;
    let item = helpText[i];// 使用let而不是var，因此每个闭包都绑定了块作用域的变量，这意味着不再需要额外的闭包
    document.getElementById(item.id).onfocus = function() &#123;
      showHelp(item.help);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h6 data-id="heading-15">4. 使用 <code>forEach()</code>来遍历<code>helpText</code>数组</h6>
<ul>
<li>
<pre><code class="copyable"> helpText.forEach(function(text) &#123;
    document.getElementById(text.id).onfocus = function() &#123;
      showHelp(text.help);
    &#125;
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-16">五. 性能考量</h3>
<ul>
<li>
<p>如果不是某些特定任务需要使用闭包，在其它函数中创建函数是不明智的，因为闭包在处理速度和内存消耗方面对脚本性能具有负面影响。</p>
</li>
<li>
<p>在创建新的对象或者类时，方法通常应该关联于对象的原型，而不是定义到对象的构造器中。</p>
</li>
<li>
<p>原因是这将导致每次构造器被调用时，方法都会被重新赋值一次（也就是说，对于每个对象的创建，方法都会被重新赋值）。</p>
</li>
<li>
<pre><code class="copyable">function MyObject(name, message) &#123;
  this.name = name.toString();
  this.message = message.toString();
&#125;
MyObject.prototype.getName = function() &#123;
  return this.name;
&#125;;
MyObject.prototype.getMessage = function() &#123;
  return this.message;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            