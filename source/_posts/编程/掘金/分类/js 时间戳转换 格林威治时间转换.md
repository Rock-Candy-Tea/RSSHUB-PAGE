
---
title: 'js 时间戳转换 格林威治时间转换'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8588'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 02:21:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=8588'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>Moment.js很重(源码为4600行左右)，所以有很多替代方案的，如：Dayjs、miment等，所以可以根据浏览器的兼容情况自行写个轻量级的库。</p>
<p>1、 简单通过时间对象转换需要的时间格式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 时间戳 转时间</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">farmatDate</span>(<span class="hljs-params">time, zone = <span class="hljs-number">8</span>, fmt</span>) </span>&#123;
 <span class="hljs-keyword">const</span> getCurrentZoneTimestrap = getGLWZTime(time, zone);
 <span class="hljs-keyword">const</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(getCurrentZoneTimestrap);
 <span class="hljs-keyword">if</span>(<span class="hljs-regexp">/(y+)/</span>.test(fmt))
   fmt = fmt.replace(<span class="hljs-built_in">RegExp</span>.$1, <span class="hljs-string">`<span class="hljs-subst">$&#123;date.getFullYear()&#125;</span>`</span>);
 <span class="hljs-keyword">let</span> o = &#123;
  <span class="hljs-string">'M+'</span>: getMonth() + <span class="hljs-number">1</span>,
  <span class="hljs-string">'d+'</span>: getDay(),
  <span class="hljs-string">'h+'</span>: getHours(),
  <span class="hljs-string">'m+'</span>: getMinutes(),
  <span class="hljs-string">'s+'</span>: getSeconds()
 &#125;;
 <span class="hljs-keyword">let</span> str;
 <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> o) &#123;
  <span class="hljs-keyword">if</span>(<span class="hljs-built_in">RegExp</span>(<span class="hljs-string">`(<span class="hljs-subst">$&#123;key&#125;</span>)`</span>).test(fmt)) &#123;
     str = <span class="hljs-string">`<span class="hljs-subst">$&#123;o[key]&#125;</span>`</span>;
     fmt = fmt.replace(<span class="hljs-built_in">RegExp</span>.$1, str.length === <span class="hljs-number">2</span> ? str:addLeftZero(str))
  &#125;
 &#125;
 <span class="hljs-keyword">return</span> fmt;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addLeftZero</span>(<span class="hljs-params">str</span>) </span>&#123;
 <span class="hljs-keyword">return</span> <span class="hljs-string">`00<span class="hljs-subst">$&#123;str&#125;</span>`</span>.substr(str.length);
&#125;

<span class="hljs-comment">// 不同时区下 对时间戳的处理</span>
<span class="hljs-comment">// getTimezoneOffset() 方法可返回格林威治时间和本地时间之间的时差，以分钟为单位。</span>
<span class="hljs-comment">// param &#123; timestrap 需要转换的时间， zone转换的时区&#125;</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getGLWZTime = <span class="hljs-function">(<span class="hljs-params">timestrap:number, zone:number</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> hours = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTimezoneOffset() / <span class="hljs-number">60</span>; <span class="hljs-comment">// 计算格林威治时间和本地时间之间相差几个小时 如果是北京东八时区 返回 -8</span>
  <span class="hljs-keyword">const</span> millisecond = hours * <span class="hljs-number">3600000</span>; <span class="hljs-comment">// 毫秒为单位的时差</span>
  <span class="hljs-keyword">const</span> standardTime = timestrap + millisecond;<span class="hljs-comment">// 格林威治时间 = 传入时间戳 + 本地与格林威治时差</span>
  <span class="hljs-keyword">const</span> targetZone = standardTime + zone * <span class="hljs-number">3600000</span>; <span class="hljs-comment">// 目标zone时区时间戳 = 格林威治时间 + 目标时区与格林威治时差</span>
  <span class="hljs-keyword">return</span> targetZone;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            