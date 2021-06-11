
---
title: 'JS中的堆栈内存及闭包详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1466'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:02:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=1466'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">js执行上下文与作用域</h2>
<ol>
<li>var和function声明创建在全局对象中，而let const class声明的变量创建在全局scope中</li>
<li>先在全局scope中找变量，查找不到再在全局对象查找</li>
</ol>
<p>顶级函数：不在大括号中</p>
<h2 data-id="heading-1">全局上下文</h2>
<p>Step1:：创建全局执行上下文，并加入栈顶
Step2：分析：</p>
<ul>
<li>找到所有的非函数中的var声明</li>
<li>找到所有的顶级函数声明</li>
<li>找到顶级let const class声明</li>
</ul>
<p>Step3：</p>
<ul>
<li>名字重复处理</li>
</ul>
<p>Step4： 创建绑定</p>
<ul>
<li>登录并初始化var为undefined</li>
<li>顶级函数声明：登录function名字，并初始化为新创建函数对象</li>
<li>块级中函数声明：登记名字，初始化为undefined</li>
<li>登记let cosnt class，但未初始化</li>
</ul>
<p>Step5：执行语句</p>
<p>函数对象体内会保存，函数创建时的执行上下文的文本环境。它对理解函数闭包和函数执行作用域很有帮助。</p>
<p>函数的调用是创建函数执行上下文。比如foo(),是创建foo执行上下文。</p>
<h2 data-id="heading-2">作用域</h2>
<ul>
<li>作用域是解析（查找）变量名的一个集合，就是当前运行上下文（也可以是当前上下文的词法环境）</li>
</ul>
<p>全局作用域就是全局运行上下文<br>
函数作用域就是函数运行上下文</p>
<ul>
<li>函数调用时的执行上下文看“身世”——函数在哪里创建，就保存哪里的运行上下文</li>
</ul>
<p>函数的作用域是在函数创建的时候绝对的而不是调用的时候决定</p>
<h2 data-id="heading-3">词法作用域</h2>
<ul>
<li>并非根据调用嵌套形成（运行上下文）作用域，而是根据函数创建嵌套形成作用域链，也就是<code>函数的书写位置形成作用域链</code>，因此称为词法作用域。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 2</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">3</span>;
    foo();
&#125;
<span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;
bar()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">块级作用域</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-string">'out if statement'</span>
<span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>)&#123;
    <span class="hljs-keyword">let</span> a = <span class="hljs-string">'in if statement'</span>
    <span class="hljs-built_in">console</span>.log(a)
&#125;
<span class="hljs-built_in">console</span>.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>栈内存：提供代码执行的环境</p>
<p>堆内存：存放东西（存放的是属性和方法）</p>
<p>浏览器会在计算机内存中分配一块内存，专门用来供代码执行的。
=》栈内存ECStack，执行环境栈</p>
<p>全局对象GO。浏览器会让window指向GO，浏览器把内置的一些方法和属性放在一个单独的内存中 ，叫堆内存（heap）</p>
<p>任何开辟的内存都有一个16进制的内存地址，方便后期找到这个内存（isNaN parseInt）</p>
<p>先进后出，垃圾回收机制</p>
<p>VO（变量对象）：在当前的上下文中，用来存放创建的变量和值得地方（每一个执行上下文中都会有一个自己的变量对象）。函数私有上下文中叫做AO（活动对象，但是也是变量对象，AO是VO的分支。）</p>
<p>var a = 12;
创建变量和赋值操作的底层操作有3部：</p>
<ol>
<li>创建一个值</li>
<li>创建一个变量</li>
<li>让变量和值关联</li>
</ol>
<p>基本数据类型值都是直接存在栈内存中。而引用类型值是先开辟一个堆内存，把地址存储进去，最后把地址放到栈中供变量关联使用的。</p>
<p>所有的指针赋值都是指针的关联指向。</p>
<p>对象：</p>
<ol>
<li>创建一个堆内存</li>
<li>把键值对存储到堆内存中</li>
<li>堆内存地址放到栈中，供变量调用</li>
</ol>
<ul>
<li>栈内存也是作用域（包含全局栈内存 和 私有栈内存）</li>
</ul>
<ol>
<li>提供一个供JS代码自上而下执行的环境（代码都是在栈中执行的）</li>
<li>由于基本数据类型值比较简单，他们都是直接在栈内存中开辟一个位置，把值直接存储进去的</li>
</ol>
<p>=>当 栈内存被销毁，存储的那些基本值也都跟着销毁了。</p>
<ul>
<li>堆内存：引用值对应的空间</li>
</ul>
<ol>
<li>存储引用类型值得（对象：键值对  函数：代码字符串）</li>
</ol>
<p>=> 当前堆内存释放销毁，那么这个引用值彻底没了
=> 堆内存的释放：当堆内存没有被任何的变量或者其他东西所占用，浏览器会在空闲的时候，自主的进行内存回收，把所有不被占用的堆内存销毁掉（谷歌浏览器）</p>
<p>xxx=null 通过空对象指针null可以让原始变量（或者其他东西）谁都不指向，那么原有被占用的堆内存就没有被东西占用了，浏览器会销毁它。</p>
<pre><code class="hljs language-js copyable" lang="js">考察 创建变量和赋值操作的底层操作有<span class="hljs-number">3</span>步

<span class="hljs-number">1.</span> 创建值
    + 开辟一个堆AAAFFF000
    + 存储键值对
        <span class="hljs-attr">name</span>:<span class="hljs-string">'hhy'</span>
        <span class="hljs-attr">fn</span>:自执行函数执行，需要把obj.name的值当做实参传递进来 =>其实是obj找不到，因为这个时候还没赋值 <span class="hljs-literal">undefined</span>.name
    
<span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'hhy'</span>,
    <span class="hljs-attr">fn</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>)</span>&#123;
        <span class="hljs-keyword">return</span> x + <span class="hljs-number">10</span>;
    &#125;)(obj.name)<span class="hljs-comment">//在给fn赋值的时候，是把自执行函数执行的返回结果赋值给fn属性</span>
&#125;
<span class="hljs-built_in">console</span>.log(obj.fn)  <span class="hljs-comment">// 报错name找不到</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>学会画框框，分析变量提升和栈堆内存，才能出正确的结果</strong></p>
<h2 data-id="heading-5">变量提升</h2>
<p>当栈内存（作用域）形成，JS代码自上而执行之前，浏览器首先会把所有带var、function关键词的进行提前“声明”或者“定义”，这种预先处理机制称之为“变量提升”。</p>
<ul>
<li>声明(declare):var a (默认值undefined)</li>
<li>定义（defined）：a=12 (定义其实就是赋值操作)</li>
</ul>
<p>变量提升阶段</p>
<ul>
<li>
<p>带var的只声明未定义</p>
</li>
<li>
<p>带function的声明和赋值都完成了</p>
</li>
<li>
<p>变量提升只发生在当前作用域</p>
</li>
</ul>
<p>例如：开始加载页面的时候只对全局作用域下的进行提升，因为此时函数中存储的都是字符串而已</p>
<ul>
<li>在全局作用域下声明的函数或者变量是“全局变量”，同理，在私有作用域下声明的变量是“私有变量”</li>
</ul>
<p>带var和funciton的才是声明</p>
<ul>
<li>
<p>浏览器很懒，做过的事情不会重复执行第二遍，也就是，当代码执行遇到创建函数这部分代码后，直接的跳过即可（因为在提升阶段就已经完成函数的赋值操作了）</p>
</li>
<li>
<p>私有作用域形成后，也不是立即代码执行，而是先进行遍历提升（变量提升钱，先形参赋值）</p>
</li>
<li>
<p>在ES3/ES5语法规范中，只有全局作用域和函数执行的私有作用域（栈内存），其它大括号不会形成栈内存</p>
</li>
</ul>
<h2 data-id="heading-6">带var和不带的区别</h2>
<p>在全局作用域下声明一个变量，也相当于给window全局对象设置了一个属性，变量的值就是属性值（私有作用域中声明的私有变量和window没啥关系）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.a) <span class="hljs-comment">//undefined</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span> <span class="hljs-keyword">in</span> <span class="hljs-built_in">window</span>) <span class="hljs-comment">// true  </span>
在变量提升阶段，在全局作用域中声明了一个变量A，此时就已经把A当做属性赋值给<span class="hljs-built_in">window</span>了，只不过此时还没有给A赋值，默认值<span class="hljs-literal">undefined</span>

<span class="hljs-keyword">in</span>：检测某个属性是否隶属于这个对象
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**全局变量和window中的属性存在“映射机制” **</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 报错</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.a) <span class="hljs-comment">//undefined</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span> <span class="hljs-keyword">in</span> <span class="hljs-built_in">window</span>)  <span class="hljs-comment">//false</span>
a = <span class="hljs-number">12</span>;  <span class="hljs-comment">//window.a = 12</span>
<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 12</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.a) <span class="hljs-comment">// 12</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不加var的本质是window的属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = b = <span class="hljs-number">12</span>; 这样写的b是不带<span class="hljs-keyword">var</span>的
相当于 
<span class="hljs-keyword">var</span> a = <span class="hljs-number">12</span>;
b = <span class="hljs-number">12</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a,b) <span class="hljs-comment">//undefined  undefined</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">12</span>, b =<span class="hljs-number">12</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a,b) <span class="hljs-comment">//undefined  12</span>
    <span class="hljs-keyword">var</span> a = b = <span class="hljs-number">13</span>;
    <span class="hljs-built_in">console</span>.log(a,b)<span class="hljs-comment">//13 13</span>
&#125;
fn()
<span class="hljs-built_in">console</span>.log(a,b); <span class="hljs-comment">//12 13</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>私有作用域中带var和不带也有区别：</p>
<ol>
<li>带var的在私有作用域变量提升阶段，都声明为私有变量，和外界没有任何的关系</li>
<li>不带var不是私有变量，会向它的上级作用域查找，看是否为上级的变量，不是，继续向上查找，一直找到window为止（我们把这种查找机制叫做：作用域链），也就是我们在私有作用域中操作的这个非私有变量，是一直操作别人的</li>
</ol>
<h2 data-id="heading-7">变量提升的一些细节</h2>
<p>只对等号左边进行变量提升</p>
<p>在当前作用域下，不管条件是否成立成立都要进行变量提升</p>
<ul>
<li>带var的还是只声明</li>
<li>带function的在老版本浏览器渲染机制下，声明和定义都处理，但是为了迎合es6中的块级作用域，新版浏览器对于函数（在条件判断中的函数），不管条件是否成立，都只是先声明，没有定义，类似于var</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">//undefined</span>
<span class="hljs-keyword">if</span>(<span class="hljs-string">'a'</span> <span class="hljs-keyword">in</span> <span class="hljs-built_in">window</span>)&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">100</span>
&#125;
<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">//100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">f = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>&#125; ; => <span class="hljs-built_in">window</span>.f=...
g = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>&#125;; =><span class="hljs-built_in">window</span>.g=...
<span class="hljs-comment">//自执行函数肯定有私有作用域</span>
~<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-comment">//变量提升：function g; //=>g是私有变量</span>
    <span class="hljs-keyword">if</span>(g() && [] == ![])&#123;  <span class="hljs-comment">//新版本报错  g is not a function(此时g是undefined)</span>
        f = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>&#125; =>把全局中的d进行修改
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">g</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>&#125; => 私有
    &#125;
&#125;()
<span class="hljs-built_in">console</span>.log(f())
<span class="hljs-built_in">console</span>.log(g())  <span class="hljs-comment">//执行全局的</span>

<span class="hljs-comment">//老版本if会执行，输出false  false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">条件判断下的变量提升到底有多坑</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(fn) <span class="hljs-comment">//undefined  变量提升</span>
<span class="hljs-keyword">if</span>(<span class="hljs-number">1</span> === <span class="hljs-number">1</span>)&#123;
    <span class="hljs-built_in">console</span>.log(fn) 
    <span class="hljs-comment">//函数本身</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ok'</span>)  
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(fn) <span class="hljs-comment">//函数本身</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当条件成立，进入到判断体中（在ES6中它是一个块级作用域）第一件事并不是代码执行，而是类似于变量提升一样，先把fn声明和定义了，也就是判断体中代码执行之前，fn就已经赋值了。</p>
<h2 data-id="heading-9">变量提升机制下重名的处理</h2>
<ol>
<li>
<p>带var 和 function 关键字声明相同的名字，这种也算是重名了（其实是一个fn，只是存储值得类型不一样）</p>
</li>
<li>
<p>关于重名的处理：如果名字重复了，不会重新的声明，但是会重新的定义（重新赋值）【不管是变量提升还是代码执行阶段都是如此】</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">fn()  <span class="hljs-comment">//4</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);&#125;
fn() <span class="hljs-comment">//4</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);&#125;
fn() <span class="hljs-comment">//4</span>
<span class="hljs-keyword">var</span> fn=<span class="hljs-number">100</span>; <span class="hljs-comment">//带var提升只是声明，没有赋值，代码执行的时候赋值</span>
fn(); <span class="hljs-comment">//报错，fn is not a function  ，报错了后面的不会执行</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);&#125;
fn()   <span class="hljs-comment">//这里执行不到</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>);&#125;

fn函数声明并赋值
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">ES6的let不存在变量提升</h2>
<p>在es6中基于let、const等方式创建变量或者函数，不存在变量提升机制。</p>
<ul>
<li>切断了全局变量和window属性的映射关系</li>
</ul>
<p>在相同的作用域中，基于let不能声明相同名字的变量（不管用什么方式在当前作用域下声明了变量，再次使用let创建都会报错）</p>
<p>虽然没有变量提升机制，但是在当前作用域代码自上而下执行之前，浏览器会做一个重复性检测（语法检测）；自上而下查找当前作用域下所有变量，一旦发现有重复的，直接抛出异常，代码也不会在执行了（虽然没有把变量提前声明定义，但是浏览器已经记住了，当前作用域下有哪些变量）</p>
<pre><code class="hljs language-js copyable" lang="js">a = <span class="hljs-number">12</span>;<span class="hljs-comment">//报错：a has already been declared</span>
<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-keyword">let</span> a = <span class="hljs-number">13</span>;
<span class="hljs-built_in">console</span>.log(a);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">12</span>;<span class="hljs-comment">//报错：a has already been declared</span>
<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-keyword">let</span> a = <span class="hljs-number">13</span>;
<span class="hljs-built_in">console</span>.log(a);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">10</span>, b = <span class="hljs-number">10</span>;
<span class="hljs-keyword">let</span> fn = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-comment">//私有作用域</span>
    <span class="hljs-built_in">console</span>.log(a,b)  <span class="hljs-comment">//报错：a is not defined</span>
    <span class="hljs-keyword">let</span> a = b = <span class="hljs-number">20</span>;
&#125;
fn();
<span class="hljs-built_in">console</span>.log(a,b)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">ES6的暂时性死区问题</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a= <span class="hljs-number">12</span>；
<span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>)&#123;
    <span class="hljs-comment">//块级作用域</span>
    <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">//报错：a is not defined</span>
    <span class="hljs-keyword">let</span> a = <span class="hljs-number">13</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于let创建变量，会把大部分&#123;&#125;当做一个私有的块级作用域（类似于函数的私有作用域），在这里也是重新检测语法规范，看一下是否是基于新语法创建的变量，如果是按照新语法规范来解析。</p>
<p><strong>暂存死区</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> a) <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> a)  <span class="hljs-comment">// 报错：a is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在原有浏览器渲染机制下，基于typeof等逻辑运算符检测一个未被声明过的变量，不会报错，返回undefined</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> a)<span class="hljs-comment">// 报错：a is not defined</span>
<span class="hljs-keyword">let</span> a;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果当前变量是基于es6语法处理，在没有声明这个变量的时候，使用typeof检测会直接报错，不会是undefined，解决了原有的JS死区。</p>
<h2 data-id="heading-12">私有变量和全局变量</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">12</span>, b = <span class="hljs-number">13</span>, c = <span class="hljs-number">14</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">a</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a,b,c); <span class="hljs-comment">//12 undefined 14</span>
    <span class="hljs-keyword">var</span> b = c = a = <span class="hljs-number">20</span>;
    <span class="hljs-built_in">console</span>.log(a,b,c) <span class="hljs-comment">//20 20 20</span>
&#125;
fn(a)
<span class="hljs-built_in">console</span>.log(a,b,c) <span class="hljs-comment">//12 13 20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">有关私有作用域和作用域链的练习</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> ary = [<span class="hljs-number">12</span>, <span class="hljs-number">23</span>];
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">ary</span>)</span>&#123;
<span class="hljs-comment">// 形参ary是私有变量，和全局ary指向的地址是一样的</span>
    <span class="hljs-built_in">console</span>.log(ary);
    ary[<span class="hljs-number">0</span>] = <span class="hljs-number">100</span>;
    ary = [<span class="hljs-number">100</span>];  <span class="hljs-comment">// 重新指向新的地址，此处ary是私有的，跟全局地址没关系了</span>
    ary[<span class="hljs-number">0</span>] = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">console</span>.log(ary)  <span class="hljs-comment">// [0]</span>
&#125;
fn(ary)
<span class="hljs-built_in">console</span>.log(ary) <span class="hljs-comment">// [100, 23]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>注意：形参是私有变量</code></strong></p>
<h2 data-id="heading-14">上级作用域查找</h2>
<p>当前函数执行，形参衣蛾私有作用域A，A的上级作用域是谁，和他在哪执行的没有关系，和他在哪创建有关系，在哪里创建的，它的上级作用域就是谁。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">12</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">//12</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">120</span>;
    fn()
&#125;
sum()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> n = <span class="hljs-number">10</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> n = <span class="hljs-number">20</span>;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
        n++;
        <span class="hljs-built_in">console</span>..log(n); 
    &#125;
    f();
    <span class="hljs-keyword">return</span> f;
&#125;
<span class="hljs-keyword">var</span> x = fn();  <span class="hljs-comment">// 第一次结果是21</span>
x();  <span class="hljs-comment">// 第一次结果是22</span>
x();  <span class="hljs-comment">// 第一次结果是23</span>
<span class="hljs-built_in">console</span>.log(n)<span class="hljs-comment">//10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">闭包及堆内存释放</h2>
<p>堆内存：存储引用数据类型值（对象：键值对  函数：代码字符串）
栈内存：提供JS代码执行的环境和存储基本类型值</p>
<ul>
<li>【堆内存释放】</li>
</ul>
<p>让所有引用堆内存空间地址的变量赋值为null即可（没有变量占用这个对内存了，浏览器会在空闲的时候把它释放掉）</p>
<ul>
<li>【栈内存释放】</li>
</ul>
<p>一般情况下，当函数执行完成，所形成的私有作用域（栈内存）都会自动释放掉（在栈内存中存储的值也都会释放掉），但是也有特殊不销毁的情况：</p>
<ol>
<li>函数执行完成，当前形成的栈内存中，某些内容被栈内存以外的变量占用了，此时栈内存不能释放（一旦释放外面找不到原有的内容了）</li>
<li>全局栈内存只有在页面关闭的时候才会被释放掉</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">i</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(n + (++i));
    &#125;
&#125;
<span class="hljs-keyword">var</span> f = fn(<span class="hljs-number">2</span>)  <span class="hljs-comment">// i = 2 </span>
f(<span class="hljs-number">3</span>)   <span class="hljs-comment">// n=3  6</span>
fn(<span class="hljs-number">5</span>)(<span class="hljs-number">6</span>) <span class="hljs-comment">//i=5 n=6  12</span>
fn(<span class="hljs-number">7</span>)(<span class="hljs-number">8</span>) <span class="hljs-comment">//i=7 n=8   16</span>
f(<span class="hljs-number">4</span>) <span class="hljs-comment">// i=3 n=4   8</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> k = <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span> + k++, k) <span class="hljs-comment">//6  2</span>
k = <span class="hljs-number">1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span> + ++k, k) <span class="hljs-comment">//7  2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">闭包作用之保护</h2>
<p>函数执行形成一个私有的作用域，保护里面的私有变量不受外界的干扰，这种保护机制称之为“闭包”</p>
<p>市面上的开发者认为的闭包是：形成一个不销毁的私有作用域（私有栈内存）才是闭包</p>
<pre><code class="hljs language-js copyable" lang="js">闭包：柯里化函数
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;
&#125;
<span class="hljs-comment">// 被f占有了，不能被销毁</span>
<span class="hljs-keyword">var</span> f = fn();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">闭包：惰性函数   立即执行函数
<span class="hljs-keyword">var</span> utils = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;&#125;
&#125;)()

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>面试的时候可以写以上形式，都是形成不销毁内存</strong></p>
<p>闭包项目实战应用：
真实项目中为了保证JS的性能（堆栈内存的性能优化），应该尽可能的减少闭包的使用（不销毁的堆栈内存是耗性能的）</p>
<ul>
<li>闭包具有“保护”作用：保护私有变量不受外界的干扰</li>
</ul>
<p>在真实项目中，尤其是团队协作开发的时候，应当尽可能得减少全局变量的使用，以防止相互之间的冲突（“全局变量污染”），那么此时我们完全可以把自己这一部分内容封装到一个闭包中，让全局变量转换为私有变量</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> n = <span class="hljs-number">12</span>;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(n)&#125;
    <span class="hljs-keyword">return</span> fn
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不仅如此，我们封装类库插件的时候，也会把自己的程序都存放到闭包中保护起来，防止和用户的程序冲突，但是我们又需要暴露一些方法给客户使用，这样我们如何处理呢？</p>
<ol>
<li>Jquery这种方式：把需要暴露的方法抛给全局</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jQuery</span>(<span class="hljs-params"></span>)</span>&#123;c&#125;
    <span class="hljs-built_in">window</span>.jQuery = <span class="hljs-built_in">window</span>.$ = jQuery; <span class="hljs-comment">// 把需要供外面使用的方法，通过给win设置属性的方式暴露出去</span>
&#125;)()
jQuery();
$();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>Zepto这种凡是：基于return把需要供外面使用的方法暴露出来</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Zepto = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">xxx</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    &#125;
&#125;)()
Zepto.xxx()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>闭包具有“保存”作用：形成不销毁的栈内存，把一些值保存下来，方便后面得调取使用</li>
</ul>
<h2 data-id="heading-17">闭包作用之保存</h2>
<p>实例：tab切换</p>
<pre><code class="hljs language-js copyable" lang="js">i不是私有的

<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>, i<tabList.length;i++)&#123;
    tabList[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        changeTab(i)<span class="hljs-comment">//执行方法，形成一个私有的栈内存，遇到变量i，i不是私有变量，向上一级作用域查找（上级作用域是window），因为执行完了代码才会click，这时候全局i为3</span>
    &#125;
&#125;

以上点击的时候会报错
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在老版本中，判断和循环不能形成作用域，只有全局作用域和函数中的私有作用域</p>
<p>所有的事件绑定都是异步编程，所以当我们点击执行方法的时候，循环早已结束（让全局的i等于循环最后的结果3）</p>
<p>作用域查找机制  和 异步编程解释以上代码报错</p>
<p>解决方案：自定义属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>, i<tabList.length;i++)&#123;
    tabList[i].myIndex = i
    <span class="hljs-comment">//点击的时候执行的是小函数，自执行函数在给时间赋值的时候就已经执行</span>
    tabList[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        changeTab(<span class="hljs-built_in">this</span>.myIndex)<span class="hljs-comment">//this指向当前操作的元素对象</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决方案：闭包</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>, i<tabList.length;i++)&#123;
    tabList[i].onclick = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>) </span>&#123;
        <span class="hljs-keyword">var</span> i = n;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
          changeTab(i)  
        &#125;
    &#125;)(i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：循环3次，形成3个不销毁的私有作用域（自执行函数执行），而每一个不销毁的栈内存中都存储了一个私有变量i，而这个值分别是每一次执行传递进来的全局i的值（也就是：第一个不销毁额作用域存储的是0，第二个是1，第三个是2）；当点击的时候，执行返回的小函数，遇到变量i，向它自己的上级作用域查找，找到的i值分别是：0/1/2，达到了我们想要的效果；</p>
<p>耗性能，虽然能实现，最好不要这么写</p>
<pre><code class="hljs language-js copyable" lang="js">每个循序形成自己的私有作用域
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>, i<tabList.length;i++)&#123;
    (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>) </span>&#123;
        tabList[n].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            changeTab(n)<span class="hljs-comment">//this指向当前操作的元素对象</span>
        &#125;
    &#125;)(i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理都是形成3个不销毁的私有作用域，分别存储需要的索引值</p>
<p>解决方案：基于es6</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>, i<tabList.length;i++)&#123;
    tabList[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        changeTab(i)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">总结关键点</h2>
<ul>
<li>在当前作用域下，不管条件是否成立成立都要进行变量提升</li>
<li>带var 和 function 关键字声明相同的名字，这种也算是重名了（其实是一个fn，只是存储值得类型不一样）</li>
<li>关于重名的处理：如果名字重复了，不会重新的声明，但是会重新的定义（重新赋值）【不管是变量提升还是代码执行阶段都是如此】</li>
<li>暂存死区 typeof a为undefined 可以说明</li>
<li>堆内存：存储引用数据类型值（对象：键值对  函数：代码字符串）</li>
<li>栈内存：提供JS代码执行的环境和存储基本类型值</li>
<li>当前函数执行，形参是私有作用域A，A的上级作用域是谁，和它在哪执行的没有关系，<code>和它在哪创建有关系，在哪里创建的，它的上级作用域就是谁</code>。</li>
<li>闭包是形成一个不销毁的私有作用域（私有栈内存）</li>
<li>闭包有保存和保护作用</li>
</ul></div>  
</div>
            