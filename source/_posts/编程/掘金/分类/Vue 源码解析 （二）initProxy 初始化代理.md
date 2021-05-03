
---
title: 'Vue 源码解析 （二）initProxy 初始化代理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1377'
author: 掘金
comments: false
date: Sun, 02 May 2021 21:37:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=1377'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue 源码解析 （二）initProxy 初始化代理</h1>
<p>在 src/core/instance/proxy.js 找到源码</p>
<h1 data-id="heading-1">makeMap，allowedGlobals</h1>
<p>我们先来看看 makeMap 这个方法，做了什么处理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*makeMap函数, str参数是接受的字符串, expectsLowerCase参数是否需要小写*/</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeMap</span>(<span class="hljs-params">str, expectsLowerCase </span>) </span>&#123;
  <span class="hljs-comment">/* 创建一个对象 */</span>
  <span class="hljs-keyword">var</span> map = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
  <span class="hljs-comment">/*将字符串分割成数组*/</span>
  <span class="hljs-keyword">var</span> list = str.split(<span class="hljs-string">','</span>);
  <span class="hljs-comment">/*对数组进行遍历*/</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < list.length; i++) &#123;
     <span class="hljs-comment">/*将每个key对应的值设置为true*/</span>
     map[list[i]] = <span class="hljs-literal">true</span>;
  &#125;
  <span class="hljs-comment">/*最终返回, 根据参数设置是否是需要转换大小写*/</span>
  <span class="hljs-keyword">return</span> expectsLowerCase
       ? <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">val</span>) </span>&#123;
          <span class="hljs-keyword">return</span> map[val.toLowerCase()];
       &#125;
       : <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">val</span>) </span>&#123;
          <span class="hljs-keyword">return</span> map[val];
       &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后给一些 js 内置的全局方法做了相应的处理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> allowedGlobals = makeMap(
    <span class="hljs-string">'Infinity,undefined,NaN,isFinite,isNaN,'</span> +
    <span class="hljs-string">'parseFloat,parseInt,decodeURI,decodeURIComponent,encodeURI,encodeURIComponent,'</span> +
    <span class="hljs-string">'Math,Number,Date,Array,Object,Boolean,String,RegExp,Map,Set,JSON,Intl,'</span> +
    <span class="hljs-string">'require'</span> <span class="hljs-comment">// for Webpack/Browserify</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>makeMap 函数的只要作用把这些全局的API转成以下的形式,</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">Infinity</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-attr">undefined</span>:<span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">isNative</h1>
<p>可以学习一下源码是如何检测是不是支持原生方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isNative</span> (<span class="hljs-params">Ctor: any</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> Ctor === <span class="hljs-string">'function'</span> && <span class="hljs-regexp">/native code/</span>.test(Ctor.toString())
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">warnNonPresent</h1>
<p>这个方法的意思是不存在，未定义的属性，方法被使用给出警告，我们来看看例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <script src="../vue.js"></script>
    <div id="app">
        <p>
            &#123;&#123;msg&#125;&#125;
        </p>
    </div>
    <script>
        const vm = new Vue(&#123;
            el: '#app',
        &#125;)
        console.log(vm)
    </script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面例子直接在魔板中使用 msg 变量，但是他没有在 data 中定义，此时 warnNonPresent 会处理抛出警告如图所示</p>
<h1 data-id="heading-4">warnReservedPrefix</h1>
<p>源码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> warnReservedPrefix = <span class="hljs-function">(<span class="hljs-params">target, key</span>) =></span> &#123;
    warn(
      <span class="hljs-string">`Property "<span class="hljs-subst">$&#123;key&#125;</span>" must be accessed with "$data.<span class="hljs-subst">$&#123;key&#125;</span>" because `</span> +
      <span class="hljs-string">'properties starting with "$" or "_" are not proxied in the Vue instance to '</span> +
      <span class="hljs-string">'prevent conflicts with Vue internals. '</span> +
      <span class="hljs-string">'See: https://vuejs.org/v2/api/#data'</span>,
      target
    )
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用于检测属性 key 的声明方法，是否是 $ 或者 _ 开头的，如果是，会给出警告，拿个简单的例子来看下效果：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
            &#123;&#123;$hhh&#125;&#125;
            &#123;&#123;_dddd&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
            <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">$hhh</span>: <span class="hljs-string">'ddd'</span>,
                    <span class="hljs-attr">_dddd</span>: <span class="hljs-string">'ffff'</span>
                &#125;
            &#125;,
        &#125;)
        <span class="hljs-built_in">console</span>.log(vm)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">hasHandler</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> hasHandler = &#123;
    <span class="hljs-comment">/*target要代理的对象, key在外部操作时访问的属性*/</span>
    <span class="hljs-attr">has</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">has</span>(<span class="hljs-params">target, key</span>) </span>&#123;
        <span class="hljs-comment">/*key in target返回true或者false*/</span>
        <span class="hljs-keyword">var</span> has = key <span class="hljs-keyword">in</span> target;
        <span class="hljs-comment">/*在模板引擎里面,有一些属性vm没有进行代理, 但是也能使用, 像Number,Object等*/</span>
        <span class="hljs-keyword">var</span> isAllowed = allowedGlobals(key) ||
            (<span class="hljs-keyword">typeof</span> key === <span class="hljs-string">'string'</span> && key.charAt(<span class="hljs-number">0</span>) === <span class="hljs-string">'_'</span> && !(key <span class="hljs-keyword">in</span> target.$data));
        <span class="hljs-comment">/*在上面的has和isAllowed为false的情况下*/</span>
        <span class="hljs-keyword">if</span> (!has && !isAllowed) &#123;
            <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> target.$data) &#123;
                warnReservedPrefix(target, key);
            &#125;
            <span class="hljs-comment">/*warnNonPresent函数, 当访问属性,没有存在vm实例上, 会报错提示*/</span>
            <span class="hljs-keyword">else</span> &#123;
                warnNonPresent(target, key);
            &#125;
        &#125;
        <span class="hljs-comment">/*has或者isAllowed*/</span>
        <span class="hljs-keyword">return</span> has || !isAllowed
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>hasHandler 只配置了 has 钩子 ,当进行propKey in proxy in 操作符 或者 with() 操作时, 会触发 has钩子函数</p>
<p>hasHandler在查找key时,从三个方向进行查找</p>
<ul>
<li>代理的 target 对象 通过 in 操作符</li>
<li>全局对象API allowedGlobals 函数</li>
<li>查找是否是渲染函数的内置方法 第一个字符以_开始 typeof key === 'string' && key.charAt(0) === '_'</li>
</ul>
<p>hasHandler, 首先去检测 vm 实例上是否有该属性, 下面的代码是vm实例上可以查看到test</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
   <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
   <span class="hljs-attr">template</span>:<span class="hljs-string">"<div>&#123;&#123;test&#125;&#125;</div>"</span>,
   <span class="hljs-attr">data</span>:&#123;
       test
   &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在 vm 实例上没有找到, 然后再去判断下是否是一些全局的对象, 例如 Number 等, Number是语言所提供的 在模板中也可以使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
   <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
   <span class="hljs-comment">/*Number属于语言提供的全局API*/</span>
   <span class="hljs-attr">template</span>:<span class="hljs-string">"<div> &#123;&#123; Number(test) +1 &#125;&#125;</div>"</span>,
   <span class="hljs-attr">data</span>:&#123;
       test
   &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">getHandler</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getHandler = &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> key === <span class="hljs-string">'string'</span> && !(key <span class="hljs-keyword">in</span> target)) &#123;
        <span class="hljs-comment">// 检测 data 是属性 key 是不是 $,_ 开头</span>
        <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> target.$data) warnReservedPrefix(target, key)
        <span class="hljs-keyword">else</span> warnNonPresent(target, key)
      &#125;
      <span class="hljs-keyword">return</span> target[key]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">initProxy</h1>
<pre><code class="hljs language-js copyable" lang="js">initProxy = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initProxy</span>(<span class="hljs-params">vm</span>) </span>&#123;
<span class="hljs-comment">/*hasProxy 判断当前环境是否支持es 提供的 Proxy*/</span>
<span class="hljs-keyword">if</span> (hasProxy) &#123;
   <span class="hljs-comment">// determine which proxy handler to use</span>
   <span class="hljs-keyword">var</span> options = vm.$options;
   <span class="hljs-comment">/*不同条件返回不同的handlers, getHandler或者hasHandler */</span>
   <span class="hljs-keyword">var</span> handlers = options.render && options.render._withStripped
       ? getHandler
       : hasHandler;
   <span class="hljs-comment">/* 代理vm实例 */</span>
   vm._renderProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(vm, handlers);
&#125; <span class="hljs-keyword">else</span> &#123;
   vm._renderProxy = vm;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            