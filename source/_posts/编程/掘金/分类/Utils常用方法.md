
---
title: 'Utils常用方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8014'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 17:47:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=8014'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>从前的车马邮件都很慢 人这辈子只用打一份工 现在信息技术高速发展的年代 我们打工人怎么能慢下来 让我们众志成城 埋头苦干 午安 打工人</p>
<h3 data-id="heading-0">格式化时间</h3>
<ul>
<li><strong>1970-01-01 08:00:00</strong> <strong>自定义格式</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@description </span>格式化时间
 * <span class="hljs-doctag">@param <span class="hljs-variable">time</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-variable">cFormat</span></span>
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;string|null&#125;</span></span>---2008-07-22 22:49:41
 */</span>
 
 <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parseTime</span>(<span class="hljs-params">time, cFormat</span>) </span>&#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">0</span>) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
&#125;
<span class="hljs-keyword">const</span> format = cFormat || <span class="hljs-string">'&#123;y&#125;-&#123;m&#125;-&#123;d&#125; &#123;h&#125;:&#123;i&#125;:&#123;s&#125;'</span>
<span class="hljs-keyword">let</span> date
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> time === <span class="hljs-string">'object'</span>) &#123;
date = time
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> time === <span class="hljs-string">'string'</span> && <span class="hljs-regexp">/^[0-9]+$/</span>.test(time)) &#123;
time = <span class="hljs-built_in">parseInt</span>(time)
&#125;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> time === <span class="hljs-string">'number'</span> && time.toString().length === <span class="hljs-number">10</span>) &#123;
time = time * <span class="hljs-number">1000</span>
&#125;
date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(time)
&#125;
<span class="hljs-keyword">const</span> formatObj = &#123;
<span class="hljs-attr">y</span>: date.getFullYear(),
<span class="hljs-attr">m</span>: date.getMonth() + <span class="hljs-number">1</span>,
<span class="hljs-attr">d</span>: date.getDate(),
<span class="hljs-attr">h</span>: date.getHours(),
<span class="hljs-attr">i</span>: date.getMinutes(),
<span class="hljs-attr">s</span>: date.getSeconds(),
<span class="hljs-attr">a</span>: date.getDay(),
&#125;
<span class="hljs-keyword">const</span> time_str = format.replace(<span class="hljs-regexp">/&#123;(y|m|d|h|i|s|a)+&#125;/g</span>, <span class="hljs-function">(<span class="hljs-params">result, key</span>) =></span> &#123;
<span class="hljs-keyword">let</span> value = formatObj[key]
<span class="hljs-keyword">if</span> (key === <span class="hljs-string">'a'</span>) &#123;
<span class="hljs-keyword">return</span> [<span class="hljs-string">'日'</span>, <span class="hljs-string">'一'</span>, <span class="hljs-string">'二'</span>, <span class="hljs-string">'三'</span>, <span class="hljs-string">'四'</span>, <span class="hljs-string">'五'</span>, <span class="hljs-string">'六'</span>][value]
&#125;
<span class="hljs-keyword">if</span> (result.length > <span class="hljs-number">0</span> && value < <span class="hljs-number">10</span>) &#123;
value = <span class="hljs-string">'0'</span> + value
&#125;
<span class="hljs-keyword">return</span> value || <span class="hljs-number">0</span>
&#125;)
<span class="hljs-keyword">return</span> time_str
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>刚刚 几分钟前 几小时前</strong> <strong>1月1日8时0分</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">formatTime</span>(<span class="hljs-params">time, option</span>) </span>&#123;
<span class="hljs-keyword">if</span> ((<span class="hljs-string">''</span> + time).length === <span class="hljs-number">10</span>) &#123;
time = <span class="hljs-built_in">parseInt</span>(time) * <span class="hljs-number">1000</span>
&#125; <span class="hljs-keyword">else</span> &#123;
time = +time
&#125;
<span class="hljs-keyword">const</span> d = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(time)
<span class="hljs-keyword">const</span> now = <span class="hljs-built_in">Date</span>.now()

<span class="hljs-keyword">const</span> diff = (now - d) / <span class="hljs-number">1000</span>

<span class="hljs-keyword">if</span> (diff < <span class="hljs-number">30</span>) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-string">'刚刚'</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (diff < <span class="hljs-number">3600</span>) &#123;
<span class="hljs-comment">// less 1 hour</span>
<span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.ceil(diff / <span class="hljs-number">60</span>) + <span class="hljs-string">'分钟前'</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (diff < <span class="hljs-number">3600</span> * <span class="hljs-number">24</span>) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.ceil(diff / <span class="hljs-number">3600</span>) + <span class="hljs-string">'小时前'</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (diff < <span class="hljs-number">3600</span> * <span class="hljs-number">24</span> * <span class="hljs-number">2</span>) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-string">'1天前'</span>
&#125;
<span class="hljs-keyword">if</span> (option) &#123;
<span class="hljs-keyword">return</span> parseTime(time, option)
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">return</span> (
d.getMonth() +
<span class="hljs-number">1</span> +
<span class="hljs-string">'月'</span> +
d.getDate() +
<span class="hljs-string">'日'</span> +
d.getHours() +
<span class="hljs-string">'时'</span> +
d.getMinutes() +
<span class="hljs-string">'分'</span>
)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>10位时间戳转换</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tenBitTimestamp</span>(<span class="hljs-params">time</span>) </span>&#123;
<span class="hljs-keyword">const</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(time * <span class="hljs-number">1000</span>)
<span class="hljs-keyword">const</span> y = date.getFullYear()
<span class="hljs-keyword">let</span> m = date.getMonth() + <span class="hljs-number">1</span>
m = m < <span class="hljs-number">10</span> ? <span class="hljs-string">''</span> + m : m
<span class="hljs-keyword">let</span> d = date.getDate()
d = d < <span class="hljs-number">10</span> ? <span class="hljs-string">''</span> + d : d
<span class="hljs-keyword">let</span> h = date.getHours()
h = h < <span class="hljs-number">10</span> ? <span class="hljs-string">'0'</span> + h : h
<span class="hljs-keyword">let</span> minute = date.getMinutes()
<span class="hljs-keyword">let</span> second = date.getSeconds()
minute = minute < <span class="hljs-number">10</span> ? <span class="hljs-string">'0'</span> + minute : minute
second = second < <span class="hljs-number">10</span> ? <span class="hljs-string">'0'</span> + second : second
<span class="hljs-keyword">return</span> y + <span class="hljs-string">'年'</span> + m + <span class="hljs-string">'月'</span> + d + <span class="hljs-string">'日 '</span> + h + <span class="hljs-string">':'</span> + minute + <span class="hljs-string">':'</span> + second
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>13位时间戳转换</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">thirteenBitTimestamp</span>(<span class="hljs-params">time</span>) </span>&#123;
<span class="hljs-keyword">const</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(time / <span class="hljs-number">1</span>)
<span class="hljs-keyword">const</span> y = date.getFullYear()
<span class="hljs-keyword">let</span> m = date.getMonth() + <span class="hljs-number">1</span>
m = m < <span class="hljs-number">10</span> ? <span class="hljs-string">''</span> + m : m
<span class="hljs-keyword">let</span> d = date.getDate()
d = d < <span class="hljs-number">10</span> ? <span class="hljs-string">''</span> + d : d
<span class="hljs-keyword">let</span> h = date.getHours()
h = h < <span class="hljs-number">10</span> ? <span class="hljs-string">'0'</span> + h : h
<span class="hljs-keyword">let</span> minute = date.getMinutes()
<span class="hljs-keyword">let</span> second = date.getSeconds()
minute = minute < <span class="hljs-number">10</span> ? <span class="hljs-string">'0'</span> + minute : minute
second = second < <span class="hljs-number">10</span> ? <span class="hljs-string">'0'</span> + second : second
<span class="hljs-keyword">return</span> y + <span class="hljs-string">'年'</span> + m + <span class="hljs-string">'月'</span> + d + <span class="hljs-string">'日 '</span> + h + <span class="hljs-string">':'</span> + minute + <span class="hljs-string">':'</span> + second
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            