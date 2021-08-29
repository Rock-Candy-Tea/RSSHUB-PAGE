
---
title: '重温js——执行上下文'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f24b3d576294db2894397485967b512~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 02:28:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f24b3d576294db2894397485967b512~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>执行上下文这个词大家都听过，但是里面内容有啥呢，那就继续往下看看。</p>
</blockquote>
<p>要明白上下文是啥，那么我们先来了解一下js的执行环境，运行过程等。</p>
<h1 data-id="heading-0">执行环境</h1>
<p>在函数的那一张中，提到了<strong>全局环境</strong>和<strong>局部环境</strong>的概念，就是说在函数的执行过程中，函数内部的环境和外面是独立的，只是说函数内部可以使用外面全局环境的变量或者在调用全局函数的方法。在此，来总结一下js的执行环境。</p>
<ul>
<li><code>Global</code>全局环境：这个全局的环境，是js引擎一启动的时候就加载好的环境，用于<strong>处理任何JS代码</strong>（变量的定义，函数声明，函数调用等）；</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f24b3d576294db2894397485967b512~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>Function</code>函数体环境：对于function函数环境来说，大部分人都清楚。函数内部是一块独立的空间，变量定义，再次声明函数，函数调用等都可以做到（当函数调用时候才会执行）。函数的本质是：<strong>降低代码的耦合</strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_41499782%2Farticle%2Fdetails%2F119683325" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_41499782/article/details/119683325" ref="nofollow noopener noreferrer">详情查看</a></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f2574585d804e77b223caa422f31be3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>eval</code>环境：使用<code>eval()</code>函数动态执行的JS代码</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e447ae527c284b7eba6b3cded87fde16~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>不同类型的<code>JS</code>代码具有不同的执行环境，所有的<code>JS</code>代码都是在一个执行环境中被执行的。执行环境是一种概念，同时也是一种机制。用来描述<code>js运行过程</code>（处理每一行代码所做的事情）。执行环境定义了变量或函数是否具有访问其他数据的权限，进而决定各自行为。</p>
</blockquote>
<h1 data-id="heading-1">运行过程</h1>
<blockquote>
<p>这里讨论js的代码的运行过程，但是在讨论前，这里先介绍几个特殊的名词：</p>
<ul>
<li><code>call stack(执行栈)</code>： 栈的特点是<code>FILO(first in, last out)</code>.js在执行代码的时候，会往执行栈中开辟一个内存空间，当代码执行完成后，相应的内存空间释放。</li>
<li><code>VO(variable object)</code>变量对象: 就是说js在执行栈中创建的内存空间是一个代码执行环境，每一个执行环境都会有一个<strong>变量映射表（类似对象）</strong>，来记录当前环境每一个变量对应的值。</li>
<li><code>GO(global object)</code>全局对象： 在执行栈中的最底层（一开进入栈的js执行环境）的vo对象，我们称之为<strong>全局对象</strong>，<strong>浏览器环境指代的是window对象，node环境指代的是global对象等</strong></li>
<li><code>AO(activity object)</code>活动对象： 在执行栈中当前活跃的执行环境，就是说在每一次栈中最<code>顶层的vo</code>,我们称之为<code>AO(活跃对象)</code>;</li>
</ul>
</blockquote>
<p>有了上面的那些概念，咋们来看一段代码，然后探讨一下代码是怎么运行的。</p>
<pre><code class="copyable">var global = 0;
console.log(global); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码运行图如下：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8932849c534641bebd05688bed33a7ff~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2"><code>函数执行环境</code>的规则</h2>
<p>虽然说js是解释性语言，但是在js在运行代码的时候会先扫码一下代码，然后遇到函数环境会做以下事情：</p>
<ol>
<li>确定形参和argument的参数一一对应；</li>
<li>确定本函数体内（除了内部的其他声明函数的区域）<code>var</code> 声明的变量(var 里面可以保存，函数，对象等),将他的值设置为undefined,如果当前的VO中已有变量则忽略。也就是说，argument在VO中的变量会是第一个声明，并且值是undefined；</li>
<li>确定通过<strong>字面量声明的函数（function aaa()&#123;&#125;的形式）</strong>，将他的值设置为函数的地址，如果VO中存在，<strong>会被覆盖</strong></li>
</ol>
<blockquote>
<p>当一个上下文中执行的代码的时候，如果当前<code>VO</code>不存在某个属性，将会通过作用域链的上一个<code>VO</code>中寻找。这里的作用域链是一块比较大的内容，留给后面的文章中。</p>
</blockquote>
<p>上面说到了函数执行环境的具体规则。那么咋们来小试牛刀，拿几道题目来练练手。不然原理说那么多也容易忘。</p>
<pre><code class="copyable">console.log(a);
var a = 123;
function a() &#123;
    console.log('眼见为实');
&#125;;
console.log(a);
function a() &#123;
    console.log('理解才是真');
&#125;;
console.log(a) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码的开始的扫码图如下：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ea23738da824ea28d1266c883c85afe~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过代码的扫码预检，我们可以发现，<code>全局的GO</code>对象中的a,最后被赋值给了<code>fn</code>(fn是一个函数，并且地址指向<strong>函数的内容是理解才是真</strong>)，所以第一行输出 <strong>fn(理解才是真)</strong>，然后执行代码，a 被赋值给了123，后面的函数被预检后就没有任何作用。所以后面两个输出的结果都是 123；</p>
<p><strong>结果</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcccc4395b044e7a92c480dd6bb69008~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>为了方便大家理解执行上下文，所以再来一道题目。</p>
</blockquote>
<p><strong>题目升级</strong></p>
<pre><code class="copyable">var g1 = 123;
function Test(a,b)&#123;
console.log(a,b,g1);
var b = 123;
function b()&#123;&#125;;
var a = function()&#123;&#125;;
console.log(a,b)
&#125;
var g2 = 456;
var g3 = function()&#123;&#125;;
Test(1,2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一道题目就不画执行上下文的内存图了，有兴趣的可以去画一画，加深自己的理解。</p>
<p><strong>解题：</strong></p>
<pre><code class="copyable">

GO:&#123;
 g1: undefined
 g2： undefined
 g3： undefied
&#125;


GO:&#123;
 g1: undefined
 g2： undefined
 g3： undefied
 Test: fn
&#125;


GO:&#123;
 g1: 123
 g2： 456
 g3： fn(g3)
 Test: fn(test)
&#125;



VO(Test)&#123;
a:1,
b: 2
&#125;


在这一步中会发现使用var定义的a,b在形参中都存在了，不管


VO(Test)&#123;
a:1,
b: fn（）
&#125;

第一行console.log 输出的a和b在当前的VO中都存在，g1不存在去全局的GO中寻找，得出的结果是 1，fn(), 123

第二行b是一个赋值语句，赋值给了123
VO(Test)&#123;
a:1,
b: 123
&#125;

第三行b那个声明函数不用管

第四行的a赋值给了一个函数
VO(Test)&#123;
a:fn(),
b: 123
&#125;

第五行输出结果的a和b在当前的VO中都存在，结果是 fn, 123
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>结果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e988e02ddba45ceada82541d3edf6c2~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>能看到这里的不容易，我为你点赞，但是对于这种理论性的知识，自己一定需要多画一画，有练一练才可能掌握哦！</p>
</blockquote></div>  
</div>
            