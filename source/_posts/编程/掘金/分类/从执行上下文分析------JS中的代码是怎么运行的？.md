
---
title: '从执行上下文分析------JS中的代码是怎么运行的？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aed2bb89a6264c098743d014e6b1f525~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 23:20:13 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aed2bb89a6264c098743d014e6b1f525~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aed2bb89a6264c098743d014e6b1f525~tplv-k3u1fbpfcp-watermark.image" alt="src=http___img4.orsoon.com_ico_201910_09101709_af0923f23b.png&refer=http___img4.orsoon.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">一、了解JS</h1>
<p>我们知道JS属于脚本语言，是一种解释型语言，可以一边转换一边执行，不会生成可执行文件，支持跨平台执行，而它能这样做主要是归功于解释器这个中间层。</p>
<blockquote>
<p>这里指的跨平台是源代码可以跨平台，不是解释器跨平台。
官方针对不同的平台开发不同的解释器，使得它们遵从相同的函数，相同的语法，有着相同功能。</p>
</blockquote>
<p>在chrome浏览器中的V8引擎就充当着解释器这样一个身份，将JS源代码解释执行。</p>
<h1 data-id="heading-1">二、执行上下文</h1>
<p>执行上下文简单的来说就是JS代码运行的环境,全局执行上下文就是全局环境，函数执行上下文就是函数内的环境了。</p>
<p>代码要运行首先要进入到全局执行上下文。</p>
<p><strong>执行上下文分为</strong>：</p>
<p><strong>全局执行上下文</strong>：全局上下文只有一个，不在函数中的代码都位于全局执行上下文中。</p>
<p><strong>函数执行上下文</strong>：每个函数都有自己的函数执行上下文，但只有函数调用时才会创建函数执行上下文，函数执行上下文数量是没有限制的。</p>
<p><strong>eval执行上下文</strong>：基本很少用上。</p>
<h2 data-id="heading-2">执行上下文的阶段</h2>
<p>执行上下文分为创建、执行、回收三个阶段，创建阶段分为三步：</p>
<ol>
<li>
<p><strong>变量对象（VO）</strong>：用于变量提升，函数声明，这一步也可以称为预编译，在全局环境下VO 也可看作预编译创建的GO。</p>
</li>
<li>
<p><strong>作用域链</strong>：作用域在创建变量对象之后创建，作用域用来解析变量，当变量在自己的作用域内无法找到，就会从它的父级作用域下寻找，依次下去，直到找到或到了最外层作用域。</p>
</li>
<li>
<p><strong>this</strong>：确定this的指向，在全局下this指向window，当然，this的值在执行时才会确定。</p>
</li>
</ol>
<p>执行上下文的执行阶段：给变量赋值，函数调用，执行代码。</p>
<p>执行上下文回收阶段：将执行上下文弹出栈，等待回收。</p>
<h1 data-id="heading-3">三、执行堆栈</h1>
<p>可以把他理解成一种栈结构，遵循先进后出原则，创建的执行上下文要执行就要将其放入执行栈中。</p>
<h2 data-id="heading-4">执行栈的运行过程</h2>
<ol>
<li>
<p>浏览器最开始执行代码创建全局执行上下文，将其压入执行栈的底部。</p>
</li>
<li>
<p>当遇到函数调用时，创建函数执行上下文，将其压入栈，此时位于全局执行上下文的上方，当在函数执行中又遇到函数调用，继续创建新的函数执行上下文，将其压入栈，此时它位于上一个函数上下文上方。当函数执行结束，将函数执行上下文弹出执行栈，等待回收。</p>
</li>
<li>
<p>浏览器只会调用位于栈顶的执行上下文。</p>
</li>
<li>
<p>全局执行上下文在浏览器关闭时弹出。</p>
</li>
</ol>
<h2 data-id="heading-5">代码演示</h2>
<p>我们通过一段简单的代码来演示这一过程</p>
<pre><code class="copyable">var a= 3
var b = 3
function output1() &#123;
    console.log(a)
    output2()
&#125;

function output2()  &#123;
    console.log(b);
&#125;
output1()
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p>浏览器创建全局执行上下文，将其压入最底层</p>
</li>
<li>
<p>函数声明不会创建函数执行上下文，直到<code>output1</code>函数调用，创建同名函数执行上下文，将它压入栈</p>
</li>
<li>
<p>在<code>output1</code>函数调用过程中，遇到了<code>output2</code>的调用，创建<code>output2</code>函数执行上下文，继续压入栈。</p>
</li>
<li>
<p><code>output2</code>执行完毕，将其弹出栈，将控制权交给它下方的上下文，即<code>output1</code>函数执行上下文。</p>
</li>
<li>
<p><code>output1</code>也执行完毕，同样也弹出执行栈，控制权交给全局执行上下文，直到全局也最后弹出。</p>
</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfb0c3fe055c4866b520a4cd036c11c1~tplv-k3u1fbpfcp-watermark.image" alt="未命名文件.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">四、变量提升/预编译</h1>
<p>预编译发生在函数执行之前，会对代码进行一次扫描，找到函数声明以及变量声明。</p>
<p>变量提升发生在执行上下文的创建阶段，对变量，函数声明进行提升。</p>
<p>就我个人理解来说，其实预编译和变量提升的区别不是很大，应该说是预编译就是变量提升的另一种叫法。</p>
<h2 data-id="heading-7">预编译过程：</h2>
<h3 data-id="heading-8">预编译发生在全局  三部曲</h3>
<ol>
<li>创建<code>GO</code>对象 （在全局执行上下文中<strong>VO = GO</strong>）</li>
<li>找变量声明，将变量声明作为<code>GO</code>对象的属性名，值赋予<code>undefined</code></li>
<li>找全局里的函数声明，将函数名作为<code>GO</code>对象的属性名，值赋予函数体</li>
</ol>
<h3 data-id="heading-9">预编译发生在函数内  四部曲</h3>
<ol>
<li>创建一个<code>AO</code>对象（activation object）</li>
<li>找形参和变量声明，将形参和变量声明作为<code>AO</code>对象的属性名，值为<code>undefined</code></li>
<li>将实参和形参统一</li>
<li>在函数体里找函数声明，将函数名作为<code>AO</code>对象的属性名，值赋予函数体</li>
</ol>
<h2 data-id="heading-10">预编译规则：</h2>
<ol>
<li>
<p>变量声明提升：对于用var定义的变量，在预编译阶段会对变量进行提升，将变量提升到所在作用域的顶部，并初始化为undefined。</p>
</li>
<li>
<p>函数声明提升：对于函数声明来说，同样会受到提升，但是函数声明提升的是整个函数，会创建一个函数变量，并把函数中的所有东西都保存在里面，但不会执行。</p>
</li>
<li>
<p>函数声明优先级更高，当函数声明和变量声明同时提升时，函数声明会覆盖掉同名变量声明，但变量声明可以重新赋值。</p>
</li>
<li>
<p>例如 <code>a = 2</code>这样的赋值语句不属于声明，在执行阶段运行，创建的变量属于全局变量，作用域是全局。</p>
</li>
</ol>
<h2 data-id="heading-11">代码演示</h2>
<pre><code class="copyable">         var a = 1
         function fn(a) &#123;
             var a = 2
             function a() &#123;&#125;
             var b = a
             console.log(a);
            
        &#125;
         fn(3)     //2
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p>创建<code>GO</code>对象，对变量<code>a</code>进行变量提升，初始化为<code>undefined</code>，接着对<code>fn</code>函数声明提升，提升整个<code>fn</code>函数，但先不执行，接着进入代码执行，<code>a</code>被赋值为1，下一步调用函数<code>fn</code>。</p>
</li>
<li>
<p>遇到<code>fn</code>函数调用，创建<code>Ao</code>对象，将形参及变量<code>a</code>提升，初始化为<code>undefined</code>，变量b提升，初始化为undefined。</p>
</li>
<li>
<p>将形参和实参值统一为3，即a为3，最后将函数a提升，由于<strong>函数优先原则</strong>，a此时被初始化为函数a，进入代码执行阶段，a被赋值为2，b被赋值为a，即2，最后输出a为2。</p>
</li>
</ol>
<p><strong>GO、AO对象的创建结果</strong></p>
<pre><code class="copyable">    go:&#123;
        a: undefined  1
        fn: function

    &#125;

    ao: &#123;
        a:undefined 3  function  2
        b: undefined  2 
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">五、分析代码运行步骤</h1>
<p><strong>我们通过下面这段代码分析代码是怎样一步步运行</strong></p>
<pre><code class="copyable">var a = 1

function fo(a) &#123;
    var b = 2
    console.log(a);  //输出2
    function fo1() &#123;
        console.log(b);  // 输出2
    &#125;

    return fo1  // 产生闭包
&#125;

var c = fo(2)
c()
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>创建全局执行上下文，将其压入执行栈最底部，上下文创建阶段--创建变量对象/预编译阶段（变量声明、函数声明提升）、创建作用域链、this绑定。</li>
</ol>
<ul>
<li>创建<code>go</code>对象，将<code>a</code>，<code>c</code>提升并初始化为<code>undefined</code>，<code>fo</code>函数声明提升整个函数体，将它们都保存在<code>go</code>对象中，this指向window。</li>
</ul>
<ol start="2">
<li>全局执行上下文进入执行阶段。</li>
</ol>
<ul>
<li>在<code>go</code>对象中将a赋值为1，将<code>c</code>赋值为<code>fo(2)</code>的返回值，此时遇到函数调用，创建函数执行上下文。</li>
</ul>
<ol start="3">
<li>创建<code>fo</code>函数执行上下文，将它压入执行栈，此时全局执行上下文在它下方，进入函数执行上下文创建阶段，依然进行同样的三步。</li>
</ol>
<ul>
<li>创建<code>ao</code>对象，将<code>a，b</code>初始化为<code>undefined</code>，之后将形参和实参统一，即<code>a</code>赋值为2，最后进行函数声明提升，将它们都保存在<code>ao</code>对象中。</li>
</ul>
<ol start="4">
<li><code>fo</code>函数执行上下文进入执行阶段。</li>
</ol>
<ul>
<li>将<code>b</code>赋值为2，输出此时的<code>a</code>的值，由于创建阶段进行了预编译，此时<code>a</code>的值为2，于是输出2，遇到<code>return</code>需要返回，将<code>fo1</code>函数里面的所有内容保存在<code>fo1</code>中返回，此时函数<code>fo</code>调用结束，通常情况会下，将<code>fo</code>执行上下文弹出执行栈，但是由于<code>return</code>的是一个函数，<strong>产生闭包机制，使得作用域未被删除，里面的变量仍可以使用。</strong></li>
</ul>
<ol start="5">
<li>
<p><code>fo</code>函数调用结束，返回值是一个函数<code>fo1</code>，将它赋值给<code>c</code>，于是在全局上下文中，它不在是<code>fo1</code>，它被叫做<code>c</code>，接下来，调用<code>c</code>。</p>
</li>
<li>
<p>遇到函数调用，创建<code>c</code>函数执行上下文，压入执行栈，上下文创建阶段--创建变量对象、创建作用域链、this绑定。</p>
</li>
</ol>
<ul>
<li>创建<code>ao</code>对象，只有一句输出语句，所以没有变量、函数提升。</li>
</ul>
<ol start="7">
<li><code>fo1</code>执行阶段，由于在外部调用<code>fo</code>的内部函数，闭包机制导致<code>fo</code>作用域不释放，所以输出b时，向父级作用域查找，找到此时<code>b</code>为2，输出2。</li>
</ol>
<ul>
<li>调用<code>fo1</code>结束，弹出函数执行栈，最后代码执行完毕，将执行栈清空。</li>
</ul>
<h3 data-id="heading-13">创建的变量对象：</h3>
<pre><code class="copyable">go: &#123;
    a: undefined  1
    fo: function
    c: undefined fo1
&#125;

ao: &#123;
    b: undefined 2
    a: undefined 2
    fo1: function  
&#125;

ao: &#123;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">六、总结</h1>
<p>本文介绍了js、执行上下文内容、执行栈、变量提升规则以及从执行上下文方面分析代码
，由于本人也是只是位初学者，将自己的看法进行总结记录，还是希望各位大佬能多多斧正，喜欢的可以点个小小的👍，感谢🙇‍🙇‍。</p></div>  
</div>
            