
---
title: 'PHP 学习之路：第十天—— 闭包_循环_构造器与原型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=539'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 00:19:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=539'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、作用域与闭包</h1>
<h2 data-id="heading-1">1. 作用域</h2>
<h3 data-id="heading-2">1.1 全局作用域</h3>
<p>(1) 全局作用域在页面打开时被创建,页面关闭时被销毁
(2) 写在 script 标签中的变量和函数,作用域为全局，在页面的任意位置都可以访问到
(3) 在全局作用域中有全局对象 window,代表一个浏览器窗口,由浏览器创建,可以直接调用
(4) 全局作用域中声明的变量和函数会作为 window 对象的属性和方法保存</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1. 全局作用域,默认的,不可删除</span>
ver name = <span class="hljs-string">'php中文网'</span>;
<span class="hljs-built_in">console</span>.log(name);
<span class="hljs-comment">// 由全局对象调用的</span>
<span class="hljs-comment">// 全局对象: 如果在是浏览器中运行js,那么全局对象就是window</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.name);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.2 函数作用域</h3>
<p>(1) 调用函数时,函数作用域被创建,函数执行完毕,函数作用域被销毁
(2) 每调用一次函数就会创建一个新的函数作用域,他们之间是相互独立的
(3) 在函数作用域中可以访问到全局作用域的变量,在函数外无法访问到函数作用域内的变量
(4) 在函数作用域中访问变量、函数时,会先在自身作用域中寻找,若没有找到,则会到函数的上一级作用域中寻找,一直到全局作用域
(5) 在函数作用域中也有声明提前的特性,对于变量和函数都起作用,此时函数作用域相当于一个小的全局作用域
(6) 在函数作用域中,不使用变量关键字声明的变量,在赋值时会往上一级作用域寻找已经声明的同名变量,直到全局作用域时还没找到,则会成为 window 的属性
(7) 在函数中定义形参,等同于声明变量</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> site = <span class="hljs-string">'php中文网'</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSite</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// site是声明在函数外部的全局变量</span>
  <span class="hljs-comment">// 在函数内部可以访问到外部的全局变量</span>
  <span class="hljs-comment">// let site = "京东商城";</span>
  
  <span class="hljs-comment">// 私有成员,仅限在当前作用内访问, 外部不可见</span>
  <span class="hljs-keyword">let</span> domain = <span class="hljs-string">'php.cn'</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;site&#125;</span> [ <span class="hljs-subst">$&#123;domain&#125;</span> ]`</span>;
  <span class="hljs-comment">// 这里要返回一个叫site的变量</span>
  <span class="hljs-comment">// 有一个查询的过程, 先在自身的作用域找一个有没有一个叫site</span>
  <span class="hljs-comment">// 如果有则直接返回它</span>
  <span class="hljs-comment">// 如果函数中没有这个site,则自动函数的上一级作用域中去查看site</span>
  <span class="hljs-comment">// 全局正好有一个site,于是就返回了全局的site</span>
  <span class="hljs-comment">// 内部的site ---> 到它的上一级作用域中去查找</span>
  <span class="hljs-comment">// 上面的查询变量的过程,就是是一个链式查询的一个过程,称为:作用域链</span>
&#125;
<span class="hljs-built_in">console</span>.log(getSite());
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.3 块作用域</h3>
<p>(1)用&#123;&#125;创建快作用域<br>
(2) let, const 支持块作用域; var 不支持块作用域</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">const</span> B = <span class="hljs-string">'hello'</span>;
  <span class="hljs-comment">// var:不支持块作用域</span>
  <span class="hljs-keyword">var</span> c = <span class="hljs-number">1</span>;
&#125;
<span class="hljs-built_in">console</span>.log(a, B, c);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">2. 闭包</h2>
<p>闭包:能够访问自由变量的函数;理论上讲,所有函数都是闭包</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> c = <span class="hljs-number">100</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-comment">// 自由变量,函数参数以外的变量;c 为自由变量</span>
  <span class="hljs-keyword">return</span> a + b + c;
&#125;
<span class="hljs-built_in">console</span>.log(sum(<span class="hljs-number">4</span>, <span class="hljs-number">5</span>));

<span class="hljs-comment">// 通过闭包来访问内部的私有变量;</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">demo1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 私有变量</span>
  <span class="hljs-keyword">let</span> email = <span class="hljs-string">'a@qq.com'</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">d</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 对于这个子函数来说,email就是它的自由变量</span>
    <span class="hljs-keyword">return</span> email;
  &#125;;
&#125;
<span class="hljs-built_in">console</span>.log(demo1()());
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">二、循环</h1>
<h2 data-id="heading-7">1. while: 入口判断</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> colors = [<span class="hljs-string">"red"</span>, <span class="hljs-string">"green"</span>, <span class="hljs-string">"blue"</span>];
<span class="hljs-comment">// 1. while: 入口判断</span>
<span class="hljs-comment">//   循环变量的初始化</span>
<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
<span class="hljs-comment">//   i < colors.length: 循环条件</span>
<span class="hljs-keyword">while</span> (i < colors.length) &#123;
  <span class="hljs-comment">// console.log(colors[i]);</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"%c%s"</span>, <span class="hljs-string">"color: red"</span>, colors[i]);
  <span class="hljs-comment">// 更新循环条件,如果不更新就进入了死循环</span>
  <span class="hljs-comment">// i = i + 1;</span>
  <span class="hljs-comment">// i += 1;</span>
  <span class="hljs-comment">// 自增1</span>
  i++;
  <span class="hljs-comment">// i+=2;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">2. while: 出口判断</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> colors = [<span class="hljs-string">"red"</span>, <span class="hljs-string">"green"</span>, <span class="hljs-string">"blue"</span>];
<span class="hljs-comment">// 2. while: 出口判断</span>
<span class="hljs-comment">//   当条件不满足的时候至少执行一次</span>
<span class="hljs-comment">//   循环变量的初始化</span>
i = <span class="hljs-number">10</span>;
<span class="hljs-comment">//   i < colors.length: 循环条件</span>
<span class="hljs-keyword">do</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"%c%s"</span>, <span class="hljs-string">"color: blue"</span>, colors[i]);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我被执行了一次"</span>);
  <span class="hljs-comment">// 更新循环条件,如果不更新就进入了死循环</span>
  i++;
&#125; <span class="hljs-keyword">while</span> (i < colors.length);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">3. 对象的遍历 for-in</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 3. 对象的遍历， for -in</span>
<span class="hljs-keyword">const</span> lesson = &#123; <span class="hljs-string">"my name"</span>: <span class="hljs-string">"JavaScript编程"</span>, <span class="hljs-attr">score</span>: <span class="hljs-number">88</span> &#125;;
<span class="hljs-built_in">console</span>.log(lesson);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> lesson) &#123;
  <span class="hljs-built_in">console</span>.log(lesson[key]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4. for 循环</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 4. for 循环</span>
<span class="hljs-keyword">const</span> colors = [<span class="hljs-string">"red"</span>, <span class="hljs-string">"green"</span>, <span class="hljs-string">"blue"</span>];
<span class="hljs-comment">// 循环变量的初始化</span>
i = <span class="hljs-number">0</span>;
<span class="hljs-comment">// i < colors.length: 循环条件</span>
<span class="hljs-keyword">while</span> (i < colors.length) &#123;
  <span class="hljs-comment">// console.log(colors[i]);</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"%c%s"</span>, <span class="hljs-string">"color: red"</span>, colors[i]);
  <span class="hljs-comment">// 更新循环条件,如果不更新就进入了死循环</span>
  <span class="hljs-comment">// i = i + 1;</span>
  <span class="hljs-comment">// i += 1;</span>
  <span class="hljs-comment">// 自增1</span>
  i++;
  <span class="hljs-comment">// i+=2;</span>
&#125;
<span class="hljs-comment">// while的简化版</span>
<span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < colors.length; i++) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"%c%s"</span>, <span class="hljs-string">"color: green"</span>, colors[i]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">5.迭代器 for-of,遍历数组</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 迭代器,将所有类型的数据的遍历进行了统一操作</span>
<span class="hljs-comment">// for - of</span>
<span class="hljs-comment">// 遍历数组</span>
<span class="hljs-keyword">const</span> colors = [<span class="hljs-string">"red"</span>, <span class="hljs-string">"green"</span>, <span class="hljs-string">"blue"</span>];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> colors) &#123;
  <span class="hljs-built_in">console</span>.log(item);
&#125;
<span class="hljs-comment">// 遍历对象,会报错</span>
<span class="hljs-keyword">const</span> lesson = &#123; <span class="hljs-string">"my name"</span>: <span class="hljs-string">"JavaScript编程"</span>, <span class="hljs-attr">score</span>: <span class="hljs-number">88</span> &#125;;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> lesson) &#123;
  <span class="hljs-built_in">console</span>.log(item);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">三、迭代器</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myIterator</span>(<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-comment">// 迭代器中必须要有一个next()</span>
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-function"><span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// done: 表示遍历是否完成?</span>
      <span class="hljs-comment">// value: 当前正在遍历的数据</span>
      <span class="hljs-keyword">let</span> done = i >= data.length;
      <span class="hljs-keyword">let</span> value = !done ? data[i++] : <span class="hljs-literal">undefined</span>;
      <span class="hljs-keyword">return</span> &#123; done, value &#125;;
    &#125;,
  &#125;;
&#125;

<span class="hljs-keyword">let</span> iterator = myIterator([<span class="hljs-string">"html"</span>, <span class="hljs-string">"css"</span>, <span class="hljs-string">"js"</span>, <span class="hljs-string">"php"</span>]);
<span class="hljs-built_in">console</span>.log(iterator.next());
<span class="hljs-built_in">console</span>.log(iterator.next());
<span class="hljs-built_in">console</span>.log(iterator.next());
<span class="hljs-built_in">console</span>.log(iterator.next());
<span class="hljs-built_in">console</span>.log(iterator.next());
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">四、构造函数和原型</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 常识: 任何一个函数都是对象，有一个属性叫: prototype(原型属性)</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params">a, b, c</span>) </span>&#123;&#125;
<span class="hljs-built_in">console</span>.dir(f1);

<span class="hljs-comment">// 函数有二个功能</span>
<span class="hljs-comment">// 基本功能是封装操作步骤</span>
<span class="hljs-comment">// 扩展功能: 当成对象的构造器,构造函数,对象生成器来用</span>
<span class="hljs-comment">// 在js中没有“类”的概念，都是通过原型来实现继承的</span>
<span class="hljs-comment">// 为了区别函数的这二个功能，当一个函数当成构造函数来使用时，必须使用“new"来调用</span>

<span class="hljs-comment">// 通过构造函数创建对象的过程，叫”类的实例化"</span>
<span class="hljs-comment">// 此时,构造函数就可以看成一个类</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">User</span>(<span class="hljs-params">name, email</span>) </span>&#123;
  <span class="hljs-comment">// 1.内部会自动创建一个this,指向新生成的对象</span>
  <span class="hljs-comment">// let this = new User();</span>

  <span class="hljs-comment">// 2.第二步是给这个新生成的对象添加一些成员(属性,方法)</span>
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.email = email;

  <span class="hljs-comment">// 3.返回这个新对象</span>
  <span class="hljs-comment">// return this;</span>
&#125;

<span class="hljs-comment">// 当成普通函数调用</span>
<span class="hljs-comment">// const user = User();</span>

<span class="hljs-comment">// 当成构造函数调用 new</span>
<span class="hljs-keyword">const</span> user = <span class="hljs-keyword">new</span> User(<span class="hljs-string">"admin"</span>, <span class="hljs-string">"admin@php.cn"</span>);
<span class="hljs-built_in">console</span>.log(user, <span class="hljs-keyword">typeof</span> user);

<span class="hljs-comment">// user对象的原型属性永远指向它的构造函数的原型属性对象</span>
<span class="hljs-comment">// user对象的原型</span>
<span class="hljs-built_in">console</span>.log(user.__proto__);
<span class="hljs-comment">// user的构造函数的原型</span>
<span class="hljs-built_in">console</span>.log(User.prototype);
<span class="hljs-built_in">console</span>.log(user.__proto__ === User.prototype);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">五、类与类的继承</h1>
<h2 data-id="heading-15">1.类: 使用 class 关键字</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">User1</span> </span>&#123;
  <span class="hljs-comment">// 构造方法：初始化对象的</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, email</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.email = email;
  &#125;

  <span class="hljs-comment">// 原型方法(共享方法),通过对象来调用的</span>
  <span class="hljs-function"><span class="hljs-title">show</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">this</span>.name, <span class="hljs-attr">email</span>: <span class="hljs-built_in">this</span>.email, <span class="hljs-attr">age</span>: <span class="hljs-built_in">this</span>.#age &#125;;
  &#125;

  <span class="hljs-comment">// 静态方法: 不需要实例化(new class),直接用类来调用</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">fetch</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 静态成员中的this表示的就是当前的类</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.userName;
  &#125;
  <span class="hljs-comment">// 静态属性/变量</span>
  <span class="hljs-keyword">static</span> userName = <span class="hljs-string">'灭绝小师妹'</span>;

  <span class="hljs-comment">// 私有成员</span>
  #age = <span class="hljs-number">50</span>;

  <span class="hljs-comment">// 还可以声明访问器属性: 伪装成属性的方法,有get,set</span>
  <span class="hljs-comment">// 使用访问器属性来访问私有成员</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">age</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.#age;
  &#125;

  <span class="hljs-keyword">set</span> <span class="hljs-title">age</span>(<span class="hljs-params">value</span>) &#123;
    <span class="hljs-keyword">if</span> (value >= <span class="hljs-number">18</span> && value < <span class="hljs-number">60</span>) <span class="hljs-built_in">this</span>.#age = value;
    <span class="hljs-keyword">else</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'年龄非法'</span>);
  &#125;
&#125;

<span class="hljs-keyword">const</span> user1 = <span class="hljs-keyword">new</span> User1(<span class="hljs-string">'天蓬老师'</span>, <span class="hljs-string">'tp@qq.com'</span>);
<span class="hljs-built_in">console</span>.log(user1.show());

<span class="hljs-comment">//   静态方法直接用类调用</span>
<span class="hljs-built_in">console</span>.log(User1.fetch());

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'my age = '</span>, user1.age);
user1.age = <span class="hljs-number">160</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'my age = '</span>, user1.age);
user1.age = <span class="hljs-number">32</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'my age = '</span>, user1.age);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">2.继承:使用 extends 关键字</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 继承,通常是对父类进行一些扩展(添加一些新的属性或方法)</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">User1</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, email, gender</span>)</span> &#123;
    <span class="hljs-comment">// 第一步必须将父类的构造方法来执行一下，否则this用不了</span>
    <span class="hljs-built_in">super</span>(name, email);
    <span class="hljs-comment">// 第二步给子类的新成中去初始化</span>
    <span class="hljs-built_in">this</span>.gender = gender;
  &#125;
  <span class="hljs-comment">// 父类的原型方法</span>
  <span class="hljs-function"><span class="hljs-title">show</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">this</span>.name, <span class="hljs-attr">email</span>: <span class="hljs-built_in">this</span>.email, <span class="hljs-attr">gender</span>: <span class="hljs-built_in">this</span>.gender &#125;;
  &#125;
&#125;

<span class="hljs-keyword">const</span> child = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'欧阳老师'</span>, <span class="hljs-string">'oy@qq.com'</span>, <span class="hljs-string">'男'</span>);
<span class="hljs-built_in">console</span>.log(child.show());
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            