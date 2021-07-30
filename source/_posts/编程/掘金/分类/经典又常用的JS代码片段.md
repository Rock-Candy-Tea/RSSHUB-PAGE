
---
title: '经典又常用的JS代码片段'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4a2bedf64854b9fb8a978b631b3c501~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 22:00:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4a2bedf64854b9fb8a978b631b3c501~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>日常开发中，<code>一般的程序员</code>通常会遇到以下场景：</p>
<ol>
<li>vue中遍历一个列表，但接口数据没有唯一标识，需要手动生成UUID来v-bind:key，怎么生成呢？Google一下</li>
<li>运行一段复杂代码，记得好像H5新的Api <code>Worker</code>可以开启多线程执行还能避免阻塞，但是具体怎么用呢？Google一下</li>
<li>当脱离框架，要实现删除一个节点、为节点添加或删除类、插入节点等操作时，隐隐记得好像都做过，但是忘了，Google一下</li>
<li>遇到设备兼容问题要对某个环境做特殊处理时，怎么判断移动端下的ios设备的自带浏览器？Google一下</li>
<li>有一个打乱数组的需求，这个我做过，(⊙o⊙)…好像写不太出来。算了，Google一下</li>
</ol>
<p>不知道各位程序猿兄弟姐妹有没有出现以上类似场景，笔者是历历在目了。在开发时，很多功能我们都实现过，或者死记硬背过，或者看过实现原理。但是一旦到了应用的时候，脑袋便一片空白。所以还是那句老话，好记性不如烂笔头。开发不比面试，遇到问题随心所欲，要百度就百度，要谷歌就谷歌，但是查到的内容就参差不齐了，如果查到的文章本身就有问题，那试错成本就太高了。为了避免<code>一般的程序员</code>日复一日的Google，本文旨在打造一份满足日常开发的原生js代码片段库。可让<code>一般的程序员</code>可开箱即用，节省额外搜索的时间。</p>
<p>js代码片段使用 <code>ES6</code> 编写，已尽量精简和考虑兼容问题，大家可点赞、收藏一波，以便使用，闲暇时可常打开看看推敲其实现原理。</p>
<p>笔者会不定期更新哟，有问题可在评论区一起讨论，谢谢大家..</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4a2bedf64854b9fb8a978b631b3c501~tplv-k3u1fbpfcp-watermark.image" alt="感谢.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">工具</h2>
<h3 data-id="heading-2">生成 UUID</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> UUIDGeneratorBrowser = <span class="hljs-function">() =></span>
  ([<span class="hljs-number">1e7</span>] + -<span class="hljs-number">1e3</span> + -<span class="hljs-number">4e3</span> + -<span class="hljs-number">8e3</span> + -<span class="hljs-number">1e11</span>).replace(<span class="hljs-regexp">/[018]/g</span>, <span class="hljs-function">(<span class="hljs-params">c</span>) =></span>
    (
      c ^
      (crypto.getRandomValues(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(<span class="hljs-number">1</span>))[<span class="hljs-number">0</span>] & (<span class="hljs-number">15</span> >> (c / <span class="hljs-number">4</span>)))
    ).toString(<span class="hljs-number">16</span>)
  );

<span class="hljs-comment">// Examples</span>
UUIDGeneratorBrowser(); <span class="hljs-comment">// '7982fcfe-5721-4632-bede-6000885be57d'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">解析 cookie</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> parseCookie = <span class="hljs-function">(<span class="hljs-params">str</span>) =></span>
  str
    .split(<span class="hljs-string">";"</span>)
    .map(<span class="hljs-function">(<span class="hljs-params">v</span>) =></span> v.split(<span class="hljs-string">"="</span>))
    .reduce(<span class="hljs-function">(<span class="hljs-params">acc, v</span>) =></span> &#123;
      acc[<span class="hljs-built_in">decodeURIComponent</span>(v[<span class="hljs-number">0</span>].trim())] = <span class="hljs-built_in">decodeURIComponent</span>(v[<span class="hljs-number">1</span>].trim());
      <span class="hljs-keyword">return</span> acc;
    &#125;, &#123;&#125;);

<span class="hljs-comment">// Examples</span>
parseCookie(<span class="hljs-string">"foo=bar; equation=E%3Dmc%5E2"</span>);
<span class="hljs-comment">// &#123; foo: 'bar', equation: 'E=mc^2' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">获取网址参数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getURLParameters = <span class="hljs-function">(<span class="hljs-params">url</span>) =></span>
  (url.match(<span class="hljs-regexp">/([^?=&]+)(=([^&]*))/g</span>) || []).reduce(
    <span class="hljs-function">(<span class="hljs-params">a, v</span>) =></span> (
      (a[v.slice(<span class="hljs-number">0</span>, v.indexOf(<span class="hljs-string">"="</span>))] = v.slice(v.indexOf(<span class="hljs-string">"="</span>) + <span class="hljs-number">1</span>)), a
    ),
    &#123;&#125;
  );

<span class="hljs-comment">// Examples</span>
getURLParameters(<span class="hljs-string">"google.com"</span>); <span class="hljs-comment">// &#123;&#125;</span>
getURLParameters(<span class="hljs-string">"http://url.com/page?name=Adam&surname=Smith"</span>);
<span class="hljs-comment">// &#123;name: 'Adam', surname: 'Smith'&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">复制到剪切板</h3>
<p>以下方式仅在用户执行操作时有效，如：click 事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> copyToClipboard = <span class="hljs-function">(<span class="hljs-params">str</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> el = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"textarea"</span>);
  el.value = str;
  el.setAttribute(<span class="hljs-string">"readonly"</span>, <span class="hljs-string">""</span>);
  el.style.position = <span class="hljs-string">"absolute"</span>;
  el.style.left = <span class="hljs-string">"-9999px"</span>;
  <span class="hljs-built_in">document</span>.body.appendChild(el);
  <span class="hljs-keyword">const</span> selected =
    <span class="hljs-built_in">document</span>.getSelection().rangeCount > <span class="hljs-number">0</span>
      ? <span class="hljs-built_in">document</span>.getSelection().getRangeAt(<span class="hljs-number">0</span>)
      : <span class="hljs-literal">false</span>;
  el.select();
  <span class="hljs-built_in">document</span>.execCommand(<span class="hljs-string">"copy"</span>);
  <span class="hljs-built_in">document</span>.body.removeChild(el);
  <span class="hljs-keyword">if</span> (selected) &#123;
    <span class="hljs-built_in">document</span>.getSelection().removeAllRanges();
    <span class="hljs-built_in">document</span>.getSelection().addRange(selected);
  &#125;
&#125;;

<span class="hljs-comment">// Examples</span>
copyToClipboard(<span class="hljs-string">"Lorem ipsum"</span>); <span class="hljs-comment">// 'Lorem ipsum' copied to clipboard.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">简版 jquery 选择器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 仅选中第一个元素</span>
<span class="hljs-keyword">const</span> $ = <span class="hljs-built_in">document</span>.querySelector.bind(<span class="hljs-built_in">document</span>);
<span class="hljs-comment">// 选中所有</span>
<span class="hljs-keyword">const</span> $$ = <span class="hljs-built_in">document</span>.querySelectorAll.bind(<span class="hljs-built_in">document</span>);

<span class="hljs-keyword">const</span> mainContent = $(<span class="hljs-string">".main-content"</span>);
<span class="hljs-keyword">const</span> externalLinks = $$(<span class="hljs-string">'a[target="_blank"]'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">多线程执行函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> runAsync = <span class="hljs-function">(<span class="hljs-params">fn</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> worker = <span class="hljs-keyword">new</span> Worker(
    URL.createObjectURL(<span class="hljs-keyword">new</span> Blob([<span class="hljs-string">`postMessage((<span class="hljs-subst">$&#123;fn&#125;</span>)());`</span>]), &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">"application/javascript; charset=utf-8"</span>,
    &#125;)
  );
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">res, rej</span>) =></span> &#123;
    worker.onmessage = <span class="hljs-function">(<span class="hljs-params">&#123; data &#125;</span>) =></span> &#123;
      res(data), worker.terminate();
    &#125;;
    worker.onerror = <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
      rej(err), worker.terminate();
    &#125;;
  &#125;);
&#125;;

<span class="hljs-comment">// Examples</span>
<span class="hljs-keyword">const</span> longRunningFunction = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">let</span> result = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1000</span>; i++)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < <span class="hljs-number">700</span>; j++)
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k = <span class="hljs-number">0</span>; k < <span class="hljs-number">300</span>; k++) result = result + i + j + k;

  <span class="hljs-keyword">return</span> result;
&#125;;
<span class="hljs-comment">/*
  <span class="hljs-doctag">NOTE:</span> Since the function is running in a different context, closures are not supported.
  The function supplied to `runAsync` gets stringified, so everything becomes literal.
  All variables and functions must be defined inside.
*/</span>
runAsync(longRunningFunction).then(<span class="hljs-built_in">console</span>.log); <span class="hljs-comment">// 209685000000</span>
runAsync(<span class="hljs-function">() =></span> <span class="hljs-number">10</span> ** <span class="hljs-number">3</span>).then(<span class="hljs-built_in">console</span>.log); <span class="hljs-comment">// 1000</span>
<span class="hljs-keyword">let</span> outsideVariable = <span class="hljs-number">50</span>;
runAsync(<span class="hljs-function">() =></span> <span class="hljs-keyword">typeof</span> outsideVariable).then(<span class="hljs-built_in">console</span>.log); <span class="hljs-comment">// 'undefined'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">业务功能</h2>
<h3 data-id="heading-9">判断所有数据类型</h3>
<p>@param obj 要判断类型的数据</p>
<p>@return &#123;string&#125; 数据类型（小写）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> type = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 映射类型</span>
  <span class="hljs-keyword">const</span> classType =
    <span class="hljs-string">"Boolean Number String Function Array Date RegExp Object Error Null Undefined"</span>
      .split(<span class="hljs-string">" "</span>)
      .reduce(<span class="hljs-function">(<span class="hljs-params">obj, item</span>) =></span> &#123;
        obj[<span class="hljs-string">"[object "</span> + item + <span class="hljs-string">"]"</span>] = item.toLowerCase();
        <span class="hljs-keyword">return</span> obj;
      &#125;, &#123;&#125;);

  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-comment">// 仅 undefined 与 null 成立</span>
    <span class="hljs-keyword">if</span> (obj == <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">return</span> obj + <span class="hljs-string">""</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">"object"</span>
      ? classType[<span class="hljs-built_in">Object</span>.prototype.toString.call(obj)]
      : <span class="hljs-keyword">typeof</span> obj;
  &#125;;
&#125;)();

<span class="hljs-comment">// Examples</span>
<span class="hljs-built_in">console</span>.log(type(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>())); <span class="hljs-comment">// date</span>
<span class="hljs-built_in">console</span>.log(type([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>])); <span class="hljs-comment">// array</span>
<span class="hljs-built_in">console</span>.log(type(<span class="hljs-number">1</span>)); <span class="hljs-comment">// number</span>
<span class="hljs-built_in">console</span>.log(type(&#123;&#125;)); <span class="hljs-comment">// object</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">判断空对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isEmptyObject</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.prototype.toString.call(obj) !== <span class="hljs-string">"[object Object]"</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">var</span> name;
  <span class="hljs-keyword">for</span> (name <span class="hljs-keyword">in</span> obj) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;

<span class="hljs-comment">// Examples</span>
<span class="hljs-built_in">console</span>.log(isEmptyObject(&#123;&#125;)); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(isEmptyObject([])); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(isEmptyObject(<span class="hljs-literal">null</span>)); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(isEmptyObject(<span class="hljs-literal">undefined</span>)); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(isEmptyObject(<span class="hljs-number">1</span>)); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(isEmptyObject(<span class="hljs-string">""</span>)); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(isEmptyObject(<span class="hljs-literal">true</span>)); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">判断当前运行环境</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">userAgent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> u = navigator.userAgent;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-comment">// 移动终端浏览器版本信息</span>
    <span class="hljs-attr">trident</span>: u.indexOf(<span class="hljs-string">"Trident"</span>) > -<span class="hljs-number">1</span>, <span class="hljs-comment">// IE内核</span>
    <span class="hljs-attr">presto</span>: u.indexOf(<span class="hljs-string">"Presto"</span>) > -<span class="hljs-number">1</span>, <span class="hljs-comment">// opera内核</span>
    <span class="hljs-attr">webKit</span>: u.indexOf(<span class="hljs-string">"AppleWebKit"</span>) > -<span class="hljs-number">1</span>, <span class="hljs-comment">// 苹果、谷歌内核</span>
    <span class="hljs-attr">gecko</span>: u.indexOf(<span class="hljs-string">"Gecko"</span>) > -<span class="hljs-number">1</span> && u.indexOf(<span class="hljs-string">"KHTML"</span>) === -<span class="hljs-number">1</span>, <span class="hljs-comment">// 火狐内核</span>
    <span class="hljs-attr">mobile</span>: !!u.match(<span class="hljs-regexp">/AppleWebKit.*Mobile.*/</span>), <span class="hljs-comment">// 是否为移动终端</span>
    <span class="hljs-attr">iPad</span>: u.indexOf(<span class="hljs-string">"iPad"</span>) > -<span class="hljs-number">1</span>, <span class="hljs-comment">// 是否iPad</span>
    <span class="hljs-attr">webApp</span>: u.indexOf(<span class="hljs-string">"Safari"</span>) === -<span class="hljs-number">1</span>, <span class="hljs-comment">// 是否web应该程序，没有头部与底部,</span>
    <span class="hljs-attr">isiOS</span>: !!u.match(<span class="hljs-regexp">/\(i[^;]+;( U;)? CPU.+Mac OS X/</span>), <span class="hljs-comment">// ios终端</span>
    <span class="hljs-attr">isAndroid</span>: u.indexOf(<span class="hljs-string">"Android"</span>) > -<span class="hljs-number">1</span> || u.indexOf(<span class="hljs-string">"Adr"</span>) > -<span class="hljs-number">1</span>,
  &#125;;
&#125;

<span class="hljs-comment">// Examples</span>
<span class="hljs-keyword">const</span> browser = userAgent();
<span class="hljs-keyword">if</span> (browser.mobile) &#123;
  <span class="hljs-comment">// 移动端 => todo something</span>
  <span class="hljs-keyword">if</span> (browser.isiOS && browser.webApp) &#123;
    <span class="hljs-comment">// IOS系统 && web程序 => todo something</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 安卓 => todo something</span>
  &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// PC => todo something</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">平滑滚动到页面顶部</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> scrollToTop = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> c = <span class="hljs-built_in">document</span>.documentElement.scrollTop || <span class="hljs-built_in">document</span>.body.scrollTop;
  <span class="hljs-keyword">if</span> (c > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-built_in">window</span>.requestAnimationFrame(scrollToTop);
    <span class="hljs-built_in">window</span>.scrollTo(<span class="hljs-number">0</span>, c - c / <span class="hljs-number">8</span>);
  &#125;
&#125;;

<span class="hljs-comment">// Examples</span>
scrollToTop();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">将视口平滑滚动到指定元素</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> smoothScroll = <span class="hljs-function">(<span class="hljs-params">element</span>) =></span>
  <span class="hljs-built_in">document</span>.querySelector(element).scrollIntoView(&#123;
    <span class="hljs-attr">behavior</span>: <span class="hljs-string">"smooth"</span>,
  &#125;);

<span class="hljs-comment">// Examples</span>
smoothScroll(<span class="hljs-string">"#fooBar"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">监听滚动结束</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> onScrollStop = <span class="hljs-function">(<span class="hljs-params">callback</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> isScrolling;
  <span class="hljs-built_in">window</span>.addEventListener(
    <span class="hljs-string">"scroll"</span>,
    <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
      <span class="hljs-built_in">clearTimeout</span>(isScrolling);
      isScrolling = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        callback();
      &#125;, <span class="hljs-number">150</span>);
    &#125;,
    <span class="hljs-literal">false</span>
  );
&#125;;

<span class="hljs-comment">// Examples</span>
onScrollStop(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"The user has stopped scrolling"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">监听点击指定元素外部</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> onClickOutside = <span class="hljs-function">(<span class="hljs-params">element, callback</span>) =></span> &#123;
  <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!element.contains(e.target)) callback();
  &#125;);
&#125;;

<span class="hljs-comment">// Examples</span>
onClickOutside(<span class="hljs-string">"#my-element"</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Hello"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">获取浏览器当前语言</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// defaultLang 为默认语言</span>
<span class="hljs-keyword">const</span> detectLanguage = <span class="hljs-function">(<span class="hljs-params">defaultLang = <span class="hljs-string">"en-US"</span></span>) =></span>
  navigator.language ||
  (<span class="hljs-built_in">Array</span>.isArray(navigator.languages) && navigator.languages[<span class="hljs-number">0</span>]) ||
  defaultLang;

<span class="hljs-comment">// Examples</span>
detectLanguage(); <span class="hljs-comment">// 'nl-NL'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">控制浏览器全屏、退出全屏</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fullscreen = <span class="hljs-function">(<span class="hljs-params">mode = <span class="hljs-literal">true</span>, el = <span class="hljs-string">"body"</span></span>) =></span>
  mode
    ? <span class="hljs-built_in">document</span>.querySelector(el).requestFullscreen()
    : <span class="hljs-built_in">document</span>.exitFullscreen();

<span class="hljs-comment">// Examples</span>
fullscreen(); <span class="hljs-comment">// Opens `body` in fullscreen mode</span>
fullscreen(<span class="hljs-literal">false</span>); <span class="hljs-comment">// Exits fullscreen mode</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">封装原生 GET、POST 请求</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> httpGet = <span class="hljs-function">(<span class="hljs-params">url, callback, err = <span class="hljs-built_in">console</span>.error</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest();
  request.open(<span class="hljs-string">"GET"</span>, url, <span class="hljs-literal">true</span>);
  request.onload = <span class="hljs-function">() =></span> callback(request.responseText);
  request.onerror = <span class="hljs-function">() =></span> err(request);
  request.send();
&#125;;

<span class="hljs-keyword">const</span> httpPost = <span class="hljs-function">(<span class="hljs-params">url, data, callback, err = <span class="hljs-built_in">console</span>.error</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest();
  request.open(<span class="hljs-string">"POST"</span>, url, <span class="hljs-literal">true</span>);
  request.setRequestHeader(<span class="hljs-string">"Content-type"</span>, <span class="hljs-string">"application/json; charset=utf-8"</span>);
  request.onload = <span class="hljs-function">() =></span> callback(request.responseText);
  request.onerror = <span class="hljs-function">() =></span> err(request);
  request.send(data);
&#125;;

<span class="hljs-comment">// Examples</span>
httpGet(<span class="hljs-string">"https://jsonplaceholder.typicode.com/posts/1"</span>, <span class="hljs-built_in">console</span>.log); <span class="hljs-comment">/*
Logs: &#123;
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
&#125;
*/</span>

httpPost(
  <span class="hljs-string">"https://jsonplaceholder.typicode.com/posts"</span>,
  <span class="hljs-literal">null</span>, <span class="hljs-comment">// does not send a body</span>
  <span class="hljs-built_in">console</span>.log
); <span class="hljs-comment">/*
Logs: &#123;
  "id": 101
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">DOM 操作</h2>
<h3 data-id="heading-20">元素添加、移除、切换类</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> addClass = <span class="hljs-function">(<span class="hljs-params">el, className</span>) =></span> el.classList.add(className);
<span class="hljs-keyword">const</span> removeClass = <span class="hljs-function">(<span class="hljs-params">el, className</span>) =></span> el.classList.remove(className);
<span class="hljs-keyword">const</span> toggleClass = <span class="hljs-function">(<span class="hljs-params">el, className</span>) =></span> el.classList.toggle(className);

<span class="hljs-comment">// Examples</span>
addClass(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"p"</span>), <span class="hljs-string">"special"</span>);
removeClass(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"p.special"</span>), <span class="hljs-string">"special"</span>);
toggleClass(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"p.special"</span>), <span class="hljs-string">"special"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">移除一个元素</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> removeElement = <span class="hljs-function">(<span class="hljs-params">el</span>) =></span> el.parentNode.removeChild(el);

<span class="hljs-comment">// Examples</span>
removeElement(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#my-element"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">判断元素上是否包含指定的类</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> hasClass = <span class="hljs-function">(<span class="hljs-params">el, className</span>) =></span> el.classList.contains(className);

<span class="hljs-comment">// Examples</span>
hasClass(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"p.special"</span>), <span class="hljs-string">"special"</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">获取一个元素下所有图片地址</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// includeDuplicates 是否去重</span>
<span class="hljs-keyword">const</span> getImages = <span class="hljs-function">(<span class="hljs-params">el, includeDuplicates = <span class="hljs-literal">false</span></span>) =></span> &#123;
  <span class="hljs-keyword">const</span> images = [...el.getElementsByTagName(<span class="hljs-string">"img"</span>)].map(<span class="hljs-function">(<span class="hljs-params">img</span>) =></span>
    img.getAttribute(<span class="hljs-string">"src"</span>)
  );
  <span class="hljs-keyword">return</span> includeDuplicates ? images : [...new <span class="hljs-built_in">Set</span>(images)];
&#125;;

<span class="hljs-comment">// Examples</span>
getImages(<span class="hljs-built_in">document</span>, <span class="hljs-literal">true</span>); <span class="hljs-comment">// ['image1.jpg', 'image2.png', 'image1.png', '...']</span>
getImages(<span class="hljs-built_in">document</span>, <span class="hljs-literal">false</span>); <span class="hljs-comment">// ['image1.jpg', 'image2.png', '...']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">创建字符串片段的元素</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 注意：最外层不可有同级兄弟元素，如果有只会返回第一个</span>
<span class="hljs-keyword">const</span> createElement = <span class="hljs-function">(<span class="hljs-params">str</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> el = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
  el.innerHTML = str;
  <span class="hljs-keyword">return</span> el.firstElementChild;
&#125;;

<span class="hljs-comment">// Examples</span>
<span class="hljs-keyword">const</span> el = createElement(
  <span class="hljs-string">`<div class="container">
    <p>Hello!</p>
  </div>`</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">主动触发 dom 事件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> triggerEvent = <span class="hljs-function">(<span class="hljs-params">el, eventType, detail</span>) =></span>
  el.dispatchEvent(<span class="hljs-keyword">new</span> CustomEvent(eventType, &#123; detail &#125;));

<span class="hljs-comment">// Examples</span>
triggerEvent(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myId"</span>), <span class="hljs-string">"click"</span>);
triggerEvent(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myId"</span>), <span class="hljs-string">"click"</span>, &#123; <span class="hljs-attr">username</span>: <span class="hljs-string">"bob"</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">Date</h2>
<h3 data-id="heading-27">获取月份的总天数</h3>
<p>利用 setDatesh(0)时，会将日期设置为对应月份的最后一天。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> daysInMonth = <span class="hljs-function">(<span class="hljs-params">year, month</span>) =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(year, month, <span class="hljs-number">0</span>).getDate();

<span class="hljs-comment">// Examples</span>
daysInMonth(<span class="hljs-number">2020</span>, <span class="hljs-number">12</span>)); <span class="hljs-comment">// 31</span>
daysInMonth(<span class="hljs-number">2024</span>, <span class="hljs-number">2</span>)); <span class="hljs-comment">// 29</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">将日期转换为 yyyy-MM-dd</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getISODate = <span class="hljs-function">(<span class="hljs-params">date</span>) =></span> data.toISOString().split(<span class="hljs-string">"T"</span>)[<span class="hljs-number">0</span>];

<span class="hljs-comment">// Examples</span>
getISODate(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()); <span class="hljs-comment">// "2021-07-28"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">将日期转换为 HH:MM:SS</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getColonTimeFromDate = <span class="hljs-function">(<span class="hljs-params">date</span>) =></span> date.toTimeString().slice(<span class="hljs-number">0</span>, <span class="hljs-number">8</span>);

<span class="hljs-comment">// Examples</span>
getColonTimeFromDate(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()); <span class="hljs-comment">// '08:38:00'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">返回天、时、分、秒、毫秒</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> formatDuration = <span class="hljs-function">(<span class="hljs-params">ms</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (ms < <span class="hljs-number">0</span>) ms = -ms;
  <span class="hljs-keyword">const</span> time = &#123;
    <span class="hljs-attr">day</span>: <span class="hljs-built_in">Math</span>.floor(ms / <span class="hljs-number">86400000</span>),
    <span class="hljs-attr">hour</span>: <span class="hljs-built_in">Math</span>.floor(ms / <span class="hljs-number">3600000</span>) % <span class="hljs-number">24</span>,
    <span class="hljs-attr">minute</span>: <span class="hljs-built_in">Math</span>.floor(ms / <span class="hljs-number">60000</span>) % <span class="hljs-number">60</span>,
    <span class="hljs-attr">second</span>: <span class="hljs-built_in">Math</span>.floor(ms / <span class="hljs-number">1000</span>) % <span class="hljs-number">60</span>,
    <span class="hljs-attr">millisecond</span>: <span class="hljs-built_in">Math</span>.floor(ms) % <span class="hljs-number">1000</span>,
  &#125;;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.entries(time)
    .filter(<span class="hljs-function">(<span class="hljs-params">val</span>) =></span> val[<span class="hljs-number">1</span>] !== <span class="hljs-number">0</span>)
    .map(<span class="hljs-function">(<span class="hljs-params">[key, val]</span>) =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;val&#125;</span> <span class="hljs-subst">$&#123;key&#125;</span><span class="hljs-subst">$&#123;val !== <span class="hljs-number">1</span> ? <span class="hljs-string">"s"</span> : <span class="hljs-string">""</span>&#125;</span>`</span>)
    .join(<span class="hljs-string">", "</span>);
&#125;;

<span class="hljs-comment">// examples</span>
formatDuration(<span class="hljs-number">1001</span>); <span class="hljs-comment">// '1 second, 1 millisecond'</span>
formatDuration(<span class="hljs-number">34325055574</span>);
<span class="hljs-comment">// '397 days, 6 hours, 44 minutes, 15 seconds, 574 milliseconds'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">返回给定秒数的 ISO 格式('00:00:00')</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> formatSeconds = <span class="hljs-function">(<span class="hljs-params">s</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> [hour, minute, second, sign] =
    s > <span class="hljs-number">0</span>
      ? [s / <span class="hljs-number">3600</span>, (s / <span class="hljs-number">60</span>) % <span class="hljs-number">60</span>, s % <span class="hljs-number">60</span>, <span class="hljs-string">""</span>]
      : [-s / <span class="hljs-number">3600</span>, (-s / <span class="hljs-number">60</span>) % <span class="hljs-number">60</span>, -s % <span class="hljs-number">60</span>, <span class="hljs-string">"-"</span>];

  <span class="hljs-keyword">return</span> (
    sign +
    [hour, minute, second]
      .map(<span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.floor(v)&#125;</span>`</span>.padStart(<span class="hljs-number">2</span>, <span class="hljs-string">"0"</span>))
      .join(<span class="hljs-string">":"</span>)
  );
&#125;;

<span class="hljs-comment">// Examples</span>
formatSeconds(<span class="hljs-number">200</span>); <span class="hljs-comment">// '00:03:20'</span>
formatSeconds(-<span class="hljs-number">200</span>); <span class="hljs-comment">// '-00:03:20'</span>
formatSeconds(<span class="hljs-number">99999</span>); <span class="hljs-comment">// '27:46:39'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">判断两个时间是否相同</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isSameDate = <span class="hljs-function">(<span class="hljs-params">dateA, dateB</span>) =></span>
  dateA.toISOString() === dateB.toISOString();

<span class="hljs-comment">// Examples</span>
isSameDate(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-number">2010</span>, <span class="hljs-number">10</span>, <span class="hljs-number">20</span>), <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-number">2010</span>, <span class="hljs-number">10</span>, <span class="hljs-number">20</span>)); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">判断给定年份是否是闰年</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isLeapYear = <span class="hljs-function">(<span class="hljs-params">year</span>) =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(year, <span class="hljs-number">1</span>, <span class="hljs-number">29</span>).getMonth() === <span class="hljs-number">1</span>;

<span class="hljs-comment">// Examples</span>
isLeapYear(<span class="hljs-number">2019</span>); <span class="hljs-comment">// false</span>
isLeapYear(<span class="hljs-number">2020</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">判断给定日期是否是周末</h3>
<p>利用 getDay 方法，周 6 时返回 6，周日时返回 0。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isWeekend = <span class="hljs-function">(<span class="hljs-params">d = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()</span>) =></span> d.getDay() % <span class="hljs-number">6</span> === <span class="hljs-number">0</span>;

<span class="hljs-comment">// Examples</span>
isWeekend(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-number">2021</span>, <span class="hljs-number">6</span>, <span class="hljs-number">29</span>)); <span class="hljs-comment">// false</span>
isWeekend(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-number">2021</span>, <span class="hljs-number">6</span>, <span class="hljs-number">31</span>)); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">返回给指定日期添加增量时间后的时间</h3>
<p>利用<code>setDate</code>方法会自动换算大于 31 天的日期。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> addDaysToDate = <span class="hljs-function">(<span class="hljs-params">date, n</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> d = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(date);
  d.setDate(d.getDate() + n);
  <span class="hljs-keyword">return</span> d.toISOString().split(<span class="hljs-string">"T"</span>)[<span class="hljs-number">0</span>];
&#125;;

<span class="hljs-comment">// Examples</span>
addDaysToDate(<span class="hljs-string">"2020-10-15"</span>, <span class="hljs-number">10</span>); <span class="hljs-comment">// '2020-10-25'</span>
addDaysToDate(<span class="hljs-string">"2020-10-15"</span>, -<span class="hljs-number">10</span>); <span class="hljs-comment">// '2020-10-05'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-36">算法</h2>
<h3 data-id="heading-37">快速排序</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> quickSort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> a = [...arr];
  <span class="hljs-keyword">if</span> (a.length < <span class="hljs-number">2</span>) <span class="hljs-keyword">return</span> a;
  <span class="hljs-keyword">const</span> pivotIndex = <span class="hljs-built_in">Math</span>.floor(arr.length / <span class="hljs-number">2</span>);
  <span class="hljs-keyword">const</span> pivot = a[pivotIndex];
  <span class="hljs-keyword">const</span> [lo, hi] = a.reduce(
    <span class="hljs-function">(<span class="hljs-params">acc, val, i</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (val < pivot || (val === pivot && i != pivotIndex)) &#123;
        acc[<span class="hljs-number">0</span>].push(val);
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (val > pivot) &#123;
        acc[<span class="hljs-number">1</span>].push(val);
      &#125;
      <span class="hljs-keyword">return</span> acc;
    &#125;,
    [[], []]
  );
  <span class="hljs-keyword">return</span> [...quickSort(lo), pivot, ...quickSort(hi)];
&#125;;

<span class="hljs-comment">// Examples</span>
quickSort([<span class="hljs-number">1</span>, <span class="hljs-number">6</span>, <span class="hljs-number">1</span>, <span class="hljs-number">5</span>, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">4</span>]); <span class="hljs-comment">// [1, 1, 1, 2, 3, 4, 5, 6]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">选择排序</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> selectionSort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> a = [...arr];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < a.length; i++) &#123;
    <span class="hljs-keyword">const</span> min = a
      .slice(i + <span class="hljs-number">1</span>)
      .reduce(<span class="hljs-function">(<span class="hljs-params">acc, val, j</span>) =></span> (val < a[acc] ? j + i + <span class="hljs-number">1</span> : acc), i);
    <span class="hljs-keyword">if</span> (min !== i) [a[i], a[min]] = [a[min], a[i]];
  &#125;
  <span class="hljs-keyword">return</span> a;
&#125;;

<span class="hljs-comment">// Examples</span>
selectionSort([<span class="hljs-number">5</span>, <span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]); <span class="hljs-comment">// [1, 2, 3, 4, 5]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-39">插入排序</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> insertionSort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span>
  arr.reduce(<span class="hljs-function">(<span class="hljs-params">acc, x</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!acc.length) <span class="hljs-keyword">return</span> [x];
    acc.some(<span class="hljs-function">(<span class="hljs-params">y, j</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (x <= y) &#123;
        acc.splice(j, <span class="hljs-number">0</span>, x);
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
      &#125;
      <span class="hljs-keyword">if</span> (x > y && j === acc.length - <span class="hljs-number">1</span>) &#123;
        acc.splice(j + <span class="hljs-number">1</span>, <span class="hljs-number">0</span>, x);
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;);
    <span class="hljs-keyword">return</span> acc;
  &#125;, []);

<span class="hljs-comment">// Examples</span>
insertionSort([<span class="hljs-number">6</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>]); <span class="hljs-comment">// [1, 3, 4, 6]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40">冒泡排序</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> bubbleSort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> swapped = <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">const</span> a = [...arr];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < a.length; i++) &#123;
    swapped = <span class="hljs-literal">false</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < a.length - i; j++) &#123;
      <span class="hljs-keyword">if</span> (a[j + <span class="hljs-number">1</span>] < a[j]) &#123;
        [a[j], a[j + <span class="hljs-number">1</span>]] = [a[j + <span class="hljs-number">1</span>], a[j]];
        swapped = <span class="hljs-literal">true</span>;
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (!swapped) <span class="hljs-keyword">return</span> a;
  &#125;
  <span class="hljs-keyword">return</span> a;
&#125;;

<span class="hljs-comment">// Examples</span>
bubbleSort([<span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">3</span>]); <span class="hljs-comment">// [1, 2, 3, 4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41">归并排序</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mergeSort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (arr.length < <span class="hljs-number">2</span>) <span class="hljs-keyword">return</span> arr;
  <span class="hljs-keyword">const</span> mid = <span class="hljs-built_in">Math</span>.floor(arr.length / <span class="hljs-number">2</span>);
  <span class="hljs-keyword">const</span> l = mergeSort(arr.slice(<span class="hljs-number">0</span>, mid));
  <span class="hljs-keyword">const</span> r = mergeSort(arr.slice(mid, arr.length));
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>.from(&#123; <span class="hljs-attr">length</span>: l.length + r.length &#125;, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (!l.length) <span class="hljs-keyword">return</span> r.shift();
    <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!r.length) <span class="hljs-keyword">return</span> l.shift();
    <span class="hljs-keyword">else</span> <span class="hljs-keyword">return</span> l[<span class="hljs-number">0</span>] > r[<span class="hljs-number">0</span>] ? r.shift() : l.shift();
  &#125;);
&#125;;

<span class="hljs-comment">// Examples</span>
mergeSort([<span class="hljs-number">5</span>, <span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]); <span class="hljs-comment">// [1, 2, 3, 4, 5]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-42">桶排序</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> bucketSort = <span class="hljs-function">(<span class="hljs-params">arr, size = <span class="hljs-number">5</span></span>) =></span> &#123;
  <span class="hljs-keyword">const</span> min = <span class="hljs-built_in">Math</span>.min(...arr);
  <span class="hljs-keyword">const</span> max = <span class="hljs-built_in">Math</span>.max(...arr);
  <span class="hljs-keyword">const</span> buckets = <span class="hljs-built_in">Array</span>.from(
    &#123; <span class="hljs-attr">length</span>: <span class="hljs-built_in">Math</span>.floor((max - min) / size) + <span class="hljs-number">1</span> &#125;,
    <span class="hljs-function">() =></span> []
  );
  arr.forEach(<span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
    buckets[<span class="hljs-built_in">Math</span>.floor((val - min) / size)].push(val);
  &#125;);
  <span class="hljs-keyword">return</span> buckets.reduce(<span class="hljs-function">(<span class="hljs-params">acc, b</span>) =></span> [...acc, ...b.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b)], []);
&#125;;

<span class="hljs-comment">// Examples</span>
bucketSort([<span class="hljs-number">6</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>]); <span class="hljs-comment">// [1, 3, 4, 6]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">二分搜索</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> binarySearch = <span class="hljs-function">(<span class="hljs-params">arr, item</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> l = <span class="hljs-number">0</span>,
    r = arr.length - <span class="hljs-number">1</span>;
  <span class="hljs-keyword">while</span> (l <= r) &#123;
    <span class="hljs-keyword">const</span> mid = <span class="hljs-built_in">Math</span>.floor((l + r) / <span class="hljs-number">2</span>);
    <span class="hljs-keyword">const</span> guess = arr[mid];
    <span class="hljs-keyword">if</span> (guess === item) <span class="hljs-keyword">return</span> mid;
    <span class="hljs-keyword">if</span> (guess > item) r = mid - <span class="hljs-number">1</span>;
    <span class="hljs-keyword">else</span> l = mid + <span class="hljs-number">1</span>;
  &#125;
  <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
&#125;;

<span class="hljs-comment">// Examples</span>
binarySearch([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>], <span class="hljs-number">1</span>); <span class="hljs-comment">// 0</span>
binarySearch([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>], <span class="hljs-number">5</span>); <span class="hljs-comment">// 4</span>
binarySearch([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>], <span class="hljs-number">6</span>); <span class="hljs-comment">// -1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">打乱数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> shuffle = <span class="hljs-function">(<span class="hljs-params">[...arr]</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> m = arr.length;
  <span class="hljs-keyword">while</span> (m) &#123;
    <span class="hljs-keyword">const</span> i = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  &#125;
  <span class="hljs-keyword">return</span> arr;
&#125;;

<span class="hljs-comment">// Examples</span>
shuffle([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]); <span class="hljs-comment">// [2, 3, 1]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-45">有趣的 JS</h2>
<h3 data-id="heading-46">如何在 JS 实现睡眠功能</h3>
<h4 data-id="heading-47">同步版本</h4>
<p>Date.prototype.getTime()可以在 while 循环内使用以暂停执行一段时间。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sleepSync = <span class="hljs-function">(<span class="hljs-params">ms</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> end = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() + ms;
  <span class="hljs-keyword">while</span> (<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() < end) &#123;
    <span class="hljs-comment">/* do nothing */</span>
  &#125;
&#125;;

<span class="hljs-keyword">const</span> printNums = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  sleepSync(<span class="hljs-number">500</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;;

printNums(); <span class="hljs-comment">// Logs: 1, 2, 3 (2 and 3 log after 500ms)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-48">异步版本</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sleep = <span class="hljs-function">(<span class="hljs-params">ms</span>) =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> <span class="hljs-built_in">setTimeout</span>(resolve, ms));

<span class="hljs-keyword">const</span> printNums = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">await</span> sleep(<span class="hljs-number">500</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;;

printNums(); <span class="hljs-comment">// Logs: 1, 2, 3 (2 and 3 log after 500ms)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-49">后语</h2>
<p><strong>参考文章：</strong></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.30secondsofcode.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.30secondsofcode.org/" ref="nofollow noopener noreferrer">《30 seconds of code》</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fmozhata%2Fdocument-library%2Fblob%2Fmaster%2Farticles%2Fjs%25E7%259B%25B8%25E5%2585%25B3%2F%25E6%2595%25B0%25E6%258D%25AE%25E7%25B1%25BB%25E5%259E%258B%2Fjs%25E6%2595%25B0%25E6%258D%25AE%25E7%25B1%25BB%25E5%259E%258B%25E5%2588%25A4%25E6%2596%25AD.md" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/mozhata/document-library/blob/master/articles/js%E7%9B%B8%E5%85%B3/%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B/js%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%E5%88%A4%E6%96%AD.md" ref="nofollow noopener noreferrer">数据类型判断</a></li>
</ul>
<p>该文章笔者会不定期更新，大家可以收藏一下。</p>
<p>我也会不定时的更新一些前端方面的知识内容以及自己的原创文章🎉</p>
<p>你的鼓励就是我持续创作的主要动力 😊.</p>
<p><strong>相关推荐</strong></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwenfujie%2Fdocument-library" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wenfujie/document-library" ref="nofollow noopener noreferrer">《前端知识库》</a></li>
<li><a href="https://juejin.cn/post/6927219159918968845" target="_blank" title="https://juejin.cn/post/6927219159918968845">《搭建个人脚手架》</a></li>
</ul></div>  
</div>
            