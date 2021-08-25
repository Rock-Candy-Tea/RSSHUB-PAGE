
---
title: '从λ演算到函数式编程聊闭包(2)：彻底理解JavaScript闭包规则'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6621'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 06:08:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=6621'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>闭包是很多语言都具备的特性，上篇《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fwebfront%2FECMAScript%2Fjs6%2F2015_0814_240.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/webfront/ECMAScript/js6/2015_0814_240.html" ref="nofollow noopener noreferrer">从抽象代数漫游函数式编程(1)：闭包概念再Java/PHP/JS中的定义</a>》</p>
<h2 data-id="heading-0">闭包的特性</h2>
<p><strong>闭包有三个特性：</strong></p>
<ul>
<li>
<p>函数嵌套函数</p>
</li>
<li>
<p>函数内部可以引用外部的参数和变量</p>
</li>
<li>
<p>参数和变量不会被垃圾回收机制回收</p>
</li>
</ul>
<p>在js中,闭包主要涉及到js的几个其他的特性：作用域链,垃圾(内存)回收机制,函数嵌套,等等。</p>
<p>闭包（closure）是Javascript语言特色(函数式编程特色)，很多高级应用都要依靠闭包实现。但是JavaScript的一个难点，因为JavaScript这个早产儿先天不足，不想强类型语言那么泾渭分明。引用《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fwebfront%2FECMAScript%2Fjs6%2F2014_0213_214.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/webfront/ECMAScript/js6/2014_0213_214.html" ref="nofollow noopener noreferrer">ECMAScript进化史(1):话说Web脚本语言王者JavaScript的加冕历史</a> 》的段落：</p>
<blockquote>
<p>Javascript其实**（简化的）函数式编程+（简化的）面向对象编程**，这是由Brendan Eich（函数式编程）与网景公司（面向对象编程）共同决定的。它是C语言和Self语言一夜情的怪胎。'它的优秀之处并非原创，它的原创之处并不优秀。'</p>
<p>总的来说，Brendan Eich的设计思路是这样的：</p>
<ol>
<li>
<p>借鉴C语言的基本语法；</p>
</li>
<li>
<p>借鉴Java语言的数据类型和内存管理；</p>
</li>
<li>
<p>借鉴Scheme语言，将函数提升到"第一等公民"（first class）的地位；</p>
</li>
<li>
<p>借鉴Self语言，使用基于原型（prototype）的继承机制。</p>
</li>
</ol>
<p>…………</p>
<p>原因一：<strong>javascript是一个函数编程语言，怪就怪在它也有this指针，说明这个函数编程语言也是面向对象的语言</strong>**，说的具体点，javascript里的函数是一个高阶函数，编程语言里的高阶函数是可以作为对象传递的，同时javascript里的函数还有可以作为构造函数，这个构造函数可以创建实例化对象，结果导致方法执行时候this指针的指向会不断发生变化，很难控制。**</p>
<p><strong>原因二：javascript里的全局作用域对this指针有很大的影响，由上面java的例子我们看到，this指针只有在使用new操作符后才会生效，但是javascript里的this在没有进行new操作也会生效，这时候this往往会指向全局对象window。</strong></p>
<p>　　<strong>原因三：javascript里call和apply操作符可以随意改变this指向，这看起来很灵活，但是这种不合常理的做法破坏了我们理解this指针的本意，同时也让写代码时候很难理解this的真正指向</strong></p>
</blockquote>
<h2 data-id="heading-1">诠释JS闭包函数</h2>
<p>在理解闭包以前.最好能先理解一下JavaScript的垃圾回收机制与作用域链的含义，推荐阅读《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fwebfront%2FECMAScript%2Fjs6%2F2016_0219_7612.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/webfront/ECMAScript/js6/2016_0219_7612.html" ref="nofollow noopener noreferrer">再谈JavaScript垃圾回收机制：分析与排查JS内存泄露情形</a>》</p>
<h3 data-id="heading-2">javascript的垃圾回收原理</h3>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.cppblog.com%2Fsmagle%2Farchive%2F2010%2F07%2F23%2F120758.html" title="http://www.cppblog.com/smagle/archive/2010/07/23/120758.html" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer"><strong>引用计数</strong></a><strong>(reference counting)</strong>：机制就是跟踪一个值的引用次数，当声明一个变量并将一个引用类型赋值给该变量时该值引用次数加1，当这个变量指向其他一个时该值的引用次数便减一。当该值引用次数为0时就会被回收。该方式会引起内存泄漏的原因是它不能解决循环引用的问题： var a=&#123;&#125;;var b=&#123;&#125;;a.prop = b;b.prop = a;</p>
</li>
<li>
<p><strong>标记清除(mark and sweep)</strong>：大部分浏览器以此方式进行垃圾回收，当变量进入执行环境（函数中声明变量）的时候，垃圾回收器将其标记为“进入环境”，当变量离开环境的时候（函数执行结束）将其标记为“离开环境”，在离开环境之后还有的变量则是需要被删除的变量。标记方式不定，可以是某个特殊位的反转或维护一个列表等。</p>
<p>垃圾收集器给内存中的所有变量都加上标记，然后去掉环境中的变量以及被环境中的变量引用的变量的标记。在此之后再被加上的标记的变量即为需要回收的变量，因为环境中的变量已经无法访问到这些变量。</p>
</li>
</ul>
<p>其实我们只需要记住：</p>
<ul>
<li>
<p>在javascript中，如果一个对象不再被引用，那么这个对象就会被GC回收；</p>
</li>
<li>
<p>如果两个对象互相引用，而不再被第3者所引用，那么这两个互相引用的对象也会被回收。</p>
</li>
</ul>
<h3 data-id="heading-3">JavaScript作用域链</h3>
<p>简单来说,，<strong>作用域链就是函数在定义的时候创建的,用于寻找使用到的变量的值的一个索引</strong>**，**而他内部的规则是：</p>
<ul>
<li>
<p>把函数自身的本地变量放在最前面,</p>
</li>
<li>
<p>把自身的父级函数中的变量放在其次</p>
</li>
<li>
<p>把再高一级函数中的变量放在更后面</p>
</li>
<li>
<p>……以此类推直至全局对象为止</p>
</li>
</ul>
<p><strong>当函数中需要查询一个变量的值的时候，js解释器会去作用域链去查找。从最前面的本地变量中先找，如果没有找到对应的变量，则到下一级的链上找，一旦找到了变量，则不再继续。如果找到最后也没找到需要的变量，则解释器返回undefined</strong>。</p>
<p>一般来说，一个函数在执行开始的时候，会给其中定义的变量划分内存空间保存，以备后面的语句所用，等到函数执行完毕返回了，这些变量就被认为是无用的了。对应的内存空间也就被回收了。下次再执行此函数的时候，所有的变量又回到最初的状态，重新赋值使用。</p>
<p>但是如果这个<strong>函数内部又嵌套了另一个函数，而这个函数是有可能在外部被调用到的</strong>。并且这个<strong>内部函数又使用了外部函数的某些变量的话</strong>。这种内存回收机制就会出现问题：如果在外部函数返回后，又直接调用了内部函数，那么内部函数就无法读取到他所需要的外部函数中变量的值了。所以JavaScript解释器在遇到函数定义的时候，<strong>会自动把函数和他可能使用的变量(包括本地变量和父级和祖先级函数的变量(自由变量))一起保存起来</strong>**。也就是构建一个闭包，这些变量将不会被内存回收器所回收，只有当内部的函数不可能被调用以后(例如被删除了，或者没有了指针)，才会销毁这个闭包，而没有任何一个闭包引用的变量才会被下一次内存回收启动时所回收**。</p>
<p>也就是说,有了闭包,嵌套的函数结构才可以运作,这也是符合我们的预期的.</p>
<p>在生活上，我们去看中共政办事，找A办事，你还先得找B门盖个章，B说，你先得找C盖个章，C说，这个东西不是我们的职权范围…… 踢皮球，这就是非闭包。闭包就是负责到底，你找到A部门，A部门接待的那个人负责到底，他/她去协调B部门和C部门。</p>
<p>在工程上，闭包就是项目经理，负责调度项目所需要的资源。老板、客户有什么事情，直接找项目经理即可，不用再去找其它的人。</p>
<h2 data-id="heading-4">闭包的定义及其优缺点概况</h2>
<p><strong>闭包 是指有权访问另一个函数作用域中的变量的函数</strong>，创建闭包的最常见的方式就是在一个函数内创建另一个函数，通过另一个函数访问这个函数的局部变量。</p>
<h3 data-id="heading-5">闭包的缺点</h3>
<p>一般函数执行完毕后，局部活动对象就被销毁，内存中仅仅保存全局作用域。但闭包的情况不同！</p>
<p><strong>闭包的缺点</strong>就是常驻内存，会增大内存使用量，使用不当很容易造成内存泄露。</p>
<h3 data-id="heading-6">使用闭包的好处</h3>
<p>那么使用闭包有什么好处呢？使用闭包的好处是：</p>
<ul>
<li>
<p>希望一个变量长期驻扎在内存中</p>
</li>
<li>
<p>避免全局变量的污染</p>
</li>
<li>
<p>私有成员的存在（设计私有的方法和变量。）</p>
</li>
</ul>
<h2 data-id="heading-7">嵌套函数的闭包</h2>
<pre><code class="copyable">function closure () &#123;
    var a = 1;
    return function () &#123;
        console.log(a++);
    &#125;;
&#125;

var fun = closure();
fun();// 1 执行后 a++，，然后a还在~
fun();// 2
fun = null;//a被回收！！
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>闭包会使变量始终保存在内存中，如果不当使用会增大内存消耗</strong>。</p>
<h2 data-id="heading-8">代码演示JS闭包</h2>
<p>talk is cheap ,show me code</p>
<h3 data-id="heading-9">一、全局变量的累加</h3>
<pre><code class="copyable">var a = 1;
function abc()&#123;
    a++;
    console.log(a);
&#125;
abc();// 2
abc();// 3
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">二、局部变量</h3>
<pre><code class="copyable">function abc()&#123;
    var a = 1;
    a++;
    console.log(a);
&#125;
abc();// 2                     
abc();// 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么怎么才能做到变量a既是局部变量又可以累加呢？</p>
<h3 data-id="heading-11">三、局部变量的累加</h3>
<pre><code class="copyable">function outer () &#123;
    var x = 10;
    //函数嵌套函数
    return function () &#123;
        x++;
        alert(x);
    &#125;;
&#125;

//外部函数赋给变量y;
var y = outer();
//y函数调用一次，结果为11，相当于outer()()；
y();
//y函数调用第二次，结果为12，实现了累加
y();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">函数声明与函数表达式</h3>
<p>在js中我们可以通过关键字<code>function</code>来声明一个函数：</p>
<pre><code class="copyable">function abc () &#123;
    console.log(123);
&#125;
abc();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以通过一个"()"来将这个声明变成一个表达式：</p>
<pre><code class="copyable">//然后通过()直接调用前面的表达式即可，因此函数可以不必写名字；
(function () &#123;
    console.log(123);
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">四、模块化代码，减少全局变量的污染</h3>
<pre><code class="copyable">var abc = (function()&#123;      //abc为外部匿名函数的返回值
    var a = 1;
    return function()&#123;
        a++;
        console.log(a);
    &#125;
&#125;)();
abc();    //2 ；调用一次abc函数，其实是调用里面内部函数的返回值    
abc();    //3
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">五、私有成员的存在</h3>
<pre><code class="copyable">var aaa = (function()&#123;
    var a = 1;
    function bbb()&#123;
        a++;
        console.log(a);
    &#125;
    function ccc()&#123;
        a++;
        alert(a);
    &#125;
    return &#123; b:bbb, c:ccc &#125;           //json结构
&#125;)();
aaa.b();     //2
aaa.c();     //3
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">六.使用匿名函数实现累加</h3>
<pre><code class="copyable">function box()&#123;
    var age = 100;
    return function()&#123;          //匿名函数
        age++;
        return age;
    &#125;;

&#125;
var b = box();
console.log(b());
console.log(b());    //即alert(box()())；
console.log(b());
console.log(b);
b = null;  //解除引用，等待垃圾回收
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">七、在循环中直接找到对应元素的索引</h3>
<pre><code class="copyable"> window.onload = function () &#123;
    var aLi = document.getElementsByTagName('li')
    for(let i =0 ;i<aLi.length;i++)&#123;
        (function () &#123;
            //TODO
        &#125;)(i)
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">九.内存泄露问题</h3>
<p>由于<code>IE</code>的<code>js</code>对象和<code>DOM</code>对象使用不同的垃圾收集方法，因此闭包在<code>IE</code>中会导致内存泄露问题，也就是无法销毁驻留在内存中的元素</p>
<pre><code class="copyable">function closure()&#123;
    var oDiv = document.getElementById('oDiv');//oDiv用完之后一直驻留在内存中
    oDiv.onclick = function () &#123;
        console.log('oDiv.innerHTML');//这里用oDiv导致内存泄露
    &#125;;
&#125;
closure();
//最后应将oDiv解除引用来避免内存泄露
function closure()&#123;
    var oDiv = document.getElementById('oDiv');
    var test = oDiv.innerHTML;
    oDiv.onclick = function () &#123;
        alert(test);
    &#125;;
    oDiv = null;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>扩展阅读：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fsegmentfault.com%2Fblog%2Ftrigkit4%2F1190000000660786" target="_blank" rel="nofollow noopener noreferrer" title="http://segmentfault.com/blog/trigkit4/1190000000660786" ref="nofollow noopener noreferrer">javascript学习总结（四）function函数部分</a></p>
<p>转载<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/" ref="nofollow noopener noreferrer">本站</a>文章《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fwebfront%2FECMAScript%2Fjs6%2F2015_1024_325.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/webfront/ECMAScript/js6/2015_1024_325.html" ref="nofollow noopener noreferrer">从λ演算到函数式编程聊闭包(2)：彻底理解JavaScript闭包规则</a>》,<br>
请注明出处：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fwebfront%2FECMAScript%2Fjs6%2F2015_1024_325.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/webfront/ECMAScript/js6/2015_1024_325.html" ref="nofollow noopener noreferrer">www.zhoulujun.cn/html/webfro…</a></p></div>  
</div>
            