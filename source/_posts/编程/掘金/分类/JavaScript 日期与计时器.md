
---
title: 'JavaScript 日期与计时器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4977'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 02:31:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=4977'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Date</h2>
<ol>
<li>
<p>Date 是一个构造函数，其原型上定义了一些日期方法</p>
</li>
<li>
<p>Date()</p>
<p>执行 Date()，返回表示日期的字符串</p>
</li>
<li>
<p>new Date()</p>
<p>没有参数，返回当前日期实例对象</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(date)); <span class="hljs-comment">// [Object Date]</span>
date.getFullYear() <span class="hljs-comment">// 返回年份，如 2020</span>
dae.getMonth() <span class="hljs-comment">// 返回月份减一，加一得到月份</span>
date.getDate() <span class="hljs-comment">// 返回几号，1 到 31</span>
date.getDay() <span class="hljs-comment">// 返回周几，0 到 7，周日开始</span>
date.getHours() <span class="hljs-comment">// 返回小时</span>
date.getMinutes() <span class="hljs-comment">// 返回分钟</span>
date.getSeconds() <span class="hljs-comment">// 返回秒数</span>
date.getMilliseconds() <span class="hljs-comment">// 返回毫秒数</span>
<span class="hljs-comment">// 有 get 同样有 set 方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有参数，返回对应的日期</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-number">2020</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">8</span>, <span class="hljs-number">30</span>, <span class="hljs-number">10</span>);
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">'2020/1/1 8:30:10'</span>);
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">'2020/01/01 08:30:10'</span>);
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">'2020-1-1 8:30:10'</span>);
<span class="hljs-comment">// Sat Feb 01 2020 8:30:10 GMT+0800 (中国标准时间)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>getTime()</p>
<p>返回时间戳，即毫秒数</p>
<p>计算机纪元时间 1970 年 1 月 1 日 0 点 0 分 0 秒</p>
<p>时间戳：某个时间距离计算机纪元时间的经过的毫秒数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> dateTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime(); <span class="hljs-comment">// 返回当前时间的时间戳</span>
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(dateTime); <span class="hljs-comment">// 返回时间戳对应时间</span>
date.setTime(dateTime); <span class="hljs-comment">// 以时间戳为标准设置时间</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-1">计时器</h2>
<ol>
<li>
<p>setInterval</p>
<p>每隔特定的毫秒数执行一次内部函数，从当前开始计时</p>
<p>返回一个数字，是计时器的唯一标识，代表在所有计时器和延时器中的序号</p>
<p>是 window 下的方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    
&#125;, <span class="hljs-number">1000</span>) <span class="hljs-comment">// 匿名函数</span>
funtion <span class="hljs-function"><span class="hljs-title">Test</span>(<span class="hljs-params"></span>)</span> &#123;
    
&#125;
<span class="hljs-built_in">setInterval</span>(test, <span class="hljs-number">1000</span>);
<span class="hljs-built_in">setInterval</span>(<span class="hljs-string">'test()'</span>, <span class="hljs-number">1000</span>); <span class="hljs-comment">// 字符串形式传入方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>clearInterval</p>
<p>清除计时器</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;, <span class="hljs-number">1000</span>); <span class="hljs-comment">// timer 是唯一标识，代表在所有计时器中的序号</span>
<span class="hljs-built_in">clearInterval</span>(timer);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-2">延时器</h2>
<ol>
<li>
<p>setTimout</p>
<p>延迟指定时间执行一次内部函数</p>
<p>返回一个数字，是延时器的唯一标识，代表在所有计时器中和延时器的序号</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    
&#125;, <span class="hljs-number">1000</span>) <span class="hljs-comment">// 匿名函数</span>
funtion <span class="hljs-function"><span class="hljs-title">Test</span>(<span class="hljs-params"></span>)</span> &#123;
    
&#125;
<span class="hljs-built_in">setTimeout</span>(test, <span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>clearTimeout</p>
<p>清除延时器</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;, <span class="hljs-number">1000</span>); <span class="hljs-comment">// timer 是唯一标识，代表在所有计时器中的序号</span>
<span class="hljs-built_in">clearTimeout</span>(timer);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-3">定时任务</h2>
<ol>
<li>
<p>功能</p>
<p>等待条件满足时执行任务，设定时间内条件未满足则执行回调函数</p>
</li>
<li>
<p>参数</p>
<ul>
<li>re: 判断条件函数，return 要执行 fn 的条件</li>
<li>fn: 等待执行的目标函数</li>
<li>space: setInterVal 的间隔时间，space || 100</li>
<li>wait: setTimeOut 的等待时间，wait || 3000</li>
<li>back: fn 未成功执行时回调函数</li>
</ul>
</li>
<li>
<p>代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timer</span>(<span class="hljs-params">re, fn, space, wait, back</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (re()) &#123;
        fn();
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">var</span> interval = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">if</span> (re()) &#123;
                fn();
                <span class="hljs-built_in">clearInterval</span>(interval);
                interval = <span class="hljs-literal">null</span>;
            &#125;
        &#125;, space || <span class="hljs-number">100</span>);
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">if</span> (interval) &#123;
                <span class="hljs-built_in">clearInterval</span>(interval);
                interval = <span class="hljs-literal">null</span>;
                back && back();
            &#125;
        &#125;, wait || <span class="hljs-number">3000</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol></div>  
</div>
            