
---
title: 'js 防抖和节流'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2159'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 05:46:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=2159'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概念</h2>
<p>函数防抖(debounce)： 触发高频事件后n秒内函数只会执行一次，如果n秒内高频事件再次被触发，则重新计算时间。</p>
<p>函数节流(throttle)： 高频事件触发，但在n秒内只会执行一次，所以节流会稀释函数的执行频率。</p>
<p>函数节流（throttle）与 函数防抖（debounce）都是为了限制函数的执行频次，以优化函数触发频率过高导致的响应速度跟不上触发频率，出现延迟，假死或卡顿的现象。</p>
<p>比如如下的情况：</p>
<p>window对象的resize、scroll事件
拖拽时的mousemove事件
文字输入、自动完成的keyup事件</p>
<h2 data-id="heading-1">函数防抖(debounce)</h2>
<p>实现方式：每次触发事件时设置一个延迟调用方法，并且取消之前的延时调用方法
缺点：如果事件在规定的时间间隔内被不断的触发，则调用方法会被不断的延迟</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//防抖debounce代码：</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn,delay</span>) </span>&#123;
    <span class="hljs-keyword">var</span> timer = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 创建一个标记用来存放定时器的返回值</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-comment">// 每当用户输入的时候把前一个 setTimeout clear 掉</span>
        <span class="hljs-built_in">clearTimeout</span>(timer); 
        <span class="hljs-comment">// 然后又创建一个新的 setTimeout, 这样就能保证interval 间隔内如果时间持续触发，就不会执行 fn 函数</span>
        timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
        &#125;, delay);
    &#125;;
&#125;
<span class="hljs-comment">// 处理函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handle</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'防抖：'</span>, <span class="hljs-built_in">Math</span>.random());
&#125;
        
<span class="hljs-comment">//滚动事件</span>
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'scroll'</span>, debounce(handle,<span class="hljs-number">500</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">函数节流(throttle)</h2>
<p>实现方式：每次触发事件时，如果当前有等待执行的延时函数，则直接return</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//节流throttle代码：</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">fn,delay</span>) </span>&#123;
    <span class="hljs-keyword">let</span> canRun = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 通过闭包保存一个标记</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
         <span class="hljs-comment">// 在函数开头判断标记是否为true，不为true则return</span>
        <span class="hljs-keyword">if</span> (!canRun) <span class="hljs-keyword">return</span>;
         <span class="hljs-comment">// 立即设置为false</span>
        canRun = <span class="hljs-literal">false</span>;
        <span class="hljs-comment">// 将外部传入的函数的执行放在setTimeout中</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123; 
        <span class="hljs-comment">// 最后在setTimeout执行完毕后再把标记设置为true(关键)表示可以执行下一次循环了。</span>
        <span class="hljs-comment">// 当定时器没有执行的时候标记永远是false，在开头被return掉</span>
            fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
            canRun = <span class="hljs-literal">true</span>;
        &#125;, delay);
    &#125;;
&#125;
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'节流：'</span>, e.target.innerWidth, e.target.innerHeight);
&#125;
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'resize'</span>, throttle(sayHi,<span class="hljs-number">500</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">区别</h2>
<p>可以拿我们平时坐电梯为例来形象地表述二者的区别
函数防抖： 如果有人进电梯（触发事件），那电梯将在10秒钟后出发（执行事件监听器），这时如果又有人进电梯了（在10秒内再次触发该事件），我们又得等10秒再出发（重新计时）。
函数节流 ： 保证如果电梯第一个人进来后，10秒后准时运送一次，这个时间从第一个人上电梯开始计时，不等待，如果没有人，则不运行。</p>
<p>函数节流不管事件触发有多频繁，都会保证在规定时间内一定会执行一次真正的事件处理函数，而函数防抖只是在最后一次事件后才触发一次函数。 比如在页面的无限加载场景下，我们需要用户在滚动页面时，每隔一段时间发一次 Ajax 请求，而不是在用户停下滚动页面操作时才去请求数据。这样的场景，就适合用节流技术来实现。</p>
<p>函数防抖： 将多次操作合并为一次操作进行。原理是维护一个计时器，规定在delay时间后触发函数，但是在delay时间内再次触发的话，就会取消之前的计时器而重新设置。这样一来，只有最后一次操作能被触发。</p>
<p>函数节流：使得一定时间内只触发一次函数。原理是通过判断是否有延迟调用函数未执行。</p></div>  
</div>
            