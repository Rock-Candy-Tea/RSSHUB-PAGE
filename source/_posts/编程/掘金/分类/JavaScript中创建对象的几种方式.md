
---
title: 'JavaScript中创建对象的几种方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=768'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 01:58:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=768'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">JavaScript中创建对象的几种方式</h1>
<p>  前端学习笔记系列，内容参考自JavaScript高级程序设计（第四版）
首先先说本文会介绍到的几种创建对象的方法：</p>
<ol>
<li>工厂模式</li>
<li>构造函数模式</li>
<li>原型模式</li>
<li>对象迭代</li>
</ol>
<blockquote>
<p>  在JavaScript中，使用Object构造函数或者对象字面量都可以方便的可以很方便地创建对象，但这些方式也有明显不足：创建具有同样接口的对各对象需要重复编写很多代码。</p>
</blockquote>
<h2 data-id="heading-1">工厂模式</h2>
<p>  工厂模式是一种常见的设计模式，用于抽象创建特定对象的过程。工厂模式创建对象的一个例子如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPerson</span>(<span class="hljs-params">name, age</span>) </span>&#123;
    <span class="hljs-keyword">let</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
    o.name = name;
    o.age = age;
    o.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    &#125;
    <span class="hljs-keyword">return</span> o;
&#125;

<span class="hljs-keyword">let</span> person1 = createPerson(<span class="hljs-string">"Tom"</span>, <span class="hljs-number">21</span>);
<span class="hljs-keyword">let</span> person2 = createPerson(<span class="hljs-string">"Jack"</span>, <span class="hljs-number">22</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  createPerson()函数接收两个参数，返回拥有传入参数对应信息的对象。<strong>工厂模式的优点是我们多次调用该函数传入不同的参数，可以解决创建多个类似的对象问题，但是没有办法解决新创建的对象是什么类型的问题。</strong></p>
<h2 data-id="heading-2">构造函数模式</h2>
<p>  ECMAScript中的构造函数是用于创建特定类型对象的,Object就是一个原生的构造函数。上面的例子使用构造函数可以这样写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//按照惯例，构造函数的名称首字母都是大写的</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.age = age;
    <span class="hljs-built_in">this</span>.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    &#125;
&#125;

<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"Tom"</span>, <span class="hljs-number">21</span>);
<span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"Jack"</span>, <span class="hljs-number">22</span>);

person1.sayName();  <span class="hljs-comment">//Tom</span>
person2.sayName();  <span class="hljs-comment">//Jack</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方法和前面的工厂模式在函数内部很像，只是有以下几个区别：</p>
<ul>
<li>没有显式地创建对象</li>
<li>属性和方法直接赋值给了this</li>
<li>没有return</li>
</ul>
<p><strong>构造函数的主要问题在于其定义的函数会在每一个实例上都创建一遍。在这个例子中不同实例上的函数虽然是同名但却是不相等的，如下：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(person1.sayName == person2.sayName);  <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以把函数定义移到构造函数外部解决解决这个问题，但是这样的话自定义类型引用的代码不能很好的聚集在一起，也容易搞乱作用域，要解决这个问题，可以使用下面的原型模式。</p>
<h2 data-id="heading-3">原型模式</h2>
<p>  每个函数都会创建一个prototype属性，这个属性是一个对象，包含应该由特定引用类型的实例贡献的属性和方法。原来在构造函数直接赋值给对象实例的值，可以直接赋值给他们的原型，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

Person.prototype.name = <span class="hljs-string">"Tom"</span>;
Person.prototype.age = <span class="hljs-number">21</span>;
Person.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;

<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person();
<span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person();

person1.sayName();  <span class="hljs-comment">//Tom</span>
person2.sayName();  <span class="hljs-comment">//Tom</span>

<span class="hljs-built_in">console</span>.log(person1.sayName == person2.sayName);  <span class="hljs-comment">//ture</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用原型对象的好处是，在它上面定义的属性和方法可以被对象实例共享。但是它弱化了向构造函数传递初始化参数的能力，会导致所有默认实例都取得相同的属性值。更大的缺点也来自它的共享性：如果两个实例都有一个数组属性，实例1往该数组中添加了一个字符串时，因为该属性是直接存在prototype上而不是实例中，其他对象的这个属性也会改变。</strong></p>
<h2 data-id="heading-4">对象迭代</h2>
<p>  ECMAScript 2017新增了两个静态方法，用于将对象内容转换为序列化、可迭代的格式。这两个静态方法Object.values()和Object.entries()接收一个对象，返回他们内容的数组。如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> o = &#123;
    <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>,
    <span class="hljs-attr">baz</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">qux</span>: &#123;&#125;
&#125;;

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.values(o));  <span class="hljs-comment">//["bar", 1, &#123;&#125;]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.entries(o));  <span class="hljs-comment">//[["foo", "bar"], ["baz", 1], ["qux", &#123;&#125;]]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，这种方法非字符串属性会被转换成字符串输出，且符号属性会被忽略。</p>
<p>书中关于对象迭代内容介绍的比较少，后续有新的内容会继续改进。</p></div>  
</div>
            