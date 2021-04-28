
---
title: 'JavaScripts高阶（1）你一定要知道的数据类型的核心操作原理、堆栈内存'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6704'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 18:32:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=6704'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>全局作用域：<code>window</code>  <code>global</code></p>
<p>变量和常量能存任何数据类型</p>
</blockquote>
<h2 data-id="heading-0">js的数据类型</h2>
<h3 data-id="heading-1">基础数据类型（值类型）</h3>
<ul>
<li><code>number</code></li>
<li><code>string</code></li>
<li><code>boolean</code></li>
<li><code>null</code></li>
<li><code>undefined</code></li>
<li><code>symbol</code></li>
</ul>
<h3 data-id="heading-2">引用数据类型</h3>
<h4 data-id="heading-3">对象</h4>
<ul>
<li>&#123;&#125; <code>普通对象</code>（json）</li>
<li>[] <code>数组</code></li>
<li><code>/^$/</code> <code>正则</code></li>
<li><code>Math 对象</code>数据类型</li>
</ul>
<h4 data-id="heading-4">函数</h4>
<ul>
<li><code>function</code> 普通函数</li>
<li><code>class</code>类</li>
</ul>
<h2 data-id="heading-5">操作规律</h2>
<h3 data-id="heading-6">值类型（基本数据类型）：</h3>
<blockquote>
<p>var a=12;</p>
</blockquote>
<ul>
<li>1)首先在<code>当前作用域中声明一个变量</code>a,没有赋值是 <code>undefined</code></li>
<li>2）在当<code>前作用域</code>中<code>开辟一个位置存储</code>12</li>
<li>3）让声明的变量和存储的12<code>进行关联</code></li>
</ul>
<blockquote>
<p><code>直接按值操作：把原有的值复制一份，放在新的空间位置上，和原来的值没有关系。  变量间相互不影响</code></p>
<p>一个变量只能存一个值</p>
</blockquote>
<h3 data-id="heading-7">对象数据类型：（按内存空间操作)</h3>
<ul>
<li>1、先<code>创建一个变量</code>（声明一个函数名和声明一个变量一样 ，如果两个变量名重复 是会冲突的）；</li>
<li>2、浏览器为其<code>开辟一个新的内存空间</code>，为了方便别的地方找到这个空间 会给空间<code>分配一个16进制的地址</code> （16进制：0-9 a-f）</li>
<li>3、<code>按照一定顺序，把对象中的键值对存到内存空间</code></li>
<li>4、把开辟内存的地址赋值给变量（或者其他的东西比如事件），以后变量就可以通过地址找到内存空间然后进行操作</li>
</ul>
<blockquote>
<p><code>操作的是空间的引用地址</code>：把原来空间地址赋值给新变量，但是空间没有被克隆，还是一个空间，这样就会出现<code>多个变量关联的是相同的空间</code>，<code>相互之间就会存在影响</code></p>
</blockquote>

<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a=&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'哈哈'</span>&#125;
<span class="hljs-number">1</span>、声明变量a
<span class="hljs-number">2</span>、 开辟空间 111fff000
<span class="hljs-number">3</span>、111fff000空间内 存储键值对 name:<span class="hljs-string">'哈哈'</span>
<span class="hljs-number">4</span>、把111fff000赋值给a
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">函数的操作：</h3>
<h4 data-id="heading-9">创建函数：</h4>
<ul>
<li>1、先开一个<code>新的内存空间</code>（为其<code>分配了一个16进制的地址</code>）</li>
<li>2、把函数体中编写的<code>js代码当做 “字符串”</code> 存储到空间当中（所以<code>函数只创建不执行没有意义</code>）</li>
<li>3、把分配的<code>地址赋值给</code>声明的<code>函数名</code>  （<code>function fn()&#123;&#125;</code>和<code>var fn=function()&#123;&#125;</code> 两种声明的方式 操作原理相同，都是在当前作用域中声明了一个名字，此处两个都写的话名字是重复的）</li>
</ul>
<h4 data-id="heading-10">执行函数-目的：执行函数体中的代码</h4>
<ul>
<li>1、函数执行的时候 浏览器会<code>形成一个新的**私有作用域**</code>（只能执行函数体中的代码），供函数体中的代码执行，每次执行函数都会形成新的私有作用域</li>
<li>2、执行代码之前先<code>把创建函数的字符串 复制过来 变为真正的js表达式</code>，按照从上到下的顺序在私有作用域中执行。</li>
</ul>
<blockquote>
<p>一个函数可以被执行N次，每次执行相互之间互不干扰,因为每次执行函数都会执行上边的步骤 重新创建私有作用域。</p>
</blockquote>
<h3 data-id="heading-11">示例</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a=<span class="hljs-number">10</span>;
<span class="hljs-keyword">var</span> b=a;
b=<span class="hljs-number">14</span>;
<span class="hljs-built_in">console</span>.log(a)  => <span class="hljs-number">10</span>

<span class="hljs-comment">//改变了同一空间地址内的键值</span>
<span class="hljs-keyword">var</span> c=&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'haha'</span>&#125;
<span class="hljs-keyword">var</span> d=c;
d.name=<span class="hljs-string">'quququ'</span>;
<span class="hljs-built_in">console</span>.log(c) =>  &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">"quququ"</span>&#125;

<span class="hljs-comment">//从新定义了地址  不改变原有空间</span>
<span class="hljs-keyword">var</span> m=&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'aaa'</span>&#125;
<span class="hljs-keyword">var</span> n=m;
n=&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'bbb'</span>&#125;
<span class="hljs-built_in">console</span>.log(m.name) => aaa
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">“闭包”：</h2>
<blockquote>
<p>执行函数时形成的私有作用域把函数体中的私有变量都包裹起来（保护起来），在私有作用域中操作私有变量和外界没有关系，外界也无法直接的操作私有变量，我们把函数执行的这种机制叫做闭包（<code>函数执行，形成一个私有作用域，保护里面的私有变量不受外界的干扰，这种保护机制就叫**闭包**</code>）</p>
<p>但是现在也有很多人认为，函数执行，形成一个不销毁的私有作用域，除了保护私有变量以外，还可以存储一些内容，这样的模式才叫闭包</p>
</blockquote>
<h2 data-id="heading-13">JS中的堆栈内存：</h2>
<h3 data-id="heading-14">栈内存：俗称作用域（全局作用域/私有作用域）</h3>
<blockquote>
<p>为js代码提供执行的环境（<code>js代码都是在栈内存中执行的</code>）</p>
<p><code>基本数据类型值是直接存放在栈内存中的</code>（因为基本数据类型值比较简单，他们直接在栈内存中开辟一个位置把值存进去）</p>
<p>当栈内存被销毁时，存储的那些基本数据类型值也都跟着销毁了</p>
</blockquote>
<h3 data-id="heading-15">堆内存：</h3>
<blockquote>
<p>存储引用数据类型值的（相当于一个存储的仓库）</p>
<p>对象存储的是键值对</p>
<p>函数存储的是代码字符串</p>
</blockquote>
<h2 data-id="heading-16">内存处理：</h2>
<h3 data-id="heading-17">堆内存处理：</h3>
<blockquote>
<p>var o=&#123;&#125; 当前对象对应的内存被变量O占用着，堆内存是无法销毁的；</p>
<p>销毁方法  o=null;null空对象指针（不指向任何的堆内存），这时候原来的堆内存就没被占用了，</p>
<p>谷歌浏览器会在空闲时间把没有被占用堆内存自动释放</p>
</blockquote>
<h3 data-id="heading-18">栈内存处理：</h3>
<blockquote>
<p>一般情况下<code>函数执行形成栈内存</code>，函数执行完浏览器会把形成的栈内存自动释放，</p>
<p>特殊情况下，函数执行完成后栈内存不能被释放（返回引用数据类型被别处引用）。</p>
<p>全局作用域在加载页面时执行，在关掉页面时销毁。</p>
</blockquote></div>  
</div>
            