
---
title: '判断JavaScript数据类型的四种方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5641259cf4f401193b2a354e1f63575~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 00:49:52 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5641259cf4f401193b2a354e1f63575~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、对JavaScript数据类型的解析</h2>
<p>在 ECMAScript 规范中，共定义了 7 种数据类型，分为 基本类型 和 引用类型 两大类，如下所示：</p>
<blockquote>
<p>基本类型：String、Number、Boolean、Symbol、Undefined、Null</p>
<p>引用类型：Object</p>
</blockquote>
<ul>
<li>
<p>基本类型也称为简单类型，由于其占据空间固定，是简单的数据段，为了便于提升变量查询速度，将其存储在栈中，即按值访问。</p>
</li>
<li>
<p>引用类型也称为复杂类型，由于其值的大小会改变，所以不能将其存放在栈中，否则会降低变量查询速度，因此，其值存储在堆(heap)中，而存储在变量处的值，是一个指针，指向存储对象的内存处，即按址访问。引用类型除 Object 外，还包括 Function 、Array、RegExp、Date 等等。</p>
</li>
<li>
<p>鉴于 ECMAScript 是松散类型的，因此需要有一种手段来检测给定变量的数据类型。对于这个问题，JavaScript 也提供了多种方法，但遗憾的是，不同的方法得到的结果参差不齐。</p>
</li>
</ul>
<p>下面介绍常用的4种方法，并对各个方法存在的问题进行简单的分析。</p>
<h2 data-id="heading-1">2、typeof</h2>
<p>typeof 是一个操作符，其右侧跟一个一元表达式，并返回这个表达式的数据类型。返回的结果用该类型的字符串(全小写字母)形式表示，包括以下 7 种：number、boolean、symbol、string、object、undefined、function 等。</p>
<ol>
<li>
<blockquote>
<p>typeof'';// string 有效</p>
</blockquote>
</li>
<li>
<blockquote>
<p>typeof1;// number 有效</p>
</blockquote>
</li>
<li>
<blockquote>
<p>typeofSymbol();// symbol 有效</p>
</blockquote>
</li>
<li>
<blockquote>
<p>typeoftrue;//boolean 有效</p>
</blockquote>
</li>
<li>
<blockquote>
<p>typeofundefined;//undefined 有效</p>
</blockquote>
</li>
<li>
<blockquote>
<p>typeofnull;//object 无效</p>
</blockquote>
</li>
<li>
<blockquote>
<p>typeof<code>[]</code> ;//object 无效</p>
</blockquote>
</li>
<li>
<blockquote>
<p>typeofnewFunction();// function 有效</p>
</blockquote>
</li>
<li>
<blockquote>
<p>typeofnewDate();//object 无效</p>
</blockquote>
</li>
<li>
<blockquote>
<p>typeofnewRegExp();//object 无效</p>
</blockquote>
</li>
</ol>
<p>有些时候，typeof 操作符会返回一些令人迷惑但技术上却正确的值：</p>
<ul>
<li>对于基本类型，除 null 以外，均可以返回正确的结果。</li>
<li>对于引用类型，除 function 以外，一律返回 object 类型。</li>
<li>对于 null ，返回 object 类型。</li>
<li>对于 function 返回  function 类型。</li>
</ul>
<p>其中，null 有属于自己的数据类型 Null ， 引用类型中的 数组、日期、正则 也都有属于自己的具体类型，而 typeof 对于这些类型的处理，只返回了处于其原型链最顶端的 Object 类型，没有错，但不是我们想要的结果。</p>
<h2 data-id="heading-2">3、instanceof</h2>
<p>instanceof 是用来判断 A 是否为 B 的实例，表达式为：A instanceof B，如果 A 是 B 的实例，则返回 true,否则返回 false。 在这里需要特别注意的是：instanceof 检测的是原型，我们用一段伪代码来模拟其内部执行过程：</p>
<pre><code class="copyable">1. instanceof (A,B) = &#123;
2.     varL = A.__proto__;
3.     varR = B.prototype;
4.     if(L === R) &#123;
5.         // A的内部属性 __proto__ 指向 B 的原型对象
6.         returntrue;
7.     &#125;
8.     returnfalse;
9. &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述过程可以看出，当 A 的 <code>__proto__</code> 指向 B 的 prototype 时，就认为 A 就是 B 的实例，我们再来看几个例子：</p>
<pre><code class="copyable">1.  [] instanceof Array;// true
2.  &#123;&#125; instanceof Object;// true
3.  newDate() instanceof Date;// true

4.  function Person()&#123;&#125;;
5.  newPerson() instanceof Person;

6.  [] instanceof Object;// true
7.  newDate() instanceof Object;// true
8.  newPerson instanceof Object;// true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们发现，虽然 instanceof 能够判断出 <code>[ ]</code> 是Array的实例，但它认为<code>[ ]</code>也是Object的实例，为什么呢？</p>
<p>我们来分析一下<code> [ ]</code>、Array、Object 三者之间的关系：</p>
<p>从 instanceof 能够判断出 <code>[ ].__proto__ </code> 指向 Array.prototype，而 Array.prototype.<code>__proto__ </code>又指向了Object.prototype，最终 Object.prototype.<code>__proto__</code> 指向了null，标志着原型链的结束。因此，<code>[]</code>、Array、Object 就在内部形成了一条原型链：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5641259cf4f401193b2a354e1f63575~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>从原型链可以看出，[] 的 <strong>proto</strong>  直接指向Array.prototype，间接指向 Object.prototype，所以按照 instanceof 的判断规则，[] 就是Object的实例。依次类推，类似的 new Date()、new Person() 也会形成一条对应的原型链 。因此，instanceof 只能用来判断两个对象是否属于实例关系， 而不能判断一个对象实例具体属于哪种类型。</p>
</li>
<li>
<p>instanceof 操作符的问题在于，它假定只有一个全局执行环境。如果网页中包含多个框架，那实际上就存在两个以上不同的全局执行环境，从而存在两个以上不同版本的构造函数。如果你从一个框架向另一个框架传入一个数组，那么传入的数组与在第二个框架中原生创建的数组分别具有各自不同的构造函数。</p>
</li>
</ul>
<pre><code class="copyable">variframe = document.createElement('iframe');
document.body.appendChild(iframe);
xArray = window.frames[0].Array;
vararr =newxArray(1,2,3);// [1,2,3]
arr instanceof Array;// false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>针对数组的这个问题，ES5 提供了 Array.isArray() 方法 。该方法用以确认某个对象本身是否为 Array 类型，而不区分该对象在哪个环境中创建。
Array.isArray() 本质上检测的是对象的<code> [[Class]]</code> 值，<code>[[Class]] </code>是对象的一个内部属性，里面包含了对象的类型信息，其格式为<code> [object Xxx]</code> ，Xxx 就是对应的具体类型 。对于数组而言，<code>[[Class]]</code> 的值就是 <code>[object Array]</code> 。</p>
<h2 data-id="heading-3">4、constructor</h2>
<p>当一个函数 F被定义时，JS引擎会为F添加 prototype 原型，然后再在 prototype上添加一个 constructor 属性，并让其指向 F 的引用。如下所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/742ed6bd4f8e4e1db32b2706a45a4674~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当执行 var f = new F() 时，F 被当成了构造函数，f 是F的实例对象，此时 F 原型上的 constructor 传递到了 f 上，因此 f.constructor == F</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46455f0279e54fee98c8830036e88b29~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出，F 利用原型对象上的 constructor 引用了自身，当 F 作为构造函数来创建对象时，原型上的 constructor 就被遗传到了新创建的对象上， 从原型链角度讲，构造函数 F 就是新对象的类型。这样做的意义是，让新对象在诞生以后，就具有可追溯的数据类型。</p>
<p>同样，JavaScript 中的内置对象在内部构建时也是这样做的：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f41b7d59af14ea981a87d8f1c2aba18~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>细节问题：</p>
<ol>
<li>
<p>null 和 undefined 是无效的对象，因此是不会有 constructor 存在的，这两种类型的数据需要通过其他方式来判断。</p>
</li>
<li>
<p>函数的 constructor 是不稳定的，这个主要体现在自定义对象上，当开发者重写 prototype 后，原有的 constructor 引用会丢失，constructor 会默认为 Object</p>
</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc5e50ea741940348ce7b83e0fa9c855~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer">
为什么变成了 Object？</p>
<p>因为 prototype 被重新赋值的是一个 &#123; &#125;， &#123; &#125; 是 new Object() 的字面量，因此 new Object() 会将 Object 原型上的 constructor 传递给 &#123; &#125;，也就是 Object 本身。</p>
<p>因此，为了规范开发，在重写对象原型时一般都需要重新给 constructor 赋值，以保证对象实例的类型不被篡改。</p>
<h2 data-id="heading-4">5、toString</h2>
<p>toString() 是 Object 的原型方法，调用该方法，默认返回当前对象的<code> [[Class]]</code> 。这是一个内部属性，其格式为 <code>[object Xxx]</code> ，其中 Xxx 就是对象的类型。</p>
<p>对于 Object 对象，直接调用 toString()  就能返回 <code>[object Object] </code>。而对于其他对象，则需要通过 call / apply 来调用才能返回正确的类型信息。</p>
<pre><code class="copyable">1. Object.prototype.toString.call('') ;  // [object String]
2. Object.prototype.toString.call(1) ;   // [object Number]
3. Object.prototype.toString.call(true) ;// [object Boolean]
4. Object.prototype.toString.call(Symbol());//[object Symbol]
5. Object.prototype.toString.call(undefined) ;// [object Undefined]
6. Object.prototype.toString.call(null) ;// [object Null]
7. Object.prototype.toString.call(newFunction()) ;// [object Function]
8. Object.prototype.toString.call(newDate()) ;// [object Date]
9. Object.prototype.toString.call([]) ;// [object Array]
10. Object.prototype.toString.call(newRegExp()) ;// [object RegExp]
11. Object.prototype.toString.call(newError()) ;// [object Error]
12. Object.prototype.toString.call(document) ;// [object HTMLDocument]
13. Object.prototype.toString.call(window) ;//[object global] window 是全局对象 global 的引用
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            