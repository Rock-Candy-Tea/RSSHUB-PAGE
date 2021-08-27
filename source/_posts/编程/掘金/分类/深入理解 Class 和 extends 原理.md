
---
title: '深入理解 Class 和 extends 原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75fed1ac94b54776bfa391fb1658b273~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 00:32:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75fed1ac94b54776bfa391fb1658b273~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>ES6 里面的 class 和 extends 大家想必都会用了，但对于他们的实现是否了解呢，babel 后 <code>class</code> 和 <code>extends</code> 又是如何实现的呢？
这节课将带领你深入理解 babel 编译后 <code>class</code> 和 <code>extends</code> 的实现方式。</p>
<blockquote>
<p>注意：本文涉及到 立即执行函数（ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FGlossary%2F%25E7%25AB%258B%25E5%258D%25B3%25E6%2589%25A7%25E8%25A1%258C%25E5%2587%25BD%25E6%2595%25B0%25E8%25A1%25A8%25E8%25BE%25BE%25E5%25BC%258F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Glossary/%E7%AB%8B%E5%8D%B3%E6%89%A7%E8%A1%8C%E5%87%BD%E6%95%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F" ref="nofollow noopener noreferrer">IIFE</a> ）、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Finstanceof" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/instanceof" ref="nofollow noopener noreferrer">instanceof</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2FdefineProperty" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty" ref="nofollow noopener noreferrer">Object.defineProperty</a>，如果还未接触过，建议先点击链接学习。</p>
</blockquote>
<h2 data-id="heading-1">准备工作</h2>
<p>在开始之前，我们需要一个 babel 的环境，方便查看 babel 后的代码，这里我推荐两种方式。</p>
<ol>
<li>chrome 插件 —— <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.cnplugins.com%2Fdevtool%2Fscratch-js-v0-0-23%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.cnplugins.com/devtool/scratch-js-v0-0-23/" ref="nofollow noopener noreferrer">ScratchJS</a>，可以设置 babel 来转换代码，通过点击 Toggle output 就能看到 babel 后的代码。</li>
<li>babel 官网推荐的在线编译工具 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.babeljs.cn%2Frepl" target="_blank" rel="nofollow noopener noreferrer" title="https://www.babeljs.cn/repl" ref="nofollow noopener noreferrer">试一试</a>，可以实时看到转换前后的代码。</li>
</ol>
<p>本文将以 ScratchJS 转换后的代码为例进行代码分析。</p>
<h2 data-id="heading-2">1. class 实现</h2>
<p>先从最简单的 <code>class</code> 开始看，下面这段代码涵盖了使用 <code>class</code> 时所有会出现的情况（静态属性、构造函数、箭头函数）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-keyword">static</span> instance = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getInstance</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">super</span>.instance;
    &#125;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name;
        <span class="hljs-built_in">this</span>.age = age;
    &#125;
    <span class="hljs-function"><span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hi'</span>);
    &#125;
    sayHello = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>);
    &#125;
    sayBye = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'bye'</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而经过 babel 处理后的代码是这样的：</p>
<pre><code class="copyable">'use strict';

var _createClass = function () &#123; 
    function defineProperties(target, props) &#123; 
        for (var i = 0; i < props.length; i++) &#123; 
            var descriptor = props[i]; 
            descriptor.enumerable = descriptor.enumerable || false; 
            descriptor.configurable = true; 
            if ("value" in descriptor) 
                descriptor.writable = true; 
            Object.defineProperty(target, descriptor.key, descriptor); 
        &#125; 
    &#125; 
    return function (Constructor, protoProps, staticProps) &#123; 
        if (protoProps) 
            defineProperties(Constructor.prototype, protoProps); 
        if (staticProps) 
            defineProperties(Constructor, staticProps); 
        return Constructor; 
    &#125;; 
&#125;();

function _classCallCheck(instance, Constructor) &#123; 
    if (!(instance instanceof Constructor)) &#123; 
        throw new TypeError("Cannot call a class as a function"); 
    &#125; 
&#125;

var Person = function () &#123;
  function Person(name, age) &#123;
    _classCallCheck(this, Person);

    this.sayHello = function () &#123;
      console.log('hello');
    &#125;;
    
    this.sayBye = function () &#123;
      console.log('bye');
    &#125;;
    
    this.name = name;
    this.age = age;
  &#125;

  _createClass(Person, [&#123;
    key: 'sayHi',
    value: function sayHi() &#123;
      console.log('hi');
    &#125;
  &#125;]);

  return Person;
&#125;();

Person.instance = null;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最外层的 Person 变量被赋值给了一个立即执行函数，立即执行函数里面返回的是里面的 Person 构造函数，实际上最外层的 Person 就是里面的 Person 构造函数。</p>
<p>在 Person 类上用 <code>static</code> 设置的静态属性instance，在这里也被直接挂载到了 Person 构造函数上。</p>
<h3 data-id="heading-3">1.1 挂载属性方法</h3>
<p>Person 类上各个属性的关系是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75fed1ac94b54776bfa391fb1658b273~tplv-k3u1fbpfcp-watermark.image" alt="image_1dmjbel2cfvdls41h2e1hcmpn39.png-30.9kB" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你是不是很好奇，为什么在 Person 类上面设置的 <code>sayHi</code> 和 <code>sayHello</code>、<code>sayBye</code> 三个方法，编译后被放到了不同的地方处理？</p>
<p>从编译后的代码中可以看到 <code>sayHello</code> 和 <code>sayBye</code> 被放到了 Person 构造函数中定义，而 <code>sayHi</code> 用 <code>_createClass</code> 来处理（<code>_createClass</code> 将 <code>sayHi</code> 添加到了 Person 的原型上面）。</p>
<p>曾经我也以为是 <code>sayHello</code> 使用了箭头函数的缘故才让它最终被绑定到了构造函数里面，后来我看到 <code>sayBye</code> 这种用法才知道这和箭头函数无关。</p>
<p>实际上 <code>class</code> 中定义属性还有一种写法，这种写法和 <code>sayBye</code> 如出一辙，在 babel 编译后会将其属性放到构造函数中，而非原型上面。</p>
<pre><code class="copyable">class Person &#123;
    name = 'tom';
    age = 23;
&#125;
// 等价于
class Person &#123;
    constructor() &#123;
        this.name = 'tom';
        this.age = 23;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们将 <code>name</code> 后面的 <code>'tom'</code> 换成函数呢？甚至箭头函数呢？这不就是 <code>sayBye</code> 和 <code>sayHello</code> 了吗？</p>
<p><em><strong>因此，在 <code>class</code> 中不直接使用 <code>=</code> 来定义的方法，最终都会被挂载到原型上，使用 <code>=</code> 定义的属性和方法，最终都会被放到构造函数中。</strong></em></p>
<h3 data-id="heading-4">1.2 _classCallCheck</h3>
<p><code>Person</code> 构造函数中调用了 <code>_classCallCheck</code> 函数，并将 <code>this</code> 和自身传入进去。
在 <code>_classCallCheck</code> 中通过 <code>instanceof</code> 来进行判断，<code>instance</code> 是否在 <code>Constructor</code> 的原型链上面，如果不在上面则抛出错误。这一步主要是为了避免直接将 Person 类当做函数来调用。
因此，在ES5中构造函数是可以当做普通函数来调用的，但在ES6中的类是无法直接当普通函数来调用的。</p>
<blockquote>
<p>注意：为什么通过 <code>instanceof</code> 可以判断是否将 Person 类当函数来调用呢？
因为如果使用 <code>new</code> 操作符实例化 Person 的时候，那么 <code>instance</code> 就是当前的实例，指向 <code>Person.prototype</code>，<code>instance instanceof Constructor</code> 必然为true。反之，直接调用 Person 构造函数，那么 instance 就不会指向 <code>Person.prototype</code>。</p>
</blockquote>
<h3 data-id="heading-5">1.3 _createClass</h3>
<p>我们再来看 <code>_createClass</code> 函数，这个函数在 Person 原型上面添加了 <code>sayHi</code> 方法。</p>
<pre><code class="copyable">// 创建原型方法
_createClass(Person, [&#123;
    key: 'sayHi',
    value: function sayHi() &#123;
      console.log('hi');
    &#125;
&#125;]);
    
// _createClass也是一个立即执行函数
var _createClass = function () &#123; 
    // 将props属性挂载到目标target上面
    function defineProperties(target, props) &#123; 
        for (var i = 0; i < props.length; i++) &#123; 
            var descriptor = props[i]; 
            descriptor.enumerable = descriptor.enumerable || false; 
            descriptor.configurable = true; 
            if ("value" in descriptor) 
                descriptor.writable = true; 
            // 通过defineProperty来挂载属性
            Object.defineProperty(target, descriptor.key, descriptor); 
        &#125; 
    &#125; 
    // 这个才是“真正的”_createClass
    return function (Constructor, protoProps, staticProps) &#123; 
        // 如果传入了需要挂载的原型方法
        if (protoProps) 
            defineProperties(Constructor.prototype, protoProps); 
        // 如果传入了需要挂载的静态方法
        if (staticProps) 
            defineProperties(Constructor, staticProps); 
        return Constructor; 
    &#125;; 
&#125;();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_createClass</code> 函数接收三个参数，分别是 <code>Constructor</code> （构造函数）、protoProps（需要挂载到原型上的方法）、staticProps（需要挂载到类上的静态方法）。
在接收到参数之后，<code>_createClass</code> 会进行判断如果有 <code>staticProps</code>，则挂载到 <code>Constructor</code> 构造函数上；如果有 <code>protoProps</code> ，那么挂载到 <code>Constructor</code> 原型上面。
这里的挂载函数 <code>defineProperties</code> 是关键，它对传入的 <code>props</code> 进行了遍历，并设置了其 <code>enumerable</code>（是否可枚举） 和 <code>configurable</code>（是否可配置）、<code>writable</code>（是否可修改）等数据属性。
最后使用了 <code>Object.defineProperty</code> 函数来给设置当前对象的属性描述符。</p>
<h2 data-id="heading-6">2. extends 实现</h2>
<p>通过上文对 <code>Person</code> 的分析，相信你已经知道了 ES6 中类的实现，这与ES5中的实现大同小异，接下来我们来具体看一下 <code>extends</code> 的实现。
以下面的 ES6 代码为例：</p>
<pre><code class="copyable">class Child extends Parent &#123;
  constructor(name, age) &#123;
    super(name, age);
    this.name = name;
    this.age = age;
  &#125;
  getName() &#123;
    return this.name;
  &#125;
&#125;

class Parent &#123;
  constructor(name, age) &#123;
    this.name = name;
    this.age = age;
  &#125;
  getName() &#123;
    return this.name;
  &#125;
  getAge() &#123;
    return this.age;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>babel后的代码则是这样的：</p>
<pre><code class="copyable">"use strict";

// 省略 _createClass
// 省略 _classCallCheck

function _possibleConstructorReturn(self, call) &#123; 
    if (!self) &#123; 
        throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); 
    &#125; 
    return call 
        && (typeof call === "object" || typeof call === "function") ? call : self; 
&#125;

function _inherits(subClass, superClass) &#123; 
    if (typeof superClass !== "function" && superClass !== null) &#123; 
        throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); 
    &#125; 
    subClass.prototype = Object.create(superClass && superClass.prototype, &#123; 
        constructor: &#123; 
            value: subClass, 
            enumerable: false, 
            writable: true, 
            configurable: true 
        &#125; 
    &#125;); 
    if (superClass) 
        Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; 
&#125;

var Child = function (_Parent) &#123;
  _inherits(Child, _Parent);

  function Child(name, age) &#123;
    _classCallCheck(this, Child);

    var _this = _possibleConstructorReturn(this, Object.getPrototypeOf(Child).call(this, name, age));

    _this.name = name;
    _this.age = age;
    return _this;
  &#125;

  _createClass(Child, [&#123;
    key: "getName",
    value: function getName() &#123;
      return this.name;
    &#125;
  &#125;]);

  return Child;
&#125;(Parent);

// 省略 Parent（类似上面的 Person 代码）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以清楚地看到，继承是通过<code>_inherits</code>实现的。
为了方便理解，我这里整理了一下原型链的关系：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/964c3a1bc8c0465aa108adf382b427dd~tplv-k3u1fbpfcp-watermark.image" alt="image_1dmec296p60q11bp1f8c1rid1rc52a.png-43.1kB" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除去一些无关紧要的代码，最终的核心实现代码就只有这么多：</p>
<pre><code class="copyable">var Child = function (_Parent) &#123;

  _inherits(Child, _Parent);

  function Child(name, age) &#123;

    var _this = _possibleConstructorReturn(this, Object.getPrototypeOf(Child).call(this, name, age));

    _this.name = name;
    _this.age = age;
    return _this;
  &#125;

  return Child;
&#125;(Parent);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和前面的 <code>Person</code> 类实现有所不同的地方是，在 <code>Child</code> 方法中增加调用了 <code>_inherits</code>，还有在设置 <code>name</code> 和 <code>age</code> 属性的时候，使用的是执行 <code>_possibleConstructorReturn</code> 后返回的 <code>_this</code>，而非自身的 <code>this</code>，我们就重点分析这两步。</p>
<h3 data-id="heading-7">2.1 _inherits</h3>
<p>先来看_inherits函数的实现代码：</p>
<pre><code class="copyable">function _inherits(subClass, superClass) &#123; 
    // 如果有一个不是函数，则抛出报错
    if (typeof superClass !== "function" && superClass !== null) &#123; 
        throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); 
    &#125; 
    // 将 subClass.prototype 设置为 superClass.prototype 的实例
    subClass.prototype = Object.create(superClass && superClass.prototype, &#123; 
        constructor: &#123; 
            value: subClass, 
            enumerable: false, 
            writable: true, 
            configurable: true 
        &#125; 
    &#125;); 
    // 将 subClass 设置为 superClass 的实例（优先使用 Object.setPrototypeOf）
    if (superClass) 
        Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_inherits</code> 函数接收两个参数，分别是 <code>subClass</code> （子构造函数）和 <code>subClass</code> （父构造函数），将这个函数做的事情稍微做一下梳理。</p>
<ol>
<li>设置 <code>subClass.prototype</code> 的 <code>[[Prototype]]</code>指向 <code>superClass.prototype</code> 的 <code>[[Prototype]]</code></li>
<li>设置 <code>subClass</code> 的 <code>[[Prototype]]</code> 指向 <code>superClass</code></li>
</ol>
<p>在《深入理解类和继承》一文中，曾经提到过 ES5 中的寄生组合式继承，<code>extends</code> 的实现与寄生组合式继承实则大同小异，仅仅只增加了第二步操作。</p>
<h3 data-id="heading-8">2.2 _possibleConstructorReturn</h3>
<p>在 <code>Child</code> 中调用了 <code>_possibleConstructorReturn</code> 函数，将 <code>this</code> 和 <code>Object.getPrototypeOf(Child).call(this, name, age))</code> 传了进去。
这个 <code>this</code> 我们很容易理解，就是构造函数的 <code>this</code>，但后面这么长的一串又是什么意思呢？
刚刚在 <code>_inherits</code> 中设置了 <code>Child</code> 的 <code>[[Prototype]]</code> 指向了 <code>Parent</code>，因此可以将后面这串代码简化为 <code>Parent.call(this, name, age)</code>。
这样你是不是就很熟悉了？这不就是组合继承中的执行一遍父构造函数吗？
那么 <code>Parent.call(this, name, age)</code> 执行后返回了什么呢？
正常情况下，应该会返回 undefined，但不排除 <code>Parent</code> 构造函数中直接返回一个对象或者函数的可能性。
*** 小课堂：**
在构造函数中，如果什么也没有返回或者返回了原始值，那么默认会返回当前的 <code>this</code>；而如果返回的是引用类型，那么最终实例化后的实例依然是这个引用类型（仅相当于对这个引用类型进行了扩展）。</p>
<pre><code class="copyable">const obj = &#123;&#125;;
function Parent(name) &#123;
    this.name = name;
    return obj;
&#125;
const p = new Parent('tom');
obj.name; // 'tom'
p === obj; // true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有 <code>self</code>，这里就会直接抛出错误，提示 <code>super</code> 函数还没有被调用。
最后会对 <code>call</code> 进行判断，如果 <code>call</code> 为引用类型，那么返回 <code>call</code>，否则返回 <code>self</code>。</p>
<blockquote>
<p>注意：<code>call</code> 就是 <code>Parent.call(this, name, age)</code> 执行后返回的结果。</p>
</blockquote>
<pre><code class="copyable">function _possibleConstructorReturn(self, call) &#123; 
    if (!self) &#123; 
        throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); 
    &#125; 
    return call 
        && (typeof call === "object" || typeof call === "function") ? call : self; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>Child</code> 方法中，最终拿到 <code>_possibleConstructorReturn</code> 执行后的结果作为新的 <code>this</code> 来设置构造函数里面的属性。</p>
<blockquote>
<p>思考题：如果直接用 <code>this</code>，而不是 <code>_this</code>，会出现什么问题？</p>
</blockquote>
<h2 data-id="heading-9">总结</h2>
<p>ES6 中提供的 <code>class</code> 和 <code>extends</code> 本质上只是语法糖，底层的实现原理依然是构造函数和寄生组合式继承。
所以对于一个合格的前端工程师来说，即使 ES6 已经到来，对于 ES5 中的这些基础原理我们依然需要好好掌握。</p></div>  
</div>
            