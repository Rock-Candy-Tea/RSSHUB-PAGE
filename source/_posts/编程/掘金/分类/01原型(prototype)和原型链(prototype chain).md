
---
title: '01.原型(prototype)和原型链(prototype chain)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b3491b8fe6848b6964ee72325e4f7e8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 18:17:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b3491b8fe6848b6964ee72325e4f7e8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>[toc]</p>
<h2 data-id="heading-0">一.原型</h2>
<p><em>1. 函数的prototype属性(图)</em></p>
<p>** 每个函数都有一个prototype属性, 它默认指向一个Object空对象(即称为: 原型对象)*</p>
<p>** 原型对象中有一个属性constructor, 它指向函数对象*</p>
<p><em>2. 给原型对象添加属性(一般都是方法)</em></p>
<p>** 作用: 函数的所有实例对象自动拥有原型中的属性(方法)*</p>
<pre><code class="copyable"> <script type="text/javascript">
      // 每个函数都有一个prototype属性, 它默认指向一个Object空对象(即称为: 原型对象)
      console.log(Date.prototype, typeof Date.prototype)

      function Fun() &#123;

      &#125;
      console.log(Fun.prototype) // 默认指向一个Object空对象(没有我们的属性)

      // // 原型对象中有一个属性constructor, 它指向函数对象
      console.log(Date.prototype.constructor === Date)
      console.log(Fun.prototype.constructor === Fun)

      // //给原型对象添加属性(一般是方法) ===>实例对象可以访问
      Fun.prototype.test = function () &#123;
        console.log('test()')
      &#125;
      var fun = new Fun()
      fun.test()
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">1.1 prototype(原型)和_ _ proto _ _(隐式)</h3>
<p>在JavaScript中，每个函数都有一个prototype属性，这个属性指向函数的原型对象。</p>
<p>1.<em>每个函数function都有一个prototype，即显式原型(属性)</em></p>
<p><em>2. 每个实例对象都有一个<code>__proto__</code>，可称为隐式原型(属性)</em></p>
<p><em>3. 对象的隐式原型的值为其对应构造函数的显式原型的值</em></p>
<pre><code class="copyable"> // 3. 对象的隐式原型的值为其对应构造函数的显式原型的值
console.log(Fn.prototype === fn.__proto__) // true
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2 理解原型的内存图</h3>
<pre><code class="copyable"><!--
    1. 每个函数function都有一个prototype，即显式原型(属性)
    2. 每个实例对象都有一个__proto__，可称为隐式原型(属性)
    3. 对象的隐式原型的值为其对应构造函数的显式原型的值
    4. 内存结构(图)
    5. 总结:
      * 函数的prototype属性: 在定义函数时自动添加的, 默认值是一个空Object对象
      * 对象的__proto__属性: 创建对象时自动添加的, 默认值为构造函数的prototype属性值
      * 程序员能直接操作显式原型, 但不能直接操作隐式原型(ES6之前)
    -->
    <script type="text/javascript">
      //一.定义构造函数
      function Fn() &#123; // 内部语句: this.prototype = &#123;&#125;

      &#125;
      // 1. 每个函数function都有一个prototype，即显式原型属性, 默认指向一个空的Object对象
      console.log(Fn.prototype)
      // 2. 每个实例对象都有一个__proto__，可称为隐式原型
      //二.创建实例对象
      var fn = new Fn() // 内部语句: this.__proto__ = Fn.prototype
      console.log(fn.__proto__)
      // 3. 对象的隐式原型的值为其对应构造函数的显式原型的值
      console.log(Fn.prototype === fn.__proto__) // true
      //三.给原型添加方法
      Fn.prototype.test = function () &#123;
        console.log('test()')
      &#125;
      //四.通过实例调用原型的方法
      fn.test() //test()
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b3491b8fe6848b6964ee72325e4f7e8~tplv-k3u1fbpfcp-zoom-1.image" alt="prototypeMemoryMap" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">1.3 原型的基本使用</h3>
<p>通常我们在使用原型写代码的时候，我们都会这样做：</p>
<p>==1.在构造函数里面写属性。==</p>
<p>==2.在原型对象上写方法。==</p>
<p>这样做就避免了<code>浪费内存</code>的问题</p>
<h3 data-id="heading-4">1.4 构造函数和实例对象，原型对象的三角关系</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13ae1c63fa84f25afeb88789d4549f3~tplv-k3u1fbpfcp-zoom-1.image" alt="threeAngle" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">/*
    原型:
        1.是构造函数的一个属性，是一个对象，是在我们创建构造函数的时候 系统 自动分配的
           作用是给 构造函数的 实例对象 提供方法
        2.可以通过构造函数.prototype 得到   

     总结：
         1. 原型对象 - 作用是给实例对象提供方法
         2. 构造函数.prototype 和 实例对象.__proto__
         3. 有prorotype属性是 构造函数  ，有 __proto__ 属性 就是 实例对象    
    */</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, gender</span>) </span>&#123;
      <span class="hljs-built_in">this</span>.name = name
      <span class="hljs-built_in">this</span>.age = age
      <span class="hljs-built_in">this</span>.gender = gender
    &#125;

    Person.prototype.sayHi = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'sayHi被调用了'</span>);
    &#125;
    <span class="hljs-comment">// console.dir(Person)</span>
    <span class="hljs-built_in">console</span>.log(Person.prototype);
    <span class="hljs-comment">// 2.证明 原型的 constructor 属性  就是  构造函数</span>
    <span class="hljs-built_in">console</span>.log(Person.prototype.constructor === Person); <span class="hljs-comment">//true</span>

    <span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> Person()
    <span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> Person()

    <span class="hljs-comment">// p1.sayHi()</span>
    <span class="hljs-comment">// p2.sayHi()</span>
    <span class="hljs-comment">// console.log(p1);</span>
    <span class="hljs-comment">// console.log(p2);</span>

    <span class="hljs-comment">//1.证明 实例对象的 __proto__ 就是 构造函数的prototype</span>
    <span class="hljs-comment">// console.log(p1.__proto__ === p2.__proto__); //true</span>
    <span class="hljs-comment">// console.log(p1.__proto__ === Person.prototype); //true</span>
    <span class="hljs-comment">// console.log(p2.__proto__ === Person.prototype); //true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a481d02ad06f4115bce8c6f30c2255d5~tplv-k3u1fbpfcp-zoom-1.image" alt="prototype" loading="lazy" referrerpolicy="no-referrer"></p>
<p>原型其实就是一个在浏览器中，每当创建一个构造函数，就会自动分配好的对象。</p>
<p>这个对象的作用，就是给实现对象共享方法用的。</p>
<p>我们可以通过两个方式访问到这个对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span>从构造函数访问原型：构造函数.prototype
<span class="hljs-number">2.</span>从实例对象访问原型：实例对象.__proto__
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.5 原型总结</h3>
<ol>
<li>原型其实就是一个对象，存在于内存中，我们看不见</li>
<li>原型可以给构造函数的实例对象提供方法</li>
<li><code>构造函数.prototype</code> 和 <code>实例对象.__proto__</code> 都可以访问到原型对象</li>
<li>有<code>prototype</code>属性的是构造函数，有<code>__proto__</code>属性的是实例对象</li>
<li><em>函数的prototype属性: 在定义函数时自动添加的, 默认值是一个空Object对象</em></li>
<li>对象的<code>__proto__</code>属性: 创建对象时自动添加的, 默认值为构造函数的prototype属性值</li>
<li>程序员能直接操作显式原型, 但不能直接操作隐式原型(ES6之前)</li>
</ol>
<h3 data-id="heading-6">1.6 原型的原理</h3>
<p>原型之所以会比单独的构造函数好，是因为它在内存这的唯一性，于是在它身上的方法也具备唯一性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80ab4190808441f6ac279487b04b18c7~tplv-k3u1fbpfcp-zoom-1.image" alt="原型方法所在的位置" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时无论我们new多少个实例对象，它们都会在调用方法的时候，沿着它的<code>__proto__</code>属性找到原型对象，然后调用原型对象上的对应的方法，因为原型对象只会有一个，所以方法对应的函数对象也就只会有一个，就解决了浪费内存的问题。</p>
<p>而此时在内存中，已经在多个对象之前存在这样一个关联关系</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c29f246de00481084813eaa38aa6359~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210311095926999" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">二.封装一个简单的jQuery</h2>
<p>jQuery中就是使用了原型来实现了很多代码的封装，所以我们利用所学的原型的知识，模仿一下jQuery的代码封装。(这个过程比较复杂，我们可以先不看，在上课的时候再慢慢讲)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*    简单的jQuery包含的功能：        1.获取元素  $(选择器)        2.注册事件  jq对象.on()        3.修改样式  jq对象.css()    目的：        jq对象.on(事件类型,处理程序)        jQuery.prototype.on = function()&#123;&#125;*/</span><span class="hljs-comment">// 面向对象，为了区分对象，先 写 构造函数function jQuery(selector) &#123;  // 得到一个伪数组  var dom = document.querySelectorAll(selector);// 这是一个 NodeList 伪数组  // 我们自己造一个  for (var i = 0; i < dom.length; i++) &#123;    this[i] = dom[i];  &#125;  //伪数组都要长度  this.length = dom.length;&#125;// 封装css方法jQuery.prototype.css = function (prop, value) &#123;  // css方法有多个用法，可以通过判断 参数个数区分  if (arguments.length === 2) &#123;    // 把 伪数组里面的所有元素都修改    // 方法里面的this，是实例对象    // this是一个伪数组，当然要遍历    for (var i = 0; i < this.length; i++) &#123;      this[i].style[prop] = value;    &#125;  &#125; else if (arguments.length === 1) &#123;    //此时 prop 应该是一个对象,需要从prop里面得到每个键值对    for (var key in prop) &#123;      for (var i = 0; i < this.length; i++) &#123;        this[i].style[key] = prop[key];      &#125;    &#125;  &#125;  // 为了支持链式编程，返回一个jq对象  return this;&#125;// 封装on方法 - 实现注册事件jQuery.prototype.on = function (type, fn) &#123;  // 判断 当前的浏览器 是否支持  addEventListener 方法  // 事件源.addEventListener(事件类型,处理程序)  for (var i = 0; i < this.length; i++) &#123;    if (typeof this[i].addEventListener === 'function') &#123;      this[i].addEventListener(type, fn);    &#125; else &#123;      // ie 的注册事件的方法 attachEvent      this[i].attachEvent('on' + type, fn);    &#125;  &#125;  return this&#125;// 为了简单jQuery的使用，再包一层函数function $(selector) &#123;  return new jQuery(selector);&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">三.原型链</h2>
<h3 data-id="heading-9">3.1 什么是原型链？</h3>
<p>==在JavaScript 中，每个对象都有一个指向它的原型（prototype）对象的内部链接。这个原型对象又有自己的原型，直到某个对象的原型为 null 为止（也就是不再有原型指向），组成这条链的最后一环。==这种一级一级的链结构就称为<strong>原型链（prototype chain）</strong>。</p>
<p>事实上在内存中，存在多个原型对象，多个原型对象之前存在着一个链式关系，这个链式关系我们称为：<code>原型链</code></p>
<p>原型链是javascript特意为了实现面向对象的继承而设计的一种对象结构，这样可以解决代码的重复利用的问题。</p>
<p>当我们把构造函数的原型输出，再展开查看，发现原型对象上面也有<code>__proto__</code>属性，也就是说其实原型对象也是一个实例对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name,age,gender</span>)</span>&#123; &#125;<span class="hljs-built_in">console</span>.log(Person.prototype)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/123448c346144c5f9c093e32e2ba93c6~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210309183856963" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而原型对象的<code>__proto__</code>属性我们发现它也是一个对象，此时在内存中就至少存在这样一个链式关系</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5f7ef7743b049e4a362f8bd041dc30f~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210309184341705" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们就称这样的结构关系为原型链</p>
<h3 data-id="heading-10">3.2 原型链的作用</h3>
<p>我们在上方提到，==原型链是javascript专门为了实现继承而设计的==，我们先不管继承是什么，可以先看看它这样设计的用处。</p>
<p>前方已经学习过，原型对象的作用就为了给实例对象提供方法的，那么也就是说 <code>对象.__proto__</code> 上面的方法，对象就可以使用。同理，现在在原型对象(<code>对象.__proto__</code>)的上面的<code>__proto__</code>属性所指向的对象，它身上的方法能否被原型对象所使用呢？当然！</p>
<p>我们先看看在这个原型的原型上面有什么方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(Person.prototype.__proto__)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86e9ad37312544659d40cc368684131d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210309185010758" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到在原型的原型身上有一个<code>toString</code>方法,我们尝试调用一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(Person.prototype.toString()); <span class="hljs-comment">// 结果为： [object Object]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见<code>__proto__</code>属性身上的方法确实是可以被对象所使用的。</p>
<p>那么这个时候我们思考一个问题： Person构造的函数的实例对象能不能调用这个<code>toString()</code>方法呢？毕竟Person实例的<code>__proto__</code>属性是 Person.prototype,Person.prototype的<code>__proto__</code>属性的方法也相当于是Person.prototype的方法，那么实例对象访问它的<code>__proto__</code>的方法，应该也可以</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person()<span class="hljs-built_in">console</span>.log(p.toString()); <span class="hljs-comment">// 结果： [object Object]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<code>toString</code>方法确实通过多个对象之间的 <code>__proto__</code> 关系被重用了。</p>
<blockquote>
<p>小结：原型上，上游对象的方法可以被下游对象直接调用</p>
</blockquote>
<h3 data-id="heading-11">3.3 原型链结构</h3>
<p>结合之前得到的Perosn与其原型之间的关系，我们可以得到一个更加完整的关系图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e2acdbbdd554e648cca7c7930416ebe~tplv-k3u1fbpfcp-zoom-1.image" alt="70c34794aabf0c34d000e3cc2d9aab59.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8688c31992f84e84a665b79bc11334f5~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210311101213624" loading="lazy" referrerpolicy="no-referrer"></p>
<p>于是我们可以思考一个问题，Object原型对象上面还有没有<code>__proto__</code>属性呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.__proto__) <span class="hljs-comment">// null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说原型链的关系到了Object原型这，再往上就没有了 ———— 原型链的尽头是 null</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffa65c07a7db4fe980770dff6905534d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210311102138980" loading="lazy" referrerpolicy="no-referrer"></p>
<p><span>值得注意的是,这套东西不是我们发现的，而是js作者特意为了能够实现代码复用而设计出来的特殊结构，我们只不过是以推导的方式来带领大家学习</span></p>
<p>其实原型链就是我们在js中实现继承的基本原理</p>
<blockquote>
<p>小结：</p>
<ol>
<li>原型链是本来就存在的，人为故意设计的</li>
<li>原型链是指对象之间通过<code>__proto__</code>属性关联起来的关系</li>
<li>原型链末端的对象可以访问上游的对象的方法</li>
</ol>
</blockquote>
<h3 data-id="heading-12">3.4 原型链成员访问规则</h3>
<blockquote>
<p>对象成员 == 对象属性+对象方法</p>
</blockquote>
<p>原型链末端的对象可以访问上游的对象的方法，其实也是有一定的访问规则的。和作用域类似的，原型链上的成员也遵循**"就近原则"**</p>
<ul>
<li>读取对象的属性值时：</li>
</ul>
<ol>
<li>当访问一个对象的成员时，如果这个对象有自己的对应成员，优先使用自己的</li>
<li>当自己没有对应的成员时，会沿着原型链查找，找到一个最近的</li>
<li>如果直到Object.prototype身上也没有，返回undefined</li>
</ol>
<ul>
<li>
<p>设置对象的属性值时：==不会查找原型链, 如果当前对象中没有此属性, 直接添加此属性并设置其值==</p>
</li>
<li>
<p>==方法一般定义在原型中, 属性一般通过构造函数定义在对象本身上==</p>
<pre><code class="copyable">   <!--
      1. 读取对象的属性值时: 会自动到原型链中查找
      2. 设置对象的属性值时: 不会查找原型链, 如果当前对象中没有此属性, 直接添加此属性并设置其值
      3. 方法一般定义在原型中, 属性一般通过构造函数定义在对象本身上
    -->
    <script type="text/javascript">
      //例子一：
      function Fn() &#123;

      &#125;
      Fn.prototype.a = 'xxx'
      var fn1 = new Fn()
      console.log(fn1.a, fn1) //xxx Fn&#123;&#125;

      var fn2 = new Fn()
      fn2.a = 'yyy'
      console.log(fn1.a, fn2.a, fn2) //xxx yyy Fn&#123;a:'yyy'&#125;


      //例子二：
      function Person(name, age) &#123;
        this.name = name
        this.age = age
      &#125;
      Person.prototype.setName = function (name) &#123;
        this.name = name
      &#125;
      var p1 = new Person('Tom', 12)
      p1.setName('Bob')
      console.log(p1) //&#123;'Bob',12&#125;

      var p2 = new Person('Jack', 12)
      p2.setName('Cat')
      console.log(p2) //&#123;'Cat',12&#125;
      console.log(p1.__proto__ === p2.__proto__) // true
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-13">3.5 原型链案例分析(==构造函数/原型/实例对象的关系(图解)==)</h3>
<pre><code class="copyable">  <!--
      1. 原型链(图解)
        * 访问一个对象的属性时，
          * 先在自身属性中查找，找到返回
          * 如果没有, 再沿着__proto__这条链向上查找, 找到返回
          * 如果最终没找到, 返回undefined
        * 别名: 隐式原型链
        * 作用: 查找对象的属性(方法)
      2. 构造函数/原型/实体对象的关系(图解)
      3. 构造函数/原型/实体对象的关系2(图解)
-->
    <script type="text/javascript">
      // console.log(Object)
      //console.log(Object.prototype)
      //console.log(Object.prototype.__proto__)

      function Fn() &#123;
        this.test1 = function () &#123;
          console.log('test1()')
        &#125;
      &#125;
      //console.log(Fn.prototype)
      Fn.prototype.test2 = function () &#123;
        console.log('test2()')
      &#125;

      var fn = new Fn()

      fn.test1() //test1()
      fn.test2() //test2()
      console.log(fn.toString()) //[object object]
      console.log(fn.test3) //undefined
      //fn.test3()


      /*
      1. 函数的显示原型指向的对象默认是空Object实例对象(但Object不满足)
       */
      console.log(Fn.prototype instanceof Object) // true
      console.log(Object.prototype instanceof Object) // false
      console.log(Function.prototype instanceof Object) // true
      /*
      2. 所有函数都是Function的实例(包含Function)
      */
      console.log(Function.__proto__ === Function.prototype)
      /*
      3. Object的原型对象是原型链尽头
       */
      console.log(Object.prototype.__proto__) // null
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/768ae032f89b45ca860ab1f03263e971~tplv-k3u1fbpfcp-zoom-1.image" alt="prototypeChain" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">3.6 ==构造函数/原型/实例对象的关系(图解)==</h3>
<pre><code class="copyable">var o1=new Object();
var o2=&#123; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07379864d6024241975362d68ac1d42c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210619160307233" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-15">3.7 ==构造函数/原型/实例对象的关系2(图解)==</h3>
<pre><code class="copyable">function Foo( )&#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da6b5a591c5a4b859292248ac7173bad~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06c5ddbe5cd842a29e1498aab7a4beaf~tplv-k3u1fbpfcp-zoom-1.image" alt="prototypeMap" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">四.instanceOf关键字</h2>
<p>1.instanceof是如何判断的?</p>
<p>表达式: A instanceof B</p>
<p>instance关键字规则: ==<strong>如果B函数的显式原型对象在A对象的原型链上, 返回true, 否则返回false</strong>==</p>
<p>2.Function是通过new自己产生的实例</p>
<h3 data-id="heading-17">4.1 案例一：</h3>
<pre><code class="copyable">function Foo() &#123;&#125;
var f1 = new Foo()
console.log(f1 instanceof Foo) // true
console.log(f1 instanceof Object) // true
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/faab097331714becbc975465a190929d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210620084342153" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">4.2 案例二：</h3>
<pre><code class="copyable"> console.log(Object instanceof Function) // true
 console.log(Object instanceof Object) // true
 console.log(Function instanceof Function) // true
 console.log(Function instanceof Object) // true

 function Foo() &#123;&#125;
 console.log(Object instanceof Foo) // false
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0af5a196648446bd9c0c517d26d48b63~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210620085852692" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">五.面试题</h2>
<h3 data-id="heading-20">5.1 面试题一：熟悉以后，就不需要画图，要一眼看懂</h3>
<pre><code class="copyable"> function A() &#123;

      &#125;
      A.prototype.n = 1

      var b = new A()

      A.prototype = &#123;
        n: 2,
        m: 3
      &#125;

      var c = new A()
      console.log(b.n, b.m, c.n, c.m) //2 undefined 2 3
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9558ace0008842898251d08d9459b847~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210620095908102" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">5.2 面试题二：</h3>
<pre><code class="copyable">function F() &#123;&#125;
Object.prototype.a = function () &#123;
      console.log('a()')
&#125;
Function.prototype.b = function () &#123;
      console.log('b()')
&#125;

var f = new F()
f.a()
f.b()//报错
F.a()
F.b()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><span>这道题的关键在于要理解下面的终极原型链图</span></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dab630a5496f4719ba41ff266bee1bcc~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210620085852692" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            