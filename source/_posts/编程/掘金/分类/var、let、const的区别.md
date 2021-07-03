
---
title: 'var、let、const的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4456'
author: 掘金
comments: false
date: Sat, 03 Jul 2021 01:36:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=4456'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>一句话，let和const是var的改良版，能用const就不用let， 能用let就不用var。<br>
一、var的缺陷，先来看看使用var定义变量会有哪些问题:<br>
1.var不是块级作用域,下面的代码循环已经结束了，却还可以访问到变量test,可能会引起bug</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-number">10</span>;i++)&#123;
        <span class="hljs-keyword">var</span> test = i;
    &#125;

    <span class="hljs-built_in">console</span>.log(test);<span class="hljs-comment">//9</span>
    <span class="hljs-built_in">console</span>.log(i)<span class="hljs-comment">//10 用来记数的变量也可以访问， 无意中就污染了全局变量</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.var定义的变量，有变量提升，变量提升，会对程序的维护带来困扰。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>)&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行了'</span>);
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'没执行'</span>);
        <span class="hljs-keyword">var</span> j = <span class="hljs-number">2</span>;
    &#125;

    <span class="hljs-built_in">console</span>.log(j);   <span class="hljs-comment">//输出undefined 定义变量j的代码虽然没有执行，但是却依然不会报错 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.var定义的变量，不会为异步任务单独绑定变量,下面这段代码，本意是让它每隔一段时间输出0-9，结果却输出了10个10</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3</span>; i++) &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
      &#125;, <span class="hljs-number">1000</span>);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.var定义的变量，可以重复定义，这样就显得非常的随意松散</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">var</span> a =<span class="hljs-number">1</span>;
    <span class="hljs-keyword">var</span> a =<span class="hljs-number">2</span>;

    <span class="hljs-built_in">console</span>.log(a);<span class="hljs-comment">//输出后面定义的2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二、let和const就是ES6针对以上问题提出的解决方案,let和var的区别具体如下：<br>
1.let声明的变量是块级作用域的，这个特性解决了原来使用var容易污染全局变量的弊端。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-number">10</span>;i++)&#123;
        <span class="hljs-keyword">let</span> test = i;
    &#125;

    <span class="hljs-built_in">console</span>.log(i);<span class="hljs-comment">//Uncaught ReferenceError: i is not defined</span>
    <span class="hljs-built_in">console</span>.log(test)<span class="hljs-comment">//Uncaught ReferenceError: test is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.let声明的变量不存在变量提升，从let的块级作用域开始，到初始化位置，称作“暂存死区”，对于变量的暂存死区中使用变量会报Reference错误。这个特性就使得我们先定义变量再使用的变量，避免了var变量提升带来的难以查找的bug,也增强了代码的可读性。(也有文章认为let和const是有变量提升的，但是从结果上我们直接把let和const理解成没有变量提升是正确的。)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">//使用var</span>
    <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">// 输出undefined</span>
    <span class="hljs-keyword">var</span> i = <span class="hljs-number">2</span>;

    <span class="hljs-comment">//使用let</span>
    <span class="hljs-built_in">console</span>.log(j);
    <span class="hljs-keyword">let</span> j =<span class="hljs-number">10</span>; <span class="hljs-comment">//Uncaught ReferenceError: Cannot access 'j' before initialization</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.var可以重复定义变量，而let不可以，使得定义变量不再像var那么随意</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">//使用var</span>
    <span class="hljs-keyword">var</span>  a = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">var</span>  a = <span class="hljs-number">2</span>;
    <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// var可以重复定义，输出2</span>

    <span class="hljs-comment">//使用let</span>
    <span class="hljs-keyword">let</span> i =<span class="hljs-number">1</span>;
    <span class="hljs-keyword">let</span> i =<span class="hljs-number">2</span>;
    <span class="hljs-built_in">console</span>.log(i);<span class="hljs-comment">// let不能重复定义， Uncaught SyntaxError: Identifier 'i' has already been declared</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.var定义的全局变量属于顶层对象，而let、const声明的全局变量属于顶层对象，这也很容易理解， 因为let的设计初衷就是块级作用域变量，不污染全局变量，显得自由灵活安全。以浏览器为例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">var</span> a = <span class="hljs-number">0</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.a) <span class="hljs-comment">// 0</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.b) <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三、以上let具有的特性，const都有，const和let的区别如下：
1.const在声明常量的时候， 一定要初始化一个值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">     <span class="hljs-keyword">const</span> a=<span class="hljs-number">1</span>; <span class="hljs-comment">//正确</span>
     <span class="hljs-keyword">const</span> b = <span class="hljs-number">1</span>;
     b = <span class="hljs-number">5</span>;  <span class="hljs-comment">//TypeError: Assignment to constant variable.</span>
    <span class="hljs-keyword">const</span> c;  <span class="hljs-comment">//SyntaxError: Missing initializer in const declaration</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.const定义的常量值不允许修改,</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = <span class="hljs-number">0</span>;
a = <span class="hljs-number">1</span>; <span class="hljs-comment">// TypeError: Assignment to constant variabl</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是如果常量的类型为复杂类型(对象、数组等)时，对于常量值本身的操作是可以的， 因为const命令只是保证变量名指向的地址不变，并不保证该地址的数据不变。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">     <span class="hljs-keyword">const</span> a = &#123;&#125;;
     a.name=<span class="hljs-string">'小明'</span>
    <span class="hljs-built_in">console</span>.log(a);
     a = &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'小明'</span>&#125;;
     <span class="hljs-built_in">console</span>.log(a);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>四、总结
1.let和const声明的变量时块级作用域，避免了无意中全局变量污染，更加的灵活安全。另一个好处就是在循环语句中，let关键字为每次循环绑定单独绑定一个变量。
2.let和const没有变量提升，提高了代码的可维护性。
3.let和const不可以重复定义变量，修复var可以重复定义变量，使得变量的定义不再随意任性。
4.let和const定义的变量不属于顶层对象。
5.const声明一个常量的时候，一定要赋值。
6.const声明的常量并非真正意义上的常量，只保证变量名指向的地址不变，并不保证该地址的数据不变。
五、拓展
1.对于以下代码，改如何改正</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">//本意是要输出0-9，这段代码却输出10个10</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(i)
        &#125;, <span class="hljs-number">1000</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析：在js中先执行同步任务，再执行异步任务，setTimeout里面的代码是异步任务，等到执行时，var声明的变量i已经是10了。
解法1,利用setTimeout函数的第三个参数把i单独绑定</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">i</span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(i)
        &#125;, <span class="hljs-number">1000</span>, i);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解法2，利用闭包强制让setTimeout记住变量i</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">        (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">i</span>)</span>&#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(i) 
            &#125;, <span class="hljs-number">1000</span>)
        &#125;)(i);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解法3，利用let关键字</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(i)
            &#125;, <span class="hljs-number">1000</span>)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.对于以下代码，本意是要每隔1秒输出0-9，但这段代码的效果却是1秒钟后，同时输出了0-9，如何修正？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(i)
            &#125;, <span class="hljs-number">1000</span>)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析：在js中先执行同步任务，再执行异步任务，setTimeout函数的第二参数，相对的是异步任务结束的那一刻， 而不是上一个异步任务结束的那一刻，所以，修正的方法是动态改变第二个参数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(i)
            &#125;, <span class="hljs-number">1000</span>*i)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考资料：<br>
<a href="https://juejin.cn/post/6844903752139276301" target="_blank">var和let/const的区别</a><br>
<a href="https://www.cnblogs.com/JobsOfferings/p/varLetConst.html" target="_blank" rel="nofollow noopener noreferrer">var、let和const的区别详解</a></p></div>  
</div>
            