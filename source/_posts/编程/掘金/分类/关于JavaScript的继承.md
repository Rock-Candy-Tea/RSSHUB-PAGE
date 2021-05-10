
---
title: '关于JavaScript的继承'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d33fefaa2e0e449eb2b8a67831497e02~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 08 May 2021 19:05:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d33fefaa2e0e449eb2b8a67831497e02~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. 类式继承</h3>
<p>首先我们从原型中来看</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span>(<span class="hljs-params"></span>)</span>&#123; &#125;
<span class="hljs-keyword">let</span> a1 = <span class="hljs-keyword">new</span> Animal()

<span class="hljs-comment">// 每一个对象属性，其隐式原型全部指向其父级的prototype原型 </span>
<span class="hljs-comment">// 因为Animal是通过function构造出来的，所以其隐式原型指向Function的原型</span>
<span class="hljs-built_in">console</span>.log(Animal.__proto__ === <span class="hljs-built_in">Function</span>.prototype);    <span class="hljs-comment">//true</span>
<span class="hljs-comment">// 根据Function原型和Object对象的原型关系，我们可以得到 这样一层关系</span>
<span class="hljs-built_in">console</span>.log(Animal.prototype.__proto__ === <span class="hljs-built_in">Object</span>.prototype);   <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 之后可以的到任何一个实例化的对象 其隐式原型(__proto__)都是指向其父级的原型(prototype)的</span>
<span class="hljs-built_in">console</span>.log(a1.__proto__ === Animal.prototype);   <span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(a1 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>);   <span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(a1.__proto__ === <span class="hljs-built_in">Object</span>.protortpe)   <span class="hljs-comment">// false</span>

<span class="hljs-comment">// 基本结论： 任何一个实例化的对象其隐式原型(__proto__)都指向其父级的原型(protorypr)</span>
<span class="hljs-comment">// 为了证实一下</span>
<span class="hljs-keyword">let</span> temp = &#123;&#125;
<span class="hljs-built_in">console</span>.lot(temp.__proto__ === <span class="hljs-built_in">Object</span>.prototype)  <span class="hljs-comment">//true</span>

<span class="hljs-comment">// 原型链的产生，以及第一种方式继承的出现</span>
<span class="hljs-built_in">console</span>.log(a1.__proto__.__proto__ === <span class="hljs-built_in">Object</span>.prototype);   <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一种继承方式 :让子对象的原型定向为一个父级的实例，这样子类的__proto__就指向了父类</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span> (<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'animal'</span> 
    <span class="hljs-built_in">this</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    &#125;
    <span class="hljs-built_in">this</span>.setName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>)</span>&#123;
      <span class="hljs-built_in">this</span>.name = name
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;      &#125;

Cat.prototype = <span class="hljs-keyword">new</span> Animal()

<span class="hljs-keyword">const</span> RagaMuffin = <span class="hljs-keyword">new</span> Cat()
RagaMuffin.say()      <span class="hljs-comment">// animal</span>
RagaMuffin.setName(<span class="hljs-string">'褴褛猫'</span>)
RagaMuffin.say()      <span class="hljs-comment">// 褴褛猫</span>
<span class="hljs-built_in">console</span>.log(RagaMuffin);
<span class="hljs-comment">// 缺点: 父级属性共享，当修改父级属性会影响到其他实例</span>
RagaMuffin.__proto__.name = <span class="hljs-string">'褴褛猫'</span>

<span class="hljs-keyword">const</span> Tabby = <span class="hljs-keyword">new</span> Cat()
Tabby.say()           <span class="hljs-comment">// 褴褛猫</span>
Tabby.setName(<span class="hljs-string">"虎斑猫"</span>)
Tabby.say()           <span class="hljs-comment">// 虎斑猫</span>
<span class="hljs-built_in">console</span>.log(Tabby);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：</p>
<ol>
<li>直观简便的继承了父级的方法</li>
</ol>
<p>缺点:</p>
<ol>
<li>无法接收子类的动态参数</li>
<li>父级属性共享</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d33fefaa2e0e449eb2b8a67831497e02~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">2.构造函数继承</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span> (<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name 
    <span class="hljs-built_in">this</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    &#125;
&#125;
<span class="hljs-comment">// 对原型添加方法</span>
Animal.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name , <span class="hljs-string">'吃鱼'</span>);
&#125;
<span class="hljs-comment">// 创建子类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;    
    Animal.call(<span class="hljs-built_in">this</span>, name)
&#125;

<span class="hljs-keyword">const</span> RagaMuffin = <span class="hljs-keyword">new</span> Cat(<span class="hljs-string">'褴褛猫'</span>)
RagaMuffin.say()      <span class="hljs-comment">// 褴褛猫</span>
RagaMuffin.eat()      <span class="hljs-comment">// RagaMuffin.eat is not a function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3913b1b8a7e04934aed725881f95f56b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>缺点：</p>
<ol>
<li>构造函数继承没能继承父级原型上的方法</li>
</ol>
<h3 data-id="heading-2">3. 组合继承</h3>
<p>结合上述两种继承方式的方法叫做组合继承</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span> (<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name 
    <span class="hljs-built_in">this</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    &#125;
    Animal.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name , <span class="hljs-string">'吃鱼'</span>);
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;    
    Animal.call(<span class="hljs-built_in">this</span>, name)
  &#125;

  Cat.prototype = <span class="hljs-keyword">new</span> Animal()
  <span class="hljs-keyword">const</span> RagaMuffin = <span class="hljs-keyword">new</span> Cat(<span class="hljs-string">'褴褛猫'</span>)
  <span class="hljs-built_in">console</span>.loe(RageMyffin)   
  RagaMuffin.say()      <span class="hljs-comment">// 褴褛猫</span>
  RagaMuffin.eat()      <span class="hljs-comment">// 褴褛猫 吃鱼</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：</p>
<ol>
<li>子类无法传递动态参数给父类</li>
<li>父类的构造函数调用了两次</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3765ee9fe4b340e4beba1235943e37d9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">4. 原型式继承</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createObject</span>(<span class="hljs-params">o</span>) </span>&#123;
    <span class="hljs-comment">// 创建临时类</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    &#125;
    <span class="hljs-comment">// 修改类的原型为o, 于是f的实例都将继承o上的方法</span>
    f.prototype = o
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> f()
&#125;

<span class="hljs-keyword">const</span> obj = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'chang'</span>
&#125;
<span class="hljs-keyword">const</span> chang = createObject(obj)
<span class="hljs-built_in">console</span>.log(chang.name);        <span class="hljs-comment">// chang</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：  共享了属性和方法，没有解决类式继承的缺点</p>
<h3 data-id="heading-4">5.寄生继承</h3>
<p>创建一个仅用于封装继承过程的函数，该函数在内部以某种形式来做增强对象，最后返回对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAnother</span>(<span class="hljs-params">original</span>) </span>&#123;
  <span class="hljs-keyword">var</span> clone = <span class="hljs-built_in">Object</span>.create(original);    <span class="hljs-comment">//通过调用函数创建一个新对象</span>
  clone.say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;               <span class="hljs-comment">//以某种方式来增强这个对象</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello'</span>);
  &#125;;
  <span class="hljs-keyword">return</span> clone;                        <span class="hljs-comment">//返回这个对象</span>
&#125;

<span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'chang'</span>,
  <span class="hljs-attr">testArr</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
&#125;

<span class="hljs-keyword">const</span> newObj = createAnother(obj)
<span class="hljs-built_in">console</span>.log(newObj.name);     <span class="hljs-comment">// chang</span>
newObj.say()                  <span class="hljs-comment">// Hello</span>
newObj.testArr.push(<span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(newObj.testArr);  <span class="hljs-comment">//(4) [1, 2, 3, 4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6. 寄生组合继承</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inherit</span>(<span class="hljs-params">child, parent</span>) </span>&#123;
      <span class="hljs-comment">// 获取父级的原型</span>
      <span class="hljs-keyword">const</span> parent_proto = <span class="hljs-built_in">Object</span>.create(parent.prototype)
      <span class="hljs-comment">// 子类继承父类的原型</span>
      child.prototype = parent_proto
      <span class="hljs-comment">// 父类的构造函数指向child,防止污染</span>
      parent_proto.constructor = child
    &#125;

    <span class="hljs-comment">// 父类</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span>(<span class="hljs-params">name</span>) </span>&#123;
      <span class="hljs-built_in">this</span>.name = name
      <span class="hljs-built_in">this</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
      &#125;
      Animal.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name, <span class="hljs-string">'吃鱼'</span>);
      &#125;
    &#125;


    <span class="hljs-comment">// 子类</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>) </span>&#123;
      Animal.call(<span class="hljs-built_in">this</span>, name)
    &#125;

    inherit(Cat, Animal)


    <span class="hljs-keyword">const</span> RagaMuffin = <span class="hljs-keyword">new</span> Cat(<span class="hljs-string">'褴褛猫'</span>)
    <span class="hljs-built_in">console</span>.log(RagaMuffin);
    RagaMuffin.say()      <span class="hljs-comment">// 褴褛猫</span>
    RagaMuffin.eat()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1e9b16a3db94e5195f50c1f0719f596~tplv-k3u1fbpfcp-watermark.image" alt="1)RDR7TG3MQZQ`6$H2Y95N8.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            