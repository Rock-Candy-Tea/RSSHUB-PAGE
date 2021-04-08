
---
title: 'JavaScript系列之this是什么'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0078c7b31d6c4bd0891e9c630a636fda~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 02:24:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0078c7b31d6c4bd0891e9c630a636fda~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本章将专门介绍与执行上下文创建阶段直接相关的最后一个细节——<strong>this</strong>是什么？以及它的指向到底是什么。</p>
<h2 data-id="heading-0">了解this</h2>
<p>也许你在其他面向对象的编程语言曾经看过<code>this</code>，也知道它会指向某个构造器(constructor)所建立的对象。但事实上在JavaScript里面，<code>this</code>所代表的不仅仅是那个被建立的对象。</p>
<p>先来看看ECMAScript 标准规范对this 的定义：</p>
<blockquote>
<p>「The this keyword evaluates to the value of the ThisBinding of the current execution context.」
「this 这个关键字代表的值为当前执行上下文的ThisBinding。」</p>
</blockquote>
<p>然后再来看看MDN 对this 的定义：</p>
<blockquote>
<p>「In most cases, the value of this is determined by how a function is called.」
「在大多数的情况下，this 其值取决于函数的调用方式。」</p>
</blockquote>
<p>好，如果上面两行就看得懂的话那么就不用再往下看了，Congratulations！</p>
<p>...... 我想应该不会，至少我光看这两行还是不懂。</p>
<p>先来看个例子吧：</p>
<pre><code class="copyable">var getGender = function() &#123;
    return people1.gender;
&#125;;

var people1 = &#123;
    gender: 'female',
    getGender: getGender
&#125;;

var people2 = &#123;
    gender: 'male',
    getGender: getGender
&#125;;

console.log(people1.getGender());    // female
console.log(people2.getGender());    // female

<span class="copy-code-btn">复制代码</span></code></pre>
<p>what?怎么people2变性了呢，这不是我想要的结果啊，为什么呢？</p>
<p>因为<code>getGender()</code>返回(return)写死了<code>people1.gender</code>的关系，结果自然是'female'。</p>
<p>那么，如果我们把<code>getGender</code>稍改一下：</p>
<pre><code class="copyable">var getGender = function() &#123;
    return this.gender;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候，你应该会分别得到<code>female</code>与<code>male</code>两种结果。</p>
<p>所以回到前面讲的重点，从这个例子可以看出，即便<code>people1</code>与<code>people2</code>的<code>getGender</code>方法参照的都是同一个getGender function，但由于<strong>调用的对象不同，所以执行的结果也会不同</strong>。</p>
<p>现在我们知道了第一个重点，**this实际上是在函数被调用时发生的绑定，它指向什么完全取决于函数的调用方式。**如何的区分this呢？</p>
<h2 data-id="heading-1">this到底是谁</h2>
<p>看完上面的例子，还是有点似懂非懂吧？那接下来我们来看看不同的调用方式对 this 值的影响。</p>
<p><strong>情况一：全局对象&调用普通函数</strong></p>
<p>在全局环境中，this 指向全局对象，在浏览器中，它就是 window 对象。下面的示例中，无论是否是在严格模式下，this 都是指向全局对象。</p>
<pre><code class="copyable">var x = 1

console.log(this.x)               // 1
console.log(this.x === x)         // true
console.log(this === window)      // true

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果普通函数是在全局环境中被调用，在非严格模式下，普通函数中 this 也指向全局对象；如果是在严格模式下，this 将会是 undefined。ES5 为了使 JavaScript 运行在更有限制性的环境而添加了<a href="https://link.zhihu.com/?target=https%3A//developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Strict_mode" target="_blank" rel="nofollow noopener noreferrer">严格模式</a>，严格模式为了消除安全隐患，禁止了 this 关键字指向全局对象。</p>
<pre><code class="copyable">var x = 1

function fn() &#123;
    console.log(this);   // Window 全局对象
    console.log(this.x);  // 1
&#125;

fn();      

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用严格模式后：</p>
<pre><code class="copyable">"use strict"     // 使用严格模式
var x = 1

function fn() &#123;
    console.log(this);   // undefined
    console.log(this.x);  // 报错 "Cannot read property 'x' of undefined"，因为此时 this 是 undefined
&#125;

fn();  

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>情况二：作为对象方法的调用</strong></p>
<p>我们知道，在对象里的值如果是原生值（primitive type；例如，字符串、数值、布尔值），我们会把这个新建立的东西称为「<strong>属性（property）</strong>」；如果对象里面的值是函数（function）的话，我们则会把这个新建立的东西称为「<strong>方法（method）</strong>」。</p>
<p>如果函数作为对象的一个方法时，并且作为对象的一个方法被调用时，<strong>函数中的this指向这个上一级对象</strong>。</p>
<pre><code class="copyable">var x = 1
var obj = &#123;
    x: 2,
    fn: function() &#123;
        console.log(this);    
        console.log(this.x);
    &#125;
&#125;

obj.fn()     

// obj.fn()结果打印出;
// Object &#123;x: 2, fn: function&#125;
// 2

var a = obj.fn
a()   

// a()结果打印出:   
// Window 全局对象
// 1

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的例子中，直接运行 obj.fn() ，调用该函数的上一级对象是 obj，所以 this 指向 obj，得到 this.x 的值是 2；之后我们将 fn 方法首先赋值给变量 a，a 运行在全局环境中，所以此时 this 指向全局对象Window，得到 this.x 为 1。</p>
<p>我们再来看一个例子，如果函数被多个对象嵌套调用，this 会指向什么。</p>
<pre><code class="copyable">var x = 1
var obj = &#123;
  x: 2,
  y: &#123;
    x: 3,
    fn: function() &#123;
      console.log(this);   // Object &#123;x: 3, fn: function&#125;
      console.log(this.x);   // 3
    &#125;
  &#125;
&#125;

obj.y.fn();      

<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么结果不是 2 呢，因为在这种情况下记住一句话：<strong>this 始终会指向直接调用函数的上一级对象</strong>，即 y，上面例子实际执行的是下面的代码。</p>
<pre><code class="copyable">var y = &#123;
  x: 3,
  fn: function() &#123;
    console.log(this);   // Object &#123;x: 3, fn: function&#125;
    console.log(this.x);   // 3
  &#125;
&#125;

var x = 1
var obj = &#123;
  x: 2,
  y: y
&#125;

obj.y.fn();    

<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象可以嵌套，函数也可以，如果函数嵌套，this 会有变化吗？我们通过下面代码来探讨一下。</p>
<pre><code class="copyable">var obj = &#123;
    y: function() &#123;
        console.log(this === obj);   // true
        console.log(this);   // Object &#123;y: function&#125;
        fn();

        function fn() &#123;
            console.log(this === obj);   // false
            console.log(this);   // Window 全局对象
        &#125;
    &#125;
&#125;

obj.y();  

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在函数 y 中，this 指向了调用它的上一级对象 obj，这是没有问题的。但是在嵌套函数 fn 中，this 并不指向 obj。嵌套的函数不会从调用它的函数中继承 this，当嵌套函数作为函数调用时，其 this 值在非严格模式下指向全局对象，在严格模式是 undefined，所以上面例子实际执行的是下面的代码。</p>
<pre><code class="copyable">function fn() &#123;
    console.log(this === obj);   // false
    console.log(this);   // Window 全局对象
&#125;

var obj = &#123;
    y: function() &#123;
        console.log(this === obj);   // true
        console.log(this);   // Object &#123;y: function&#125;
        fn();
    &#125;
&#125;

obj.y();  

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>情况三：作为构造函数调用</strong></p>
<p>我们可以使用 new 关键字，通过构造函数生成一个实例对象。此时，<strong>this 便指向这个新对象</strong>。</p>
<pre><code class="copyable">var x = 1;

function Fn() &#123;
　  this.x = 2;
    console.log(this);  // Fn &#123;x: 2&#125;
&#125;

var obj = new Fn();   // obj和Fn(..)调用中的this进行绑定
console.log(obj.x)   // 2

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>new</code>来调用<code>Fn(..)</code>时，会构造一个新对象并把它（obj）绑定到<code>Fn(..)</code>调用中的this。还有值得一提的是，如果构造函数返回了非引用类型（string，number，boolean，null，undefined），this 仍然指向实例化的新对象。</p>
<pre><code class="copyable">var x = 1

function Fn() &#123;
  this.x = 2

  return &#123;
    x: 3
  &#125;
&#125;

var a = new Fn()

console.log(a.x)      // 3

<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为Fn()返回(return)的是一个对象（引用类型），this 会指向这个return的对象。如果return的是一个非引用类型的值呢？</p>
<pre><code class="copyable">var x = 1

function Fn() &#123;
  this.x = 2

  return 3
&#125;

var a = new Fn()

console.log(a.x)      // 2

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>情况四：call 和 apply 方法调用</strong></p>
<p>如果你想改变 this 的指向，可以使用 call 或 apply 方法。<strong>它们的第一个参数都是指定函数运行时其中的<code>this</code>指向</strong>。如果第一个参数不传（参数为空）或者传 null 、undefined，默认 this 指向全局对象（非严格模式）或 undefined（严格模式）。</p>
<pre><code class="copyable">var x = 1;

var obj = &#123;
  x: 2
&#125;

function fn() &#123;
    console.log(this);
    console.log(this.x);
&#125;

fn.call(obj)
// Object &#123;x: 2&#125;
// 2

fn.apply(obj)     
// Object &#123;x: 2&#125;
// 2

fn.call()         
// Window 全局对象
// 1

fn.apply(null)    
// Window 全局对象
// 1

fn.call(undefined)    
// Window 全局对象
// 1

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 call 和 apply 时，如果给 this 传的不是对象，JavaScript 会使用相关构造函数将其转化为对象，比如传 number 类型，会进行<code>new Number()</code>操作，如传 string 类型，会进行<code>new String()</code>操作，如传 boolean 类型，会进行new Boolean()操作。</p>
<pre><code class="copyable">function fn() &#123;
  console.log(Object.prototype.toString.call(this))
&#125;

fn.call('love')      // [object String]
fn.apply(1)          // [object Number]
fn.call(true)          // [object Boolean]

<span class="copy-code-btn">复制代码</span></code></pre>
<p>call 和 apply 的区别在于，call 的第二个及后续参数是一个参数列表，apply 的第二个参数是数组。参数列表和参数数组都将作为函数的参数进行执行。</p>
<pre><code class="copyable">var x = 1

var obj = &#123;
  x: 2
&#125;

function Sum(y, z) &#123;
  console.log(this.x + y + z)
&#125;

Sum.call(obj, 3, 4)       // 9
Sum.apply(obj, [3, 4])    // 9

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>情况五：bind 方法调用</strong></p>
<p>调用 f.bind(someObject) 会创建一个与 f 具有相同函数体和作用域的函数，但是在这个新函数中，新函数的 this <strong>会永久的指向 bind 传入的第一个参数</strong>，无论这个函数是如何被调用的。</p>
<pre><code class="copyable">var x = 1

var obj1 = &#123;
    x: 2
&#125;;
var obj2 = &#123;
    x: 3
&#125;;

function fn() &#123;
    console.log(this);
    console.log(this.x);
&#125;;

var a = fn.bind(obj1);
var b = a.bind(obj2);

fn();
// Window 全局对象
// 1

a();
// Object &#123;x: 2&#125;
// 2

b();
// Object &#123;x: 2&#125;
// 2

a.call(obj2);
// Object &#123;x: 2&#125;
// 2

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的例子中，虽然我们尝试给函数 a 重新指定 this 的指向，但是它依旧指向第一次 bind 传入的对象，即使是使用 call 或 apply 方法也不能改变这一事实，即永久的指向 bind 传入的第一次参数。</p>
<p><strong>情况六：箭头函数中this指向</strong></p>
<p>值得一提的是，从ES6 开始新增了箭头函数，先来看看MDN 上对箭头函数的说明</p>
<blockquote>
<p>An arrow function expression has a shorter syntax than a function expression and does notbind its own<code>this</code>,<code>arguments</code>,<code>super</code>, or<code>new.target</code>. Arrow functions are always anonymous. These function expressions are best suited for non-method functions, and they cannot be used as constructors.</p>
</blockquote>
<p>这里已经清楚了说明了，箭头函数没有自己的<code>this</code>绑定。<strong>箭头函数中使用的<code>this</code>，其实是直接包含它的那个函数或函数表达式中的<code>this</code></strong>。在前面情况二中函数嵌套函数的例子中，被嵌套的函数不会继承上层函数的 this，如果使用箭头函数，会发生什么变化呢？</p>
<pre><code class="copyable">var obj = &#123;
  y: function() &#123;
        console.log(this === obj);   // true
        console.log(this);           // Object &#123;y: function&#125;

      var fn = () => &#123;
          console.log(this === obj);   // true
          console.log(this);           // Object &#123;y: function&#125;
      &#125;
      fn();
  &#125;
&#125;

obj.y() 

<span class="copy-code-btn">复制代码</span></code></pre>
<p>和普通函数不一样，箭头函数中的 this 指向了 obj，这是因为它从上一层的函数中继承了 this，你可以理解为箭头函数修正了 this 的指向。所以<strong>箭头函数的this不是调用的时候决定的，而是在定义的时候处在的对象就是它的this</strong>。</p>
<p>换句话说，<strong>箭头函数的this看外层的是否有函数，如果有，外层函数的this就是内部箭头函数的this，如果没有，则this是window</strong>。</p>
<pre><code class="copyable">var obj = &#123;
  y: () => &#123;
        console.log(this === obj);   // false
        console.log(this);           // Window 全局对象 

      var fn = () => &#123;
          console.log(this === obj);   // false
          console.log(this);           // Window 全局对象 
      &#125;
      fn();
  &#125;
&#125;

obj.y() 

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中，虽然存在两个箭头函数，其实this取决于最外层的箭头函数，由于obj是个对象而非函数，所以this指向为Window全局对象。</p>
<p>同 bind 一样，箭头函数也很“顽固”，我们无法通过 call 和 apply 来改变 this 的指向，<strong>即传入的第一个参数被忽略</strong>。</p>
<pre><code class="copyable">var x = 1
var obj = &#123;
    x: 2
&#125;

var a = () => &#123;
    console.log(this.x)
    console.log(this)
&#125;

a.call(obj)       
// 1
// Window 全局对象

a.apply(obj)      
// 1
// Window 全局对象

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的文字描述过多可能有点干涩，那么就看以下的这张流程图吧，我觉得这个图总结的很好，图中的流程只针对于单个规则。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0078c7b31d6c4bd0891e9c630a636fda~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">小结</h2>
<p>本篇文章介绍了 this 指向的几种情况，不同的运行环境和调用方式都会对 this 产生影响。总的来说，函数 this 的指向取决于当前调用该函数的对象，也就是执行时的对象。在这一节中，你需要掌握：</p>
<ul>
<li>this 指向全局对象的情况；</li>
<li>严格模式和非严格模式下 this 的区别；</li>
<li>函数作为对象的方法调用时 this 指向的几种情况；</li>
<li>作为构造函数时 this 的指向，以及是否 return 的区别；</li>
<li>使用 call 和 apply 改变调用函数的对象；</li>
<li>bind 创建的函数中 this 的指向；</li>
<li>箭头函数中的 this 指向。</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            