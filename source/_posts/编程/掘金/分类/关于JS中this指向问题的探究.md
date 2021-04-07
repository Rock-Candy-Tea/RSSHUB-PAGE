
---
title: '关于JS中this指向问题的探究'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4606'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 22:44:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=4606'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0"><a href="https://juejin.cn/post/6943479050052567076"></a>写在前面</h3>
<p>本篇文章的所有例子来源都是《JS设计模式与开发实践》这本书，写这篇文章之前也去查阅了很多关于this指向问题的探讨，包括但不仅仅有像阮一峰老师，还有很多的博主的帖子，还是决定写这篇文章有以下几个原因，第一，加深自己的理解，重新理一遍关于这方面的知识，第二，我尽可能的使用通俗简单的说辞进行解释<br>
力求让更多的人明白这个东西，第三，this是js中的一个关键字，很有必要单独拿出来写一篇文章。最后一个原因是记录以下拜读这本书的过程！</p>
<h3 data-id="heading-1"><a href="https://juejin.cn/post/6943479050052567076"></a>js中的this</h3>
<h4 data-id="heading-2"><a href="https://juejin.cn/post/6943479050052567076"></a>this</h4>
<blockquote>
<p>js中的this总是指向一个对象，也就是一个obj，但是具体指向的是哪一个obj是根据具体的运行时函数的执行环境动态绑定的，而不是函数被声明的环境！<br>
看完这句话如果不是很明白的话没关系，因为这个毕竟只是一个解释，给出这句话的时候如果你们就明白了，下面我写的一切都没意义了，所以不明白是对的，明白了当然更好！</p>
</blockquote>
<h5 data-id="heading-3"><a href="https://juejin.cn/post/6943479050052567076"></a>this的指向</h5>
<p>如果不考虑常用的with和eval的情况下，具体到实际应用中，this的指向大致可以分为下面四类：</p>
<ul>
<li>作为对象的方法调用</li>
<li>作为普通函数调用</li>
<li>构造器调用</li>
<li>Function.prototype.call 或者 Function.prototype.apply调用<br>
下面我们一个一个说</li>
</ul>
<h6 data-id="heading-4"><a href="https://juejin.cn/post/6943479050052567076"></a>作为对象的方法调用</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;
        <span class="hljs-attr">a</span> : <span class="hljs-number">1</span>,
        <span class="hljs-attr">getA</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.info(<span class="hljs-built_in">this</span> === obj) <span class="hljs-comment">// true</span>
            <span class="hljs-built_in">console</span>.info(<span class="hljs-built_in">this</span>.a)   <span class="hljs-comment">// 1</span>
        &#125;
    &#125;
    obj.getA()
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-5"><a href="https://juejin.cn/post/6943479050052567076"></a>作为普通函数调用</h6>
<blockquote>
<p>当我们不把函数作为一个对象的属性被调用时，也就是我们常见的普通函数使用的时候，此时的this其实指向的是当前的全局对象，也就是windows，因为在js中全局对象就是windows</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-built_in">window</span>.name = <span class="hljs-string">"globalName"</span>
    <span class="hljs-keyword">var</span> getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
    &#125;
    <span class="hljs-built_in">console</span>.info(getName()) <span class="hljs-comment">//globalName</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>或者这样写</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-built_in">window</span>.name = <span class="hljs-string">"globalName"</span>
    <span class="hljs-keyword">var</span> obj = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'seven'</span>,
        <span class="hljs-attr">getName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
        &#125;
    &#125;
    <span class="hljs-keyword">var</span> getName = obj.getName;
    <span class="hljs-built_in">console</span>.info(getName()) <span class="hljs-comment">//globalName</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>但是当我们使用一个函数调用的时候里面有一个局部的callback的方法，callback被当作普通函数被调用的时候，根据前面说的callback这个时候的this其实指向的是windows<br>
例如：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.id = <span class="hljs-string">"windows"</span>
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'div1'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.info(<span class="hljs-built_in">this</span>.id) <span class="hljs-comment">//div1</span>
        <span class="hljs-keyword">var</span> callback = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.info(<span class="hljs-built_in">this</span>.id) <span class="hljs-comment">//windows</span>
        &#125;
        callback()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这个时候我们想callback里面的this指向不发生改变的话，就需要将this的值重新指向为当前</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.id = <span class="hljs-string">"windows"</span>
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'div1'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.info(<span class="hljs-built_in">this</span>.id) <span class="hljs-comment">//div1</span>
        <span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">var</span> callback = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.info(that.id) <span class="hljs-comment">//div1</span>
        &#125;
        callback()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其实这种写法如果你使用过一些框架或者是写过一些这种情况下的js代码的话，是很好理解的。</p>
</blockquote>
<h6 data-id="heading-6"><a href="https://juejin.cn/post/6943479050052567076"></a>作为构造器调用</h6>
<blockquote>
<p>构造器看起来是和函数一样的，他们的区别在于被调用的方式不一样，当使用new调用的时候他总会返回一个对象，那么一般情况下此时的this指向的就是该对象</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> myClass = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">this</span>.name = <span class="hljs-string">"seven"</span>
    &#125;
    <span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> myClass()
    <span class="hljs-built_in">console</span>.info(obj.name) <span class="hljs-comment">//seven</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>那么如果我们按照下面的方式写的话，可能结果就不一样了</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> myClass = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">this</span>.name = <span class="hljs-string">"seven"</span>
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"anna"</span>
        &#125;
    &#125;
    <span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> myClass()
    <span class="hljs-built_in">console</span>.info(obj.name) <span class="hljs-comment">//anna</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>解释一下为什么，因为此时构造器显式的返回了一个对象，那么他的返回值就会被这个新的对象给替换，因为this指向的是一个对象。也就是说他可以返回，如果不是一个对象的话，那么this的指向还是不会变</p>
</blockquote>
<h6 data-id="heading-7"><a href="https://juejin.cn/post/6943479050052567076"></a>Function.prototype.call 或者 Function.prototype.apply调用</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;
        <span class="hljs-attr">name</span> : <span class="hljs-string">'seven'</span>,
        <span class="hljs-attr">getName</span> : <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
        &#125;
    &#125;;
    <span class="hljs-keyword">var</span> obj2 = &#123;
        <span class="hljs-attr">name</span> : <span class="hljs-string">'anna'</span>
    &#125;;
    <span class="hljs-built_in">console</span>.info(obj.getName()) <span class="hljs-comment">//seven</span>
    <span class="hljs-built_in">console</span>.info(obj.getName.call(obj2)) <span class="hljs-comment">//anna</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>具体为什么会这样，下篇文章后面会写关于apply和call的使用，可以简单的理解为他可以直接劫持this 的指向，重新给到一个新的对象！</p>
</blockquote>
<h5 data-id="heading-8"><a href="https://juejin.cn/post/6943479050052567076"></a>this丢失的情况</h5>
<blockquote>
<p>先看一段代码</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;
        <span class="hljs-attr">myName</span> : <span class="hljs-string">'seven'</span>,
        <span class="hljs-attr">getName</span> : <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
         <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.myName
        &#125;
    &#125;;
    <span class="hljs-built_in">console</span>.info(obj.getName()); <span class="hljs-comment">//seven</span>
    <span class="hljs-keyword">var</span> getName2 = obj.getName;
    <span class="hljs-built_in">console</span>.info(getName2()) <span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当第一次调用的时候，他是作为obj的属性被调用，那么此时的this指向的是这个对象，所以他是有myName的属性的，但是getName2是来自obj.getName<br>
此时是作为普通函数调用的，所以此时的this指向的是windows，但是我们windows并没有声明任何关于myName的值，所以是undefined</p>
</blockquote>
<ul>
<li>我们再看一种情况</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">var</span> getId = <span class="hljs-built_in">document</span>.getElementById
  getId(<span class="hljs-string">'div1'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这段代码会报错，原因是很多的引擎中document.getElementById内部实现是用到this指向的，原本这个this是指向document的，当document.getElementById这个方法被调用的时候this指向也确实是改document<br>
但是当我们使用getId来引用这个，他的this指向指的是windows</p>
</blockquote>
<ul>
<li>修复以后的代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.getElementById = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">func</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> func.apply(<span class="hljs-built_in">document</span>, <span class="hljs-built_in">arguments</span>)
        &#125;
    &#125;)(<span class="hljs-built_in">document</span>.getElementById)
    <span class="hljs-keyword">var</span> getId = <span class="hljs-built_in">document</span>.getElementById
    <span class="hljs-keyword">var</span> div = getId(<span class="hljs-string">'div1'</span>)
    <span class="hljs-built_in">console</span>.info(div.id) <span class="hljs-comment">//div1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9"><a href="https://juejin.cn/post/6943479050052567076"></a>最后</h3>
<p>其实this指向的问题和JS中很多别的不好理解的概念差不多，用的多了就明白了为什么那么写，很多的时候我们看到一个错，就知道需要使用let that = this类似这样的代码块解决，究其原因是他很理解错误的原因吗？其实是见的比较多了罢了，实践出真知，共勉！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            