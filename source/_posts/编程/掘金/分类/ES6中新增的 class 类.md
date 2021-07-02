
---
title: 'ES6中新增的 class 类'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9130'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 05:04:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=9130'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">class 类</h4>
<ul>
<li>
<p>在ES6中新增了类的概念，可以使用 <strong>class</strong>关键字声明一个类，之后以这个类来实例化对象。</p>
</li>
<li>
<p>类抽象成对象的公共部分，它泛指一大类(<strong>class</strong>)</p>
</li>
<li>
<p>class 的本质是 function</p>
</li>
<li>
<p>对象特指某一个，通过类实例化一个具体的对象</p>
</li>
<li>
<p>面向对象的思维特点</p>
<ul>
<li>抽取 (抽象) 对象公用的属性和行为组织(封装) 成一个<strong>类</strong>(模板)</li>
<li>对类进行实例化，获取类的对象</li>
</ul>
</li>
<li>
<p>类 constructor 构造 函数</p>
<p><strong>constructor( )</strong> 方法是类的构造函数(默认方法) , <strong>用于传递参数，返回实例对象</strong>，通过new命令生成实例对象实例时，如果没有显示定义，类内部会自动给我们创建一个<strong>constructor( )</strong></p>
</li>
<li>
<p>创建类和生成实例</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建类 class 创建一个学生的类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name;
        <span class="hljs-built_in">this</span>.age = age;
    &#125;
&#125;

<span class="hljs-comment">// 2.利用类创建对象 new</span>
<span class="hljs-keyword">let</span> stu1 = <span class="hljs-keyword">new</span> Student(<span class="hljs-string">"小明"</span>, <span class="hljs-number">18</span>);
<span class="hljs-keyword">let</span> stu2 = <span class="hljs-keyword">new</span> Student(<span class="hljs-string">"小芳"</span>, <span class="hljs-number">18</span>);
<span class="hljs-built_in">console</span>.log(stu1, stu2); <span class="hljs-comment">//Student &#123; name: '小明', age: 18 &#125; Student &#123; name: '小芳', age: 18 &#125;</span>

<span class="hljs-comment">/* 
    注意点：
        1.通过class 关键字创建类，类名我们还是习惯性定义首字母大写
        2.类里面有一个 constructor 函数，可以接受传递过来的参数，同时返回实例对象。
        3.constructor 函数只要new 生成实例时，就会自动调用这个函数，不写这个函数，那么类也会自动帮我们生成这个函数
        4.new 不能省略
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>类里面添加方法</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建类 class 创建一个学生的类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
            <span class="hljs-built_in">this</span>.name = name;
            <span class="hljs-built_in">this</span>.age = age;
        &#125;
        <span class="hljs-comment">// 添加方法</span>
    <span class="hljs-function"><span class="hljs-title">homework</span>(<span class="hljs-params">job</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + job);
    &#125;
&#125;

<span class="hljs-comment">// 2.利用类创建对象 new</span>
<span class="hljs-keyword">let</span> stu1 = <span class="hljs-keyword">new</span> Student(<span class="hljs-string">"小明"</span>, <span class="hljs-number">18</span>);
<span class="hljs-keyword">let</span> stu2 = <span class="hljs-keyword">new</span> Student(<span class="hljs-string">"小芳"</span>, <span class="hljs-number">18</span>);
<span class="hljs-built_in">console</span>.log(stu1, stu2);

stu1.homework(<span class="hljs-string">"写作文"</span>); <span class="hljs-comment">//小明写作文</span>
stu2.homework(<span class="hljs-string">"做练习"</span>); <span class="hljs-comment">//小芳做练习</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>super 关键字
<ul>
<li><strong>super</strong>关键字用于访问和调用对象父类上的函数，<strong>可以调用父类的构造函数</strong>，也可以调用父类的普通函数</li>
</ul>
</li>
<li>extends
<ul>
<li>继承父类的方法和属性</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 类的继承</span>
<span class="hljs-comment">// class Father &#123;</span>
<span class="hljs-comment">//     constructor() &#123;</span>

<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">//     money() &#123;</span>
<span class="hljs-comment">//         console.log("继承");</span>
<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-comment">// //  // 类的继承</span>
<span class="hljs-comment">// class Father &#123;</span>
<span class="hljs-comment">//     constructor() &#123;</span>

<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">//     money() &#123;</span>
<span class="hljs-comment">//         console.log("继承");</span>
<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-comment">// //  extends 继承父类的方法和属性</span>
<span class="hljs-comment">// class Son extends Father &#123;</span>

<span class="hljs-comment">// &#125;</span>
<span class="hljs-comment">// let son = new Son();</span>
<span class="hljs-comment">// son.money(); //继承</span>


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Father</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
    <span class="hljs-function"><span class="hljs-title">sum</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y);
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Father</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(x, y); <span class="hljs-comment">// 调用了父类中的构造函数</span>
    &#125;
&#125;

<span class="hljs-keyword">let</span> son = <span class="hljs-keyword">new</span> Son(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>);
son.sum(); <span class="hljs-comment">//30</span>
<span class="hljs-comment">// class Son extends Father &#123;</span>

<span class="hljs-comment">// &#125;</span>
<span class="hljs-comment">// let son = new Son();</span>
<span class="hljs-comment">// son.money(); //继承</span>


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Father</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
    <span class="hljs-function"><span class="hljs-title">sum</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y);
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Father</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(x, y); <span class="hljs-comment">// 调用了父类中的构造函数</span>
    &#125;
&#125;

<span class="hljs-keyword">let</span> son = <span class="hljs-keyword">new</span> Son(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>);
son.sum(); <span class="hljs-comment">//30</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>调用父类的普通函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// super 关键字调用父类的普通函数</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Father</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"father"</span>
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Father</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// console.log("son");</span>
        <span class="hljs-comment">// super.say() 就是调用父类中的普通函数 say()</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">super</span>.say());
    &#125;
&#125;

<span class="hljs-keyword">let</span> son = <span class="hljs-keyword">new</span> Son();
son.say(); <span class="hljs-comment">// father</span>

<span class="hljs-comment">/* 
    调用父类的普通函数
        1.继承中，如果实例化子类输出一个方法，子类有这个方法就执行子类的方法
        2.继承中，如果子类没有这个方法，就会往上找父类，父类就执行父类的方法(就近原则)
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使子类继承父类方法的同时，拥有自己的方法</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 子类继承父类方法的同时，拥有自己的方法</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Father</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
    <span class="hljs-function"><span class="hljs-title">sum</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y);
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Father</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
        <span class="hljs-comment">// 利用 super 调用父类的构造函数 super必须在子类的this之前，否则报错</span>
        <span class="hljs-built_in">super</span>(x, y);
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
    <span class="hljs-function"><span class="hljs-title">subtract</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.x - <span class="hljs-built_in">this</span>.y);
    &#125;
&#125;

<span class="hljs-keyword">let</span> son = <span class="hljs-keyword">new</span> Son(<span class="hljs-number">20</span>, <span class="hljs-number">10</span>);
son.sum(); <span class="hljs-comment">//30 </span>
son.subtract(); <span class="hljs-comment">//10</span>

<span class="hljs-comment">// 注意点：子类在构造函数中使用 super ，必须放到this前面（必须先调用父类的构造函数，再使用子类的构造函数）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">使用类的注意事项</h4>
<ul>
<li>在ES6 中类没有变量提升，所以必须先定义类，才能通过实例化对象</li>
<li>类里面的公有属性和方法必须加 <strong>this</strong> 使用</li>
<li>重复定义类
<ul>
<li>重复声明一个类会引起类型错误</li>
</ul>
</li>
</ul>
<pre><code class="copyable">class student &#123;&#125;;
class student &#123;&#125;;
// Uncaught TypeError: Identifier 'student' has already been declare
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>this</strong> 的指向问题</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Father</span> </span>&#123;
    <span class="hljs-keyword">let</span> _that;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
        _that=<span class="hljs-built_in">this</span>;
        <span class="hljs-comment">// constructor里面的this指向的是 创建的实例对象</span>
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
    <span class="hljs-function"><span class="hljs-title">sum</span>(<span class="hljs-params"></span>)</span> &#123;
 <span class="hljs-comment">// 方法这里的this 指向调用者，谁调用指向的就是谁</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y);
    &#125;
&#125;

<span class="hljs-keyword">let</span> fahter = <span class="hljs-keyword">new</span> Father();
<span class="hljs-built_in">console</span>.log(_that === father); <span class="hljs-comment">// true</span>
father.sum(); <span class="hljs-comment">// 这里的 this 的指向就是这个实例对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2"></h4></div>  
</div>
            