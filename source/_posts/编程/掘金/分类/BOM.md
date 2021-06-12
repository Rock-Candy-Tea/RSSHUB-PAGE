
---
title: 'BOM'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d057533fbd1b4f06a9260d96721c2e7e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 02:46:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d057533fbd1b4f06a9260d96721c2e7e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. BOM 概述</h1>
<h2 data-id="heading-1">1.1. 什么是BOM</h2>
<p>BOM（Browser Object Model）即浏览器对象模型，它提供了独立于内容而与浏览器窗口进行交互的对象，其核心对象是 window。</p>
<p>BOM 由一系列相关的对象构成，并且每个对象都提供了很多方法与属性。</p>
<p>BOM 缺乏标准，JavaScript 语法的标准化组织是 ECMA，DOM 的标准化组织是 W3C，BOM 最初是Netscape 浏览器标准的一部分。</p>
<h3 data-id="heading-2">1.1.1. DOM</h3>
<ul>
<li>文档对象模型</li>
<li>DOM 就是把「文档」当做一个「对象」来看待</li>
<li>DOM 的顶级对象是 document</li>
<li>DOM 主要学习的是操作页面元素</li>
<li>DOM 是 W3C 标准规范</li>
</ul>
<h3 data-id="heading-3">1.1.2. BOM</h3>
<ul>
<li>浏览器对象模型</li>
<li>把「浏览器」当做一个「对象」来看待</li>
<li>BOM 的顶级对象是 window</li>
<li>BOM 学习的是浏览器窗口交互的一些对象</li>
<li>BOM 是浏览器厂商在各自浏览器上定义的，兼容性较差</li>
</ul>
<h2 data-id="heading-4">1.2. BOM的构成</h2>
<p>BOM 比 DOM 更大，它包含 DOM。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d057533fbd1b4f06a9260d96721c2e7e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">1.3. 顶级对象window</h2>
<p>window 对象是浏览器的顶级对象，它具有双重角色。</p>
<ol>
<li>它是 JS 访问浏览器窗口的一个接口。</li>
<li>它是一个全局对象。定义在全局作用域中的变量、函数都会变成 window 对象的属性和方法。</li>
</ol>
<p>在调用的时候可以省略 window，前面学习的对话框都属于 window 对象方法，如 alert()、prompt() 等。
注意：window下的一个特殊属性 window.name</p>
<h1 data-id="heading-6">2. window 对象的常见事件</h1>
<h2 data-id="heading-7">2.1. 窗口加载事件</h2>
<h3 data-id="heading-8">2.1.1. 第一种</h3>
<pre><code class="copyable">window.onload = function()&#123;&#125; 
或者 
window.addEventListener("load",function()&#123;&#125;); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>window.onload 是窗口 (页面）加载事件,当文档内容完全加载完成会触发该事件(包括图像、脚本文件、CSS 文件等), 就调用的处理函数。</p>
<p><strong>注意：</strong></p>
<ol>
<li>有了 window.onload 就可以把 JS 代码写到页面元素的上方，因为 onload 是等页面内容全部加载完毕，再去执行处理函数。</li>
<li>window.onload 传统注册事件方式 只能写一次，如果有多个，会以最后一个 window.onload 为准。</li>
<li>如果使用 addEventListener 则没有限制</li>
</ol>
<h3 data-id="heading-9">2.1.2. 第二种</h3>
<pre><code class="copyable">document.addEventListener('DOMContentLoaded',function()&#123;&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>DOMContentLoaded 事件触发时，仅当DOM加载完成，不包括样式表，图片，flash等等。 Ie9以上才支持</p>
<p>如果页面的图片很多的话, 从用户访问到onload触发可能需要较长的时间, 交互效果就不能实现，必然影响用户的体验，此时用 DOMContentLoaded 事件比较合适。</p>
<pre><code class="copyable">    <script>
        window.addEventListener('load', function() &#123;
            var btn = document.querySelector('button');
            btn.addEventListener('click', function() &#123;
                alert('点击我');
            &#125;)
        &#125;)
        window.addEventListener('load', function() &#123;
            alert(22);
        &#125;)
        document.addEventListener('DOMContentLoaded', function() &#123;
            alert(33);
        &#125;)
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">2.2. 调整窗口大小事件</h2>
<pre><code class="copyable"> window.onresize = function()&#123;&#125; 
 window.addEventListener("resize",function()&#123;&#125;); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>window.onresize 是调整窗口大小加载事件,  当触发时就调用的处理函数。</p>
<p><strong>注意：</strong></p>
<ol>
<li>只要窗口大小发生像素变化，就会触发这个事件。</li>
<li>我们经常利用这个事件完成响应式布局。 window.innerWidth 当前屏幕的宽度</li>
</ol>
<pre><code class="copyable">    <script>
        // 注册页面加载事件
        window.addEventListener('load', function() &#123;
            var div = document.querySelector('div');
        // 注册调整窗口大小事件
            window.addEventListener('resize', function() &#123;
                // window.innerWidth 获取窗口大小
                console.log('变化了');
                if (window.innerWidth <= 800) &#123;
                    div.style.display = 'none';
                &#125; else &#123;
                    div.style.display = 'block';
                &#125;
            &#125;)
        &#125;)
    </script>
    <div></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">3. 定时器（两种）</h1>
<p>window 对象给我们提供了 2 个非常好用的方法-定时器。</p>
<ul>
<li>setTimeout()</li>
<li>setInterval()</li>
</ul>
<h2 data-id="heading-12">3.1. setTimeout() 定时器</h2>
<h3 data-id="heading-13">3.1.1. 开启定时器</h3>
<pre><code class="copyable">window.setTimeout(调用函数, [延迟的毫秒数]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>setTimeout() 方法用于设置一个定时器，该定时器在定时器到期后执行调用函数，这个调用函数我们也称为callback</p>
<p><strong>注意：</strong></p>
<ol>
<li>window 可以省略。</li>
<li>这个调用函数可以直接写函数，或者写函数名或者采取字符串‘函数名()'三种形式。第三种不推荐</li>
<li>延迟的毫秒数省略默认是 0，如果写，必须是毫秒。</li>
<li>因为定时器可能有很多，所以我们经常给定时器赋值一个标识符。</li>
</ol>
<pre><code class="copyable">普通函数是按照代码顺序直接调用。

简单理解： 回调，就是回头调用的意思。上一件事干完，再回头再调用这个函数。
例如：定时器中的调用函数，事件处理函数，也是回调函数。

以前我们讲的   element.onclick = function()&#123;&#125;   或者  element.addEventListener(“click”, fn);   里面的 函数也是回调函数。

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">    <script>
        // 回调函数是一个匿名函数
         setTimeout(function() &#123;
             console.log('时间到了');

         &#125;, 2000);
        function callback() &#123;
            console.log('爆炸了');
        &#125;
// 回调函数是一个有名函数
        var timer1 = setTimeout(callback, 3000);
        var timer2 = setTimeout(callback, 5000);
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">3.1.2. 停止定时器</h3>
<pre><code class="copyable"> window.clearTimeout(timeoutID) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>clearTimeout()方法取消了先前通过调用 setTimeout() 建立的定时器。</p>
<p>注意：</p>
<ol>
<li>window 可以省略。</li>
<li>里面的参数就是定时器的标识符 。</li>
</ol>
<pre><code class="copyable">    <button>点击停止定时器</button>
    <script>
        var btn = document.querySelector('button');
// 开启定时器
        var timer = setTimeout(function() &#123;
            console.log('爆炸了');
        &#125;, 5000);
// 给按钮注册单击事件
        btn.addEventListener('click', function() &#123;
            // 停止定时器
            clearTimeout(timer);
        &#125;)
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">3.2. setInterval() 闹钟定时器</h2>
<h3 data-id="heading-16">3.2.1. 开启定时器</h3>
<pre><code class="copyable">window.setInterval(回调函数, [间隔的毫秒数]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>setInterval() 方法重复调用一个函数，每隔这个时间，就去调用一次回调函数。</p>
<p><strong>注意：</strong></p>
<ol>
<li>window 可以省略。</li>
<li>这个调用函数可以直接写函数，或者写函数名或者采取字符串 '函数名()'  三种形式。</li>
<li>间隔的毫秒数省略默认是 0，如果写，必须是毫秒，表示每隔多少毫秒就自动调用这个函数。</li>
<li>因为定时器可能有很多，所以我们经常给定时器赋值一个标识符。</li>
<li>第一次执行也是间隔毫秒数之后执行，之后每隔毫秒数就执行一次</li>
</ol>
<pre><code class="copyable">    <script>
        // 1. setInterval 
        setInterval(function() &#123;
            console.log('继续输出');
        &#125;, 1000);
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">3.2.2. 停止定时器</h3>
<pre><code class="copyable"> window.clearInterval(intervalID); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>clearInterval()方法取消了先前通过调用 setInterval()建立的定时器。</p>
<p>注意：</p>
<ol>
<li>window 可以省略。</li>
<li>里面的参数就是定时器的标识符 。</li>
</ol>
<h2 data-id="heading-18">3.3. this指向问题</h2>
<p>this的指向在函数定义的时候是确定不了的，只有函数执行的时候才能确定this到底指向谁，一般情况下this的最终指向的是那个调用它的对象</p>
<p>现阶段，我们先了解一下几个this指向</p>
<ol>
<li>全局作用域或者普通函数中this指向全局对象window（注意定时器里面的this指向window）</li>
<li>方法调用中谁调用this指向谁</li>
<li>构造函数中this指向构造函数的实例</li>
</ol>
<pre><code class="copyable">    <button>点击</button>
    <script>
        // this 指向问题 一般情况下this的最终指向的是那个调用它的对象
        // 1. 全局作用域或者普通函数中this指向全局对象window（ 注意定时器里面的this指向window）
        console.log(this);
        function fn() &#123;
            console.log(this);
        &#125;
        window.fn();
        window.setTimeout(function() &#123;
            console.log(this);
        &#125;, 1000);
        // 2. 方法调用中谁调用this指向谁
        var o = &#123;
            sayHi: function() &#123;
                console.log(this); // this指向的是 o 这个对象
            &#125;
        &#125;
        o.sayHi();
        var btn = document.querySelector('button');
        btn.addEventListener('click', function() &#123;
                console.log(this); // 事件处理函数中的this指向的是btn这个按钮对象
            &#125;)
        // 3. 构造函数中this指向构造函数的实例
        function Fun() &#123;
            console.log(this); // this 指向的是fun 实例对象
        &#125;
        var fun = new Fun();
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">4. JS 执行机制</h1>
<p>以下代码执行的结果是什么？</p>
<pre><code class="copyable"> console.log(1);
 
 setTimeout(function () &#123;
     console.log(3);
 &#125;, 1000);
 
 console.log(2);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">4.1. JS 是单线程</h2>
<p>JavaScript 语言的一大特点就是单线程，也就是说，同一个时间只能做一件事。这是因为 Javascript 这门脚本语言诞生的使命所致——JavaScript 是为处理页面中用户的交互，以及操作 DOM 而诞生的。比如我们对某个 DOM 元素进行添加和删除操作，不能同时进行。 应该先进行添加，之后再删除。</p>
<p>单线程就意味着，所有任务需要排队，前一个任务结束，才会执行后一个任务。如果前一个任务耗时很长，后一个任务就不得不一直等着。这样所导致的问题是： 如果 JS 执行的时间过长，这样就会造成页面的渲染不连贯，导致页面渲染加载阻塞的感觉。</p>
<h2 data-id="heading-21">4.2. 同步和异步</h2>
<p>为了解决这个问题，利用多核 CPU 的计算能力，HTML5 提出 Web Worker 标准，允许 JavaScript 脚本创建多个线程,但是子线程完全受主线程控制。于是，JS 中出现了同步和异步。</p>
<h3 data-id="heading-22">4.2.1. 同步</h3>
<p>前一个任务结束后再执行后一个任务，程序的执行顺序与任务的排列顺序是一致的、同步的。比如做饭的同步做法：我们要烧水煮饭，等水开了（10分钟之后），再去切菜，炒菜。</p>
<h3 data-id="heading-23">4.2.2. 异步</h3>
<p>你在做一件事情时，因为这件事情会花费很长时间，在做这件事的同时，你还可以去处理其他事情。比如做饭的异步做法，我们在烧水的同时，利用这10分钟，去切菜，炒菜。</p>
<p>他们的本质区别： 这条流水线上各个流程的执行顺序不同。</p>
<p>JS中所有任务可以分成两种，一种是同步任务（synchronous），另一种是异步任务（asynchronous）。</p>
<p>同步任务指的是：
在主线程上排队执行的任务，只有前一个任务执行完毕，才能执行后一个任务；</p>
<pre><code class="copyable">同步任务都在主线程上执行，形成一个执行栈。 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>异步任务指的是：
不进入主线程、而进入”任务队列”的任务，当主线程中的任务运行完了，才会从”任务队列”取出异步任务放入主线程执行。</p>
<pre><code class="copyable">JS 的异步是通过回调函数实现的。 
一般而言，异步任务有以下三种类型: 
1、普通事件，如 click、resize 等 
2、资源加载，如 load、error 等 
3、定时器，包括 setInterval、setTimeout 等 
异步任务相关回调函数添加到任务队列中（任务队列也称为消息队列）。 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ecf4d779dfd4b1c80e29189debf8752~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-24">4.3. JS执行机制（事件循环）</h2>
<ol>
<li>先执行执行栈中的同步任务。</li>
<li>异步任务（回调函数）放入任务队列中。</li>
<li>一旦执行栈中的所有同步任务执行完毕，系统就会按次序读取任务队列中的异步任务，于是被读取的异步任务结束等待状态，进入执行栈，开始执行。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81f189c34734400083ce58e984ff54b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1a6352f670e469eab438ad71f170a17~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于主线程不断的重复获得任务、执行任务、再获取任务、再执行，所以这种机制被称为事件循环（ event loop）。</p>
<h1 data-id="heading-25">5. location 对象</h1>
<h2 data-id="heading-26">5.1. 什么是 location 对象</h2>
<p>window 对象给我们提供了一个 location 属性用于获取或设置窗体的 URL，并且可以用于解析 URL 。 因为这个属性返回的是一个对象，所以我们将这个属性也称为 location 对象。</p>
<h2 data-id="heading-27">5.2. URL</h2>
<p>统一资源定位符 (Uniform Resource Locator, URL) 是互联网上标准资源的地址。互联网上的每个文件都有一个唯一的 URL，它包含的信息指出文件的位置以及浏览器应该怎么处理它。</p>
<p>URL 的一般语法格式为：</p>
<pre><code class="copyable"> protocol://host[:port]/path/[?query]#fragment  http://www.itcast.cn/index.html?name=andy&age=18#link
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/695a01872d6a43819a0124624855ae95~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-28">5.3. location 对象的属性</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/286275fd253443ab903090229c361576~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重点记住： href 和 search</p>
<h2 data-id="heading-29">5.4. location 对象的方法</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b7b434e66ac4c07a65f850c59d6ca6b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">    <button>点击</button>
    <script>
        var btn = document.querySelector('button');
        btn.addEventListener('click', function() &#123;
            // 记录浏览历史，所以可以实现后退功能
            // location.assign('http://www.itcast.cn');
            // 不记录浏览历史，所以不可以实现后退功能
            // location.replace('http://www.itcast.cn');
            location.reload(true);
        &#125;)
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-30">6. navigator 对象</h1>
<p>navigator 对象包含有关浏览器的信息，它有很多属性，我们最常用的是 userAgent，该属性可以返回由客户机发送服务器的 user-agent 头部的值。</p>
<p>下面前端代码可以判断用户那个终端打开页面，实现跳转</p>
<pre><code class="copyable">if((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))) &#123;
    window.location.href = "";     //手机
 &#125; else &#123;
    window.location.href = "";     //电脑
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-31">7. history 对象</h1>
<p>window 对象给我们提供了一个 history 对象，与浏览器历史记录进行交互。该对象包含用户（在浏览器窗口中）访问过的 URL。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1d9ad83be6e417297e7ff6e89a7b45f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>history 对象一般在实际开发中比较少用，但是会在一些 OA 办公系统中见到。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a68ba0eb30bd48ff9fdce94b7fe8ed97~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            