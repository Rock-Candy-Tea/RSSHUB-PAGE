
---
title: 'JS中的节流与防抖函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/055c41ad34d148c4a33e4b0aff38b992~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 23:53:27 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/055c41ad34d148c4a33e4b0aff38b992~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">导读</h1>
<p>节流函数和防抖函数在日常的开发中还是有很多地方用到，两个函数的目的都是为了控制函数被调用的频率，今天我们就来说一说着两个函数。</p>
<h1 data-id="heading-1">例子</h1>
<p>input触发键盘输入事件，将输入内容发送到后台：</p>
<pre><code class="copyable">// 定义一个请求函数
function request(val) &#123;
    console.log("request: " + val);
&#125;

let inputEl = document.getElementById("input");

inputEl.addEventListener("keyup", function (e) &#123;
    request(e.target.value);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/055c41ad34d148c4a33e4b0aff38b992~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，我们每次按下键盘输入的时候，都会去请求，这样很浪费资源，一般应用中都是等待用户输入完整的字符，再去请求后台，所以我们用防抖函数来优化这一个。</p>
<h1 data-id="heading-2">防抖函数</h1>
<blockquote>
<p>事件被触发时，在n秒后执行函数，在n秒内多次触发事件，则重新开始计时</p>
</blockquote>
<p>利用定时器来实现，在n秒内多次触发，则先清除定时器，从新计时</p>
<pre><code class="copyable">// 定义一个请求函数
function request(val) &#123;
    console.log("request: " + val);
&#125;

// 定义一个防抖函数
function debounce(fn, delay) &#123;
    let timeout;
    return function()&#123;
      clearTimeout(timeout)
      timeout = setTimeout(()=>&#123;
        fn.apply(this, arguments)
      &#125;,delay)
    &#125;
&#125;

let inputEl = document.getElementById("input");

let debounceInput = debounce(request, 500)

inputEl.addEventListener("keyup", function (e) &#123;
    debounceInput(e.target.value);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38c346c3444843d8914cec083ab25c37~tplv-k3u1fbpfcp-watermark.image" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>只有当输入完成后才会触发函数，防止在不停是输入时调用函数，减少资源的浪费。</p>
<h1 data-id="heading-3">节流函数</h1>
<blockquote>
<p>在规定的单位时间段内，函数只能执行一次，在单位时间内多少触发，则只有一次有效</p>
</blockquote>
<h2 data-id="heading-4">定时器来实现</h2>
<p>当一个定时器执行，就会生成一个定时器id，当这个id存在就说明在单位时间内函数只执行了一次。</p>
<pre><code class="copyable">// 定义一个请求函数
function request(val) &#123;
    console.log("request: " + val);
&#125;

// 定义一个节流函数
function throttle(fn, delay) &#123;
    let timer;
    return function()&#123;
      if(!timer) &#123;
        fn.apply(this, arguments)
        timer = setTimeout(()=>&#123;
          clearTimeout(timer)
          timer = null
        &#125;,delay)
      &#125;
    &#125;
&#125;

let inputEl = document.getElementById("input");

let throttleInput = throttle(request, 500)

inputEl.addEventListener("keyup", function (e) &#123;
    throttleInput(e.target.value);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a708b4ba6b74ab58ed284a6f883a25d~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，当我们在输入框中不断输入，请求函数在我们规定的单位时间执行一次函数</p>
<h1 data-id="heading-5">总结</h1>
<ul>
<li>防抖函数和节流函数都是用于控制函数调用频率，但是两者实现原理不同</li>
<li>防抖函数是在触发事件的单位时间后执行一次函数，在单位时间内多次触发不执行函数，重新计时</li>
<li>节流函数是单位时间内只执行一次函数，多次触发也只有一次有效</li>
</ul>
<h1 data-id="heading-6">适用场景</h1>
<h2 data-id="heading-7">防抖</h2>
<ol>
<li>搜索输入框搜索内容，用户在不断的输入的时候，用防抖来节约请求资源</li>
<li>不断的触发window的resize事件，不断的改变窗口大小，利用防抖函数来只执行一次</li>
</ol>
<h2 data-id="heading-8">节流</h2>
<ol>
<li>鼠标不断的点击，用节流来限制只在规定的单位时间内执行一次函数</li>
<li>滚轮事件, 不断的往下滚轮，比如滚动到底部加载数据</li>
</ol></div>  
</div>
            