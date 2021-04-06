
---
title: 'JavaScript 面试题外的【this】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5104'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 19:31:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=5104'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>对于 <code>this</code> ，是前端基础面试题中的常客，同时在哪都有汗牛充栋的的文章一一列举 <code>this</code> 在不同的上下文环境中的指向的文章。但背会面试题却并不能应付实际的开发。</p>
</blockquote>
<p>假如在 js 中去掉 <code>this</code> ，会怎么样？</p>
<ul>
<li>全局函数 -> 直接写 <code>window</code> 嘛，干嘛用 <code>this</code></li>
<li>箭头函数 -> 在下内部本就没有 <code>this</code>，还是按照闭包的规则，该是谁就是谁</li>
<li><code>bind</code>、<code>apply</code>、<code>call</code> -> 在下本就是针对 <code>this</code> 的元编程，自然也不再需要，别了您内</li>
<li><strong>构造方法，对象方法 -> （尴尬）</strong></li>
</ul>
<p>其实 js 中的 <code>this</code> ，设计的目的便是实现看起来像 java 的 oop 模式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = <span class="hljs-keyword">new</span> foo()
a.bar() 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，作为构造函数的 <code>foo</code> 内 <code>this</code> 应该指向一个新的对象并作为结果返回，而作为方法的 <code>bar</code> 应该访问的是其对应的实例对象 <code>a</code>。</p>
<p>让我们再瞟一眼声明</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)&#125;

<span class="hljs-comment">// 在某不知名的角落里</span>
foo.prototype.bar = bar
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在声明的时候我哪知道谁是构造函数，谁是实例方法（掀桌）。</p>
<p>好吧，那只能看函数执行时动态确定了，用 <code>new [fn](...args)</code> 执行的是构造函数，用 <code>obj.[fn](...args)</code> 执行的是对象方法。以此确定 <code>this</code> 的指向。</p>
<p>如此看来在函数中，本就不该访问 <code>this</code>，应该报错。在拥有闭包作用域的 lambda 表达式中，<code>this</code> 应该按闭包的规则向上层查找。</p>
<p>慢着，js 的函数本身就带闭包作用域那咋办？</p>
<p><del>啊啊啊，不管了，</del> 直接就指向 <code>window</code> 吧，<del>本就一周设计出来的玩意，还想咋地，又不是不能用</del>……</p>
<hr>
<p>js 相比其他很多语言拥有更高度的动态性，而这种动态性并非都是优势，一些来自于过于敷衍的设计的动态性，往往会造成各种灾难，<code>this</code> 便是一例。</p>
<p>this 这种灾难来自于设计者想把全局函数、lambda 表达式、构造函数、对象上的方法糅合在一起。然而这并无必要。</p>
<p>为什么其他语言不会有这种问题，因为其他语言把全局函数、lambda 表达式、构造函数、对象上的方法声明时分的很清楚，并不需要动态去确定。</p>
<p>以 rust 举例</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">pub</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">ClassName</span></span> &#123;
    field: <span class="hljs-built_in">i32</span>,
&#125;

<span class="hljs-keyword">impl</span> ClassName &#123;
    <span class="hljs-comment">// 充当构造函数的静态方法 new，返回一个 ClassName 实例</span>
    <span class="hljs-keyword">pub</span> <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">new</span></span>(value: <span class="hljs-built_in">i32</span>) -> ClassName &#123;
        ClassName &#123;
            field: value
        &#125;
    &#125;

    <span class="hljs-keyword">pub</span> <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">public_method</span></span>(&<span class="hljs-keyword">self</span>) &#123;
        <span class="hljs-comment">// 方法内显示声明的 self 即是 js 内部隐式声明的 this</span>
        <span class="hljs-built_in">println!</span>(<span class="hljs-string">"from public method"</span>);
        <span class="hljs-keyword">self</span>.private_method();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">private_method</span></span>(&<span class="hljs-keyword">self</span>) &#123;
        <span class="hljs-built_in">println!</span>(<span class="hljs-string">"from private method"</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 scala 的设计显然更为精妙。</p>
<pre><code class="hljs language-scala copyable" lang="scala"><span class="hljs-comment">// class 的声明代表这是一个构造函数</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span>(<span class="hljs-params">xc: <span class="hljs-type">Int</span>, yc: <span class="hljs-type">Int</span></span>) </span>&#123;
   <span class="hljs-comment">// 构造函数中声明的变量/常量就是对象的属性</span>
   <span class="hljs-keyword">var</span> x: <span class="hljs-type">Int</span> = xc
   <span class="hljs-keyword">var</span> y: <span class="hljs-type">Int</span> = yc

   <span class="hljs-comment">// 构造函数中声明的函数就是对象的方法</span>
   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">move</span></span>(dx: <span class="hljs-type">Int</span>, dy: <span class="hljs-type">Int</span>) &#123;
      x = x + dx
      y = y + dy
      println (<span class="hljs-string">"x 的坐标点: "</span> + x);
      println (<span class="hljs-string">"y 的坐标点: "</span> + y);
   &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>今时今日的 js 已经不再是那个 js 了。在 <code>this</code> 问题上，TC39 委员会又做了那些努力呢。</p>
<p>首先，箭头函数替代了履行了 function 中 lambda 表达式的职能。在箭头函数中访问 <code>this</code>，也会以闭包的方式逐层向上查找了。<code>var _this = this</code> 已经成为了历(li)史(shi)。</p>
<p>全局函数中的 <code>this</code>，其实在严格模式中已经解决了一部分。</p>
<p>而真正应该用到 <code>this</code> 的地方即构造方法和实例方法，全都在 <code>class</code> 声明的括号内部。</p>
<p>也就说一般情况下，在我们的代码中， <code>this</code> 只能出现在 <code>class</code> 的括号内。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
    <span class="hljs-comment">// 显示声明的构造函数</span>
    <span class="hljs-built_in">this</span>.x = x;
    <span class="hljs-built_in">this</span>.y = y;
  &#125;

  <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 显示声明的对象方法</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">'('</span> + <span class="hljs-built_in">this</span>.x + <span class="hljs-string">', '</span> + <span class="hljs-built_in">this</span>.y + <span class="hljs-string">')'</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>为啥整篇文章避而不谈 <code>call/apply/bind</code>。因为在我看来这仨都属于 js 元编程的范畴。</p>
<p>何谓元编程？</p>
<blockquote>
<p>元编程,即编写的程序可以生成、操纵其它程序,又或是在程序运行时改变其自身。</p>
</blockquote>
<p>简而言之，就是在代码层面上赋予新的解释，针对代码进行编程。可以是由原来的代码生成新的代码，也可以是改写原代码的功能。</p>
<p>例如 <code>proxy</code> 就是让用户改写对象上的操作，<code>call/apply/bind</code> 则是改写函数内部的动态作用域规则（由于箭头函数内没有动态作用域，所以对它没用）， <code>with</code>那更是厉害到让人闻风丧胆。</p>
<p>而元编程则是业务代码中不允许出现，框架代码中慎之又慎的东西。</p>
<p>我希望在你用到的时候已经不需要这篇文章了。</p>
<hr>
<p>时下，不少人选择以面向面试题学习作为自己的学习方式。然而实际上应试教育和实际开发是有比较大的出入的。</p>
<p>譬如 <code>this</code> ，是前端基础面试题中的常客，同时在哪都有汗牛充栋的的文章一一列举 <code>this</code> 在不同的上下文环境中的指向的文章。有些文章甚至想出各种“花式”技巧，什么就近原则啊，什么各种嵌套啊。有用吗？私以为并没有啥用。反倒是那些能真的讲讲 this 为什么如此设计，以及如何应用的文章寥寥。</p>
<hr>
<p>下一篇，打算聊聊绝大多数人都没在代码里写过的 <code>WeakMap</code> <code>WeakSet</code>，如果大家觉得本文还有点内容，还请高抬贵手点个赞哈。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            