
---
title: 'js引用类型引起的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8c6ab7d34a74c9ebfc250713236a3e1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 02:02:22 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8c6ab7d34a74c9ebfc250713236a3e1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p><strong>背景</strong></p>
<ul>
<li>被问道的引用问题
<ul>
<li>1 一次会议问道的引用类型问题，同学想使用惰性加载，希望在网页中fetch得到的数据保存下了，如果某些不改变参数，就不在发起请求，前提是会对fetch返回的数据进行修改，但还有使用之前的fetchdata</li>
</ul>
<pre><code class="copyable">if(window.fetchData&&window.fetchDataSomeKeyLength=== window.fetchData.length) return
const data = fetch(`$&#123;url&#125;`
window.fetchData = data
window.fetchDataSomeKeyLength=data.someKey.length
processData(data)//data.someKey的length做了处理
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<hr>
<ul>
<li>要get的点
<ul>
<li>1 js基本类型和引用类型的区别</li>
<li>2 栈存储和堆存的区别</li>
<li>3 js垃圾回收机制</li>
<li>4 活动对象、执行上下文、this</li>
<li>5 闭包的形成</li>
<li>6 深copy的实现</li>
</ul>
</li>
</ul>
<h3 data-id="heading-1">基本类型和引用类型的区别</h3>
<h4 data-id="heading-2">6种基本类型</h4>
<ul>
<li>string</li>
<li>number</li>
<li>bool</li>
<li>null</li>
<li>undefined</li>
<li>symbol</li>
</ul>
<p>通俗易懂的话来讲，js的基本类型使用用来存储值得，它们分配大小是有限度 在定义基本类型变量的时候它们的内存都被分配完成，</p>
<ul>
<li>数字有最大值和最小值</li>
<li>null undefined的是固定的值</li>
<li>bool 值为 true和false</li>
</ul>
<p><code>string</code> 、<code>number</code> 、<code>boolean</code> 和 <code>symbol</code> 这四种类型统称为<strong>原始类型（Primitive）</strong> ，表示不能再细分下去的基本类型；<code>symbol</code> 表示独一无二的值，通过 <code>Symbol</code> 函数调用生成，由于生成的 <code>symbol</code> 值为原始类型，所以 <code>Symbol</code> 函数不能使用 <code>new</code> 调用；<code>null</code> 和 <code>undefined</code> 通常被认为是特殊值，这两种类型的值唯一，就是其本身。</p>
  <h4 data-id="heading-3">引用类型</h4>
<ul>
<li>
<p>对象</p>
</li>
<li>
<p>数组</p>
</li>
<li>
<p>函数</p>
</li>
</ul>
<p>和基本类型区分开来。对象在逻辑上是属性的无序集合或者有序集合，是存放各种值的容器。对象值存储的是引用地址，所以和基本类型值不可变的特性不同，对象值是可变的。</p>
 <h4 data-id="heading-4">包装对象</h4>
 我们知道对象拥有属性和方法。但比如字符串这种基本类型值不属于对象为什么还拥有属性和方法呢？
<p>实际上在引用字符串的属性或方法时，会通过调用 <code>new String()</code> 的方式转换成对象，该对象继承了字符串的方法来处理属性的引用，一旦引用结束，便会销毁这个临时对象，这就是<strong>包装对象</strong>的概念。</p>
<p>不仅仅只是字符串有包装对象的概念，数字和布尔值也有相对应的 <code>new Number()</code> 和 <code>new Boolean()</code> 包装对象。<code>null</code> 和 <code>undefined</code> 没有包装对象，访问它们的属性会报类型错误。</p>
<p>字符串、数字和布尔值通过构造函数显式生成的包装对象，既然属于对象，和基本类型的值必然是有区别的，这点可以通过 <code>typeof</code> 检测出来。</p>
<pre><code class="copyable">typeof 'seymoe'                 // 'string'
typeof new String('seymoe')     // 'object'

<span class="copy-code-btn">复制代码</span></code></pre>
  <h4 data-id="heading-5">数据类型的判断</h4>
<ul>
<li>
<p>typeof</p>
</li>
<li>
<p>instanceof</p>
</li>
<li>
<p>Object.prototype.toString()</p>
<h5 data-id="heading-6">typeof</h5>
 `typeof` 操作符来判断一个值属于哪种基本类型,返回值是一个string，对null判断有误，认为null是个空指针
<pre><code class="copyable">typeof 'seymoe' // 'string' 
typeof true // 'boolean' 
typeof 10 // 'number' 
typeof Symbol() // 'symbol' 
typeof null // 'object' 
无法判定是否为 null 
typeof undefined // 'undefined'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果使用 <code>typeof</code> 操作符对对象类型及其子类型，譬如函数（可调用对象）、数组（有序索引对象）等进行判定，则除了函数都会得到 <code>object</code> 的结果。</p>
<pre><code class="copyable">typeof &#123;&#125; // 'object'
typeof [] // 'object'
typeof(() => &#123;&#125;)// 'function'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于无法得知一个值到底是数组还是普通对象，显然通过 <code>typeof</code> 判断具体的对象子类型远远不够。</p>
<h5 data-id="heading-7">instanceof</h5>
通过 `instanceof` 操作符也可以对对象类型链上的构造函数进行判定，其原理就是测试构造函数的 `prototype` 是否出现在被检测对象的原型链上。
```
[] instanceof Array            // true
(&#123;&#125;) instanceof Object         // true
(()=>&#123;&#125;) instanceof Function   // true
```
<p><strong>注意：<code>instanceof</code> 也不是万能的。其原理就是测试构造函数</strong></p>
<pre><code class="copyable"> var a=&#123;&#125;
 a.__proto__=[]
 a instanceof Array //true
 a instanceof Object //true

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">Object.prototype.toString()</h5>
`Object.prototype.toString()` 可以说是判定 JavaScript 中数据类型的终极解决方法了，具体用法请看以下代码：
<pre><code class="copyable"> Object.prototype.toString.call(&#123;&#125;)            // '[object Object]'
 Object.prototype.toString.call([])              // '[object Array]'
 Object.prototype.toString.call(() => &#123;&#125;)        // '[object Function]'
 Object.prototype.toString.call('seymoe')        // '[object String]'
 Object.prototype.toString.call(1)               // '[object Number]'
 Object.prototype.toString.call(true)            // '[object Boolean]'
 Object.prototype.toString.call(Symbol())        // '[object Symbol]'
 Object.prototype.toString.call(null)            // '[object Null]'
 Object.prototype.toString.call(undefined)       // '[object Undefined]'

 Object.prototype.toString.call(new Date())      // '[object Date]'
 Object.prototype.toString.call(Math)            // '[object Math]'
 Object.prototype.toString.call(new Set())       // '[object Set]'
 Object.prototype.toString.call(new WeakSet())   // '[object WeakSet]'
 Object.prototype.toString.call(new Map())       // '[object Map]'
 Object.prototype.toString.call(new WeakMap())   // '[object WeakMap]'
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
  <h4 data-id="heading-9">数据类型转换</h4>
   <h5 data-id="heading-10">ToPrimitive</h5>
   JavaScript 对象转换到基本类型值时，会使用 ToPrimitive 算法，这是一个内部算法，是编程语言在内部执行时遵循的一套规则。
<p>ToPrimitive 算法在执行时，会被传递一个参数 <code>hint</code>，表示这是一个什么类型的运算（也可以叫运算的期望值），根据这个 <code>hint</code> 参数，ToPrimitive 算法来决定内部的执行逻辑。</p>
<p><code>hint</code> 参数的取值只能是下列 3 者之一：</p>
<ul>
<li><code>string</code></li>
<li><code>number</code></li>
<li><code>default</code></li>
</ul>
   <h5 data-id="heading-11">转换算法</h5>
   当对象与到基本类型值发生转换时，会按照下面的逻辑调用对象上的方法：
**为了进行转换，JavaScript 会尝试查找并调用三个对象方法：**
<ol>
<li>
<p>调用<code>obj[Symbol.toPrimitive](hint)</code>- 带有符号键<code>Symbol.toPrimitive</code>（系统符号）的方法，如果存在这样的方法，</p>
</li>
<li>
<p>否则如果提示是 <code>"string"</code></p>
<ul>
<li>尝试<code>obj.toString()</code>和<code>obj.valueOf()</code>，无论存在什么。</li>
</ul>
</li>
<li>
<p>否则，如果提示是<code>"number"</code>或<code>"default"</code></p>
<ul>
<li>尝试<code>obj.valueOf()</code>和<code>obj.toString()</code>，无论存在什么。</li>
</ul>
</li>
</ol>
   <h5 data-id="heading-12"> 确定 hint</h5>
<p>我们提到了 ToPrimitive 算法中用到的 <code>hint</code> 参数，那怎样确定一次运算场景下的 <code>hint</code> 取值是什么呢？很简单----新建一个对象，打印各个运算场景下的 <code>hint</code> 值：</p>
<pre><code class="copyable">let obj = &#123;
  name: "John",
  money: 1000,

  [Symbol.toPrimitive](hint) &#123;
    console.log(`hint: $&#123;hint&#125;`);
  &#125;
&#125;;

alert(obj) // hint: string 
+obj // hint: number
obj + 500 // hint: default



// 一个没有提供 Symbol.toPrimitive 属性的对象，参与运算时的输出结果
var obj1 = &#123;&#125;;
console.log(+obj1);     // NaN
console.log(`$&#123;obj1&#125;`); // "[object Object]"
console.log(obj1 + ""); // "[object Object]"

// 接下面声明一个对象，手动赋予了 Symbol.toPrimitive 属性，再来查看输出结果
var obj2 = &#123;
  [Symbol.toPrimitive](hint) &#123;
    if (hint == "number") &#123;
      return 10;
    &#125;
    if (hint == "string") &#123;
      return "hello";
    &#125;
    return true;
  &#125;
&#125;;
console.log(+obj2);     // 10      -- hint 参数值是 "number"
console.log(`$&#123;obj2&#125;`); // "hello" -- hint 参数值是 "string"
console.log(obj2 + ""); // "true"  -- hint 参数值是 "default"
<span class="copy-code-btn">复制代码</span></code></pre>
   <h5 data-id="heading-13">## Symbol.toPrimitive 和 toString/valueOf 方法</h5>
   并不要求 `Symbol.toPrimitive` 和 `toString/valueOf` 方法必须返回 `hint` 参数值所暗示的类型值。
<p>但要注意下面两点：</p>
<ol>
<li><code>Symbol.toPrimitive</code> 和 <code>toString</code> 方法的返回值必须是基本类型值。</li>
<li><code>valueOf</code> 方法除了可以返回基本类型值，也可以返回其他类型值。</li>
</ol>
<p>当我们创建一个普通对象时（<code>&#123;&#125;</code> 或 <code>new Object()</code> 的方式等），对象上是不具备 <code>[Symbol.toPrimitive]</code> （方法）属性的。所以，对于普通对象的到基本类型值的运算，一般按照具体场景：</p>
<ol>
<li><code>hint</code> 值为 <code>"string"</code> 时，先调用 <code>toString</code>，<code>toString</code> 如果返回一个基本类型值了，则返回、终止运算；否则接着调用 <code>valueOf</code> 方法。</li>
<li>否则，先调用 <code>valueOf</code>，<code>valueOf</code> 如果返回一个基本类型值了，则返回、终止运算；否则接着调用 <code>toString</code> 方法。</li>
</ol>
<h2 data-id="heading-14">2 栈存储和堆存的区别</h2>
 <h5 data-id="heading-15">栈数据结构</h5>
<p>栈是一种特殊的列表，栈内的元素只能通过列表的一端访问，这一端称为栈顶。 栈被称为是一种后入先出（LIFO，last-in-first-out）的数据结构。 由于栈具有后入先出的特点，所以任何不在栈顶的元素都无法访问。 为了得到栈底的元素，必须先拿掉上面的元素。</p>
<p>在这里，为方便理解，通过类比乒乓球盒子来分析栈的存取方式。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8c6ab7d34a74c9ebfc250713236a3e1~tplv-k3u1fbpfcp-watermark.image" alt="16b8c0af7dd2aa15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这种乒乓球的存放方式与栈中存取数据的方式如出一辙。 处于盒子中最顶层的乒乓球 5，它一定是最后被放进去，但可以最先被使用。 而我们想要使用底层的乒乓球 1，就必须将上面的 4 个乒乓球取出来，让乒乓球1处于盒子顶层。 这就是栈空间先进后出，后进先出的特点。</p>
 <h5 data-id="heading-16"> 堆数据结构</h5>
堆是一种经过排序的树形数据结构，每个结点都有一个值。 通常我们所说的堆的数据结构，是指二叉堆。 堆的特点是根结点的值最小（或最大），且根结点的两个子树也是一个堆。 由于堆的这个特性，常用来实现优先队列，堆的存取是随意，这就如同我们在图书馆的书架上取书， 虽然书的摆放是有顺序的，但是我们想取任意一本时不必像栈一样，先取出前面所有的书， 我们只需要关心书的名字。
 <h5 data-id="heading-17"> 变量类型与内存的关系</h5>
<p>基本数据类型保存在栈内存中，因为基本数据类型占用空间小、大小固定，通过按值来访问，属于被频繁使用的数据。
为了更好的搞懂基本数据类型变量与栈内存，我们结合以下例子与图解进行理解：</p>
<pre><code class="copyable">let num1 = 1; 
let num2 = 1;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cac9568935f489fae1bfcb5c715da35~tplv-k3u1fbpfcp-watermark.image" alt="16b8c0b2fba2bdef.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>引用数据类型存储在堆内存中，因为引用数据类型占据空间大、大小不固定。 如果存储在栈中，将会影响程序运行的性能； 引用数据类型在栈中存储了指针，该指针指向堆中该实体的起始地址。 当解释器寻找引用值时，会首先检索其在栈中的地址，取得地址后从堆中获得实体</p>
<pre><code class="copyable">// 基本数据类型-栈内存
let a1 = 0;
// 基本数据类型-栈内存
let a2 = 'this is string';
// 基本数据类型-栈内存
let a3 = null;

// 对象的指针存放在栈内存中，指针指向的对象存放在堆内存中
let b = &#123; m: 20 &#125;;
// 数组的指针存放在栈内存中，指针指向的数组存放在堆内存中
let c = [1, 2, 3];

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0416776bcf30468e9b0f4aebb5bb572c~tplv-k3u1fbpfcp-watermark.image" alt="16b8c0b5752823f6.png" loading="lazy" referrerpolicy="no-referrer">
因此当我们要访问堆内存中的引用数据类型时，实际上我们首先是从变量中获取了该对象的地址指针， 然后再从堆内存中取得我们需要的数据。</p>
 <h5 data-id="heading-18">从内存角度来看变量复制</h5>
<pre><code class="copyable">let a = 20;
let b = a;
b = 30;
console.log(a); // 此时a的值是50

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，a、b 都是基本类型，它们的值是存储在栈内存中的，a、b 分别有各自独立的栈空间， 所以修改了 b 的值以后，a 的值并不会发生变化。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebb52f4d169e4f09bf6cc80f3f45860c~tplv-k3u1fbpfcp-watermark.image" alt="16b8c0b73d4ebd08.png" loading="lazy" referrerpolicy="no-referrer"></p>
 <h6 data-id="heading-19">引用数据类型的复制</h6>
<pre><code class="copyable">let m = &#123; a: 10, b: 20 &#125;;
let n = m;
n.a = 15;
console.log(m.a) //此时m.a的值是多少，是10？还是15？

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，m、n都是引用类型，栈内存中存放地址指向堆内存中的对象， 引用类型的复制会为新的变量自动分配一个新的值保存在变量中， 但只是引用类型的一个地址指针而已，实际指向的是同一个对象， 所以修改 n.a 的值后，相应的 m.a 也就发生了改变。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efcd23dbdc374242b03bca365108faee~tplv-k3u1fbpfcp-watermark.image" alt="16b8c0b9df03d885.png" loading="lazy" referrerpolicy="no-referrer"></p>
 <h6 data-id="heading-20">栈内存和堆内存的优缺点</h6>
<p>在JS中，基本数据类型变量大小固定，并且操作简单容易，所以把它们放入栈中存储。 引用类型变量大小不固定，所以把它们分配给堆中，让他们申请空间的时候自己确定大小，这样把它们分开存储能够使得程序运行起来占用的内存最小。</p>
<p>栈内存由于它的特点，所以它的系统效率较高。 堆内存需要分配空间和地址，还要把地址存到栈中，所以效率低于栈。</p>
<h2 data-id="heading-21">3 js垃圾回收机制</h2>
 <h5 data-id="heading-22">为什么要有垃圾回收</h5>
<p>在C语言和C++语言中，我们如果想要开辟一块堆内存的话，需要先计算需要内存的大小，然后自己通过<strong>malloc</strong>函数去手动分配，在用完之后，还要时刻记得用<strong>free</strong>函数去清理释放，否则这块内存就会被永久占用，造成内存泄露。</p>
<p>但是我们在写JavaScript的时候，却没有这个过程，因为人家已经替我们封装好了，V8引擎会根据你当前定义对象的大小去自动申请分配内存。</p>
<p>不需要我们去手动管理内存了，所以自然要有<strong>垃圾回收</strong>，否则的话只分配不回收，岂不是没多长时间内存就被占满了吗，导致应用崩溃。</p>
<p>垃圾回收的好处是不需要我们去管理内存，把更多的精力放在实现复杂应用上，但坏处也来自于此，不用管理了，就有可能在写代码的时候不注意，造成循环引用等情况，导致内存泄露。</p>
 <h5 data-id="heading-23">垃圾回收机制</h5>
  <h6 data-id="heading-24">标记清除</h6>
<p>当变量进入环境（例如，在函数中声明一个变量）时，就将这个变量标记为“进入环境”。从逻辑上讲，永远不能释放进入环境的变量所占用的内存，因为只要执行流进入相应的环境，就可能会用到它们。而当变量离开环境时，则将其标记为“离开环境”。</p>
<p>可以使用任何方式来标记变量。比如，可以通过翻转某个特殊的位来记录一个变量何时进入环境，或者使用一个“进入环境的”变量列表及一个“离开环境的”变量列表来跟踪哪个变量发生了变化。如何标记变量并不重要，关键在于采取什么策略。</p>
<ul>
<li>（1）垃圾收集器在运行的时候会给存储在内存中的所有变量都加上标记（当然，可以使用任何标记方式）。</li>
<li>（2）然后，它会去掉运行环境中的变量以及被环境中变量所引用的变量的标记</li>
<li>（3）此后，依然有标记的变量就被视为准备删除的变量，原因是在运行环境中已经无法访问到这些变量了。</li>
<li>（4）最后，垃圾收集器完成内存清除工作，销毁那些带标记的值并回收它们所占用的内存空间。</li>
</ul>
<p>目前，IE、Firefox、Opera、Chrome和Safari的JavaScript实现使用的都是标记清除式的垃圾回收策略（或类似的策略），只不过垃圾收集的时间间隔互有不同。</p>
  <h6 data-id="heading-25">引用计数</h6>
  引用计数的垃圾收集策略不太常见。含义是跟踪记录每个值被引用的次数。当声明了一个变量并将一个引用类型值赋给该变量时，则这个值的引用次数就是1。
<p>如果同一个值又被赋给另一个变量，则该值的引用次数加1。相反，如果包含对这个值引用的变量改变了引用对象，则该值引用次数减1。</p>
<p>当这个值的引用次数变成0时，则说明没有办法再访问这个值了，因而就可以将其占用的内存空间回收回来。</p>
<p>这样，当垃圾收集器下次再运行时，它就会释放那些引用次数为0的值所占用的内存。</p>
<pre><code class="copyable">  循环引用是指对象A中包含一个指向对象B的指针，而对象B中也包含一个指向对象A的引用，看个例子：
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">function foo () &#123;
    var objA = new Object();
    var objB = new Object();
    
    objA.otherObj = objB;
    objB.anotherObj = objA;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子中，objA和objB通过各自的属性相互引用，也就是说，这两个对象的引用次数都是2。</p>
<p>在采用标记清除策略的实现中，由于函数执行后，这两个对象都离开了作用域，因此这种相互引用不是问题。</p>
<p>但在采用引用次数策略的实现中，当函数执行完毕后，objA和objB还将继续存在，因为它们的引用次数永远不会是0。加入这个函数被重复多次调用，就会导致大量内存无法回收</p>
<p>还要注意的是，我们大部分人时刻都在写着循环引用的代码，看下面这个例子，相信大家都这样写过：</p>
<pre><code class="copyable">var el = document.getElementById('#el');
el.onclick = function (event) &#123;
    console.log('element was clicked');
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们为一个元素的点击事件绑定了一个匿名函数，我们通过<strong>event</strong>参数是可以拿到相应元素<strong>el</strong>的信息的。</p>
<p>大家想想，这是不是就是一个循环引用呢？ <strong>el</strong>有一个属性<strong>onclick</strong>引用了一个函数（其实也是个对象），函数里面的参数又引用了<strong>el</strong>，这样<strong>el</strong>的引用次数一直是2，即使当前这个页面关闭了，也无法进行垃圾回收。</p>
<p>如果这样的写法很多很多，就会造成内存泄露。我们可以通过在页面卸载时清除事件引用，这样就可以被回收了</p>
<pre><code class="copyable">var el = document.getElementById('#el');
el.onclick = function (event) &#123;
    console.log('element was clicked');
&#125;

// ...
// ...

// 页面卸载时将绑定的事件清空
window.onbeforeunload = function()&#123;
    el.onclick = null;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-26">V8垃圾回收策略</h5>
自动垃圾回收有很多算法，由于不同对象的生存周期不同，所以无法只用一种回收策略来解决问题，这样效率会很低。
<p>所以，V8采用了一种代回收的策略，将内存分为两个生代：<strong>新生代（new generation）<strong>和</strong>老生代（old generation）</strong> 。</p>
<p>新生代中的对象为存活时间较短的对象，老生代中的对象为存活时间较长或常驻内存的对象，分别对新老生代采用不同的垃圾回收算法来提高效率，对象最开始都会先被分配到新生代（如果新生代内存空间不够，直接分配到老生代），新生代中的对象会在满足某些条件后，被移动到老生代，这个过程也叫晋升，后面我会详细说明。</p>
<h6 data-id="heading-27">分代内存 </h6>
<p>默认情况下，32位系统新生代内存大小为16MB，老生代内存大小为700MB，64位系统下，新生代内存大小为32MB，老生代内存大小为1.4GB。</p>
<p>新生代平均分成两块相等的内存空间，叫做semispace，每块内存大小8MB（32位）或16MB（64位）。</p>
<h6 data-id="heading-28">分配方式</h6>
<p>新生代存的都是生存周期短的对象，分配内存也很容易，只保存一个指向内存空间的指针，根据分配对象的大小递增指针就可以了，当存储空间快要满时，就进行一次垃圾回收。</p>
<h6 data-id="heading-29">算法</h6>
<p>新生代采用<strong>Scavenge</strong>垃圾回收算法，在算法实现时主要采用<strong>Cheney</strong>算法。
Cheney算法将内存一分为二，叫做semispace，一块处于使用状态，一块处于闲置状态。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05c4f56cd7974062a731377ff993c53b~tplv-k3u1fbpfcp-watermark.image" alt="162c3526b85b16a7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>处于使用状态的semispace称为<strong>From空间</strong>，处于闲置状态的semispace称为<strong>To空间</strong>。</p>
<p>接下来我会结合流程图来详细说明Cheney算法是怎么工作的。 垃圾回收在下面我统称为 <strong>GC（Garbage Collection）</strong> 。
<strong>step1</strong>. 在From空间中分配了3个对象A、B、C</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0a0038d2cc84277a3df8c537bbbdcca~tplv-k3u1fbpfcp-watermark.image" alt="162c3526d601da9e.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>step2</strong>. GC进来判断对象B没有其他引用，可以回收，对象A和C依然为活跃对象</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0c412a2fd224f498f23388059c5771b~tplv-k3u1fbpfcp-watermark.image" alt="162c3526ee73c6b5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>step3</strong>. 将活跃对象A、C从From空间复制到To空间</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9250abaf5a864b798609072c5ec9fa99~tplv-k3u1fbpfcp-watermark.image" alt="162c3526f003cd95.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>step4</strong>. 清空From空间的全部内存</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff5b4beb868347b8a50066831563cf83~tplv-k3u1fbpfcp-watermark.image" alt="162c3527027f9a35.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>step5</strong>. 交换From空间和To空间</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e30fb045a46e4afeb6583fc326c59cbd~tplv-k3u1fbpfcp-watermark.image" alt="162c352706984982.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>step6</strong>. 在From空间中又新增了2个对象D、E</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f36dca0cb984345a4ff7012b8f9ed61~tplv-k3u1fbpfcp-watermark.image" alt="162c3527047d8e26.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>step7</strong>. 下一轮GC进来发现对象D没有引用了，做标记</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab97e24a0bf742f099c562a6dd36410b~tplv-k3u1fbpfcp-watermark.image" alt="162c3527073d80a9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>step8</strong>. 将活跃对象A、C、E从From空间复制到To空间</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e21e3d84844481dbfaaba7c498fb340~tplv-k3u1fbpfcp-watermark.image" alt="162c3527099bae4b.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>step9</strong>. 清空From空间全部内存</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fed0c0740bc4ce79223bf4f6f6212a3~tplv-k3u1fbpfcp-watermark.image" alt="162c35270c3a80b6.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>step10</strong>. 继续交换From空间和To空间，开始下一轮</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97885f82768c40ac83c767f0aebeff13~tplv-k3u1fbpfcp-watermark.image" alt="162c35271dd2cfd7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上面的流程图，我们可以很清楚的看到，进行From和To交换，就是为了让活跃对象始终保持在一块semispace中，另一块semispace始终保持空闲的状态。</p>
<p>Scavenge由于只复制存活的对象，并且对于生命周期短的场景存活对象只占少部分，所以它在时间效率上有优异的体现。Scavenge的缺点是只能使用堆内存的一半，这是由划分空间和复制机制所决定的。</p>
<p>由于Scavenge是典型的牺牲空间换取时间的算法，所以无法大规模的应用到所有的垃圾回收中。但我们可以看到，Scavenge非常适合应用在新生代中，因为新生代中对象的生命周期较短，恰恰适合这个算法。</p>
<h6 data-id="heading-30">晋升</h6>
当一个对象经过多次复制仍然存活时，它就会被认为是生命周期较长的对象。这种较长生命周期的对象随后会被移动到老生代中，采用新的算法进行管理。
<p><strong>对象从新生代移动到老生代的过程叫作晋升</strong>。</p>
<p>对象晋升的条件主要有两个：</p>
<ol>
<li>对象从From空间复制到To空间时，会检查它的内存地址来判断这个对象是否已经经历过一次Scavenge回收。如果已经经历过了，会将该对象从From空间移动到老生代空间中，如果没有，则复制到To空间。<strong>总结来说，如果一个对象是第二次经历从From空间复制到To空间，那么这个对象会被移动到老生代中</strong>。</li>
<li>当要从From空间复制一个对象到To空间时，如果To空间已经使用了超过25%，则这个对象直接晋升到老生代中。设置25%这个阈值的原因是当这次Scavenge回收完成后，这个To空间会变为From空间，接下来的内存分配将在这个空间中进行。如果占比过高，会影响后续的内存分配</li>
</ol>
<h6 data-id="heading-31"> 老生代</h6>
在老生代中，存活对象占较大比重，如果继续采用Scavenge算法进行管理，就会存在两个问题：
<ol>
<li>由于存活对象较多，复制存活对象的效率会很低。</li>
<li>采用Scavenge算法会浪费一半内存，由于老生代所占堆内存远大于新生代，所以浪费会很严重。</li>
</ol>
<p>所以，V8在老生代中主要采用了<strong>Mark-Sweep</strong>和<strong>Mark-Sweep</strong>相结合的方式进行垃圾回收。</p>
<h6 data-id="heading-32"> Mark-Sweep</h6>
Mark-Sweep是标记清除的意思，它分为标记和清除两个阶段。
<p>与Scavenge不同，Mark-Sweep并不会将内存分为两份，所以不存在浪费一半空间的行为。Mark-Sweep在标记阶段遍历堆内存中的所有对象，并标记活着的对象，在随后的清除阶段，只清除没有被标记的对象。</p>
<p>也就是说，Scavenge只复制活着的对象，而Mark-Sweep只清除死了的对象。活对象在新生代中只占较少部分，死对象在老生代中只占较少部分，这就是两种回收方式都能高效处理的原因。</p>
<p><strong>step1</strong>. 老生代中有对象A、B、C、D、E、F
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b27902f275db4deab041d0420f2f8af8~tplv-k3u1fbpfcp-watermark.image" alt="162c35271e20f9ab.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>step2</strong>. GC进入标记阶段，将A、C、E标记为存活对象</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f49ae8d21d2472d97ddcd19678db603~tplv-k3u1fbpfcp-watermark.image" alt="162c3527204267ca.png" loading="lazy" referrerpolicy="no-referrer">
<strong>step3</strong>. GC进入清除阶段，回收掉死亡的B、D、F对象所占用的内存空间</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b196c2ddfa154e8599c8dee6c67564a2~tplv-k3u1fbpfcp-watermark.image" alt="162c3527267e7eae.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，Mark-Sweep最大的问题就是，在进行一次清除回收以后，内存空间会出现不连续的状态。这种内存碎片会对后续的内存分配造成问题。</p>
<p>如果出现需要分配一个大内存的情况，由于剩余的碎片空间不足以完成此次分配，就会提前触发垃圾回收，而这次回收是不必要的。</p>
<h6 data-id="heading-33"> Mark-Compact</h6>
为了解决Mark-Sweep的内存碎片问题，Mark-Compact就被提出来了。
<p>**Mark-Compact是标记整理的意思，**是在Mark-Sweep的基础上演变而来的。Mark-Compact在标记完存活对象以后，会将活着的对象向内存空间的一端移动，移动完成后，直接清理掉边界外的所有内存。如下图所示：
<strong>step1</strong>. 老生代中有对象A、B、C、D、E、F（和Mark—Sweep一样）</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1b5d3b692aa4882a206537bf7ef9e54~tplv-k3u1fbpfcp-watermark.image" alt="162c3527267a55b2.png" loading="lazy" referrerpolicy="no-referrer">
<strong>step2</strong>. GC进入标记阶段，将A、C、E标记为存活对象（和Mark—Sweep一样）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bff5ea7e3186438d9a3ad9d559ff1986~tplv-k3u1fbpfcp-watermark.image" alt="162c3527204267ca.png" loading="lazy" referrerpolicy="no-referrer">
<strong>step3</strong>. GC进入整理阶段，将所有存活对象向内存空间的一侧移动，灰色部分为移动后空出来的空间</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dbf0156786a41509f9f0a10ee6d68e0~tplv-k3u1fbpfcp-watermark.image" alt="162c35272976bf46.png" loading="lazy" referrerpolicy="no-referrer">
<strong>step4</strong>. GC进入清除阶段，将边界另一侧的内存一次性全部回收</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fb2c8956fac4bad813b33b62de67dc0~tplv-k3u1fbpfcp-watermark.image" alt="162c352731840c87.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-34"> 两者结合</h6>
<p>在V8的回收策略中，Mark-Sweep和Mark-Conpact两者是结合使用的。</p>
<p>由于Mark-Conpact需要移动对象，所以它的执行速度不可能很快，在取舍上，V8主要使用Mark-Sweep，在空间不足以对从新生代中晋升过来的对象进行分配时，才使用Mark-Compact。</p>
<h6 data-id="heading-35"> 总结 </h6>
<p>V8的垃圾回收机制分为新生代和老生代。</p>
<p>新生代主要使用Scavenge进行管理，主要实现是Cheney算法，将内存平均分为两块，使用空间叫From，闲置空间叫To，新对象都先分配到From空间中，在空间快要占满时将存活对象复制到To空间中，然后清空From的内存空间，此时，调换From空间和To空间，继续进行内存分配，当满足那两个条件时对象会从新生代晋升到老生代。</p>
<p>老生代主要采用Mark-Sweep和Mark-Compact算法，一个是标记清除，一个是标记整理。两者不同的地方是，Mark-Sweep在垃圾回收后会产生碎片内存，而Mark-Compact在清除前会进行一步整理，将存活对象向一侧移动，随后清空边界的另一侧内存，这样空闲的内存都是连续的，但是带来的问题就是速度会慢一些。在V8中，老生代是Mark-Sweep和Mark-Compact两者共同进行管理的。</p>
<p>以上就是本文的全部内容，书写过程中参考了很多中外文章，参考书籍包括朴大大的《深入浅出NodeJS》以及《JavaScript高级程序设计》等。我们这里并没有对具体的算法实现进行探讨，感兴趣的朋友可以继续深入研究一下。</p>
<p>最后，谢谢大家能够读到这里，如果文中有任何不明确或错误的地方，欢迎给我留言~~</p>
<h2 data-id="heading-36">4 执行环境、执行上下文、活动对象、this</h2>
   <h3 data-id="heading-37">执行环境</h3>
    执行环境是js中重要的一个概念。执行环境定义了变量和函数有权访问其他变量，决定了他们的各自行为，每个函数执行都有自己的执行环境，当执行流入一个函数，函数的执行环境就会给推到当前执行栈中，函数执行完毕，函数的执行环境就会被弹出，执行权交给当前栈，这就是js的执行流
   <h3 data-id="heading-38">变量对象</h3>
    每个执行环境都有一个与之关联变量对象，环境中定义的所有的变量和函数都保存在这个变量中，虽然我们编写代码无法访问这个对象，但是解析器能够在处理数据的时会在后台使用。
   <h3 data-id="heading-39">全局执行环境</h3>
       全局执行环境，是最外围的一个执行环境。根据ecmascript实现所在的宿主不同，表示执行环境也不一样，web全局执行环境被认为是window，因此全局所有的变量和函数都被认为是window的属性和函数被创建，某个执行环境的中的代码执行完毕后，该环境就会给销毁，该环境变量对象也会被销毁
   <h3 data-id="heading-40">作用域链</h3>
    当代码在执行环境中执行时，会创建变量对象的一个作用域链，作用域链的用途，是保证执行环境有权访问所有的变量和函数有序访问，作用域的最前端是当前执行环境的的变量对象，如果这个环境是函数，就将其 **活动对象** ，作为变量对象，活动对象刚开始就只包含一个变量就是arguments对象（这个对象在全局是不存在的），作用域的下一个变量对象来之与当前函数所在的执行栈的变量对象（可以理解为当前函数的执行栈），下一个的下一个就是当前函数执行栈的执行栈，这样一直延续到全局执行环境中的变量对象，为作用域的末端。
<p>标识符解析（变量查找），是按照作用域链一级一级的操作，查找顺序是从当前变量对象开始，知道找到为止，如果找不到就会通常会有异常</p>
<pre><code class="copyable">var color = "blue";
function changeColor() &#123;
var otherColor = "red";
function swapColor() &#123;
 var tempColor = otherColor;
 otherColor = color;
 color = tempColor;
 // 这里可以访问 tempColor otherColor color
&#125;
swapColor();
// 这里可以访问  otherColor color swapColor
&#125;
changeColor();
// 这里可以访问 changeColor  color
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a1dfa3903164c25a289281e7714676f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
  <h3 data-id="heading-41"> this是什么</h3>
  一般对this的误解分为两个方面
<ul>
<li>1 this是指向当前函数的本身</li>
<li>2 this 指向的是当前函数的 作用域</li>
</ul>
  <h3 data-id="heading-42"> this是指向当前函数的本身</h3>
<p>下面代码中大家要理解函数的多面性，多个身份</p>
<ul>
<li>普通的函数</li>
<li>普通的对象</li>
<li>构造函数</li>
</ul>
<p>接下来讲用到函数的是两个身份普通函数、普通对象， 看代码（）</p>
<pre><code class="copyable">function foo()&#123;
    this.count++
&#125;
var count=0;
foo.count=0;
for(var i=0;i<5;i++)&#123;
    
    foo()
&#125;
console.log(foo.count)//0
console.log(count)//5

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从打印的结果上来看显然，this指向的不是本身函数，当然咱们一般看到这类的问题咱们就会绕道而行，看代码</p>
<pre><code class="copyable">function foo()&#123;
    this.count++
&#125;
var bar=&#123;
    count:0
&#125;
foo.count=0;
for(var i=0;i<5;i++)&#123;
    
    foo.call(bar)
&#125;
console.log(bar.count)//5
console.log(count)//0

<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然这种解决方案很好，也会有其他的解决方案，但是我们还是不理解this的问题，心里还是有种不安之感</p>
  <h3 data-id="heading-43"> this 指向的是当前函数的 作用域</h3>
<p>接下来讲用到函数的是两个身份普通函数、普通对象， 看代码（）</p>
<pre><code class="copyable"> function foo()&#123;
     var num=2;
     console.log(this.num)
 &#125;
 var num=0;
 foo()//0

<span class="copy-code-btn">复制代码</span></code></pre>
<p>咱们看到代码的执行结果后，发现this指向的并不是该函数的作用域。</p>
  <h3 data-id="heading-44">this到底是什么 </h3>
  this是在函数调用的时候绑定，不是在函数定义的时候绑定。它的上下文取决于函数调用时的各种条件，函数执行的时候会创建一个活动记录，这个记录里面包含了该函数中定义的参数和参数，包含函数在哪里被调用（调用栈）...,this就是其中的一个属性。 来看图
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f42fcdd3da0b4a7fb973466a526edbc0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中咱们看到this是在函数执行的时候创建的。</p>
<p><br></p><h2 data-id="heading-45">全面解析this</h2><br><p></p>
<p>前面几步咱们已经确定的this的创建和this的指向的误区，接下啦咱们要看看this的绑定的规则，分为4个规则。</p>
<ul>
<li>默认绑定</li>
<li>隐式绑定（上下文绑定）</li>
<li>显式绑定</li>
<li>new 绑定</li>
</ul>
<p><br></p><h3 data-id="heading-46">默认绑定</h3><br>
默认绑定的字面意思就是，不满足其他的绑定方式，而执行的绑定规则。默认绑定会把this绑定到全局对象（是一个危险的操作，文章后面会说为什么）
看代码<p></p>
<pre><code class="copyable"> function foo()&#123;
     var num=2;
     this.num++
     console.log(this.num)
 &#125;
 var num=0;
 foo()//1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中就实现了默认绑定，在foo方法的代码块中操作的是window.num++。</p>
<p><br></p><h3 data-id="heading-47">隐式绑定（上下文绑定）</h3><br>
定义：<br>
函数被调用的位置有上下文，或者是该函数的引用地址是不是被某个对象的属性引用，并通过对象的属性直接运行该函数。如果出现上述的情况，就会触发this的隐式绑定，this就会被绑定成当前对象
看代码<p></p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.name)
&#125;
var bar=&#123;
    name:'shiny',
    foo:foo
&#125;
bar.foo()//shiny
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ef7028c136647468ac6cef8b5eb4496~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>要需要补充一点，不管你的对象嵌套多深，this只会绑定为直接引用该函数的地址属性的对象，看代码</p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.name)
&#125;
var shiny=&#123;
    name:'shiny',
    foo:foo
&#125;
var red=&#123;
    name:'red',
    obj:shiny
    
&#125;
red.obj.foo()//shiny
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf0e2861da245ff8136787abdc5db8c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><br></p><h4 data-id="heading-48">隐式绑定的丢失</h4><br>
先看代码<p></p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.name)
&#125;
var shiny=&#123;
    name:'shiny',
    foo:foo
&#125;
function doFoo(fn)&#123;
    fn()
&#125;
doFoo(shiny.foo)//undefind
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家知道函数参数在函数执行的时候，其实有一个赋值的操作，我来解释一下上面的，当函数doFoo执行的时候会开辟一个新的栈并被推入到全局栈中执行，在执行的过程中会创建一个活动对象，这个活动对象会被赋值传入的参数以及在函数中定义的变量函数，在函数执行时用到的变量和函数直接从该活动对象上面取值使用。
看图
doFoo的执行栈</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6eaaa65aa5645dab8c5e7525b55aa28~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>fn的执行栈</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/251af84ba84a47af93fc130b641bfab1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看下面原理和上面一样通过赋值，导致隐式绑定的丢失，看代码</p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.name)
&#125;
var shiny=&#123;
    name:'shiny',
    foo:foo
&#125;
var bar = shiny.foo
bar()//undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家是不是已经明白了为什么是undefined，来解释一波，其实shiny的foo属性是引用了foo函数的引用内存地址，那么有把foo的引用地址赋值给了 bar 那么现在的bar的引用地址个shiny.foo的引用地址是一个，那么执行bar的时候也会触发默认绑定规则因为没有其他规则可以匹配，bar函数执行时，函数内部的this绑定的是全局变量。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be385bb8fad0400784450468381fcd18~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看下满的引用地址赋值是出现的，奇葩 隐式绑定丢失，看代码</p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.name)
&#125;
var shiny=&#123;
    name:'shiny',
    foo:foo
&#125;
var red=&#123;
    name:'red'
&#125;
(red.foo=shiny.foo)()//undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>赋值表达式 p.foo = o.foo 的返回值是目标函数的引用，因此调用位置是 foo() 而不是
p.foo() 或者 o.foo()。根据我们之前说过的，这里会应用默认绑定。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf6e1090b83e4da49e309ad7dae4e58d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><br></p><h3 data-id="heading-49">显式绑定</h3><br><p></p>
<h4 data-id="heading-50">call、apply绑定</h4><br>
javascript,在Function的porpertype上提供了3个方法来强行修改this，分别是 call、apply、bind，大家经常用的莫过于call和apply了，这两个函数的第一个参数，都是需要执行函数绑定的this，对于apply只有连个参数，第二个参数是一个数组，这个数组是要传入执行函数的参数，而call可以跟很多参数，从第二个参数起都会被传入到要执行函数的参数中
<p>看代码</p>
<pre><code class="copyable">function foo()&#123;
   console.log(this.age)
&#125;
var shiny=&#123;
   age:20
&#125;
foo.call(shiny)//20

function bar()&#123;
console.log(this.age)
&#125;
var red=&#123;
age:18
&#125;
bar.apply(red)//18
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两个方法都是显式的绑定了tihs
<br></p><h4 data-id="heading-51">硬绑定：</h4><br>
类似与 bind方法行为，是显式绑定的一种方式<p></p>
<pre><code class="copyable">function foo(b)&#123;
  return this.a+b
&#125;
var obj=&#123;
  a:2
&#125;
function bind(fn,obj)&#123;
  return function()&#123;
     return fn.apply(obj,arguments)
  &#125;
&#125;
bind(foo,obj)(3)//5
<span class="copy-code-btn">复制代码</span></code></pre>
<p>语言解释：
通过apply + 闭包机制 实现bind方法，实现强行绑定规则</p>
<p>API调用的“上下文”
第三方库或者寄生在环境，以及js内置的一些方法都提供了一下 content 上下文参数，他的作用和 bind一样，就是确保回调函数的this被绑定</p>
<pre><code class="copyable">function foo (el)&#123;
  console.log(el,this.id)
&#125;
var obj =&#123;
 id:'some one'
&#125;;
[1,2,4].forEach(foo,obj)
// 1 some one 2 some one 4 some one
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br></p><h3 data-id="heading-52">new 绑定</h3><br>
说道new 大家都会想到js的构造函数，咱们想不用着急new 绑定this的问题，咱们先看看咱们对js的构造函数的误解，传统面向类的语言中的构函数和js的构造函数时不一样<p></p>
<ul>
<li>
<p>传统面向类的语言中的构函数，是在使用new操作符实例化类的时候，会调用类中的一些特殊方法（构造函数）</p>
</li>
<li>
<p>很多人认为js中的new操作符和传统面向类语言的构造函数是一样的，其实有很大的差别</p>
</li>
<li>
<p>从新认识一下js中的构造函数，js中的构造函数 在被new操作符调用时，这个构造函数不属于每个类，也不会创造一个类，它就是一个函数，只是被new操作符调用。</p>
</li>
<li>
<p>使用new操作符调用 构造函数时会执行4步</p>
<ul>
<li>创建一个全新的对象</li>
<li>对全新的对象的__proto__属性地址进行修改成构造函数的原型（prototype）的引用地址</li>
<li>构造函数的this被绑定为这个全新的对象</li>
<li>如果构造函数有返回值并且这个返回值是一个对象，则返回该对象，否则返回当前新对象</li>
</ul>
</li>
</ul>
<p>咱们了解了js new 操作符调用构造函数时都做了些什么，哪么咱们就知道构造函数里面的this是谁了</p>
<p>代码实现</p>
<pre><code class="copyable">function Foo(a)&#123;
  this.a=a
&#125;
var F = new Foo(2)
console.log(F.a)//2
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br></p><h3 data-id="heading-53">绑定规则的顺序 </h3><br>
咱们在上面了解this绑定的4大规则，那么咱们就看看这4大绑定规则的优先级。
<br><h4 data-id="heading-54">默认绑定 </h4>
咱们根据字面意思，都能理解只有其余的3个绑定规则无法触发的时候就会触发默认绑定，没有比较意义<p></p>
<p><br></p><h4 data-id="heading-55">显式绑定 VS 隐式绑定</h4><br><p></p>
<p>看代码</p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.name)
&#125;
var  shiny=&#123;
    name:'shiny',
    foo:foo
&#125;
var red=&#123;
    name:'red'
&#125;

shiny.foo()//shiny
shiny.foo.call(red)// red
shiny.foo.apply(red)// red
shiny.foo.bind(red)()//red
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然在这场绑定this比赛中，显式绑定赢了隐式绑定</p>
<p><br></p><h4 data-id="heading-56">隐式绑定 VS new 操作符绑定</h4><br>
看代码<p></p>
<pre><code class="copyable">function  foo(name)&#123;
    this.name=name
&#125;
var shiny=&#123;
    foo:foo
&#125;
shiny.foo('shiny')
console.log(shiny.name)//shiny

var red = new shiny.foo('red')
console.log(red.name)//red
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然在这场绑定this比赛中new 操作符绑定赢了隐式绑定</p>
<p><br></p><h4 data-id="heading-57">显式绑定（硬绑定） VS new 操作符绑定</h4><br><p></p>
<p>使用call、apply方法不能结合new操作符会报错误</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ada79a6684d14c97b22ee01f6ea7557f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
但是咱们可以是bind绑定this来比较 显式绑定和new操作符的绑定this优先级。
看代码</p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.name)
&#125;
var shiny=&#123;
    name:'shiny'
&#125;

var bar = foo.bind(shiny)
var obj = new bar();
console.log(obj.name)// undefind
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然 new操作符绑定 战胜了 显式绑定</p>
<p><br></p><h4 data-id="heading-58">this的判断</h4><br>
咱们在上面已经了解 4个绑定this的优先级。咱们可以列举出来<p></p>
<ul>
<li>1 判断该函数是不是被new操作符调用，有的话 this就是 构造函数运行时创建的新对象
var f = new foo()</li>
<li>2 判断 函数是不是使用显式绑定 call、apply、bind，如果有，那么该函数的this就是 这个三个方法的第一个参数</li>
</ul>
<p>foo.call(window)</p>
<ul>
<li>3 判断该函数是不是被一个对象的属性引用了地址，该函数有上下文（隐式绑定），在函数执行的时候是通过该对象属性的引用触发，这个函数的this就是当前对象的。</li>
</ul>
<p>obj.foo();</p>
<ul>
<li>4 上面的三种都没有的话，就是默认绑定，该函数的this就是全局对象或undefined（严格模式下）</li>
</ul>
<p><br></p><h4 data-id="heading-59">绑定例外</h4><br>
😁 规则总是会有意外的，this绑定也是会有的，某些场面的绑定也是会出乎意料的，有可能触发了默认绑定
看代码<p></p>
<pre><code class="copyable">function foo()&#123;
    console.log(name)
&#125;
var name ='shiny'
foo.call(null)//shiny
foo.call(undefined)//shiny
var bar = foo.bind(null)
var baz = foo.bind(undefined)
bar()//siny
baz()//siny
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把 null、undefined通过 apply、call、bind 显式绑定，虽然实现可默认绑定，但是建议这么做因为在非严格的模式下会给全局对象添加属性，有时候会造成不可必要的bug。</p>
<p><br></p><h4 data-id="heading-60">更安全的this</h4><br>
咱们从上面知道在非严格模式下 默认绑定是并操作this的话会该全局对象添加属性，这样的操作是有风险性的<p></p>
<pre><code class="copyable">function foo(a,b) &#123;
console.log( "a:" + a + ", b:" + b );
&#125;
// 我们的空对象
var ø = Object.create( null );
// 把数组展开成参数
foo.apply( ø, [2, 3] ); // a:2, b:3
// 使用 bind(..) 进行柯里化
var bar = foo.bind( ø, 2 );
bar( 3 ); // a:2, b:3

<span class="copy-code-btn">复制代码</span></code></pre>
<p><br></p><h4 data-id="heading-61">es6中的this</h4><br>
在es5及一下版本，我们被this深深的困惑，但是看完了上面的文章，应该判断this没有关系，但是 重点来了 es6的this可以通过箭头函数直接绑定在该函数的执行的作用域上。
看代码<p></p>
<pre><code class="copyable"> function foo()&#123;
     return ()=>&#123;
          console.log(this.name)
     &#125;
 &#125;
 var obj =&#123;
     name:'obj'
 &#125;
  var shiny =&#123;
     name:'shiny'
 &#125;
 var bar = foo.call(obj);
 bar.call(shiny)// foo
 

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到箭头函数的this被绑定到该函数执行的作用域上。</p>
<p>咱们在看看 js内部提供内置函数使用箭头函数</p>
<pre><code class="copyable"> function foo() &#123;
    setTimeout(() => &#123;
    // 这里的 this 在此法上继承自 foo()
    console.log( this.a );
    &#125;,100);
&#125;
var obj = &#123;
    a:2
&#125;;
foo.call( obj ); // 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe825708b88741969fc2269a6b911b38~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
箭头函数可以像 bind(..) 一样确保函数的 this 被绑定到指定对象，此外，其重要性还体
现在它用更常见的词法作用域取代了传统的 this 机制。实际上，在 ES6 之前我们就已经
在使用一种几乎和箭头函数完全一样的模式。</p>
<pre><code class="copyable">function foo() &#123;
var self = this; // lexical capture of this
setTimeout( function()&#123;
    console.log( self.a );
    &#125;, 100 );
&#125;
var obj = &#123;
    a: 2
&#125;;
foo.call( obj ); // 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然 self = this 和箭头函数看起来都可以取代 bind(..)，但是从本质上来说，它们想替
代的是 this 机制。
如果你经常编写 this 风格的代码，但是绝大部分时候都会使用 self = this 或者箭头函数。
如果完全采用 this 风格，在必要时使用 bind(..)，尽量避免使用 self = this 和箭头函数。</p>
<h2 data-id="heading-62">5 闭包的形成</h2>
  <h3 data-id="heading-63">闭包</h3>
   有关如何创建作用域链以及作用域链有什么作用的细节，对彻底 理解闭包至关重要。当某个函数被调用时，会创建一个执行环境（execution context）及相应的作用域链。 然后，使用 arguments 和其他命名参数的值来初始化函数的活动对象（activation object）。但在作用域 链中，外部函数的活动对象始终处于第二位，外部函数的外部函数的活动对象处于第三位，……直至作为作用域链终点的全局执行环境
<p>在函数执行过程中，为读取和写入变量的值，就需要在作用域链中查找变量。来看下面的例子。</p>
<pre><code class="copyable">function compare(value1, value2) &#123;
if (value1 < value2) &#123;
 return -1;
&#125; else if (value1 > value2) &#123;
 return 1;
&#125; else &#123;
 return 0;
&#125;
&#125;
var result = compare(5, 10);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码先定义了 compare()函数，然后又在全局作用域中调用了它。当调用 compare()时，会 创建一个包含 arguments、value1 和 value2 的活动对象。全局执行环境的变量对象（包含 result 和 compare）在 compare()执行环境的作用域链中则处于第二位。图片 展示了包含上述关系的 compare()函数执行时的作用域链。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/722d679cae2246deb74fb9f936ae3009~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
后台的每个执行环境都有一个表示变量的对象——变量对象。全局环境的变量对象始终存在，而像 compare()函数这样的局部环境的变量对象，则只在函数执行的过程中存在。在创建 compare()函数 时，会创建一个预先包含全局变量对象的作用域链，这个作用域链被保存在内部的[[Scope]]属性中。 当调用 compare()函数时，会为函数创建一个执行环境，然后通过复制函数的[[Scope]]属性中的对 象构建起执行环境的作用域链。此后，又有一个活动对象（在此作为变量对象使用）被创建并被推入执 行环境作用域链的前端。对于这个例子中 compare()函数的执行环境而言，其作用域链中包含两个变 量对象：本地活动对象和全局变量对象。显然，作用域链本质上是一个指向变量对象的指针列表，它只 引用但不实际包含变量对象。 无论什么时候在函数中访问一个变量时，就会从作用域链中搜索具有相应名字的变量。一般来讲， 当函数执行完毕后，局部活动对象就会被销毁，内存中仅保存全局作用域（全局执行环境的变量对象）。 但是，闭包的情况又有所不同。</p>
<p>在看一个案例</p>
<pre><code class="copyable">function createComparisonFunction(propertyName) &#123;
  return function (object1, object2) &#123;
    var value1 = object1[propertyName];
    var value2 = object2[propertyName];

    if (value1 < value2) &#123;
      return -1;
    &#125; else if (value1 > value2) &#123;
      return 1;
    &#125; else &#123;
      return 0;
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，object1[propertyName] object2[propertyName] 两行代码是内部函数（一个匿名函数）中的代码，这两行代码访问了外部 函数中的变量 propertyName。即使这个内部函数被返回了，而且是在其他地方被调用了，但它仍然可 以访问变量 propertyName。之所以还能够访问这个变量，是因为内部函数的作用域链中包含 createComparisonFunction()的作用域。要彻底搞清楚其中的细节，必须从理解函数被调用的时候 都会发生什么入手。</p>
<p>当某个函数被调用时，会创建一个执行环境（execution context）及相应的作用域链。 然后，使用 arguments 和其他命名参数的值来初始化函数的活动对象（activation object）。但在作用域 链中，外部函数的活动对象始终处于第二位，外部函数的外部函数的活动对象处于第三位，……直至作为作用域链终点的全局执行环境</p>
<p>看图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95ecad5b5c274800978a3c64137f6730~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-64">闭包与变量</h3>
作用域链的这种配置机制引出了一个值得注意的副作用，即闭包只能取得包含函数中任何变量的最 后一个值。别忘了闭包所保存的是整个变量对象，而不是某个特殊的变量。下面这个例子可以清晰地说 明这个问题。
<pre><code class="copyable">function createFunctions() &#123;
  var result = new Array();
  for (var i = 0; i < 10; i++) &#123;
    result[i] = function () &#123;
      return i;
    &#125;;
  &#125;
  return result;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f86833a1da054710bbc01a6ed14b46a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个函数会返回一个函数数组。表面上看，似乎每个函数都应该返自己的索引值，即位置 0 的函数 返回 0，位置 1 的函数返回 1，以此类推。但实际上，每个函数都返回 10。因为每个函数的作用域链中 都保存着 createFunctions() 函数的活动对象，所以它们引用的都是同一个变量 i 。 当 createFunctions()函数返回后，变量 i 的值是 10，此时每个函数都引用着保存变量 i 的同一个变量 对象，所以在每个函数内部 i 的值都是 10。但是，我们可以通过创建另一个匿名函数强制让闭包的行为 符合预期，如下所示。</p>
<pre><code class="copyable">function createFunctions() &#123;
  var result = new Array();
  for (var i = 0; i < 10; i++) &#123;
    result[i] = (function (num) &#123;
      return function () &#123;
        return num;
      &#125;;
    &#125;)(i);
  &#125;
  return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc581bc2c87649059b4b3d6ee8025c93~tplv-k3u1fbpfcp-watermark.image" alt="下载 (1).png" loading="lazy" referrerpolicy="no-referrer">
在重写了前面的 createFunctions()函数后，每个函数就会返回各自不同的索引值了。在这个版 本中，我们没有直接把闭包赋值给数组，而是定义了一个匿名函数，并将立即执行该匿名函数的结果赋 给数组。这里的匿名函数有一个参数 num，也就是最终的函数要返回的值。在调用每个匿名函数时，我 们传入了变量 i。由于函数参数是按值传递的，所以就会将变量 i 的当前值复制给参数 num。而在这个 匿名函数内部，又创建并返回了一个访问 num 的闭包。这样一来，result 数组中的每个函数都有自己 num 变量的一个副本，因此就可以返回各自不同的数值了。</p>
<h3 data-id="heading-65">关于this</h3>
在闭包中使用 this 对象也可能会导致一些问题。我们知道，this 对象是在运行时基于函数的执 行环境绑定的：在全局函数中，this 等于 window，而当函数被作为某个对象的方法调用时，this 等 于那个对象。不过，匿名函数的执行环境具有全局性，因此其 this 对象通常指向 window。但有时候 由于编写闭包的方式不同，这一点可能不会那么明显。下面来看一个例子。
<pre><code class="copyable">var name = "The Window";
var object = &#123;
  name: "My Object",
  getNameFunc: function () &#123;
    return function () &#123;
      return this.name;
    &#125;;
  &#125;,
&#125;;
alert(object.getNameFunc()()); //"The Window"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个函数在被调用时都会自动取得两个特殊变量：this 和 arguments。内部函 数在搜索这两个变量时，只会搜索到其活动对象为止，因此永远不可能直接访问外部函数中的这两个变 量。不过，把外部作用域中的 this 对象保存在一个闭包能够访问 到的变量里，就可以让闭包访问该对象了。</p>
<pre><code class="copyable">var name = "The Window";
var object = &#123;
  name: "My Object",
  getNameFunc: function () &#123;
    var that = this;
    return function () &#123;
      return that.name;
    &#125;;
  &#125;,
&#125;;
alert(object.getNameFunc()()); //"My Object"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在几种特殊情况下，this 的值可能会意外地改变。比如，下面的代码是修改前面例子的结果。</p>
<pre><code class="copyable">var name = "The Window";
var object = &#123;
  name: "My Object",
  getName: function () &#123;
    return this.name;
  &#125;,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一行代码跟平常一样调用了 object.getName()，返回的是"My Object"，因为 this.name 就是 object.name。第二行代码在调用这个方法前先给它加上了括号。虽然加上括号之后，就好像只 是在引用一个函数，但 this 的值得到了维持，因为 object.getName 和(object.getName)的定义 是相同的。第三行代码先执行了一条赋值语句，然后再调用赋值后的结果。因为这个赋值表达式的值是 函数本身，所以 this 的值不能得到维持，结果就返回了"The Window"。 当然，你不大可能会像第二行和第三行代码一样调用这个方法。不过，这个例子有助于说明即使是 语法的细微变化，都有可能意外改变 this 的值。</p>
<h2 data-id="heading-66">6 深copy的实现</h2>
 <h3 data-id="heading-67"> 深拷贝和浅拷贝的定义</h3>
 深拷贝已经是一个老生常谈的话题了，也是现在前端面试的高频题目，但是令我吃惊的是有很多同学还没有搞懂深拷贝和浅拷贝的区别和定义
<p>浅拷贝：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96d34ade341c4bd1ba5fdf20f62e3cc3~tplv-k3u1fbpfcp-watermark.image" alt="16ce894a1f1b5c32.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建一个新对象，这个对象有着原始对象属性值的一份精确拷贝。如果属性是基本类型，拷贝的就是基本类型的值，如果属性是引用类型，拷贝的就是内存地址 ，所以如果其中一个对象改变了这个地址，就会影响到另一个对象。</p>
<p>深拷贝：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1f457fbbd4b4d5cbfe9573d044de566~tplv-k3u1fbpfcp-watermark.image" alt="16ce893a54f6c13d.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将一个对象从内存中完整的拷贝一份出来,从堆内存中开辟一个新的区域存放新对象,且修改新对象不会影响原对象</p>
 <h3 data-id="heading-68"> 乞丐版</h3>
 在不使用第三方库的情况下，我们想要深拷贝一个对象，用的最多的就是下面这个方法。
<pre><code class="copyable">JSON.parse(JSON.stringify());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种写法非常简单，而且可以应对大部分的应用场景，但是它还是有很大缺陷的，比如拷贝其他引用类型、拷贝函数、循环引用等情况。</p>
 <h3 data-id="heading-69"> 基础版本</h3>
<pre><code class="copyable">function clone(target) &#123;
   if (typeof target === 'object') &#123;
       let cloneTarget = &#123;&#125;;
       for (const key in target) &#123;
           cloneTarget[key] = clone(target[key]);
       &#125;
       return cloneTarget;
   &#125; else &#123;
       return target;
   &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4965f11218b42d299d18072e3fc2b6a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是一个最基础版本的深拷贝，这段代码可以让你向面试官展示你可以用递归解决问题，但是显然，他还有非常多的缺陷，比如，还没有考虑数组。</p>
  <h3 data-id="heading-70"> 考虑数组</h3>
<p>在上面的版本中，我们的初始化结果只考虑了普通的<code>object</code>，下面我们只需要把初始化代码稍微一变，就可以兼容数组了：</p>
<pre><code class="copyable">module.exports = function clone(target) &#123;
    if (typeof target === 'object') &#123;
        let cloneTarget = Array.isArray(target) ? [] : &#123;&#125;;
        for (const key in target) &#123;
            cloneTarget[key] = clone(target[key]);
        &#125;
        return cloneTarget;
    &#125; else &#123;
        return target;
    &#125;
&#125;;

const target = &#123;
    field1: 1,
    field2: undefined,
    field3: &#123;
        child: 'child'
    &#125;,
    field4: [2, 4, 8]
&#125;;



<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/435d79d6e9b349ff977823fcee49d0bb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
OK，没有问题，你的代码又向合格迈进了一小步。</p>
 <h3 data-id="heading-71"> 循环引用</h3>
<pre><code class="copyable">const target = &#123;
   field1: 1,
   field2: undefined,
   field3: &#123;
       child: 'child'
   &#125;,
   field4: [2, 4, 8]
&#125;;
target.target = target;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9229439b39bf4190b9480fd41a527a4a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
很明显，因为递归进入死循环导致栈内存溢出了。</p>
<p>原因就是上面的对象存在循环引用的情况，即对象的属性间接或直接的引用了自身的情况：</p>
<p>解决循环引用问题，我们可以额外开辟一个存储空间，来存储当前对象和拷贝对象的对应关系，当需要拷贝当前对象时，先去存储空间中找，有没有拷贝过这个对象，如果有的话直接返回，如果没有的话继续拷贝，这样就巧妙化解的循环引用的问题。</p>
<p>这个存储空间，需要可以存储<code>key-value</code>形式的数据，且<code>key</code>可以是一个引用类型，我们可以选择<code>Map</code>这种数据结构：</p>
<ul>
<li>检查<code>map</code>中有无克隆过的对象</li>
<li>有 - 直接返回</li>
<li>没有 - 将当前对象作为<code>key</code>，克隆对象作为<code>value</code>进行存储</li>
<li>继续克隆</li>
</ul>
<pre><code class="copyable">
 function clone(target, map = new Map()) &#123;
    if (typeof target === 'object') &#123;
        let cloneTarget = Array.isArray(target) ? [] : &#123;&#125;;
        if (map.get(target)) &#123;
            return map.get(target);
        &#125;
        map.set(target, cloneTarget);
        for (const key in target) &#123;
            cloneTarget[key] = clone(target[key], map);
        &#125;
        return cloneTarget;
    &#125; else &#123;
        return target;
    &#125;
&#125;;


<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f7dd36aec474af59ec543dcc9d65769~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来，我们可以使用，<code>WeakMap</code>提代<code>Map</code>来使代码达到画龙点睛的作用。</p>
<pre><code class="copyable">function clone(target, map = new WeakMap()) &#123;
    // ...
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么要这样做呢？，先来看看<code>WeakMap</code>的作用：</p>
<blockquote>
<p>WeakMap 对象是一组键/值对的集合，其中的键是弱引用的。其键必须是对象，而值可以是任意的。</p>
</blockquote>
<blockquote>
</blockquote>
<p>什么是弱引用呢？</p>
<blockquote>
<p>在计算机程序设计中，弱引用与强引用相对，是指不能确保其引用的对象不会被垃圾回收器回收的引用。 一个对象若只被弱引用所引用，则被认为是不可访问（或弱可访问）的，并因此可能在任何时刻被回收。</p>
</blockquote>
<blockquote>
</blockquote>
<p>举个例子：</p>
<pre><code class="copyable">let obj = &#123; name : 'ConardLi'&#125;
const target = new Map();
target.set(obj,'code秘密花园');
obj = null;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然我们手动将<code>obj</code>，进行释放，然是<code>target</code>依然对<code>obj</code>存在强引用关系，所以这部分内存依然无法被释放。</p>
<p>再来看<code>WeakMap</code>：</p>
<pre><code class="copyable">let obj = &#123; name : 'ConardLi'&#125;
const target = new WeakMap();
target.set(obj,'code秘密花园');
obj = null;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是<code>WeakMap</code>的话，<code>target</code>和<code>obj</code>存在的就是弱引用关系，当下一次垃圾回收机制执行时，这块内存就会被释放掉。</p>
<p>设想一下，如果我们要拷贝的对象非常庞大时，使用<code>Map</code>会对内存造成非常大的额外消耗，而且我们需要手动清除<code>Map</code>的属性才能释放这块内存，而<code>WeakMap</code>会帮我们巧妙化解这个问题。</p>
<ul>
<li><a href="https://juejin.cn/post/6844903873992196110" target="_blank" title="https://juejin.cn/post/6844903873992196110">前端进阶」JS中的栈内存堆内存</a></li>
<li><a href="https://juejin.cn/post/6844903591510016007" target="_blank" title="https://juejin.cn/post/6844903591510016007">聊聊V8引擎的垃圾回收</a></li>
<li><a href="https://juejin.cn/post/6844903591510016007" target="_blank" title="https://juejin.cn/post/6844903591510016007">如何写出一个惊艳面试官的深拷贝?</a></li>
</ul></div>  
</div>
            