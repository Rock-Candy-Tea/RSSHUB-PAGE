
---
title: '【JS 逆向百例】百度翻译接口参数逆向'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e702b8aa29426f9e1b73a38ec1e335~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 23:48:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e702b8aa29426f9e1b73a38ec1e335~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e702b8aa29426f9e1b73a38ec1e335~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">逆向目标</h2>
<ul>
<li>目标：百度翻译接口参数</li>
<li>主页：<a href="https://link.juejin.cn/?target=https%3A%2F%2Ffanyi.youdao.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://fanyi.youdao.com/" ref="nofollow noopener noreferrer">fanyi.youdao.com/</a></li>
<li>接口：<a href="https://link.juejin.cn/?target=https%3A%2F%2Ffanyi.baidu.com%2Fv2transapi" target="_blank" rel="nofollow noopener noreferrer" title="https://fanyi.baidu.com/v2transapi" ref="nofollow noopener noreferrer">fanyi.baidu.com/v2transapi</a></li>
<li>逆向参数：
<ul>
<li>Form Data：
<ul>
<li><code>sign: 706553.926920</code></li>
<li><code>token: d838e2bd3d5a3bb67100a7b789463022</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-1">逆向过程</h2>
<h3 data-id="heading-2">抓包分析</h3>
<p>我们在百度翻译页面随便输入文字，可以看到没有刷新页面，翻译结果就出来了，由此可以推断是 Ajax 加载的，打开开发者工具，选择 XHR 过滤 Ajax 请求，可以看到有一条 URL 为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ffanyi.baidu.com%2Fv2transapi%3Ffrom%3Dzh%26to%3Den" target="_blank" rel="nofollow noopener noreferrer" title="https://fanyi.baidu.com/v2transapi?from=zh&to=en" ref="nofollow noopener noreferrer">fanyi.baidu.com/v2transapi?…</a> 的 POST 请求，当我们输入“测试”的时候，他返回的数据经过 Unicode 转中文后类似于如下结构：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
<span class="hljs-attr">"trans_result"</span>: &#123;
<span class="hljs-attr">"data"</span>: [&#123;
<span class="hljs-attr">"dst"</span>: <span class="hljs-string">"test"</span>,
<span class="hljs-attr">"prefixWrap"</span>: <span class="hljs-number">0</span>,
<span class="hljs-attr">"result"</span>: [
[<span class="hljs-number">0</span>, <span class="hljs-string">"test"</span>, [<span class="hljs-string">"0|6"</span>],
[],
[<span class="hljs-string">"0|6"</span>],
[<span class="hljs-string">"0|4"</span>]
]
],
<span class="hljs-attr">"src"</span>: <span class="hljs-string">"测试"</span>
&#125;],
<span class="hljs-attr">"from"</span>: <span class="hljs-string">"zh"</span>,
<span class="hljs-attr">"status"</span>: <span class="hljs-number">0</span>,
<span class="hljs-attr">"to"</span>: <span class="hljs-string">"en"</span>,
<span class="hljs-attr">"type"</span>: <span class="hljs-number">2</span>
&#125;,
<span class="hljs-attr">"dict_result"</span>: &#123;
        <span class="hljs-comment">// 略</span>
    &#125;,
<span class="hljs-attr">"liju_result"</span>: &#123;
        <span class="hljs-comment">// 略</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>trans_result</code> 是翻译的结果，<code>dict_result</code> 是更多翻译结果，<code>liju_result</code> 是例句、标签等，那么这个 URL 就是我们需要的翻译接口了。</p>
<p>由于是 POST 请求，我们观察它的 Form Data：</p>
<ul>
<li><code>from</code>：待翻译的语言；</li>
<li><code>to</code>：目标语言；</li>
<li><code>query</code>：待翻译的字符串；</li>
<li><code>transtype</code>：实时翻译 <code>realtime</code>，手动点击翻译 <code>translang</code>；</li>
<li><code>simple_means_flag</code>、<code>domain</code>：固定值；</li>
<li><code>sign</code>：如果待翻译字符串改变的话，它的值也会跟着变，需要进一步分析；</li>
<li><code>token</code>：它的值虽然不会变，但是不知道是怎么来的，需要进一步分析。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c0a9e1e90ed432986e59bf40828d0dd~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在抓包过程中我们还注意到有一条 URL 为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ffanyi.baidu.com%2Flangdetect" target="_blank" rel="nofollow noopener noreferrer" title="https://fanyi.baidu.com/langdetect" ref="nofollow noopener noreferrer">fanyi.baidu.com/langdetect</a> 的 POST 请求，而它返回的数据如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;<span class="hljs-attr">"error"</span>:<span class="hljs-number">0</span>,<span class="hljs-attr">"msg"</span>:<span class="hljs-string">"success"</span>,<span class="hljs-attr">"lan"</span>:<span class="hljs-string">"zh"</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显，这个是自动检测待翻译字符串的语言，它的 Form Data 也很简单，<code>query</code> 就是待翻译的字符串，这个接口可以根据实际场景进行使用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c25ff94f2194d1ea5fc8ed1448b9f24~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">获取 token</h3>
<p><code>token </code> 的值由于是固定的，所以我们可以尝直接搜索，可以在首页源码里面找到，使用正则表达式可以直接提取。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b394c63523d14d5291abb04152bedef2~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">获取 sign</h3>
<p><code>sign </code> 是会改变的，怀疑是 JS 动态生成，所以我们尝试全局搜索 <code>sign</code>，这里有个技巧，只搜索 <code>sign</code> 会出来很多结果，可以加上冒号或者等于号来缩小范围，搜索 <code>sign:</code> 可以在 index_a8b7098.js 里面找到 5 个符合的位置，观察可以发现在第 8392 行的位置处，数据最全面，和前面抓包看到的 Form Data 数据一致。</p>
<p>点击行号，在此处埋下断点，点击翻译按钮，可以看到成功断下，此时 <code>sign</code> 的值就是最终我们想要的的值：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f05529ffd8c64ecda32f52eaa65155f8~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里将待翻译字符串传入了 <code>L</code> 函数，鼠标放到 <code>L</code> 函数上，直接点击跟进这个函数，可以发现 <code>sign</code> 的值其实是 <code>function e(r)</code> 这个函数进行一系列操作之后得到的，直接复制这个函数进行本地调试，调试过程中可以发现缺少一个 <code>i</code> 的值，在右边的 Closure 栏里，或者鼠标选中 <code>i</code>，可以看到 <code>i</code> 的值，多次调试发现它是固定的，可以直接写死：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b9e8f746e174fb7bdb3aa422eb362ea~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>继续调试 <code>function e(r)</code>，还会提示缺少一个函数 <code>n</code>，那么直接跟进这个函数，将函数 <code>n</code> 一同复制下来即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c3c2fe285e042ad862b407d1cead0c8~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">完整代码</h2>
<h3 data-id="heading-6">baidu_encrypt.js</h3>
<p>获取 <code>sign</code> 的值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> i = <span class="hljs-string">'320305.131321201'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">n</span>(<span class="hljs-params">r, o</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> t = <span class="hljs-number">0</span>; t < o.length - <span class="hljs-number">2</span>; t += <span class="hljs-number">3</span>) &#123;
        <span class="hljs-keyword">var</span> a = o.charAt(t + <span class="hljs-number">2</span>);
        a = a >= <span class="hljs-string">"a"</span> ? a.charCodeAt(<span class="hljs-number">0</span>) - <span class="hljs-number">87</span> : <span class="hljs-built_in">Number</span>(a), a = <span class="hljs-string">"+"</span> === o.charAt(t + <span class="hljs-number">1</span>) ? r >>> a : r << a, r = <span class="hljs-string">"+"</span> === o.charAt(t) ? r + a & <span class="hljs-number">4294967295</span> : r ^ a
    &#125;
    <span class="hljs-keyword">return</span> r
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">e</span>(<span class="hljs-params">r</span>) </span>&#123;
    <span class="hljs-keyword">var</span> o = r.match(<span class="hljs-regexp">/[\uD800-\uDBFF][\uDC00-\uDFFF]/g</span>);
    <span class="hljs-keyword">if</span> (<span class="hljs-literal">null</span> === o) &#123;
        <span class="hljs-keyword">var</span> t = r.length;
        t > <span class="hljs-number">30</span> && (r = <span class="hljs-string">""</span> + r.substr(<span class="hljs-number">0</span>, <span class="hljs-number">10</span>) + r.substr(<span class="hljs-built_in">Math</span>.floor(t / <span class="hljs-number">2</span>) - <span class="hljs-number">5</span>, <span class="hljs-number">10</span>) + r.substr(-<span class="hljs-number">10</span>, <span class="hljs-number">10</span>))
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> e = r.split(<span class="hljs-regexp">/[\uD800-\uDBFF][\uDC00-\uDFFF]/</span>), C = <span class="hljs-number">0</span>, h = e.length, f = []; h > C; C++) <span class="hljs-string">""</span> !== e[C] && f.push.apply(f, a(e[C].split(<span class="hljs-string">""</span>))), C !== h - <span class="hljs-number">1</span> && f.push(o[C]);
        <span class="hljs-keyword">var</span> g = f.length;
        g > <span class="hljs-number">30</span> && (r = f.slice(<span class="hljs-number">0</span>, <span class="hljs-number">10</span>).join(<span class="hljs-string">""</span>) + f.slice(<span class="hljs-built_in">Math</span>.floor(g / <span class="hljs-number">2</span>) - <span class="hljs-number">5</span>, <span class="hljs-built_in">Math</span>.floor(g / <span class="hljs-number">2</span>) + <span class="hljs-number">5</span>).join(<span class="hljs-string">""</span>) + f.slice(-<span class="hljs-number">10</span>).join(<span class="hljs-string">""</span>))
    &#125;
    <span class="hljs-keyword">var</span> u = <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>, l = <span class="hljs-string">""</span> + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">103</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">116</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">107</span>);
    u = <span class="hljs-literal">null</span> !== i ? i : (i = <span class="hljs-built_in">window</span>[l] || <span class="hljs-string">""</span>) || <span class="hljs-string">""</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> d = u.split(<span class="hljs-string">"."</span>), m = <span class="hljs-built_in">Number</span>(d[<span class="hljs-number">0</span>]) || <span class="hljs-number">0</span>, s = <span class="hljs-built_in">Number</span>(d[<span class="hljs-number">1</span>]) || <span class="hljs-number">0</span>, S = [], c = <span class="hljs-number">0</span>, v = <span class="hljs-number">0</span>; v < r.length; v++) &#123;
        <span class="hljs-keyword">var</span> A = r.charCodeAt(v);
        <span class="hljs-number">128</span> > A ? S[c++] = A : (<span class="hljs-number">2048</span> > A ? S[c++] = A >> <span class="hljs-number">6</span> | <span class="hljs-number">192</span> : (<span class="hljs-number">55296</span> === (<span class="hljs-number">64512</span> & A) && v + <span class="hljs-number">1</span> < r.length && <span class="hljs-number">56320</span> === (<span class="hljs-number">64512</span> & r.charCodeAt(v + <span class="hljs-number">1</span>)) ? (A = <span class="hljs-number">65536</span> + ((<span class="hljs-number">1023</span> & A) << <span class="hljs-number">10</span>) + (<span class="hljs-number">1023</span> & r.charCodeAt(++v)), S[c++] = A >> <span class="hljs-number">18</span> | <span class="hljs-number">240</span>, S[c++] = A >> <span class="hljs-number">12</span> & <span class="hljs-number">63</span> | <span class="hljs-number">128</span>) : S[c++] = A >> <span class="hljs-number">12</span> | <span class="hljs-number">224</span>, S[c++] = A >> <span class="hljs-number">6</span> & <span class="hljs-number">63</span> | <span class="hljs-number">128</span>), S[c++] = <span class="hljs-number">63</span> & A | <span class="hljs-number">128</span>)
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> p = m, F = <span class="hljs-string">""</span> + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">43</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">45</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">97</span>) + (<span class="hljs-string">""</span> + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">94</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">43</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">54</span>)), D = <span class="hljs-string">""</span> + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">43</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">45</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">51</span>) + (<span class="hljs-string">""</span> + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">94</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">43</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">98</span>)) + (<span class="hljs-string">""</span> + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">43</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">45</span>) + <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">102</span>)), b = <span class="hljs-number">0</span>; b < S.length; b++) p += S[b], p = n(p, F);
    <span class="hljs-keyword">return</span> p = n(p, D), p ^= s, <span class="hljs-number">0</span> > p && (p = (<span class="hljs-number">2147483647</span> & p) + <span class="hljs-number">2147483648</span>), p %= <span class="hljs-number">1e6</span>, p.toString() + <span class="hljs-string">"."</span> + (p ^ m)
&#125;

<span class="hljs-comment">// console.log(e('测试'))</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">baidufanyi.py</h3>
<pre><code class="hljs language-python copyable" lang="python"><span class="hljs-comment">#!/usr/bin/env python3</span>
<span class="hljs-comment"># -*- coding: utf-8 -*-</span>


<span class="hljs-keyword">import</span> re

<span class="hljs-keyword">import</span> execjs
<span class="hljs-keyword">import</span> requests


index_url = <span class="hljs-string">'https://fanyi.baidu.com/'</span>
lang_url = <span class="hljs-string">'https://fanyi.baidu.com/langdetect'</span>
translate_api = <span class="hljs-string">'https://fanyi.baidu.com/v2transapi'</span>
headers = &#123;
    <span class="hljs-string">'Accept'</span>: <span class="hljs-string">'*/*'</span>,
    <span class="hljs-string">'Accept-Encoding'</span>: <span class="hljs-string">'gzip, deflate, br'</span>,
    <span class="hljs-string">'Accept-Language'</span>: <span class="hljs-string">'zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7'</span>,
    <span class="hljs-string">'Connection'</span>: <span class="hljs-string">'keep-alive'</span>,
    <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/x-www-form-urlencoded; charset=UTF-8'</span>,
    <span class="hljs-string">'Cookie'</span>: <span class="hljs-string">'BIDUPSID=3BE16D933E9C0182F2A6E93D7A9D1424; PSTM=1623723330; BAIDUID=8496908995397662040287D2CE1C4224:FG=1; __yjs_duid=1_779078c2c847bb3217554b8549ad49bd1623728424311; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDSFRCVID_BFESS=BkFOJeCT5G3_WP5eFqJ2T4D2p2KKN9OTTPjcTR5qJ04BtyCVNKsaEG0PtOgMNBDbJ2MRogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJ4toCPMJI_3fP36q45HMt00qxby26PDajn9aJ5nQI5nhU7505oqDJ0Z0ROOWhRute3i2DTvQUbmjRO206oay6O3LlO83h5wW57KKl0MLPbcep68LxODy6DI0xnMBMnr52OnaU513fAKftnOM46JehL3346-35543bRTLnLy5KJYMDF4D5_ae5O3DGRf-b-XKD600PK8Kb7VbUF6qfnkbft7jtteyhbTJCID-UQKQPnc_pC4yURFef473b3B5h3NJ66ZoIbPbPTTSlroKPQpQT8r5-nMWx6G3IrZoq64ab3vOpRTXpO13fAzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjDjJRCOoI--f-3bfTrP-trf5DCShUFs3tnlB2Q-5M-a3KOrSUtGbfjay6D7j-8HbTjiW2_82MbmLncjSM_GKfC2jMD32tbpWfneKmTxoUJ2Bb3Y8loe-xCKXqDebPRiWPb9QgbP2pQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjKbDTvL3f; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1624438637,1624603638,1624928461,1624953786; H_PS_PSSID=34131_34099_31253_34004_33607_34107_34135; delPer=0; PSINO=6; BAIDUID_BFESS=8496908995397662040287D2CE1C4224:FG=1; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1624962661; __yjs_st=2_MzJhZTMxZGU5MjZjNGJiZTJiZjQwYjVkMWM5ZjYyMGFjZDlkMDJmNTU3OGU5ZTM4N2JjNjNkODAwYWJiY2M3NDA1NWEyODNkMzNkMDEzNThiZTU4NzNhMTQxYzIxOTQyMzg3MjhiMzA5ZjY2MDczZTBhZDdmZDg4YTFhNjVmZTMwZTYyZTRjNmRhMWNmYzg3NDFjODYzYTRlZTE2NzBmODAyMWI4MTI3NTZmNjg1MDk4OWIxZTYzNTc4NzhjY2E3NzU3ZGYyZmI1ODdjZTM5ZDNlOGU0ZGQ2NzE5OGU2NzUzM2ZhZTcxZmVjNjI4MDIyN2Y1N2NlMzZmMmRlY2U4Yl83XzQ5NzQ4ZWE4; ab_sr=1.0.1_MmUwODU0NGE4NjIwZmY4NjgxZmM1NGYxOTI5ZWQwOGU2NjU3ZjgwNzhkMTNjNDI5NWE0ODQwYzlkZDVjY2Q1YWEyZDQyZWI0ZjNkMWQ0NTEyMGFjYzdiNDdmNzYxYjNiMjkxZTI1M2I3Y2VhZGE3NDEzOTgyMjY1MjBlZGM4OGJiZGVjMzFkYTM3ODgyMTRkZjJhMGYzNGM0MGJmMGY1Yg=='</span>,
    <span class="hljs-string">'Host'</span>: <span class="hljs-string">'fanyi.baidu.com'</span>,
    <span class="hljs-string">'Origin'</span>: <span class="hljs-string">'https://fanyi.baidu.com'</span>,
    <span class="hljs-string">'Referer'</span>: <span class="hljs-string">'https://fanyi.baidu.com/'</span>,
    <span class="hljs-string">'sec-ch-ua'</span>: <span class="hljs-string">'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"'</span>,
    <span class="hljs-string">'sec-ch-ua-mobile'</span>: <span class="hljs-string">'?0'</span>,
    <span class="hljs-string">'Sec-Fetch-Dest'</span>: <span class="hljs-string">'empty'</span>,
    <span class="hljs-string">'Sec-Fetch-Mode'</span>: <span class="hljs-string">'cors'</span>,
    <span class="hljs-string">'Sec-Fetch-Site'</span>: <span class="hljs-string">'same-origin'</span>,
    <span class="hljs-string">'User-Agent'</span>: <span class="hljs-string">'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'</span>,
    <span class="hljs-string">'X-Requested-With'</span>: <span class="hljs-string">'XMLHttpRequest'</span>
&#125;


<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get_token</span>():</span>
    response = requests.get(url=index_url, headers=headers).text
    token = re.findall(<span class="hljs-string">r"token: '([0-9a-z]+)"</span>, response)[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">return</span> token


<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get_sign</span>(<span class="hljs-params">query</span>):</span>
    <span class="hljs-keyword">with</span> <span class="hljs-built_in">open</span>(<span class="hljs-string">'baidu_encrypt.js'</span>, <span class="hljs-string">'r'</span>, encoding=<span class="hljs-string">'utf-8'</span>) <span class="hljs-keyword">as</span> f:
        baidu_js = f.read()
    sign = execjs.<span class="hljs-built_in">compile</span>(baidu_js).call(<span class="hljs-string">'e'</span>, query)
    <span class="hljs-keyword">return</span> sign


<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get_result</span>(<span class="hljs-params">lang, query, sign, token</span>):</span>
    data = &#123;
        <span class="hljs-string">'from'</span>: lang,
        <span class="hljs-string">'to'</span>: <span class="hljs-string">'en'</span>,
        <span class="hljs-string">'query'</span>: query,
        <span class="hljs-string">'transtype'</span>: <span class="hljs-string">'realtime'</span>,
        <span class="hljs-string">'simple_means_flag'</span>: <span class="hljs-string">'3'</span>,
        <span class="hljs-string">'sign'</span>: sign,
        <span class="hljs-string">'token'</span>: token,
    &#125;
    response = requests.post(url=translate_api, headers=headers, data=data)
    result = response.json()[<span class="hljs-string">'trans_result'</span>][<span class="hljs-string">'data'</span>][<span class="hljs-number">0</span>][<span class="hljs-string">'dst'</span>]
    <span class="hljs-keyword">return</span> result


<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">main</span>():</span>
    query = <span class="hljs-built_in">input</span>(<span class="hljs-string">'请输入要翻译的文字：'</span>)
    response = requests.post(url=lang_url, headers=headers, data=&#123;<span class="hljs-string">'query'</span>: query&#125;)
    lang = response.json()[<span class="hljs-string">'lan'</span>]
    token = get_token()
    sign = get_sign(query)
    result = get_result(lang, query, sign, token)
    <span class="hljs-built_in">print</span>(<span class="hljs-string">'翻译成英文的结果为：'</span>, result)


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">'__main__'</span>:
    main()
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            