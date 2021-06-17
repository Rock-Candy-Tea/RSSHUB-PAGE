
---
title: 'chapter 7、JS----从入门到熟练的小白之路（持续更新....)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=209'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 02:48:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=209'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、时间对象 （Date）</h1>
<blockquote>
<p>作用：用来处理日期和时间</p>
</blockquote>
<h2 data-id="heading-1">如何创建时间对象</h2>
<p>new Date()</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> myDate = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(); <span class="hljs-comment">//Tue Jun 15 2021 19:20:33 GMT+0800 (中国标准时间);</span>
<span class="hljs-keyword">typeof</span> myDate;  <span class="hljs-comment">// "object" 获取到是一个对象，并不是字符串</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">时间对象相关属性和方法</h2>
<pre><code class="copyable">getFullYear（）；//获取年
getMonth（）；//获取月 0到11 代表1月到12月
getDate（）；//获取日期
getDay（）；//星期几 （0---6）代表周日到到周六
getHours（）；//时
getMinutes();//分
getSeconds()；//秒
getMilliseconds()；//毫秒
getTime();//获取当前日期到1970年1月1号 00：00:00 之间的毫秒差
toLocaleString();// 获取到的是年月日，时分秒"2019/12/25 上午10:15:50"
toLocaleDateString();//  获取到是字符串的年月日，例如："2019/12/25"
toLocaleTimeString();// 获取到的是字符串的时分秒上午10:18:28
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">二、时钟案例</h1>
<p>css:</p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <div class="clock" id="clock"></div>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>js:</p>
<pre><code class="hljs language-js copyable" lang="js">
<script>
    <span class="hljs-keyword">var</span> clock = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"clock"</span>);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTime</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> time = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
        <span class="hljs-keyword">var</span> year = time.getFullYear();
        <span class="hljs-keyword">var</span> month = time.getMonth() + <span class="hljs-number">1</span>;
        <span class="hljs-keyword">var</span> date = time.getDate();
        <span class="hljs-keyword">var</span> day = time.getDay();
        <span class="hljs-keyword">var</span> hour = time.getHours();
        <span class="hljs-keyword">var</span> minutes = time.getMinutes();
        <span class="hljs-keyword">var</span> seconds = time.getSeconds();
        <span class="hljs-keyword">var</span> week = [<span class="hljs-string">"周日"</span>, <span class="hljs-string">"周一"</span>, <span class="hljs-string">"周二"</span>, <span class="hljs-string">"周三"</span>, <span class="hljs-string">"周四"</span>, <span class="hljs-string">"周五"</span>, <span class="hljs-string">"周六"</span>];

        <span class="hljs-keyword">var</span> res = year + <span class="hljs-string">"年"</span> + addZero(month) + <span class="hljs-string">"月"</span> + addZero(date) + <span class="hljs-string">"日"</span> + week[day] + <span class="hljs-string">" "</span> + addZero(hour) + <span class="hljs-string">":"</span> + addZero(minutes) + <span class="hljs-string">":"</span> + addZero(seconds);
        <span class="hljs-keyword">return</span> res;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addZero</span>(<span class="hljs-params">num</span>) </span>&#123;
        <span class="hljs-keyword">return</span> num < <span class="hljs-number">10</span> ? <span class="hljs-string">"0"</span> + num : num;
    &#125;
    <span class="hljs-keyword">var</span> res = getTime();
    clock.innerText = res;
    <span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> res = getTime();
        clock.innerText = res;
    &#125;, <span class="hljs-number">1000</span>)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">三、定时器</h1>
<p>定时器参数说明：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 定时器可以传递多个参数：</span>
    <span class="hljs-comment">// 1、执行的函数    2、时间     3、后面的参数就是执行函数在执行的时候传递的实参</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">num,s,m</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(num,s,m);
    &#125;,<span class="hljs-number">1000</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">6</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">1、setTimeout</h2>
<p>含义：在一定的时间后，去执行某些事情，是单词调用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    alert(<span class="hljs-string">"我是定时器"</span>);
&#125;,<span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">2、setInterval</h2>
<p>间隔多少时间去做一件事，是多次调用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我还是定时器"</span>)
&#125;,<span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>定时器室友返回值的：返回值代表定时器在当前页面的第几个</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> time1=<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是定时器1"</span>);
&#125;,<span class="hljs-number">1000</span>)

<span class="hljs-keyword">var</span> time2=<span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是定时器2"</span>)
&#125;,<span class="hljs-number">1000</span>)

<span class="hljs-keyword">var</span> time3=<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是定时器3"</span>);
&#125;,<span class="hljs-number">1000</span>)

<span class="hljs-built_in">console</span>.log(time1)=====><span class="hljs-number">1</span>
<span class="hljs-built_in">console</span>.log(time1)=====><span class="hljs-number">2</span>
<span class="hljs-built_in">console</span>.log(time1)=====><span class="hljs-number">3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>定时器是异步任务，只有当同步代码执行完毕之后，才能执行。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> time1=<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"吃饭"</span>);
&#125;,<span class="hljs-number">1000</span>)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"睡觉"</span>)
&#125;
fn();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3、清除定时器的方法</h2>
<ul>
<li>clearTimeout</li>
<li>clearInterval</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">

 <span class="hljs-keyword">var</span> time1=<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>)
 &#125;,<span class="hljs-number">1000</span>)

<span class="hljs-built_in">clearTimeout</span>(time1);


<span class="hljs-keyword">var</span> time2=<span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"in"</span>)
&#125;,<span class="hljs-number">1000</span>);

<span class="hljs-built_in">clearInterval</span>(time2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>需求：</strong></p>
<pre><code class="copyable">做一个抽奖程序，页面中有一个区域显示中奖人员的编号，
在JS中写一段代码，要求每隔1秒中随机创建一个四位的数字
（每一位数字的取值范围0-9），
当10秒结束后，最后显示的四位数字即是中奖的号码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css:</p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>中奖</title>
    <style>
    #prize&#123;
        width:200px;
        height:50px;
        border:1px solid green;
    &#125;
    </style>
</head>
<body>
    <div class="prize" id="prize"></div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><script>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCode</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> str=<span class="hljs-string">"0123456789"</span>;
        <span class="hljs-keyword">var</span> result=<span class="hljs-string">""</span>;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-number">4</span>;i++)&#123;
            <span class="hljs-keyword">var</span> index=<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">9</span>);
            result+=str[index];
        &#125;
        <span class="hljs-keyword">return</span> result;
    &#125;
    <span class="hljs-keyword">var</span> prize=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"prize"</span>);
    prize.innerHTML=getCode();
    <span class="hljs-keyword">var</span> time=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();
    <span class="hljs-keyword">var</span> time1=<span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> newTime=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();
        <span class="hljs-keyword">var</span> dif=(newTime-time)/<span class="hljs-number">1000</span>;
        <span class="hljs-keyword">if</span>(dif><span class="hljs-number">5</span>)&#123;
            <span class="hljs-built_in">clearInterval</span>(time1);
        &#125;
       <span class="hljs-keyword">var</span> res= getCode();
       prize.innerHTML=res;
    &#125;,<span class="hljs-number">1000</span>) 
</script>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            