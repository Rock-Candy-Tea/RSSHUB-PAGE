
---
title: '微信小程序 wxs日期时间处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=464'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 23:17:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=464'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、时间戳转日期</h2>
<p>在wxs中处理日期需要使用getDate(time),而不能使用new Date()来处理日期</p>
<p><strong><code>在wxs文件中</code></strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> filter = &#123;
    <span class="hljs-attr">formatNumber</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n</span>) </span>&#123;
        n = n.toString()
        <span class="hljs-keyword">return</span> n[<span class="hljs-number">1</span>] ? n : <span class="hljs-string">'0'</span> + n
      &#125;,
    <span class="hljs-attr">parseTime</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">time, type</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (time == <span class="hljs-literal">null</span> || type == <span class="hljs-string">''</span>) &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
        &#125;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">0</span>) &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
        &#125;
        <span class="hljs-keyword">var</span> date = getDate(time);<span class="hljs-comment">//在wxs中不能使用new Date()来处理日期</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"date"</span>, date);
        <span class="hljs-keyword">var</span> y = date.getFullYear();
        <span class="hljs-keyword">var</span> m = filter.formatNumber(date.getMonth() + <span class="hljs-number">1</span>);
        <span class="hljs-keyword">var</span> d = filter.formatNumber(date.getDate());
        <span class="hljs-keyword">var</span> h = filter.formatNumber(date.getHours());
        <span class="hljs-keyword">var</span> i = filter.formatNumber(date.getMinutes());
        <span class="hljs-keyword">var</span> s = filter.formatNumber(date.getSeconds());
        <span class="hljs-keyword">var</span> a = filter.formatNumber(date.getDay());
        <span class="hljs-keyword">var</span> time_str = <span class="hljs-string">""</span>;
        <span class="hljs-keyword">if</span> (type == <span class="hljs-string">'month'</span>) &#123;
          time_str = y + <span class="hljs-string">'-'</span> + m;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (type == <span class="hljs-string">'date'</span>) &#123;
          time_str = y + <span class="hljs-string">'-'</span> + m + <span class="hljs-string">'-'</span> + d;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (type == <span class="hljs-string">'datetime'</span>) &#123;
          time_str = y + <span class="hljs-string">'-'</span> + m + <span class="hljs-string">'-'</span> + d + <span class="hljs-string">' '</span> + h + <span class="hljs-string">':'</span> + i + <span class="hljs-string">':'</span> + s;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (type == <span class="hljs-string">'onlyMonth'</span>) &#123;
          time_str = m;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (type == <span class="hljs-string">'onlyYear'</span>) &#123;
          time_str = y;
        &#125;
        <span class="hljs-keyword">return</span> time_str
      &#125;,
 &#125;
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">parseTime</span>: filter.parseTime,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>在wxml中使用</code></strong></p>
<pre><code class="hljs language-js copyable" lang="js"><wxs <span class="hljs-built_in">module</span>=<span class="hljs-string">"filters"</span> src=<span class="hljs-string">"../../../filters/filter.wxs"</span>></wxs>

 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">text</span>></span>&#123;&#123;filters.parseTime(time,'date')&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">text</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2、UTC转北京时间</h2>
<p>UTC时间比北京时间晚8小时，在苹果手机上需要去除"Z"后再处理时间</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> filter = &#123;
    <span class="hljs-attr">formatNumber</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n</span>) </span>&#123;
        n = n.toString()
        <span class="hljs-keyword">return</span> n[<span class="hljs-number">1</span>] ? n : <span class="hljs-string">'0'</span> + n
      &#125;,
    <span class="hljs-attr">parseTime</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">time, type</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (time == <span class="hljs-literal">null</span> || time == <span class="hljs-string">''</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-keyword">var</span> date;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> time === <span class="hljs-string">'object'</span>) &#123;
      date = time
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">if</span> ((<span class="hljs-string">''</span> + time).length === <span class="hljs-number">10</span>) &#123;
        time = <span class="hljs-built_in">parseInt</span>(time) * <span class="hljs-number">1000</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        time = time.replace(<span class="hljs-string">"Z"</span>, <span class="hljs-string">" "</span>).replace(getRegExp(<span class="hljs-string">'-'</span>, <span class="hljs-string">'g'</span>), <span class="hljs-string">"/"</span>)<span class="hljs-comment">//去除Z，兼容苹果手机</span>
        <span class="hljs-keyword">var</span> ts = time.split(<span class="hljs-string">'T'</span>)
        <span class="hljs-keyword">var</span> t1 = ts[<span class="hljs-number">0</span>]
        <span class="hljs-keyword">var</span> t2 = ts[<span class="hljs-number">1</span>].split(<span class="hljs-string">'.'</span>)[<span class="hljs-number">0</span>]
        time = t1 + <span class="hljs-string">" "</span> + t2
        time = getDate(time).getTime() + <span class="hljs-number">8</span> * <span class="hljs-number">3600000</span>;<span class="hljs-comment">//utc时间与北京时间相差8小时</span>
      &#125;
      date = getDate(time)<span class="hljs-comment">//不能使用new Date()</span>
    &#125;
    <span class="hljs-keyword">var</span> y = date.getFullYear();
    <span class="hljs-keyword">var</span> m = filter.formatNumber(date.getMonth() + <span class="hljs-number">1</span>);
    <span class="hljs-keyword">var</span> d = filter.formatNumber(date.getDate());
    <span class="hljs-keyword">var</span> h = filter.formatNumber(date.getHours());
    <span class="hljs-keyword">var</span> i = filter.formatNumber(date.getMinutes());
    <span class="hljs-keyword">var</span> s = filter.formatNumber(date.getSeconds());
    <span class="hljs-keyword">var</span> a = filter.formatNumber(date.getDay());
    <span class="hljs-keyword">var</span> time_str = <span class="hljs-string">""</span>;
    <span class="hljs-keyword">if</span> (type == <span class="hljs-string">'month'</span>) &#123;
      time_str = y + <span class="hljs-string">'-'</span> + m;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (type == <span class="hljs-string">'date'</span>) &#123;
      time_str = y + <span class="hljs-string">'-'</span> + m + <span class="hljs-string">'-'</span> + d;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (type == <span class="hljs-string">'datetime'</span>) &#123;
      time_str = y + <span class="hljs-string">'-'</span> + m + <span class="hljs-string">'-'</span> + d + <span class="hljs-string">' '</span> + h + <span class="hljs-string">':'</span> + i + <span class="hljs-string">':'</span> + s;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (type == <span class="hljs-string">'onlyMonth'</span>) &#123;
      time_str = m;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (type == <span class="hljs-string">'onlyYear'</span>) &#123;
      time_str = y;
    &#125;
    <span class="hljs-keyword">return</span> time_str
  &#125;,
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">parseTime</span>: filter.parseTime,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            